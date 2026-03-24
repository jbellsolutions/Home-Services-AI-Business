# Cold Outreach System — Technical Specification

## Purpose
Proactively reach out to high-value B2B prospects — property managers, realtors, general contractors, facility managers, and commercial accounts — to build a commercial revenue stream for the home services company.

---

## Why Commercial Outreach Matters

- Average residential job: $350-$1,500
- Average commercial account: $5,000-$50,000/year (recurring)
- One property management company can mean 50-200 units = $25,000-$100,000/year
- One realtor relationship = 5-15 referrals/year at $500-$2,000 each
- Commercial accounts are STICKY — they don't switch unless you mess up
- Most contractors NEVER proactively pursue commercial work — they wait for it to come to them

---

## Target Segments

### Segment 1: Property Management Companies
- **Volume:** 50-200 units per company
- **Need:** Regular maintenance, emergency repairs, unit turnovers
- **Value:** $10,000-$100,000/year per company
- **Pitch:** "One contractor for all your [HVAC/plumbing/electrical] needs. Priority response. Bulk pricing."
- **Where to find:** Google Maps ("property management [city]"), Apartments.com, Zillow Rental Manager, AppFolio customer directory

### Segment 2: Real Estate Agents
- **Volume:** 10-40 transactions/year per agent
- **Need:** Pre-listing inspections, buyer home inspections, repair referrals
- **Value:** $5,000-$30,000/year in referrals per agent
- **Pitch:** "Your clients need [HVAC/plumbing] work done fast. We do same-day and make you look good."
- **Where to find:** Realtor.com agent search, local MLS directories, RE/MAX/Keller Williams/Coldwell Banker offices

### Segment 3: General Contractors
- **Volume:** 5-20 projects/year
- **Need:** Subcontract [HVAC/plumbing/electrical] on new builds and remodels
- **Value:** $10,000-$50,000/year per GC relationship
- **Pitch:** "Licensed, insured, and we show up on time. Subcontract your [trade] to us."
- **Where to find:** State contractor license database, HomeAdvisor Pro, Angi Pro

### Segment 4: Facility Managers (Hotels, Restaurants, Retail)
- **Volume:** 1-10 locations per company
- **Need:** Maintenance contracts, emergency response, compliance inspections
- **Value:** $5,000-$25,000/year per location
- **Pitch:** "24/7 emergency response + quarterly maintenance. One call for all your [trade] needs."
- **Where to find:** Google Maps by category, LinkedIn (title: "Facility Manager"), industry directories

---

## Outreach Sequences

### Sequence 1: Property Managers (5 emails over 21 days)

**Email 1 — The Problem (Day 1)**
```
Subject: your HVAC vendor still making you wait?

Hey [Name],

Quick question — when one of your tenants at [property/company name] has
an AC emergency at 10 PM, how fast does your current HVAC contractor
respond?

We specialize in property management HVAC for the [city] area.
Here's what our PM clients get:
- Priority response (under 2 hours, 24/7)
- Bulk unit pricing (20-30% below retail)
- Monthly maintenance plans (prevent the emergencies)
- One invoice, all units

Managing [X] units means [trade] issues are constant. We make them
painless.

Worth a 10-minute call to see if we'd be a good fit?

— [Owner Name], [Company]
[Phone] | [License #]
```

**Email 2 — Social Proof (Day 5)**
```
Subject: how [similar PM company] cut their HVAC costs 25%

[Name], quick follow-up:

We started working with [PM company or "a 150-unit complex in [city]"]
last year. In 12 months:
- Emergency calls dropped 40% (preventive maintenance works)
- Average response time: 90 minutes (vs. 4-6 hours with their old vendor)
- Total HVAC spend down 25% (bulk pricing + fewer emergencies)

If your [trade] vendor isn't delivering that level of service, let's chat.

— [Owner Name]
```

**Email 3 — Value Add (Day 10)**
```
Subject: free HVAC audit for your properties

[Name], one more thought:

We offer a free HVAC system audit for property management companies.
We inspect up to 10 units, assess equipment condition, and give you
a written report with:
- Equipment age and remaining lifespan
- Energy efficiency ratings
- Maintenance recommendations
- Estimated costs for any needed repairs

No obligation. No sales pitch during the audit. Just useful data
for your maintenance planning.

Want me to schedule one?

— [Owner Name]
```

**Email 4 — Objection Handler (Day 15)**
```
Subject: not trying to replace your current vendor

[Name], I get it — switching contractors is a headache.

I'm not asking you to fire anyone. I'm asking: do you have a backup?

Because when your primary vendor is booked, on vacation, or just
can't make it at 11 PM... you need someone reliable on speed dial.

We'd be happy to start as your backup [trade] vendor. No commitment.
Just give us a call when your main guy can't make it.

Once you see our response time and quality, you might not need
that backup for long.

— [Owner Name]
```

**Email 5 — Walk-Away (Day 21)**
```
Subject: last note from me

[Name], this is my last email. If you're happy with your current
[trade] setup, respect that completely.

If anything changes — vendor drops the ball, prices go up, or
you just want a second option — here's my direct line: [phone].

We service [X] properties in the [city] area and we'd be glad
to add yours to the list.

Good luck with everything.

— [Owner Name], [Company]
```

---

## Prospect List Building

### Data Sources
| Source | Data Available | Cost |
|--------|---------------|------|
| Google Maps Scraper (Apify) | Name, address, phone, website, reviews | $50/mo |
| Apollo.io | Contact emails, company size, industry | $50-$100/mo |
| State License Database | Licensed contractors (for GC segment) | Free |
| LinkedIn Sales Navigator | Decision maker names, titles | $100/mo (optional) |
| Apartments.com | Property management companies | Free (manual) |
| Realtor.com | Agent names and contact info | Free (manual) |

### List Building Workflow
1. Scrape Google Maps for "property management [city]" → 200-500 results
2. Scrape for "real estate agent [city]" → 500-1,000 results
3. Scrape for "general contractor [city]" → 200-400 results
4. Enrich with Apollo for email addresses
5. Verify emails with NeverBounce/ZeroBounce
6. Score against ICP (company size, review count, location)
7. Segment into sequences by type

### Volume Targets
- 500 new prospects entered/month
- 100 property managers
- 200 realtors
- 100 general contractors
- 100 facility managers/commercial

---

## Performance Metrics

| Metric | Target |
|--------|--------|
| Emails sent/month | 2,000-3,000 |
| Open rate | 40-50% |
| Reply rate | 3-5% |
| Positive reply rate | 50% of replies |
| Meetings booked/month | 10-20 |
| Accounts closed/month | 3-5 |
| Avg annual value/account | $10,000-$25,000 |
| **Monthly pipeline value** | **$30,000-$125,000 annually** |

---

## Compliance

- CAN-SPAM: Business-to-business emails with opt-out in every email
- Use business email addresses only (not personal)
- Physical address in footer
- Clear "unsubscribe" link
- No deceptive subject lines
- B2B cold email is legal under CAN-SPAM when compliant
- Limit: 3-5 emails per prospect per sequence, then stop
