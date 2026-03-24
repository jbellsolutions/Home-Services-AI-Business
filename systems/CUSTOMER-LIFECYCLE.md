# Customer Lifecycle Manager — Technical Specification

## Purpose
Turn one-time customers into lifetime clients through automated maintenance reminders, seasonal outreach, loyalty programs, and retention campaigns. Most home services companies lose 40-60% of customers after the first job because they never reach out again.

---

## The Lifetime Value Problem

- Average homeowner needs HVAC service 1-2x/year (tune-ups, repairs)
- Average homeowner stays in a home 8-13 years
- Potential lifetime value of one HVAC customer: $15,000-$35,000
- **Reality:** Most companies capture 1-2 transactions, then lose them forever
- Cost to acquire a new customer: $150-$300
- Cost to retain an existing customer: $5-$15
- Retained customers spend 67% more than new customers

---

## Lifecycle Stages

```
New Customer → Active Customer → Maintenance Member → Loyal Advocate → Equipment Upgrade
     │              │                    │                    │                │
  Onboarding   Regular touch       Renewal reminders    Referral program   Replacement
  sequence     (seasonal +          + value adds        + VIP perks        planning
               maintenance)                                                + financing
```

### Stage 1: New Customer Onboarding (Day 0-30)

| Day | Channel | Message |
|-----|---------|---------|
| 0 | Text | "Welcome to the [Company] family! Your [service] is complete. Here's your warranty info: [link]" |
| 1 | Email | Welcome email: company story, what to expect, maintenance tips, emergency number |
| 3 | Text | Review request (handled by Review Manager system) |
| 7 | Email | "5 tips to get the most out of your [new AC/plumbing fix/etc.]" |
| 14 | Text | "Everything still working great with your [service]? Any questions?" |
| 30 | Email | Maintenance agreement offer: "Join our maintenance club for priority service + discounts" |

### Stage 2: Active Customer (Ongoing)

**Quarterly touches:**
- Q1: "Spring is coming — time for [seasonal service]?"
- Q2: "Summer check-in — is your [equipment] running well?"
- Q3: "Fall prep — get ready for [heating season / storm season]"
- Q4: "Year-end: any projects you've been putting off? Book before the new year"

**Anniversary touches:**
- Service anniversary: "It's been 1 year since we [installed/repaired] your [equipment]. Time for a checkup?"
- Equipment age milestones: "Your [AC unit] is now 8 years old. Average lifespan is 15-20 years. Here's what to watch for..."

**Event-triggered touches:**
- Weather event (heat wave, freeze, storm): "Extreme weather alert: [tips to protect your home]. Need emergency service? Call [number]"
- Rate change: "Energy costs are going up this summer. A tune-up can save you 10-15% on your bill"

### Stage 3: Maintenance Agreement Member

**Monthly value:**
```
Month 1: Welcome + what's included
Month 2: Energy-saving tip
Month 3: "Your spring tune-up is due — scheduling now"
Month 4: Exclusive member discount on [seasonal service]
Month 5: "Did you know your membership includes [benefit]?"
Month 6: Mid-year check: "Everything running smoothly?"
Month 7: Referral bonus offer (member-exclusive)
Month 8: "Your fall tune-up is coming up — we'll text you to schedule"
Month 9: Scheduling fall tune-up
Month 10: Post-tune-up: equipment health report
Month 11: Renewal reminder (30 days out)
Month 12: Renewal: "Your membership renews [date]. Here's what you saved this year: $[amount]"
```

### Stage 4: Loyal Advocate

Customers who:
- Have been with you 2+ years
- Left 2+ positive reviews
- Referred at least 1 person

**VIP treatment:**
- Priority scheduling (same-day for any issue)
- Annual "thank you" gift (branded item, gift card, small service credit)
- First access to new services or promotions
- Personal call from owner on service anniversary
- Referral bonus: $75 (vs. $50 for regular customers)

### Stage 5: Equipment Upgrade Pipeline

**For equipment approaching end of life (10-15 years for HVAC, 8-12 for water heaters):**

| Year | Message |
|------|---------|
| Year 10 | "Your [equipment] is 10 years old. Still has 5-10 years, but here's what to watch for..." |
| Year 12 | "Your [equipment] is 12 years old. Repair costs start to increase around this age. Something to think about..." |
| Year 14 | "Your [equipment] is 14 years old. We're offering [trade-in/upgrade] deals this season. Worth a conversation?" |
| Year 15 | "Your [equipment] has served you well for 15 years. When you're ready to upgrade, we have 0% financing available." |
| After any repair on old unit | "Today's repair was $[amount]. Your unit is [age] years old. For context, a new system costs $[range] and comes with [warranty]. Want to explore options?" |

---

## Maintenance Agreement System

### The Offer
**"[Company] Comfort Club" — $199/year (or $17.99/month)**
- 2 tune-ups per year (spring AC + fall heating)
- Priority scheduling (you go to the front of the line)
- 15% off all repairs
- No overtime charges (even nights/weekends)
- Annual equipment health report
- Transferable if you sell your home

### Why This Matters for the Business
- Recurring revenue: $199/year × 200 members = $39,800/year
- Guaranteed twice-yearly visit = upsell opportunity (tech finds issues during tune-up)
- Retention rate of agreement members: 85-90% (vs. 40-50% for non-members)
- Members spend 2.5x more annually than non-members

### AI-Driven Agreement Sales
- After every completed job: "Would you like to join our Comfort Club? Your [today's service] would have been [discount]% off."
- After every positive review: "Thanks for the kind words! As a thank-you, we'd like to offer you first-year Comfort Club at $149 (save $50)."
- Seasonal pushes: "Pre-season special: join the Comfort Club and get your first tune-up FREE"
- Renewal automation: 30/15/7/1 day reminders before expiration

---

## Technical Stack

| Component | Tool | Function |
|-----------|------|----------|
| Customer database | CRM (ServiceTitan/HCP/Jobber) | Customer history, equipment data, agreements |
| Lifecycle automation | n8n/Make | Triggers sequences based on dates and events |
| Text messages | Twilio | Sends lifecycle texts |
| Email campaigns | SendGrid/ActiveCampaign | Sends lifecycle emails |
| Equipment tracking | CRM custom fields | Age, brand, model, install date, warranty expiry |
| Weather triggers | WeatherAPI | Triggers weather-event campaigns |
| Agreement management | CRM + custom | Tracks agreement status, renewals, benefits used |

---

## Data Requirements Per Customer

```
{
  "customer_id": "cust_1234",
  "name": "John Smith",
  "phone": "(813) 555-1234",
  "email": "john@email.com",
  "address": "123 Oak St, Tampa FL 33609",
  "first_service_date": "2023-06-15",
  "total_jobs": 4,
  "total_spend": "$2,847",
  "equipment": [
    {
      "type": "Central AC",
      "brand": "Carrier",
      "model": "24ACC636",
      "install_date": "2018-03-20",
      "age_years": 8,
      "warranty_expiry": "2028-03-20"
    },
    {
      "type": "Furnace",
      "brand": "Carrier",
      "model": "59TP6",
      "install_date": "2018-03-20",
      "age_years": 8
    }
  ],
  "maintenance_agreement": {
    "status": "active",
    "plan": "comfort_club",
    "renewal_date": "2026-06-15",
    "tune_ups_used": 1,
    "tune_ups_remaining": 1
  },
  "lifecycle_stage": "maintenance_member",
  "reviews_left": 2,
  "referrals_made": 1,
  "last_contact": "2026-02-10",
  "next_scheduled_touch": "2026-04-01"
}
```

---

## Performance Metrics

| Metric | Target | Industry Average |
|--------|--------|-----------------|
| Customer retention (annual) | 70-80% | 40-50% |
| Maintenance agreement conversion | 25-35% of customers | 5-10% |
| Agreement renewal rate | 85-90% | N/A (most don't have agreements) |
| Annual revenue per customer | $800-$1,200 | $350-$500 |
| Referral rate | 15-20% of customers | 3-5% |
| Equipment upgrade capture rate | 60-70% (their own customers) | 30-40% |
| Customer lifetime (years) | 8-12 | 1-3 |
| Lifetime value | $8,000-$15,000 | $500-$1,500 |

---

## Revenue Impact

**For a company with 2,000 past customers:**

| Initiative | Revenue Impact |
|-----------|---------------|
| Maintenance agreements (400 members × $199/yr) | $79,600/year |
| Seasonal campaigns to past customers | $56,000/year |
| Equipment upgrades (captured via lifecycle) | $120,000/year |
| Referrals from loyal advocates | $35,000/year |
| Reduced customer acquisition (higher retention) | $30,000/year saved |
| **Total lifecycle value** | **$320,600/year** |

**This is revenue from customers you already have. Zero acquisition cost.**
