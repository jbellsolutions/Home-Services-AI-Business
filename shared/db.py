"""
Lead tracking database using SQLite.
Tracks all ads posted, responses received, and bookings made.
"""
import aiosqlite
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'leads.db')


async def init_db():
    """Create tables if they don't exist."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS ads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                city TEXT NOT NULL,
                category TEXT,
                template_name TEXT,
                title TEXT,
                post_url TEXT,
                cl_post_id TEXT,
                posted_at TEXT NOT NULL,
                renewed_at TEXT,
                expires_at TEXT,
                status TEXT DEFAULT 'active',
                cost REAL DEFAULT 0.0
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ad_id INTEGER,
                platform TEXT NOT NULL,
                lead_name TEXT,
                lead_phone TEXT,
                lead_email TEXT,
                lead_message TEXT,
                service_requested TEXT,
                location TEXT,
                received_at TEXT NOT NULL,
                responded_at TEXT,
                response_text TEXT,
                status TEXT DEFAULT 'new',
                booking_date TEXT,
                booking_time TEXT,
                notes TEXT,
                FOREIGN KEY (ad_id) REFERENCES ads(id)
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS daily_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                platform TEXT NOT NULL,
                ads_posted INTEGER DEFAULT 0,
                ads_renewed INTEGER DEFAULT 0,
                leads_received INTEGER DEFAULT 0,
                responses_sent INTEGER DEFAULT 0,
                bookings_made INTEGER DEFAULT 0,
                total_cost REAL DEFAULT 0.0
            )
        ''')
        await db.commit()


async def log_ad(platform, city, category, template_name, title, post_url=None, cl_post_id=None, cost=0.0):
    """Log a posted ad."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            '''INSERT INTO ads (platform, city, category, template_name, title, post_url, cl_post_id, posted_at, cost)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (platform, city, category, template_name, title, post_url, cl_post_id,
             datetime.now().isoformat(), cost)
        )
        await db.commit()
        return cursor.lastrowid


async def log_lead(ad_id, platform, lead_name=None, lead_phone=None, lead_email=None,
                   lead_message=None, service_requested=None, location=None):
    """Log a new lead."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            '''INSERT INTO leads (ad_id, platform, lead_name, lead_phone, lead_email,
               lead_message, service_requested, location, received_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (ad_id, platform, lead_name, lead_phone, lead_email, lead_message,
             service_requested, location, datetime.now().isoformat())
        )
        await db.commit()
        return cursor.lastrowid


async def get_todays_ads(platform):
    """Get ads posted today for a platform."""
    today = datetime.now().strftime('%Y-%m-%d')
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute(
            "SELECT * FROM ads WHERE platform = ? AND posted_at LIKE ? ORDER BY posted_at DESC",
            (platform, f'{today}%')
        )
        return await cursor.fetchall()


async def get_active_ads(platform):
    """Get all active ads for a platform."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute(
            "SELECT * FROM ads WHERE platform = ? AND status = 'active' ORDER BY posted_at DESC",
            (platform,)
        )
        return await cursor.fetchall()


async def update_ad_status(ad_id, status):
    """Update an ad's status."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE ads SET status = ? WHERE id = ?", (status, ad_id))
        await db.commit()
