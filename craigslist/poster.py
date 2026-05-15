"""
Craigslist Poster - Jacksonville FL
Posts handyman service ads to CL skilled trade services.

Usage:
    python craigslist/poster.py --test          # Post one test ad
    python craigslist/poster.py --post          # Post next scheduled ad
    python craigslist/poster.py --schedule      # Run on full daily schedule
    python craigslist/poster.py --renew         # Renew eligible ads
    python craigslist/poster.py --status        # Show posting status
"""
import asyncio
import argparse
import os
import random
import sys
import yaml
from datetime import datetime, timedelta
from pathlib import Path

# Add parent to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from playwright.async_api import async_playwright
from dotenv import load_dotenv
from shared.db import init_db, log_ad, get_todays_ads, get_active_ads
from shared.logger import get_logger

load_dotenv(Path(__file__).parent.parent / '.env')

logger = get_logger('craigslist')

# --- Config ---
TEMPLATES_PATH = Path(__file__).parent / 'ad_templates' / 'templates.yaml'
IMAGES_DIR = Path(__file__).parent / 'ad_templates' / 'images'
PROFILES_DIR = Path(__file__).parent.parent / 'profiles' / 'craigslist'
SCREENSHOTS_DIR = Path(__file__).parent.parent / 'screenshots'

CL_BASE_URL = 'https://jacksonville.craigslist.org'
CL_EMAIL = os.getenv('CL_EMAIL', '')
CL_PASSWORD = os.getenv('CL_PASSWORD', '')

PROXY_HOST = os.getenv('PROXY_HOST', '')
PROXY_PORT = os.getenv('PROXY_PORT', '')
PROXY_USER = os.getenv('PROXY_USER', '')
PROXY_PASS = os.getenv('PROXY_PASS', '')

PHONE = os.getenv('BUSINESS_PHONE', '+1-904-XXX-XXXX')


def load_templates():
    """Load ad templates from YAML."""
    with open(TEMPLATES_PATH) as f:
        data = yaml.safe_load(f)
    return data['templates']


def pick_ad(templates, template_name, category, used_today=None):
    """Pick a random title/body variant for a specific template, avoiding today's used combos."""
    used_today = used_today or []
    template = templates[template_name]

    for title in random.sample(template['titles'], len(template['titles'])):
        for body in random.sample(template['bodies'], len(template['bodies'])):
            combo_key = f"{template_name}:{category}:{title[:30]}"
            if combo_key not in used_today:
                return {
                    'template_name': template_name,
                    'title': title,
                    'body': body.replace('{phone}', PHONE),
                    'images_folder': template.get('images_folder', ''),
                    'category': category,
                }
    # Fallback: just pick random variant
    return {
        'template_name': template_name,
        'title': random.choice(template['titles']),
        'body': random.choice(template['bodies']).replace('{phone}', PHONE),
        'images_folder': template.get('images_folder', ''),
        'category': category,
    }


# CL category display names to selector text mapping
CL_CATEGORIES = {
    'skilled_trade_services': 'skilled trade services',
    'household_services': 'household services',
}


def get_images(images_folder):
    """Get image paths for an ad template."""
    folder = IMAGES_DIR / images_folder
    if not folder.exists():
        logger.warning(f"Images folder not found: {folder}")
        return []
    images = sorted(folder.glob('*.jpg')) + sorted(folder.glob('*.png'))
    return [str(p) for p in images[:8]]  # CL allows up to 12, use 8


def get_proxy_config():
    """Build Playwright proxy config."""
    if not PROXY_HOST:
        return None
    return {
        'server': f'http://{PROXY_HOST}:{PROXY_PORT}',
        'username': PROXY_USER,
        'password': PROXY_PASS,
    }


async def create_browser(playwright, headless=True):
    """Launch browser with proxy and anti-detection settings."""
    os.makedirs(PROFILES_DIR, exist_ok=True)

    proxy = get_proxy_config()
    launch_args = [
        '--disable-blink-features=AutomationControlled',
        '--disable-infobars',
        '--no-first-run',
    ]

    context_opts = {
        'user_agent': (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/131.0.0.0 Safari/537.36'
        ),
        'viewport': {'width': 1366, 'height': 768},
        'locale': 'en-US',
        'timezone_id': 'America/New_York',
        'geolocation': {'latitude': 30.3322, 'longitude': -81.6557},  # Jacksonville FL
        'permissions': ['geolocation'],
        'storage_state': str(PROFILES_DIR / 'state.json') if (PROFILES_DIR / 'state.json').exists() else None,
    }

    if proxy:
        context_opts['proxy'] = proxy

    browser = await playwright.chromium.launch(
        headless=headless,
        args=launch_args,
    )
    context = await browser.new_context(**context_opts)

    # Anti-detection: remove webdriver flag
    await context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        window.chrome = { runtime: {} };
    """)

    return browser, context


async def login_to_cl(page):
    """Log into Craigslist account."""
    logger.info("Logging into Craigslist...")
    await page.goto(f'{CL_BASE_URL}/login')
    await page.wait_for_load_state('networkidle')

    # Check if already logged in
    if 'account' in page.url:
        logger.info("Already logged in")
        return True

    await page.fill('#inputEmailHandle', CL_EMAIL)
    await page.fill('#inputPassword', CL_PASSWORD)
    await page.click('#login')

    await page.wait_for_load_state('networkidle')
    await asyncio.sleep(2)

    if 'account' in page.url or 'login' not in page.url:
        logger.info("Login successful")
        return True
    else:
        logger.error("Login failed - may need manual verification")
        return False


async def post_ad(page, ad, test_mode=False):
    """Post a single ad to Craigslist Jacksonville in the specified category."""
    category = ad.get('category', 'skilled_trade_services')
    category_text = CL_CATEGORIES.get(category, 'skilled trade services')
    logger.info(f"Posting ad: {ad['title']} → {category_text}")

    # Navigate to posting page
    await page.goto(f'{CL_BASE_URL}/post')
    await page.wait_for_load_state('networkidle')
    await asyncio.sleep(random.uniform(1, 3))

    # Step 1: Choose "service offered"
    try:
        await page.click('input[value="so"]')  # service offered
        await asyncio.sleep(random.uniform(0.5, 1.5))
        await page.click('button.pickbutton')
        await page.wait_for_load_state('networkidle')
        await asyncio.sleep(random.uniform(1, 2))
    except Exception as e:
        logger.error(f"Failed to select posting type: {e}")
        return None

    # Step 2: Choose category dynamically
    try:
        cat_label = page.locator(f'label:has-text("{category_text}")')
        if await cat_label.count() > 0:
            await cat_label.first.click()
        else:
            # Fallback: try radio input by text
            cat_option = page.locator(f'text={category_text}')
            if await cat_option.count() > 0:
                await cat_option.first.click()
            else:
                logger.warning(f"Category '{category_text}' not found, trying first available")
                first_radio = page.locator('input[type="radio"]').first
                await first_radio.click()
        await asyncio.sleep(random.uniform(0.5, 1))
        await page.click('button.pickbutton')
        await page.wait_for_load_state('networkidle')
        await asyncio.sleep(random.uniform(1, 2))
    except Exception as e:
        logger.warning(f"Category selection issue: {e}")
        try:
            await page.click('button.pickbutton')
            await page.wait_for_load_state('networkidle')
        except Exception:
            pass

    # Step 3: Fill in the posting form
    try:
        # Title
        title_input = page.locator('#PostingTitle')
        await title_input.fill(ad['title'])
        await asyncio.sleep(random.uniform(0.3, 0.8))

        # City/area
        city_input = page.locator('#GeographicArea')
        if await city_input.count() > 0:
            await city_input.fill('Jacksonville')

        # Postal code
        postal = page.locator('#postal_code, input[name="postal"]')
        if await postal.count() > 0:
            await postal.fill('32202')

        # Body/description
        body_input = page.locator('#PostingBody')
        await body_input.fill(ad['body'])
        await asyncio.sleep(random.uniform(0.5, 1))

        # Phone number (if field exists)
        phone_input = page.locator('input[name="contact_phone"]')
        if await phone_input.count() > 0:
            await phone_input.fill(PHONE.replace('-', '').replace('+1', ''))

        logger.info("Form filled successfully")
    except Exception as e:
        logger.error(f"Failed to fill form: {e}")
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        await page.screenshot(path=str(SCREENSHOTS_DIR / f'cl_error_{datetime.now().strftime("%H%M%S")}.png'))
        return None

    if test_mode:
        logger.info("TEST MODE - Not submitting. Taking screenshot.")
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        await page.screenshot(path=str(SCREENSHOTS_DIR / f'cl_test_{datetime.now().strftime("%H%M%S")}.png'))
        return 'test'

    # Step 4: Continue / submit
    try:
        await page.click('button.go')
        await page.wait_for_load_state('networkidle')
        await asyncio.sleep(random.uniform(2, 4))

        # Upload images if available
        images = get_images(ad['images_folder'])
        if images:
            file_input = page.locator('input[type="file"]')
            if await file_input.count() > 0:
                for img_path in images:
                    await file_input.set_input_files(img_path)
                    await asyncio.sleep(random.uniform(1, 3))
                logger.info(f"Uploaded {len(images)} images")

        # Continue past images
        done_btn = page.locator('button:has-text("done with images")')
        if await done_btn.count() > 0:
            await done_btn.click()
            await page.wait_for_load_state('networkidle')
            await asyncio.sleep(2)

        # Final publish
        publish_btn = page.locator('button.go, button:has-text("publish")')
        if await publish_btn.count() > 0:
            await publish_btn.click()
            await page.wait_for_load_state('networkidle')
            await asyncio.sleep(3)

        # Check for success
        post_url = page.url
        logger.info(f"Ad posted successfully: {post_url}")

        # Save browser state for future sessions
        os.makedirs(PROFILES_DIR, exist_ok=True)
        storage = await page.context.storage_state()
        import json
        with open(PROFILES_DIR / 'state.json', 'w') as f:
            json.dump(storage, f)

        return post_url

    except Exception as e:
        logger.error(f"Failed to submit ad: {e}")
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        await page.screenshot(path=str(SCREENSHOTS_DIR / f'cl_submit_error_{datetime.now().strftime("%H%M%S")}.png'))
        return None


async def run_single_post(template_name=None, category=None, test_mode=False):
    """Post a single ad. If template/category not specified, pick the next one from schedule."""
    await init_db()
    templates = load_templates()

    # Get today's used templates to avoid repeats
    todays_ads = await get_todays_ads('craigslist')
    used_today = [f"{row['template_name']}:{row['category']}:{row['title'][:30]}" for row in todays_ads] if todays_ads else []

    if len(used_today) >= 7 and not test_mode:
        logger.info("Already posted 7 ads today. Skipping.")
        return

    # If no template specified, pick the next one from the schedule
    if not template_name:
        settings_path = Path(__file__).parent.parent / 'config' / 'settings.yaml'
        with open(settings_path) as f:
            settings = yaml.safe_load(f)
        schedule = settings['craigslist']['posting_schedule']
        # Find the next unposted slot
        posted_count = len(used_today)
        if posted_count < len(schedule):
            slot = schedule[posted_count]
            template_name = slot['template']
            category = slot['category']
        else:
            template_name = 'general_handyman'
            category = 'skilled_trade_services'

    if not category:
        category = 'skilled_trade_services'

    ad = pick_ad(templates, template_name, category, used_today)
    logger.info(f"Selected: {ad['template_name']} → {CL_CATEGORIES.get(category, category)}")

    async with async_playwright() as p:
        headless = not test_mode  # Show browser in test mode
        browser, context = await create_browser(p, headless=headless)
        page = await context.new_page()

        try:
            logged_in = await login_to_cl(page)
            if not logged_in:
                logger.error("Cannot post - login failed")
                return

            result = await post_ad(page, ad, test_mode=test_mode)

            if result and result != 'test':
                await log_ad(
                    platform='craigslist',
                    city='Jacksonville',
                    category=category,
                    template_name=ad['template_name'],
                    title=ad['title'],
                    post_url=result,
                    cost=5.0  # CL posting fee
                )
                logger.info(f"Ad logged to database. Cost: $5.00")
            elif result == 'test':
                logger.info("Test post completed. Check screenshots/ folder.")
        finally:
            await browser.close()


async def run_scheduled():
    """Run the full daily posting schedule (7 ads across 4 services and 2 categories)."""
    from apscheduler.schedulers.asyncio import AsyncIOScheduler
    from apscheduler.triggers.cron import CronTrigger

    await init_db()

    # Load schedule from settings
    settings_path = Path(__file__).parent.parent / 'config' / 'settings.yaml'
    with open(settings_path) as f:
        settings = yaml.safe_load(f)

    schedule = settings['craigslist']['posting_schedule']
    logger.info(f"Starting scheduler with {len(schedule)} posting slots")

    scheduler = AsyncIOScheduler()

    for slot in schedule:
        time_str = slot['time']
        template = slot['template']
        category = slot['category']
        hour, minute = time_str.split(':')

        scheduler.add_job(
            run_single_post,
            CronTrigger(hour=int(hour), minute=int(minute)),
            kwargs={'template_name': template, 'category': category},
            id=f'cl_{template}_{category}_{time_str}',
            name=f'{time_str} | {template} → {category}',
        )
        logger.info(f"  {time_str} | {template} → {CL_CATEGORIES.get(category, category)}")

    scheduler.start()
    logger.info("Scheduler running. 7 posts/day. Press Ctrl+C to stop.")
    logger.info(f"Estimated daily cost: ${len(schedule) * 5:.2f}")

    try:
        while True:
            await asyncio.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logger.info("Scheduler stopped.")


async def show_status():
    """Show posting status."""
    await init_db()
    todays_ads = await get_todays_ads('craigslist')
    active_ads = await get_active_ads('craigslist')

    print("\n=== Craigslist Posting Status ===")
    print(f"Today's posts: {len(todays_ads) if todays_ads else 0}/7")
    print(f"Active ads: {len(active_ads) if active_ads else 0}")

    if todays_ads:
        print("\nToday's ads:")
        for ad in todays_ads:
            print(f"  [{ad['posted_at'][:16]}] {ad['template_name']}: {ad['title']}")

    total_cost = sum(ad['cost'] for ad in (todays_ads or []))
    print(f"\nToday's CL fees: ${total_cost:.2f}")
    print()


def main():
    parser = argparse.ArgumentParser(description='Craigslist Poster - Jacksonville FL')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--test', action='store_true', help='Post one test ad (visible browser, no submit)')
    group.add_argument('--post', action='store_true', help='Post next scheduled ad')
    group.add_argument('--schedule', action='store_true', help='Run full daily schedule')
    group.add_argument('--renew', action='store_true', help='Renew eligible ads')
    group.add_argument('--status', action='store_true', help='Show posting status')
    args = parser.parse_args()

    if args.test:
        asyncio.run(run_single_post(test_mode=True))
    elif args.post:
        asyncio.run(run_single_post())
    elif args.schedule:
        asyncio.run(run_scheduled())
    elif args.status:
        asyncio.run(show_status())
    elif args.renew:
        print("Renewal feature coming soon - renew manually for now")


if __name__ == '__main__':
    main()
