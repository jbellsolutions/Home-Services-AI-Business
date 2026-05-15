# Home Services AI Business — Deployable Product

## What This Is

A complete, ready-to-deploy business system for home services companies — strategy docs, sales playbooks, AI system specs, AND the automation code to run it all. You walk in, sign the client, and deploy everything from this repo.

**The offer:** "I'll handle all your marketing, lead generation, AI phone system, and operations backend. You cover the marketing budget. I either charge a retainer OR take an equity/revenue share. You just do the work."

---

## How It Works (For You, the Operator)

1. **Sign the client** — use the partnership agreement template in `agreements/`
2. **Deploy the lead gen** — Craigslist, Facebook Marketplace, Nextdoor, free platforms (all playbooks in `lead-gen/`)
3. **Run the automation** — Craigslist poster, FB inbox monitor, lead tracker (code in `craigslist/`, `facebook/`, `shared/`)
4. **Set up the AI systems** — phone receptionist, inbox monitor, follow-up sequences (specs in `systems/`)
5. **Launch outreach** — property managers, contractors, recent home buyers (templates in `outreach/`)
6. **Manage & optimize** — track leads, adjust ads, scale what works

**Time to deploy:** 3-5 days for a basic launch. Full system in 2-3 weeks.

---

## The Offer (What You Sell)

### Option A: Retainer Model
| Tier | Setup Fee | Monthly | What They Get |
|------|-----------|---------|---------------|
| **Lead Recovery Engine** | $1,500 | $497/mo | AI phone, lead follow-up, review automation |
| **Growth Machine** | $3,500 | $997/mo | + outreach, campaigns, estimate follow-up |
| **AI Ops Hub** | $7,500 | $1,997/mo | + dispatch, scheduling, full operations |

### Option B: Partnership Model (Equity/Revenue Share)
Best for startups or operators who can't afford a retainer upfront.

| Term | Details |
|------|---------|
| **Your cut** | 25-35% of net profit (after expenses) |
| **Their cut** | 65-75% of net profit |
| **They cover** | Marketing budget ($500-$1,000/mo to start) |
| **You cover** | Your own tech stack (AI tools, APIs, software) |
| **Payout** | Biweekly |
| **Test period** | 30 days — either side can walk |
| **Growth** | Reinvest 10% of gross into marketing |

See `agreements/PARTNERSHIP-TEMPLATE.md` for the ready-to-sign agreement.

### Option C: Hybrid
Setup fee ($1,500-$3,500) + smaller equity share (15-20%). Good middle ground.

---

## Repository Structure

```
├── craigslist/                             # CL posting automation (code)
│   ├── poster.py                           # Main posting script
│   └── ad_templates/templates.yaml         # Ad copy + rotation sets
│
├── facebook/                               # FB Marketplace automation (code)
│   ├── inbox_monitor.py                    # 5-min message checker + auto-responder
│   └── FB-MARKETPLACE-WORKAROUNDS.md       # Platform workarounds & gotchas
│
├── shared/                                 # Shared utilities (code)
│   ├── db.py                               # SQLite lead tracker
│   └── logger.py                           # Logging
│
├── config/                                 # Configuration
│   └── settings.yaml                       # Cities, proxies, schedules, business info
│
├── scripts/                                # Setup & utility scripts
│   ├── setup.sh                            # Install dependencies
│   └── test_proxy.py                       # Proxy connectivity test
│
├── agreements/                             # Ready-to-sign client agreements
│   ├── PARTNERSHIP-TEMPLATE.md             # Equity/revenue share agreement
│   └── RETAINER-TEMPLATE.md               # Monthly retainer agreement
│
├── offers/                                 # Detailed offer breakdowns
│   ├── OFFER-1-LEAD-RECOVERY-ENGINE.md     # Tier 1: $1,500 + $497/mo
│   ├── OFFER-2-GROWTH-MACHINE.md           # Tier 2: $3,500 + $997/mo
│   └── OFFER-3-AI-OPS-HUB.md              # Tier 3: $7,500 + $1,997/mo
│
├── lead-gen/                               # Lead generation playbooks
│   ├── FB-MARKETPLACE-PLAYBOOK.md          # Product-style workarounds for services
│   └── POSTING-SERVICES-GUIDE.md          # How to use CL posting services
│
├── outreach/                               # Direct outreach system
│   └── FREE-PLATFORMS-AND-OUTREACH.md      # 45+ free/cheap platforms + scripts
│
├── systems/                                # AI system specifications
│   ├── AI-RECEPTIONIST.md                  # 24/7 phone answering setup
│   ├── LEAD-FOLLOW-UP-ENGINE.md            # Automated follow-up sequences
│   ├── REVIEW-MANAGER.md                   # Review request + response automation
│   ├── AI-DISPATCHER.md                    # Job routing to right technician
│   ├── ESTIMATE-CLOSER.md                  # Estimate follow-up automation
│   ├── COLD-OUTREACH.md                    # AI outreach to PMs and investors
│   ├── CUSTOMER-LIFECYCLE.md               # Retention + reactivation
│   ├── SEASONAL-CAMPAIGNS.md               # Seasonal marketing automation
│   ├── NEIGHBORHOOD-TARGETING.md           # Just-finished-a-job canvassing
│   └── SYSTEMS-SPEC.md                     # Full technical architecture
│
├── sales/                                  # How to sell this to clients
│   ├── SALES-PLAYBOOK.md                   # Full sales process + scripts
│   ├── OBJECTION-HANDLING.md               # Word-for-word rebuttals
│   ├── EMAIL-SEQUENCES.md                  # Outreach email campaigns
│   ├── CASE-STUDY-TEMPLATES.md             # Results templates
│   ├── LEAD-GEN-MASTER-PLAN.md             # How to find clients
│   ├── MARKETPLACE-CHANNELS.md             # Platform comparison
│   └── CRAIGSLIST-SYSTEM.md                # CL for client acquisition
│
├── implementation/                         # Deployment guides
│   ├── IMPLEMENTATION-GUIDE.md             # Day-by-day deployment checklist
│   ├── ONBOARDING-CHECKLIST.md             # Client onboarding steps
│   └── TECH-STACK.md                       # Tools, costs, setup
│
├── infrastructure/                         # Reusable infrastructure templates
│   └── templates/                          # Security layers, self-healing pipeline
│
├── ICP-RESEARCH.md                         # Ideal client profile
├── PRICING-ECONOMICS.md                    # Unit economics and margins
└── BUSINESS-MODEL.md                       # Full vertical strategy
```

---

## Automation Code — Quick Start

```bash
# 1. Clone
git clone https://github.com/jbellsolutions/Home-Services-AI-Business.git
cd Home-Services-AI-Business

# 2. Install
pip install -r requirements.txt
playwright install chromium

# 3. Configure
cp config/.env.example .env
# Edit .env with your proxy credentials, FB login, etc.

# 4. Test proxy
python scripts/test_proxy.py

# 5. Run CL poster (single ad test)
python craigslist/poster.py --test

# 6. Run FB inbox monitor
python facebook/inbox_monitor.py
```

### Required Environment Variables
```
# Craigslist
CL_EMAIL=your-cl-email@example.com
CL_PASSWORD=your-cl-password
PROXY_HOST=us.residential.example.com
PROXY_PORT=10000
PROXY_USER=your-proxy-user
PROXY_PASS=your-proxy-pass

# Facebook
FB_EMAIL=your-fb-email@example.com
FB_PASSWORD=your-fb-password

# Notifications
NOTIFICATION_PHONE=+1234567890
```

### Automation Architecture
```
┌─────────────────────────────────────────────┐
│              ORCHESTRATOR (n8n)              │
│         Schedule + Monitor + Alert           │
├──────────────────┬──────────────────────────┤
│  ┌───────────┐   │   ┌──────────────────┐   │
│  │ CRAIGSLIST│   │   │ FB MARKETPLACE   │   │
│  │  POSTER   │   │   │  POSTER + INBOX  │   │
│  │ Playwright│   │   │ Browser Use /    │   │
│  │ + Proxy   │   │   │ Airtop           │   │
│  └─────┬─────┘   │   └────────┬─────────┘   │
│        │         │            │              │
│  ┌─────▼─────────▼────────────▼─────────┐   │
│  │         LEAD TRACKER (SQLite)         │   │
│  │  ads posted | responses | bookings    │   │
│  └───────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

**Safety & compliance:** Respects CL's 48-hour posting rule, unique ad content per post, human handoff for complex FB conversations, kill switch for immediate stop.

---

## Deploy to a New Client in 5 Days

### Day 1: Sign & Setup
- [ ] Sign agreement (use template from `agreements/`)
- [ ] Get client's business info (services, area, phone, photos)
- [ ] Set up Google Business Profile (if they don't have one)
- [ ] Set up tracking phone numbers (CallRail or Google Voice)

### Day 2: Lead Gen Launch
- [ ] Post 7 Craigslist ads (use `lead-gen/` playbooks + `craigslist/poster.py`)
- [ ] Post 7 Facebook Marketplace listings (use `lead-gen/FB-MARKETPLACE-PLAYBOOK.md`)
- [ ] Claim Nextdoor business page
- [ ] Sign up for Porch, Yelp, BuildZoom, Home Depot Pro Referral

### Day 3: AI Systems
- [ ] Deploy AI phone receptionist (see `systems/AI-RECEPTIONIST.md`)
- [ ] Start `facebook/inbox_monitor.py` for auto-responses (5-min cycle)
- [ ] Configure lead follow-up sequences
- [ ] Set up review request automation

### Day 4: Outreach
- [ ] Pull list of local property managers — start cold calling
- [ ] Pull recent home buyers from county records — prep outreach
- [ ] Identify contractor partnership opportunities
- [ ] Post on free classified sites (Locanto, ClassifiedAds, Geebo)

### Day 5: Optimize & Monitor
- [ ] Review first leads coming in
- [ ] Adjust ad copy based on response rates
- [ ] Ensure phone system is catching all calls
- [ ] Set up lead tracking spreadsheet or CRM
- [ ] Weekly check-in call with client

---

## Works For Any Home Services Trade

- Handyman / General Repair · Wildlife Removal · Roof Repair · Property Maintenance
- HVAC · Plumbing · Electrical · Landscaping / Lawn Care
- Cleaning (Residential & Commercial) · Painting · Pest Control
- Garage Door · Fencing / Decking · Pressure Washing

Just swap the service name in `config/settings.yaml`, update the ad templates, and deploy.

---

## First Case Study: Jacksonville Handyman

**Client:** Handyman & property maintenance startup in Jacksonville, FL
**Structure:** Partnership model — 35/65 split
**Services:** Wildlife removal, roof repair, handyman, on-call property maintenance
**Lead gen:** Craigslist (7 ads/day) + Facebook Marketplace + Nextdoor + direct outreach
**90-day target:** 10 field workers, $30-50K/month gross revenue

See the full deployment in the [Handyman-Home-Services-Model](https://github.com/jbellsolutions/Handyman-Home-Services-Model) repo.
