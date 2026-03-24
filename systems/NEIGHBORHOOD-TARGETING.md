# Neighborhood Targeting System — Technical Specification

## Purpose
After every completed job, automatically market to 25-50 nearby homes. "We just serviced your neighbor's [AC/plumbing/roof]. Want us to check yours while we're in the area?"

---

## Why This Works

- Neighbors trust neighbors. Seeing a branded truck on the street is social proof.
- "While we're in the area" reduces perceived urgency to decide now while making it convenient
- Proximity = lower travel cost for the company (better unit economics)
- Response rate on neighborhood campaigns: 3-8% (vs. 1-2% on cold marketing)
- Cost per lead: $5-$15 (vs. $50-$150 on Google Ads)

---

## System Flow

```
Job Completed in CRM
        │
        ▼
Extract job address + service type
        │
        ▼
Generate 25-50 nearest home addresses
(USPS address database / Google Maps API)
        │
        ▼
Create campaign (text to past customers nearby + digital ad + optional direct mail)
        │
        ├── Past customers within 1 mile → Text message
        ├── Facebook/Instagram → Geo-targeted ad (1-mile radius)
        └── Optional: Direct mail postcards to 25-50 homes
        │
        ▼
Track responses → Route to booking system
```

---

## Campaign Channels

### Channel 1: Text to Past Customers Nearby
- Pull all past customers within 1 mile of the completed job
- Text: "Hey [Name], we're in your neighborhood this week doing [service] work. If you need anything — tune-up, repair, inspection — we can swing by while we're nearby. Reply YES for a free estimate."
- Response → route to booking flow

### Channel 2: Facebook/Instagram Geo-Targeted Ads
- Create micro-targeted ad: 1-mile radius around the job address
- Ad copy: "We just [serviced/installed/repaired] [service] for a homeowner on [street name]. Need [trade] work done? We're in your area this week."
- Budget: $10-$25 per campaign (runs for 3-5 days)
- CTA: "Book a free estimate" → landing page or phone call

### Channel 3: Direct Mail Postcards (Optional)
- Print + mail postcards to 25-50 nearest homes
- Front: "[Company] truck photo + 'We just serviced your neighbor's [AC/plumbing/roof]'"
- Back: Offer + QR code to book + phone number
- Cost: $0.75-$1.50 per postcard
- Total per campaign: $20-$75

---

## Message Templates by Trade

### HVAC
```
"We just completed an AC tune-up for a homeowner on [Street Name]. 🏠
If your AC hasn't been serviced this year, now's the time — we can
stop by while we're in the neighborhood. Free diagnostic with any
tune-up this week. [booking link]"
```

### Plumbing
```
"We just finished a plumbing repair on [Street Name]. 🔧 If you've
been dealing with a slow drain, running toilet, or any plumbing
issues — we're right around the corner this week. $50 off any
service. [booking link]"
```

### Roofing
```
"We just completed a roof inspection on [Street Name]. 🏠 After
the recent storms, it's a good idea to check for damage. We're
offering FREE roof inspections this week for homeowners in your
area. [booking link]"
```

### Electrical
```
"We just upgraded the electrical panel at a home on [Street Name]. ⚡
If your home is 20+ years old, your panel might be outdated. Free
safety inspection while we're in your neighborhood. [booking link]"
```

---

## Automation Trigger

### CRM Integration
When job status = "Completed" in ServiceTitan/HCP/Jobber:
1. Pull job address
2. Pull service type
3. Check: is this a residential service? (skip commercial)
4. Check: is this address in our campaign-eligible zone? (avoid repeat campaigns within 30 days at same location)
5. If eligible → generate campaign

### Address Proximity Lookup
- Use Google Maps Geocoding API to get lat/long of job address
- Query USPS address database or Smarty Streets API for 25-50 nearest residential addresses
- Exclude apartments/condos (optional, based on client preference)
- Filter out addresses of existing customers (they get the text message instead)

---

## Budget Per Campaign

| Component | Cost | Notes |
|-----------|------|-------|
| Text messages to past customers | $0.50-$2.00 | 5-20 texts at $0.0079 each |
| Facebook/Instagram ad | $10-$25 | 3-5 day campaign, 1-mile radius |
| Direct mail postcards (optional) | $20-$75 | 25-50 postcards |
| **Total per campaign** | **$11-$100** | |

**At 20 jobs/week = 20 campaigns/month:**
- Without mail: $220-$500/month
- With mail: $620-$2,000/month

**Revenue per campaign (conservative):**
- 3-8 responses per campaign
- 50% booking rate = 1.5-4 jobs
- At $350 avg = $525-$1,400 per campaign
- **20 campaigns/month = $10,500-$28,000 in additional revenue**

---

## Performance Metrics

| Metric | Target |
|--------|--------|
| Campaigns launched/month | 15-25 (based on job volume) |
| Text response rate | 8-15% |
| Ad click-through rate | 2-5% |
| Postcard response rate | 1-3% |
| Jobs booked per campaign | 1.5-4 |
| Revenue per campaign | $525-$1,400 |
| Cost per lead | $5-$15 |
| ROI per campaign | 5-14x |

---

## Privacy and Compliance

- Past customer texts: Existing business relationship + prior consent = compliant
- Facebook/Instagram ads: Standard advertising, fully compliant
- Direct mail: USPS mail is not regulated like digital marketing
- Never share customer names or specific job details (use "a homeowner on [Street]" not "[Name]'s house")
- Opt-out respected on all text communications
