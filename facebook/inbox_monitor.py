"""
Facebook Marketplace / Groups Inbox Monitor
Checks for new messages every 5 minutes and auto-responds.

Two modes:
  1. MONITOR: Check FB Marketplace inbox for new inquiries, auto-respond
  2. GROUP POST: Post service ads to local Jacksonville Facebook groups

Usage:
    python facebook/inbox_monitor.py --monitor     # Start 5-min inbox checking
    python facebook/inbox_monitor.py --post        # Post to groups
    python facebook/inbox_monitor.py --test        # Test login and screenshot
"""
import asyncio
import argparse
import json
import os
import random
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from playwright.async_api import async_playwright
from dotenv import load_dotenv
from shared.db import init_db, log_lead
from shared.logger import get_logger

load_dotenv(Path(__file__).parent.parent / '.env')

logger = get_logger('facebook')

# --- Config ---
FB_EMAIL = os.getenv('FB_EMAIL', '')
FB_PASSWORD = os.getenv('FB_PASSWORD', '')
PHONE = os.getenv('BUSINESS_PHONE', '+1-904-XXX-XXXX')
BUSINESS_NAME = os.getenv('BUSINESS_NAME', 'J Bell Handyman Services')
BOOKING_URL = os.getenv('BOOKING_URL', '')

PROFILES_DIR = Path(__file__).parent.parent / 'profiles' / 'facebook'
SCREENSHOTS_DIR = Path(__file__).parent.parent / 'screenshots'
RESPONDED_FILE = Path(__file__).parent / 'responded_threads.json'

CHECK_INTERVAL = 5 * 60  # 5 minutes in seconds

# Keywords that indicate the customer is asking about pricing (trigger human handoff)
HANDOFF_KEYWORDS = ['how much', 'price', 'cost', 'estimate', 'quote', 'budget',
                    'expensive', 'cheaper', 'discount', 'rate', 'charge']

# --- Response Templates ---
INITIAL_RESPONSE = f"""Hi there! Thanks for reaching out to {BUSINESS_NAME}! 👋

We'd love to help you with that. We serve all of Jacksonville and surrounding areas.

To get you a quick quote, could you share:
1. What service do you need? (repair, painting, assembly, etc.)
2. Your general location in Jax?
3. Any photos of the job? (optional but helps with pricing)

Or just give us a call/text at {PHONE} and we can chat!"""

BOOKING_RESPONSE = f"""Great, sounds like something we can definitely help with!

Let's get you on the schedule. What works better for you:
- A quick phone call to discuss details? Call/text {PHONE}
- Or reply here with your preferred day and time window for us to come take a look?

We offer FREE estimates and can usually get out there within 1-2 days."""

AFTER_HOURS_RESPONSE = f"""Thanks for your message! We're currently offline but will respond first thing in the morning.

If it's urgent, feel free to call or text us at {PHONE}.

-- {BUSINESS_NAME}"""


def load_responded():
    """Load set of already-responded thread IDs."""
    if RESPONDED_FILE.exists():
        with open(RESPONDED_FILE) as f:
            return set(json.load(f))
    return set()


def save_responded(responded):
    """Save responded thread IDs."""
    with open(RESPONDED_FILE, 'w') as f:
        json.dump(list(responded), f)


def is_after_hours():
    """Check if current time is outside business hours (7am-9pm ET)."""
    hour = datetime.now().hour
    return hour < 7 or hour >= 21


def needs_human_handoff(message_text):
    """Check if message contains pricing keywords that need human response."""
    text_lower = message_text.lower()
    return any(kw in text_lower for kw in HANDOFF_KEYWORDS)


async def create_browser(playwright, headless=False):
    """Launch browser with persistent Facebook session."""
    os.makedirs(PROFILES_DIR, exist_ok=True)

    context_opts = {
        'user_agent': (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/131.0.0.0 Safari/537.36'
        ),
        'viewport': {'width': 1366, 'height': 768},
        'locale': 'en-US',
        'timezone_id': 'America/New_York',
        'storage_state': str(PROFILES_DIR / 'state.json') if (PROFILES_DIR / 'state.json').exists() else None,
    }

    browser = await playwright.chromium.launch(
        headless=headless,
        args=[
            '--disable-blink-features=AutomationControlled',
            '--disable-infobars',
        ],
    )
    context = await browser.new_context(**context_opts)

    await context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    """)

    return browser, context


async def save_session(context):
    """Save browser session for persistence."""
    os.makedirs(PROFILES_DIR, exist_ok=True)
    storage = await context.storage_state()
    with open(PROFILES_DIR / 'state.json', 'w') as f:
        json.dump(storage, f)
    logger.info("Session saved")


async def login_to_facebook(page):
    """Log into Facebook."""
    logger.info("Checking Facebook login status...")
    await page.goto('https://www.facebook.com')
    await page.wait_for_load_state('networkidle')
    await asyncio.sleep(2)

    # Check if already logged in
    if 'login' not in page.url and 'checkpoint' not in page.url:
        logger.info("Already logged in to Facebook")
        return True

    logger.info("Logging in...")
    await page.fill('#email', FB_EMAIL)
    await asyncio.sleep(random.uniform(0.5, 1))
    await page.fill('#pass', FB_PASSWORD)
    await asyncio.sleep(random.uniform(0.5, 1))
    await page.click('button[name="login"]')
    await page.wait_for_load_state('networkidle')
    await asyncio.sleep(3)

    if 'checkpoint' in page.url or 'two_step_verification' in page.url:
        logger.warning("2FA required - please complete manually")
        logger.warning("Waiting 60 seconds for manual 2FA...")
        await asyncio.sleep(60)

    if 'login' not in page.url:
        logger.info("Facebook login successful")
        return True

    logger.error("Facebook login failed")
    return False


async def check_marketplace_inbox(page, responded):
    """Check Marketplace inbox for new messages."""
    logger.info("Checking Marketplace inbox...")

    await page.goto('https://www.facebook.com/marketplace/inbox/')
    await page.wait_for_load_state('networkidle')
    await asyncio.sleep(3)

    # Find conversation threads
    threads = page.locator('[role="row"], [data-testid="mwthreadlist-item"]')
    thread_count = await threads.count()
    logger.info(f"Found {thread_count} conversation threads")

    new_messages = 0
    for i in range(min(thread_count, 20)):  # Check top 20 threads
        try:
            thread = threads.nth(i)

            # Check for unread indicator
            unread = thread.locator('.x1cpjm7i, [data-visualcompletion="ignore"]')
            has_unread = await unread.count() > 0

            if not has_unread:
                continue

            # Get thread identifier
            thread_text = await thread.inner_text()
            thread_id = str(hash(thread_text[:100]))

            if thread_id in responded:
                continue

            # Click into thread
            await thread.click()
            await asyncio.sleep(2)

            # Read the latest message
            messages = page.locator('[data-testid="message-container"], [role="row"]')
            msg_count = await messages.count()
            if msg_count == 0:
                continue

            last_msg = await messages.last.inner_text()
            logger.info(f"New message from thread: {last_msg[:100]}...")

            # Determine response
            if is_after_hours():
                response = AFTER_HOURS_RESPONSE
            elif needs_human_handoff(last_msg):
                response = BOOKING_RESPONSE
                logger.info("HANDOFF: Pricing question detected - sending booking response")
            else:
                response = INITIAL_RESPONSE

            # Type and send response
            msg_input = page.locator('[role="textbox"][aria-label*="message"], [contenteditable="true"]')
            if await msg_input.count() > 0:
                await msg_input.first.click()
                await asyncio.sleep(0.5)

                # Type like a human (with small delays)
                for char in response:
                    await msg_input.first.type(char, delay=random.uniform(10, 30))
                    if random.random() < 0.02:  # Occasional pause
                        await asyncio.sleep(random.uniform(0.5, 1.5))

                # Send
                await page.keyboard.press('Enter')
                await asyncio.sleep(1)

                responded.add(thread_id)
                new_messages += 1
                logger.info(f"Responded to thread (auto-response sent)")

                # Log the lead
                await log_lead(
                    ad_id=None,
                    platform='facebook_marketplace',
                    lead_message=last_msg[:500],
                )

            # Go back to inbox
            await page.goto('https://www.facebook.com/marketplace/inbox/')
            await page.wait_for_load_state('networkidle')
            await asyncio.sleep(2)

        except Exception as e:
            logger.error(f"Error processing thread {i}: {e}")
            continue

    save_responded(responded)
    logger.info(f"Check complete. Responded to {new_messages} new messages.")
    return new_messages


async def run_monitor():
    """Run the 5-minute inbox monitoring loop."""
    await init_db()
    responded = load_responded()

    async with async_playwright() as p:
        browser, context = await create_browser(p, headless=False)
        page = await context.new_page()

        logged_in = await login_to_facebook(page)
        if not logged_in:
            logger.error("Cannot monitor - login failed")
            return

        await save_session(context)
        logger.info(f"Starting inbox monitor (checking every {CHECK_INTERVAL // 60} minutes)")

        try:
            while True:
                try:
                    new_msgs = await check_marketplace_inbox(page, responded)
                    if new_msgs > 0:
                        await save_session(context)
                        logger.info(f"Processed {new_msgs} new messages")
                except Exception as e:
                    logger.error(f"Monitor cycle error: {e}")
                    # Try to recover
                    try:
                        await page.goto('https://www.facebook.com')
                        await asyncio.sleep(5)
                    except Exception:
                        pass

                logger.info(f"Next check in {CHECK_INTERVAL // 60} minutes...")
                await asyncio.sleep(CHECK_INTERVAL)
        except KeyboardInterrupt:
            logger.info("Monitor stopped by user")
        finally:
            await save_session(context)
            await browser.close()


async def run_test():
    """Test login and take screenshot of inbox."""
    async with async_playwright() as p:
        browser, context = await create_browser(p, headless=False)
        page = await context.new_page()

        logged_in = await login_to_facebook(page)
        if logged_in:
            await save_session(context)
            await page.goto('https://www.facebook.com/marketplace/inbox/')
            await asyncio.sleep(3)

            os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
            await page.screenshot(
                path=str(SCREENSHOTS_DIR / f'fb_inbox_{datetime.now().strftime("%H%M%S")}.png'),
                full_page=True
            )
            logger.info("Test complete - check screenshots/ folder")
        else:
            logger.error("Login failed")

        await browser.close()


def main():
    parser = argparse.ArgumentParser(description='Facebook Marketplace Inbox Monitor')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--monitor', action='store_true', help='Start 5-min inbox monitoring')
    group.add_argument('--post', action='store_true', help='Post to local groups')
    group.add_argument('--test', action='store_true', help='Test login and screenshot inbox')
    args = parser.parse_args()

    if args.monitor:
        asyncio.run(run_monitor())
    elif args.test:
        asyncio.run(run_test())
    elif args.post:
        print("Group posting feature coming in next update")


if __name__ == '__main__':
    main()
