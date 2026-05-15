"""
Test proxy connectivity and verify Jacksonville FL geo-targeting.
Run this before attempting to post on Craigslist.

Usage:
    python scripts/test_proxy.py
    python scripts/test_proxy.py --browser  # Also test with Playwright browser
"""
import asyncio
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / '.env')

PROXY_HOST = os.getenv('PROXY_HOST', '')
PROXY_PORT = os.getenv('PROXY_PORT', '')
PROXY_USER = os.getenv('PROXY_USER', '')
PROXY_PASS = os.getenv('PROXY_PASS', '')


async def test_ip_lookup():
    """Test proxy IP and geolocation via HTTP."""
    import aiohttp

    print("=== Proxy Connectivity Test ===\n")

    if not PROXY_HOST:
        print("WARNING: No proxy configured. Testing direct connection.\n")
        proxy_url = None
    else:
        proxy_url = f'http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}'
        print(f"Proxy: {PROXY_HOST}:{PROXY_PORT}")
        print(f"User:  {PROXY_USER}\n")

    # Test 1: IP lookup
    print("1. Checking IP address...")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://httpbin.org/ip', proxy=proxy_url, timeout=aiohttp.ClientTimeout(total=15)) as resp:
                data = await resp.json()
                ip = data.get('origin', 'unknown')
                print(f"   Your IP: {ip}")
    except Exception as e:
        print(f"   FAILED: {e}")
        return False

    # Test 2: Geolocation
    print("\n2. Checking geolocation...")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://ipapi.co/{ip}/json/', timeout=aiohttp.ClientTimeout(total=15)) as resp:
                geo = await resp.json()
                city = geo.get('city', 'unknown')
                region = geo.get('region', 'unknown')
                country = geo.get('country_name', 'unknown')
                org = geo.get('org', 'unknown')
                ip_type = geo.get('type', 'unknown')
                print(f"   Location: {city}, {region}, {country}")
                print(f"   ISP/Org:  {org}")

                if 'jacksonville' in city.lower():
                    print("   ✅ PASS - IP is in Jacksonville FL")
                elif 'florida' in region.lower():
                    print("   ⚠️  WARN - IP is in Florida but not Jacksonville")
                else:
                    print(f"   ❌ FAIL - IP is in {city}, {region} (need Jacksonville FL)")
    except Exception as e:
        print(f"   FAILED: {e}")

    # Test 3: Craigslist connectivity
    print("\n3. Testing Craigslist access...")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://jacksonville.craigslist.org', proxy=proxy_url,
                                   timeout=aiohttp.ClientTimeout(total=15)) as resp:
                if resp.status == 200:
                    print(f"   ✅ PASS - CL Jacksonville loads (status {resp.status})")
                elif resp.status == 403:
                    print(f"   ❌ FAIL - CL blocked this IP (status 403)")
                else:
                    print(f"   ⚠️  Status {resp.status}")
    except Exception as e:
        print(f"   FAILED: {e}")

    # Test 4: Facebook connectivity
    print("\n4. Testing Facebook access...")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://www.facebook.com', proxy=proxy_url,
                                   timeout=aiohttp.ClientTimeout(total=15)) as resp:
                print(f"   Facebook status: {resp.status}")
                if resp.status == 200:
                    print("   ✅ PASS")
    except Exception as e:
        print(f"   FAILED: {e}")

    print("\n=== Test Complete ===\n")
    return True


async def test_browser():
    """Test proxy with a real browser via Playwright."""
    from playwright.async_api import async_playwright

    print("\n=== Browser Proxy Test ===\n")

    proxy_config = None
    if PROXY_HOST:
        proxy_config = {
            'server': f'http://{PROXY_HOST}:{PROXY_PORT}',
            'username': PROXY_USER,
            'password': PROXY_PASS,
        }

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context_opts = {
            'viewport': {'width': 1366, 'height': 768},
            'timezone_id': 'America/New_York',
        }
        if proxy_config:
            context_opts['proxy'] = proxy_config

        context = await browser.new_context(**context_opts)
        page = await context.new_page()

        # Check IP in browser
        print("Opening IP check page...")
        await page.goto('https://whatismyipaddress.com')
        await asyncio.sleep(5)

        screenshots_dir = Path(__file__).parent.parent / 'screenshots'
        screenshots_dir.mkdir(exist_ok=True)
        await page.screenshot(path=str(screenshots_dir / 'proxy_test_ip.png'))
        print("Screenshot saved: screenshots/proxy_test_ip.png")

        # Check CL
        print("\nOpening Jacksonville Craigslist...")
        await page.goto('https://jacksonville.craigslist.org')
        await asyncio.sleep(3)
        await page.screenshot(path=str(screenshots_dir / 'proxy_test_cl.png'))
        print("Screenshot saved: screenshots/proxy_test_cl.png")

        print("\n✅ Browser test complete. Check screenshots/ folder.")
        await browser.close()


def main():
    parser = argparse.ArgumentParser(description='Test proxy connectivity')
    parser.add_argument('--browser', action='store_true', help='Also test with Playwright browser')
    args = parser.parse_args()

    asyncio.run(test_ip_lookup())
    if args.browser:
        asyncio.run(test_browser())


if __name__ == '__main__':
    main()
