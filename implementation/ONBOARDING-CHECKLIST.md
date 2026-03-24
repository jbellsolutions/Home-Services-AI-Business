# Client Onboarding Checklist

## Pre-Onboarding (Sales → Ops Handoff)

- [ ] Signed agreement received
- [ ] Setup payment collected ($1,500 / $3,500 / $7,500)
- [ ] Tier confirmed (1 / 2 / 3)
- [ ] Client folder created in project management system
- [ ] Onboarding call scheduled within 48 hours of signing

---

## Onboarding Call (30 minutes)

### Business Information
- [ ] Business name (exact, as it appears on Google)
- [ ] Business address
- [ ] Service area (zip codes, counties, or mile radius)
- [ ] Business phone number(s)
- [ ] Owner's cell phone (emergency escalation)
- [ ] Owner's email
- [ ] Website URL
- [ ] Google Business Profile email/access confirmed

### Services & Pricing
- [ ] Full service menu collected (every service they offer)
- [ ] Approximate pricing ranges per service
- [ ] Emergency / after-hours surcharge details
- [ ] Financing options available
- [ ] Warranty terms
- [ ] Brands/equipment they service
- [ ] Services they DON'T offer (to avoid booking wrong jobs)

### Team Information
- [ ] Number of technicians
- [ ] Each tech's name, phone, specialties/skills
- [ ] On-call rotation schedule (who handles after-hours)
- [ ] Dispatcher name and phone (if they have one)
- [ ] Office manager name and phone (if they have one)

### Technology Access
- [ ] CRM type: ServiceTitan / Housecall Pro / Jobber / Other / None
- [ ] CRM login credentials or API key
- [ ] Google Business Profile — owner grants access to our Google account
- [ ] Phone system type (landline, VoIP, cell)
- [ ] Call forwarding capability confirmed
- [ ] Review platform accounts (Google, Yelp, Facebook)

### Brand Voice
- [ ] How should AI sound? (Professional, friendly, casual, etc.)
- [ ] Any phrases they want used ("We treat your home like our home")
- [ ] Any phrases to AVOID
- [ ] Preferred AI name or just "team member"
- [ ] Spanish language needed? (Y/N)

---

## Tier 1 Setup (Days 1-7)

### Day 1-2: AI Receptionist
- [ ] Vapi/Bland.ai agent created with client's business info
- [ ] Voice selected and approved by client (send sample recording)
- [ ] Knowledge base configured (services, pricing, FAQ, service area)
- [ ] Emergency keyword triggers configured
- [ ] Escalation routing set up (owner cell, on-call tech)
- [ ] Twilio phone number provisioned (local area code)
- [ ] Call forwarding or tracking number configured

### Day 2-3: CRM Integration
- [ ] CRM API connected and tested
- [ ] Appointment booking flow tested (create job via API)
- [ ] Customer creation/lookup working
- [ ] Technician availability query working
- [ ] Data sync verified

### Day 3-4: Follow-Up Engine
- [ ] 7-touch follow-up sequence configured in n8n
- [ ] Text templates written and loaded
- [ ] Email templates written and loaded
- [ ] Trigger rules set (new lead without booking → enter sequence)
- [ ] Stop conditions configured (booking, opt-out, reply)

### Day 4-5: Review Manager
- [ ] Google Business Profile API connected
- [ ] Review monitoring active
- [ ] Post-job review request sequence configured
- [ ] AI review response templates created (positive + negative)
- [ ] Owner notification for negative reviews configured
- [ ] Direct review link generated and tested

### Day 5-6: GBP Optimization
- [ ] Business hours verified and updated
- [ ] Service categories optimized
- [ ] Service area updated
- [ ] Business description updated with keywords
- [ ] Photos uploaded (if client provides)
- [ ] Q&A monitoring activated
- [ ] Weekly GBP post schedule created

### Day 6-7: Testing
- [ ] 20 test calls completed (booking, emergency, FAQ, transfer, Spanish)
- [ ] Web form test (submission → AI response → CRM entry)
- [ ] Review request test (job completion → text → review link)
- [ ] Review response test (new review → AI response within 4 hours)
- [ ] Follow-up sequence test (lead entry → 7-touch sequence fires correctly)
- [ ] Emergency escalation test (call → owner text within 60 sec)
- [ ] Dashboard loads with test data

### Go-Live
- [ ] Client approves test results
- [ ] Phone forwarding/tracking activated for real calls
- [ ] All automations set to LIVE mode
- [ ] Monitoring alerts configured
- [ ] Client sent "You're Live!" notification with dashboard link
- [ ] First 48-hour intensive monitoring activated

---

## Tier 2 Additional Setup (Days 8-21)

### Commercial Outreach (Days 8-12)
- [ ] Client approves target segments (PMs, realtors, GCs)
- [ ] Prospect list built: 200-500 commercial contacts in service area
- [ ] Emails verified
- [ ] 5-email outreach sequence configured per segment
- [ ] Compliance reviewed (CAN-SPAM, opt-out)
- [ ] Outreach launched at 20-50/day initial volume

### Estimate Follow-Up (Days 10-14)
- [ ] CRM estimate tracking integrated
- [ ] 6-touch estimate follow-up sequence built
- [ ] Segmentation rules set (by estimate value)
- [ ] AI phone follow-up for $2K+ estimates configured
- [ ] Incentive offer templates created

### Neighborhood Targeting (Days 12-16)
- [ ] Job completion trigger connected to CRM
- [ ] Past customer database geocoded
- [ ] Nearby customer text templates created
- [ ] Facebook/Instagram ad templates created
- [ ] Optional: postcard vendor connected (if client wants physical mail)

### Seasonal Campaigns (Days 14-18)
- [ ] 12-month campaign calendar loaded
- [ ] Customer database segmented by service history
- [ ] First seasonal campaign configured and approved
- [ ] Future campaigns scheduled with auto-triggers

### Referral Program (Days 16-20)
- [ ] Referral offer defined ($ amount, both parties)
- [ ] Post-review referral trigger configured
- [ ] Referral tracking system active
- [ ] Thank-you automation for successful referrals

---

## Tier 3 Additional Setup (Days 14-30)

### AI Dispatcher (Days 14-20)
- [ ] Technician profiles built (skills, certs, location, capacity)
- [ ] Service type → skill matching rules defined
- [ ] Google Maps routing API connected
- [ ] Dispatch algorithm configured and tested
- [ ] Tech notification templates created
- [ ] Customer ETA notification configured
- [ ] Week 1: parallel mode (AI suggests, human confirms)
- [ ] Week 2: AI dispatches routine, human handles exceptions
- [ ] Week 3+: Full AI dispatch with human oversight

### Invoicing & Payments (Days 18-24)
- [ ] Payment processor identified (Stripe, Square, QuickBooks Payments)
- [ ] Auto-invoice trigger on job completion configured
- [ ] Payment reminder sequence (Day 3, 7, 14, 30) built
- [ ] Past-due escalation rules defined

### Customer Lifecycle (Days 20-26)
- [ ] Customer database imported with equipment data
- [ ] Maintenance agreement program defined (pricing, benefits)
- [ ] Agreement sales automation configured
- [ ] Equipment age tracking activated
- [ ] Quarterly customer touch schedule loaded
- [ ] Anniversary and milestone triggers set

### Financial Dashboard (Days 24-28)
- [ ] Data sources connected (CRM, call tracking, email, review platforms)
- [ ] Revenue per technician report configured
- [ ] Cost per lead tracking active
- [ ] Job profitability calculations defined
- [ ] Daily/weekly/monthly report cadence set
- [ ] Dashboard deployed to client-accessible URL

### Weekly Briefing (Day 28+)
- [ ] AI Co-Founder briefing template configured
- [ ] Data feeds connected (all systems → briefing generator)
- [ ] Delivery method set (email, text summary, or both)
- [ ] First briefing generated and reviewed with client

---

## Post-Launch (Week 2-4)

- [ ] Day 10: Optimization call (review first week data, adjust)
- [ ] Day 21: Performance review (bookings, calls handled, reviews generated)
- [ ] Day 30: Full ROI report + guarantee assessment
- [ ] Day 30: Upsell conversation (if Tier 1 → present Tier 2 opportunity)
- [ ] Monthly reporting cadence established
