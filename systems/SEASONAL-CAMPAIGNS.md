# Seasonal Campaign Engine — Technical Specification

## Purpose
Pre-built, automated marketing campaigns that fire at the right time of year for each trade. Eliminate the feast/famine cycle by proactively filling the calendar during traditionally slow periods and maximizing revenue during peak seasons.

---

## The Problem
- Home services revenue is seasonal: 60-70% of annual revenue in 4-5 peak months
- Slow months = empty trucks, idle techs, cash flow crunch
- Most contractors do ZERO proactive marketing for slow seasons
- Those who do start too late (marketing in November for heating season that started in October)
- Result: feast/famine cycle year after year

## The Solution
Pre-loaded 12-month campaign calendar that automatically:
- Reaches out to past customers before each season
- Promotes maintenance agreements during shoulder seasons
- Runs emergency-response campaigns during peak weather events
- Fills gaps with targeted promotional offers

---

## HVAC Campaign Calendar

| Month | Campaign Name | Target Audience | Channel | Offer |
|-------|-------------|----------------|---------|-------|
| **Jan** | "Heating Emergency Ready" | All customers | Text + Email | "Heating emergency? We respond in 60 min. 24/7." |
| **Feb** | "Early Bird AC Tune-Up" | Past AC customers | Text + Email | "$79 AC tune-up (reg $129) — book before March" |
| **Mar** | "Spring AC Prep" | Full customer database | Email + FB ads | "Get your AC ready before the rush. Free thermostat check with tune-up." |
| **Apr** | "Last Chance Spring Special" | Non-responders from March | Text | "AC season starts soon. Last week for $79 tune-up pricing." |
| **May** | "Maintenance Agreement Push" | Customers without agreements | Email + Text | "Join our maintenance club: 2 tune-ups/year + priority service + 15% off repairs" |
| **Jun** | "Summer Survival Guide" | Full database | Email | Value content: energy savings tips + CTA for tune-up |
| **Jul** | "Beat the Heat" | New homebuyers (realtor referrals) | Direct mail + FB | "New home? Make sure your AC is running right. Free system evaluation." |
| **Aug** | "Back to School Comfort" | Families (inferred from service history) | Text + Email | "Make sure your home is comfortable for back-to-school. $50 off any repair." |
| **Sep** | "Early Bird Furnace Tune-Up" | Past heating customers | Text + Email | "$79 furnace tune-up (reg $129). Book before October." |
| **Oct** | "Winter Prep Campaign" | Full database | Email + FB ads + Text | "Don't wait for the first cold snap. Get your furnace inspected now." |
| **Nov** | "Holiday Comfort" | All customers | Email | "Hosting family? Make sure your home is warm. Priority scheduling available." |
| **Dec** | "Year-End Equipment Upgrade" | Customers with aging equipment | Email + Text | "Replace before Jan 1 — lock in this year's pricing + tax benefits." |

---

## Plumbing Campaign Calendar

| Month | Campaign | Offer |
|-------|---------|-------|
| **Jan** | Frozen pipe prevention | "Free pipe insulation inspection" |
| **Feb** | Valentine's plumbing special | "Show your home some love — full plumbing inspection $99" |
| **Mar** | Spring plumbing check | "Winter may have done damage. $49 whole-home plumbing inspection" |
| **Apr** | Water heater flush | "When's the last time your water heater was flushed? $79 flush + inspection" |
| **May** | Sump pump season | "Spring rain coming. Is your sump pump ready?" |
| **Jun** | Summer sewer special | "Camera inspection of your sewer line — $149 (find problems before they find you)" |
| **Jul** | Water quality month | "Free water quality test with any service" |
| **Aug** | Back to school | "Busy family? Last call for summer plumbing projects" |
| **Sep** | Fall prep | "Winterize your outdoor faucets before the freeze" |
| **Oct** | Drain cleaning | "Pre-holiday drain cleaning — $99 (avoid Thanksgiving disasters)" |
| **Nov** | Holiday hosting prep | "Having guests? Make sure your plumbing can handle the traffic" |
| **Dec** | Year-end maintenance | "End the year with a full plumbing checkup. 20% off through Dec 31" |

---

## Roofing Campaign Calendar

| Month | Campaign | Offer |
|-------|---------|-------|
| **Mar-May** | Post-storm season | "Free storm damage inspection — we work with all insurance companies" |
| **Jun-Aug** | Pre-fall booking | "Book your roof replacement now — beat the fall rush. Free upgrade to premium shingles" |
| **Sep-Oct** | Winter prep | "Gutter cleaning + roof inspection package — $199" |
| **Nov-Dec** | Emergency storm prep | "Winter storm coming? Free emergency tarp service for existing customers" |
| **Year-round** | Anniversary reminders | "It's been [X] years since we installed your roof. Time for an inspection?" |

---

## Campaign Execution System

### Automation Workflow (per campaign)

```
30 days before campaign launch:
  → Generate customer segment (past customers matching criteria)
  → Create personalized message variants (2-3 for A/B testing)
  → Load into automation platform (n8n/Make)

Campaign launch day:
  → Send text blast (batch of 100-200/day to stay under rate limits)
  → Send email campaign
  → Launch Facebook/Instagram ad (if applicable)
  → Activate landing page

During campaign (2-4 weeks):
  → Monitor responses, route to booking system
  → Send follow-up to non-responders (Day 3, Day 7)
  → Track bookings attributed to campaign
  → Adjust messaging based on early results

Campaign close:
  → Generate performance report
  → Archive campaign data
  → Feed results into next campaign optimization
```

### Message Personalization
Each campaign message includes:
- Customer first name
- Last service date and type
- Equipment age (if tracked)
- Their specific neighborhood/area
- Personalized urgency (e.g., "Your furnace was installed in 2015 — that's 11 years ago")

---

## Technical Requirements

| Component | Tool | Function |
|-----------|------|----------|
| Campaign scheduling | n8n/Make | Triggers campaigns on calendar dates |
| Customer segmentation | CRM API | Pulls customer lists by criteria |
| Text blasts | Twilio | Sends SMS campaigns |
| Email campaigns | SendGrid/ActiveCampaign | Sends email campaigns |
| Facebook/Instagram ads | Meta Ads API | Creates and manages geo-targeted ads |
| Landing pages | Custom or Carrd | Campaign-specific booking pages |
| Tracking | UTM params + CRM attribution | Tracks bookings from each campaign |

---

## Performance Benchmarks

| Metric | Text Campaign | Email Campaign | Facebook Ads |
|--------|-------------|---------------|-------------|
| Delivery rate | 98% | 95% | N/A |
| Open/view rate | 98% (texts) | 30-45% | 2-5% CTR |
| Response/click rate | 5-12% | 3-8% | 2-5% |
| Booking rate | 3-6% of sends | 1-3% of sends | 0.5-1% of impressions |
| Cost per booking | $2-$5 | $1-$3 | $15-$40 |
| ROI | 20-50x | 30-70x | 5-15x |

---

## Revenue Impact

**For a $2M HVAC company with 3,000 past customers:**

| Campaign | Audience | Response Rate | Bookings | Revenue |
|---------|---------|-------------|----------|---------|
| Spring AC tune-up | 1,500 AC customers | 6% = 90 responses | 60 bookings | $4,740 |
| Fall furnace tune-up | 1,200 heating customers | 6% = 72 responses | 48 bookings | $3,792 |
| Maintenance agreement push | 2,500 without agreement | 3% = 75 responses | 30 sign-ups | $5,970/yr recurring |
| Quarterly equipment upgrade | 200 aging systems | 8% = 16 responses | 6 replacements | $42,000 |
| **Annual total from seasonal campaigns** | | | | **$56,500+** |

**Cost: included in Tier 2 monthly fee. Incremental cost per campaign: $50-$200 (mostly ad spend)**
