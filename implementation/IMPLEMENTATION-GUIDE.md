# Implementation Guide — Client Onboarding & Deployment

## Onboarding Process (Day-by-Day)

---

## Pre-Onboarding (Before Day 1)

### What the Client Provides at Signing
1. Business name, address, service area (zip codes or radius)
2. Services offered (full menu with approximate pricing ranges)
3. Business phone number(s)
4. Owner's cell phone (for emergency escalation)
5. CRM login (ServiceTitan, Housecall Pro, Jobber — or confirmation they don't have one)
6. Google Business Profile access (owner email)
7. Website URL
8. Number of technicians and their specialties
9. Current scheduling availability / business hours
10. Logo and any brand guidelines
11. Signed agreement + setup payment collected

### What We Prepare Before the Onboarding Call
- [ ] Create client folder in project management system
- [ ] Provision Twilio phone number(s) for their area code
- [ ] Set up Vapi/Bland AI voice agent template for their trade
- [ ] Create n8n workflow instance
- [ ] Set up monitoring dashboard
- [ ] Research their top 3 competitors (reviews, response time, online presence)

---

## Day 1: The Onboarding Call (60 minutes)

### Agenda
1. **Welcome + expectations** (5 min)
   - What they'll see in the first 7 days
   - How to reach us (support channel, response time)
   - Monthly reporting cadence

2. **Business deep-dive** (20 min)
   - Walk through their service menu in detail
   - Discuss pricing (what can the AI quote? What needs a tech visit first?)
   - Emergency vs standard service definitions
   - Common customer questions and how they answer them
   - Seasonal patterns specific to their business

3. **Technical setup** (20 min)
   - Verify CRM access
   - Set up call forwarding (or SIP trunk if VoIP)
   - Verify Google Business Profile access
   - Set up review platform connections
   - Test phone system (live call to verify forwarding)

4. **Customization** (15 min)
   - AI receptionist greeting (what personality/tone?)
   - After-hours behavior (book for next day? Emergency transfer?)
   - Review request timing and messaging preferences
   - Any no-go topics (things the AI should never say/promise)

### Deliverables from Day 1
- [ ] CRM connected and syncing
- [ ] Phone forwarding configured
- [ ] AI receptionist personality and greeting scripted
- [ ] Service menu loaded into AI knowledge base
- [ ] Emergency escalation rules set
- [ ] Client has our support contact info

---

## Day 2-3: Core System Build

### AI Receptionist Configuration
- [ ] Load business info into AI voice agent
- [ ] Configure call flow (greeting → intake → booking → confirmation)
- [ ] Set up emergency detection keywords ("leak," "no heat," "no AC," "gas smell")
- [ ] Configure Spanish language option (if requested)
- [ ] Set business hours vs after-hours routing
- [ ] Build FAQ responses for common questions
- [ ] Connect to calendar/scheduling system

### SMS Automation Setup
- [ ] Configure missed-call text-back (30-second trigger)
- [ ] Build web form auto-response
- [ ] Set up GBP message auto-reply
- [ ] Create appointment reminder sequences
- [ ] Test all SMS flows end-to-end

### Email Automation Setup
- [ ] Configure welcome email template
- [ ] Build appointment confirmation email
- [ ] Set up estimate delivery format
- [ ] Create follow-up email templates

---

## Day 4-5: Follow-Up Sequences + Reviews

### Lead Follow-Up Engine
- [ ] Build new lead sequence (7-touch, 30-day)
- [ ] Build estimate follow-up sequence (7-touch, 60-day)
- [ ] Configure lead scoring rules
- [ ] Set up hot lead alerts (text to owner)
- [ ] Connect sequences to CRM triggers

### Review Management
- [ ] Connect Google Business Profile API
- [ ] Build post-job review request sequence
- [ ] Configure AI review response templates
- [ ] Set up negative review alerts
- [ ] Schedule first GBP post

---

## Day 6-7: Testing

### Test Checklist (MUST complete before go-live)
- [ ] **Phone test x20:** Call from 20 different numbers at different times
  - During business hours
  - After hours
  - Weekend
  - Emergency scenario
  - Spanish language (if enabled)
  - Transfer to owner's cell
  - Multiple calls simultaneously
- [ ] **SMS test x10:** Trigger missed call text-back, web form response
- [ ] **Email test x5:** Verify welcome email, confirmation, follow-up
- [ ] **CRM sync test:** Verify leads appear in CRM correctly
- [ ] **Appointment booking test:** Verify calendar integration works
- [ ] **Review request test:** Simulate job completion, verify review text sends
- [ ] **Review response test:** Post test review, verify AI responds
- [ ] **Emergency escalation test:** Verify owner gets emergency calls

### Quality Standards
- AI voice quality: Clear, natural, no robotic artifacts
- Response accuracy: Correctly identifies service type 95%+ of the time
- Booking accuracy: Correct date/time/service in calendar
- Transfer speed: Emergency transfer in under 10 seconds
- Text delivery: Under 30 seconds from trigger
- CRM sync: Under 2 minutes from call end

---

## Day 8-10: Go-Live + Monitoring

### Go-Live Checklist
- [ ] All tests passed
- [ ] Client approved the AI greeting (listened to recording)
- [ ] Client confirmed emergency escalation works
- [ ] Activate call forwarding to AI system
- [ ] Enable all automated sequences
- [ ] Turn on review management

### First 48-Hour Monitoring
- [ ] Monitor every call in real-time (listen to recordings)
- [ ] Check all SMS deliveries
- [ ] Verify CRM entries are accurate
- [ ] Track response times
- [ ] Note any AI mistakes or confusion points
- [ ] Immediate fix for any issues found

### Day 10: First Check-In Call (15 min)
- Review first week stats: calls handled, leads captured, appointments booked
- Address any issues or concerns
- Get client feedback on AI voice/personality
- Make adjustments based on real-world data

---

## Day 14-21: Tier 2 Additions (If Applicable)

### Cold Outreach Setup
- [ ] Build prospect list (property managers, realtors in their area)
- [ ] Configure outreach sequences
- [ ] Set up dedicated email domain for outreach
- [ ] Launch first campaign at 50% volume
- [ ] Monitor responses and flag warm leads

### Neighborhood Targeting
- [ ] Connect to job completion triggers in CRM
- [ ] Build neighborhood campaign templates
- [ ] Set up geo-targeting for digital ads (if applicable)
- [ ] Test with first completed job

### Estimate Follow-Up
- [ ] Connect to estimate/quote system in CRM
- [ ] Build recovery sequences
- [ ] Set up incentive offers (10% off, seasonal specials)
- [ ] Launch for all unsold estimates from last 30 days

### Seasonal Campaigns
- [ ] Load all pre-built campaigns for their trade
- [ ] Schedule current season's campaign
- [ ] Queue next season's campaign
- [ ] Set up past-customer database for blasts

---

## Ongoing Operations (Post-Launch)

### Weekly Tasks (Automated + Manual)
| Task | Who | Time |
|------|-----|------|
| Review call recordings (10% spot check) | Systems Builder | 30 min |
| Adjust AI responses based on patterns | Systems Builder | 15 min |
| Publish GBP posts | Automated | 0 min |
| Respond to reviews | Automated | 0 min |
| Monitor system health | Automated + alert | 0 min |

### Monthly Tasks
| Task | Who | Time |
|------|-----|------|
| Generate ROI report | Automated | 0 min |
| Monthly strategy call with client | Account Manager | 15 min |
| Sequence optimization | Systems Builder | 30 min |
| Review competitive landscape | Automated | 0 min |
| Update seasonal campaigns | Systems Builder | 15 min |

### Quarterly Tasks
| Task | Who | Time |
|------|-----|------|
| Full system audit | Systems Builder | 1 hour |
| Client satisfaction survey | Automated | 0 min |
| Upsell evaluation | Account Manager | 15 min |
| Competitive intel update | Automated | 0 min |

---

## Client Dashboard

Every client gets a dashboard showing:
- **Calls handled** (this week, this month, all-time)
- **Response time** (average, fastest, slowest)
- **Leads captured** (total, by source)
- **Appointments booked** (total, conversion rate)
- **Estimates followed up** (total, recovery rate, revenue recovered)
- **Reviews generated** (count, average rating, response time)
- **Revenue impact** (estimated revenue recovered/added)
- **System uptime** (should always be 99.9%+)

Delivered as: Weekly email summary + live web dashboard

---

## Onboarding Checklist (Copy-Paste for Each New Client)

```
## [Company Name] — Onboarding Tracker

### Pre-Onboarding
- [ ] Agreement signed
- [ ] Setup fee collected
- [ ] CRM access received
- [ ] Phone numbers provided
- [ ] GBP access granted
- [ ] Service menu documented
- [ ] Twilio number provisioned
- [ ] AI agent template created

### Day 1: Onboarding Call
- [ ] Call completed
- [ ] Business deep-dive documented
- [ ] CRM connected
- [ ] Phone forwarding configured
- [ ] AI greeting approved

### Day 2-5: System Build
- [ ] AI receptionist configured
- [ ] SMS automation live
- [ ] Email automation live
- [ ] Follow-up sequences built
- [ ] Review system connected
- [ ] Estimate follow-up active

### Day 6-7: Testing
- [ ] 20 phone tests passed
- [ ] 10 SMS tests passed
- [ ] 5 email tests passed
- [ ] CRM sync verified
- [ ] Emergency transfer verified
- [ ] Client approved AI quality

### Day 8-10: Go-Live
- [ ] System activated
- [ ] 48-hour monitoring completed
- [ ] Day 10 check-in call done
- [ ] Issues resolved

### Day 14+ (Tier 2/3)
- [ ] Cold outreach launched
- [ ] Neighborhood targeting active
- [ ] Estimate follow-up active
- [ ] Seasonal campaigns scheduled
- [ ] Referral program active
- [ ] Dispatcher configured (Tier 3)
- [ ] Invoicing automation (Tier 3)

### Ongoing
- [ ] Week 1 report sent
- [ ] Month 1 report sent
- [ ] Month 1 strategy call completed
- [ ] System optimizations applied
```
