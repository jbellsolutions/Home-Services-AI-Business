# Systems Specification — Technical Architecture

## Overview

Every client deployment consists of modular AI systems that connect to their existing tools. The core philosophy: **we don't replace their software, we make it work harder.**

---

## System Architecture

```
                    ┌─────────────────────────────┐
                    │     Client's Customers       │
                    │  (Homeowners, Property Mgrs)  │
                    └──────────┬──────────────────┘
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
       ┌────▼────┐      ┌─────▼─────┐     ┌─────▼─────┐
       │  Phone  │      │   Text    │     │  Web Form │
       │  Calls  │      │   /SMS    │     │  /Chat    │
       └────┬────┘      └─────┬─────┘     └─────┬─────┘
            │                  │                  │
            ▼                  ▼                  ▼
    ┌───────────────────────────────────────────────┐
    │           AI RECEPTIONIST LAYER                │
    │  Vapi/Bland (voice) + Twilio (SMS) + Custom   │
    │  ─ Answers calls, responds to texts/forms      │
    │  ─ Captures lead info                          │
    │  ─ Books appointments                          │
    │  ─ Transfers emergencies to owner              │
    └──────────────────┬────────────────────────────┘
                       │
                       ▼
    ┌───────────────────────────────────────────────┐
    │            LEAD MANAGEMENT ENGINE              │
    │  ─ Speed-to-lead (< 60 sec response)          │
    │  ─ Follow-up sequences (5-14 day drip)        │
    │  ─ Estimate follow-up (30-day recovery)       │
    │  ─ Lead scoring (hot/warm/cold)               │
    └──────────────────┬────────────────────────────┘
                       │
                       ▼
    ┌───────────────────────────────────────────────┐
    │              CRM INTEGRATION                   │
    │  ServiceTitan / Housecall Pro / Jobber / GoHLC │
    │  ─ Sync contacts, appointments, job status     │
    │  ─ Trigger automations on job completion       │
    │  ─ Pull estimate data for follow-up            │
    └──────────────────┬────────────────────────────┘
                       │
            ┌──────────┼──────────┐
            │          │          │
            ▼          ▼          ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐
    │  Review  │ │ Seasonal │ │  Cold    │
    │  Engine  │ │ Campaign │ │ Outreach │
    │          │ │  Engine  │ │  Engine  │
    └──────────┘ └──────────┘ └──────────┘
```

---

## Module 1: AI Receptionist

### Voice (Inbound Calls)
**Stack:** Vapi.ai or Bland.ai

**How it works:**
1. Call comes in → forwarded to AI phone number (or SIP integration)
2. AI answers: "Hi, thanks for calling [Company Name]! I'm [Name], how can I help you today?"
3. Gathers: Name, address, phone, email, service needed, urgency
4. Checks calendar availability and books appointment
5. Emergency detection → transfers to owner's cell immediately
6. Sends confirmation text to caller with appointment details
7. Creates lead record in CRM

**Configuration per client:**
- Business name, greeting style, personality
- Service menu (what they offer, what they don't)
- Service area boundaries
- Pricing guidance (ranges, not exact quotes)
- Emergency keywords and escalation number
- Business hours vs after-hours behavior
- Spanish language toggle

**Cost:** $0.05-$0.15/minute (Vapi) or $0.09/minute (Bland)
**Average call:** 2-3 minutes = $0.10-$0.45/call
**Monthly cost per client:** $15-$75 (based on call volume)

### Text/SMS
**Stack:** Twilio

**Triggers:**
- Missed call → instant text back within 30 seconds
- Web form submission → text confirmation
- GBP message → auto-reply
- Facebook message → auto-reply

**Cost:** $0.0079/text (Twilio)
**Monthly cost per client:** $5-$20

### Web Form/Chat
**Stack:** Custom webhook + Twilio/SendGrid

**How it works:**
1. Website form submission triggers webhook
2. AI processes the request
3. Sends text + email confirmation within 60 seconds
4. Creates CRM record
5. Starts follow-up sequence

---

## Module 2: Lead Follow-Up Engine

### Multi-Channel Sequences
**Stack:** n8n or Make.com for orchestration + Twilio + SendGrid

**Default Sequence (New Lead):**
| Touchpoint | Timing | Channel | Message |
|-----------|--------|---------|---------|
| 1 | Instant | Text | "Thanks for contacting [Company]. We got your request for [service]. Confirming your appointment for [date/time]." |
| 2 | 1 hour | Email | Welcome email with company info, what to expect |
| 3 | Day 1 | Text | "Your appointment is tomorrow. Any questions? Reply here." |
| 4 | Day 3 | Text | Follow-up if no appointment booked: "Still need help with [service]?" |
| 5 | Day 7 | Email | Value-add: seasonal tip, maintenance advice |
| 6 | Day 14 | Text | "Hey [Name], circling back on [service]. We have availability this week." |
| 7 | Day 30 | Email | Reactivation: special offer or seasonal tie-in |

### Estimate Follow-Up Sequence
| Touchpoint | Timing | Channel | Message |
|-----------|--------|---------|---------|
| 1 | 2 hours | Text | "Thanks for getting an estimate from [Company]. Questions? Reply here." |
| 2 | Day 2 | Text | "Ready to move forward with the [service] we quoted? We can schedule this week." |
| 3 | Day 5 | Email | Why this service matters + what happens if you wait |
| 4 | Day 10 | Text | Price incentive: "10% off if you book by [Friday]" |
| 5 | Day 21 | Email | Social proof: recent completed job in their area |
| 6 | Day 30 | Text | "Still thinking about [service]? We're running a [seasonal] special." |
| 7 | Day 60 | Email | Final reactivation attempt |

---

## Module 3: Review Management Engine

**Stack:** Google Business API + Yelp API + custom

**Post-Job Automation:**
1. Job marked complete in CRM → triggers review sequence
2. Wait 2 hours (customer has time to settle)
3. Text: "Thanks for choosing [Company]! Would you take 30 seconds to leave us a review? It really helps! [Google review link]"
4. If no review at 24 hours: Email reminder with same link
5. If no review at 72 hours: Second text (final ask)

**Review Response:**
- AI monitors Google, Yelp, Facebook for new reviews every 4 hours
- Positive reviews (4-5 stars): personalized thank you within same day
- Negative reviews (1-3 stars): empathetic response + escalation to owner
- Owner gets alert for all negative reviews immediately

**GBP Optimization:**
- Automated weekly posts (job photos, seasonal tips, offers)
- Q&A monitoring and responses
- Photo uploads from completed jobs

**Cost per client:** $10-$20/month (API costs)

---

## Module 4: Cold Outreach Engine (Tier 2+)

**Stack:** Instantly.io or Smartlead + Apollo + custom scraping

**Target Lists:**
- Property management companies (apartment complexes, HOAs, commercial)
- Real estate agents and brokerages
- General contractors who subcontract
- Facility managers
- Restaurant/retail chains

**Compliance:**
- CAN-SPAM compliant (unsubscribe, physical address, accurate headers)
- No residential emails for cold outreach
- B2B only (commercial accounts)
- Opt-out tracking and honoring within 24 hours

**Cost per client:** $20-$50/month (email sending + list building)

---

## Module 5: Seasonal Campaign Engine (Tier 2+)

**Stack:** n8n orchestration + SendGrid + Twilio

**Pre-built campaigns per trade loaded at onboarding. Each campaign includes:**
- Text blast template to past customers
- Email sequence (3-email series)
- Social media post drafts
- Google Ads copy suggestions
- Landing page template

**Trigger:** Automated based on calendar date (seasonal) or manual trigger (post-storm, etc.)

**Cost per client:** Included in Twilio/SendGrid costs above

---

## Module 6: AI Dispatcher (Tier 3 Only)

**Stack:** Custom logic + CRM API + Google Maps API

**Routing Logic:**
1. New job comes in with: type, location, urgency
2. System checks: which techs are qualified for this job type?
3. Filters by: who's available today? Who's closest?
4. Selects optimal tech based on: skill match > proximity > workload balance
5. Sends tech: job details, address, customer history, ETA
6. Sends customer: "Your technician [Name] is on the way"

**Integrations required:**
- ServiceTitan or Housecall Pro API (technician schedules, skills)
- Google Maps Distance Matrix API (drive time calculation)
- Twilio (tech + customer notifications)

**Cost per client:** $20-$40/month (API calls)

---

## Infrastructure Costs Per Client (Summary)

| Component | Monthly Cost |
|-----------|-------------|
| AI Voice (Vapi/Bland) | $15-$75 |
| SMS (Twilio) | $5-$20 |
| Email (SendGrid) | $5-$10 |
| CRM Integration hosting | $5-$10 |
| Review management APIs | $10-$20 |
| Cold outreach (Tier 2+) | $20-$50 |
| Dispatcher APIs (Tier 3) | $20-$40 |
| n8n/Make hosting (shared) | $5-$10 |
| **Total Tier 1** | **$45-$145** |
| **Total Tier 2** | **$80-$215** |
| **Total Tier 3** | **$120-$305** |

### Margin Analysis
| Tier | Monthly Price | Avg COGS | Gross Margin |
|------|-------------|----------|-------------|
| Tier 1 ($497) | $497 | $95 | 81% |
| Tier 2 ($997) | $997 | $150 | 85% |
| Tier 3 ($1,997) | $1,997 | $215 | 89% |

---

## Tech Stack Summary

| Function | Tool | Why |
|----------|------|-----|
| Voice AI | Vapi.ai or Bland.ai | Best voice quality, lowest latency, easy config |
| SMS/Text | Twilio | Industry standard, reliable, good pricing |
| Email sending | SendGrid | High deliverability, easy templates |
| Cold email | Instantly.io | Built for cold email, warmup included |
| Email finding | Apollo.io | Best B2B email database |
| Automation | n8n (self-hosted) | Open source, unlimited workflows, no per-run fees |
| CRM connectors | Custom API integrations | ServiceTitan, Housecall Pro, Jobber |
| Review monitoring | Custom + Google Business API | Real-time monitoring, automated responses |
| Call tracking | CallRail or Twilio | Attribution, recording, analytics |
| Hosting | Railway or Render | Easy deploy, auto-scaling, reasonable cost |
| Database | Supabase or PostgreSQL | Lead tracking, analytics, state management |
| Monitoring | Better Uptime + custom | System health, alert if anything goes down |
