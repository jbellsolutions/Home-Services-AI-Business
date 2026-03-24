# UAIS Sales Playbook: AI Agent Systems for Home Services

**Company:** UAIS (Using AI to Scale)
**Version:** 2.0 | March 2026
**Target Market:** Home services companies (HVAC, plumbing, roofing, electrical, landscaping, cleaning)

---

## TABLE OF CONTENTS

1. [Offer Summary](#1-offer-summary)
2. [Prospecting Strategy](#2-prospecting-strategy)
3. [Cold Email Campaigns](#3-cold-email-campaigns)
4. [Cold Call Script](#4-cold-call-script)
5. [LinkedIn Outreach](#5-linkedin-outreach)
6. [Facebook Group Strategy](#6-facebook-group-strategy)
7. [Sales Call Script (The Demo)](#7-sales-call-script-the-demo)
8. [Follow-Up Sequences](#8-follow-up-sequences)
9. [Referral System](#9-referral-system)
10. [Content Marketing Plan](#10-content-marketing-plan)
11. [Metrics and Tracking](#11-metrics-and-tracking)

---

## 1. OFFER SUMMARY

### Tier 1: Lead Recovery Engine
- **Setup:** $1,500
- **Monthly:** $497/mo
- **What's Included:**
  - AI receptionist (answers calls 24/7, books appointments)
  - Missed call text-back (instant SMS when a call is missed)
  - Automated follow-up sequences (SMS + email for new leads)
  - Review request automation (ask happy customers for Google reviews after every job)
  - Basic reporting dashboard
- **Ideal For:** Solo operators and small crews (1-5 techs) who are losing leads after hours
- **ROI Hook:** "If you're missing just 5 calls a month at $500 average ticket, that's $2,500/mo you're leaving on the table. This pays for itself from ONE recovered job."

### Tier 2: Growth Machine
- **Setup:** $3,500
- **Monthly:** $997/mo
- **What's Included:**
  - Everything in Tier 1
  - Outbound reactivation campaigns (re-engage past customers who haven't booked in 6+ months)
  - Estimate follow-up automation (chase unsold estimates automatically)
  - Seasonal campaign engine (pre-built campaigns for AC tune-ups, furnace checks, winterization, etc.)
  - Multi-channel outreach (SMS, email, voicemail drops)
  - Advanced reporting + lead source tracking
- **Ideal For:** Growing companies (5-20 techs) who have leads but can't close them all
- **ROI Hook:** "The average HVAC company closes only 40% of estimates. We chase the other 60% for you. On a $5,000 average job, recovering just 3 estimates/month is $15,000 in revenue."

### Tier 3: AI Ops Hub
- **Setup:** $7,500
- **Monthly:** $1,997/mo
- **What's Included:**
  - Everything in Tier 2
  - AI-assisted dispatch optimization (route techs, reduce windshield time)
  - Automated invoicing and payment follow-up
  - Customer satisfaction scoring
  - Full operations dashboard (real-time KPIs: close rate, response time, revenue per tech, CSat)
  - Dedicated account manager
  - Quarterly strategy reviews
- **Ideal For:** Established companies (20+ techs) who need to systemize operations
- **ROI Hook:** "You're running a $2M+ company on spreadsheets and sticky notes. We give you the AI back-office that lets you scale to $5M without hiring an office manager."

---

## 2. PROSPECTING STRATEGY

### 2.1 Where to Find Home Services Company Owners

#### Google Maps / Google Business Profile
- **What to search:** "HVAC company [city]", "plumber near [city]", "roofing contractor [city]", "electrician [city]", "landscaping company [city]", "house cleaning service [city]"
- **What to capture:** Business name, owner name (if listed), phone number, website, Google review count, average star rating, hours of operation (critical -- if they close at 5 PM, they're missing after-hours calls)
- **Tool:** Apify Google Maps Scraper -- scrape up to 500 businesses per search query
- **Pro Tip:** Search 5-10 cities in your target metro. A search for "HVAC Dallas TX" pulls different results than "air conditioning repair Dallas TX." Run both.

#### State Contractor License Databases
- **Why:** Every licensed contractor is in a public database. This gives you the owner's legal name, license type, and often their address.
- **Where to find them:**
  - Texas: TDLR (Texas Department of Licensing and Regulation)
  - California: CSLB (Contractors State License Board)
  - Florida: DBPR (Department of Business and Professional Regulation)
  - Every state has one -- Google "[state] contractor license lookup"
- **What to capture:** License holder name, business name, license number, license type (HVAC, plumbing, electrical, general), status (active), city
- **Tool:** Apify web scraper or manual export (many state sites offer CSV downloads)

#### Yelp
- **What to search:** Same categories as Google Maps
- **What to capture:** Business name, review count, star rating, phone, website
- **Why it matters:** Businesses with 3-4 stars on Yelp but 4.5+ on Google have a review management problem you can solve

#### Better Business Bureau (BBB)
- **What to search:** bbb.org > Find a Business > Category: HVAC, Plumbing, Roofing, Electrical
- **What to capture:** Accredited businesses, complaint history, owner name
- **Why it matters:** BBB-accredited businesses tend to be more established and have budget for services

#### Trade Associations
- **HVAC:** ACCA (Air Conditioning Contractors of America), PHCC (Plumbing-Heating-Cooling Contractors)
- **Plumbing:** PHCC, state plumbing associations
- **Roofing:** NRCA (National Roofing Contractors Association), state roofing associations
- **Electrical:** IEC (Independent Electrical Contractors), NECA
- **General:** NAHB (National Association of Home Builders), local Chambers of Commerce
- **What to do:** Get member directories. Many are public. If not, join the association ($200-500/year) for access to the full list. Worth it for thousands of qualified contacts.

#### Facebook Groups
- Search for: "[City] HVAC Contractors", "HVAC Business Owners", "Plumbing Business Owners", "Roofing Contractors Network", "Home Service Business Owners", "Contractor Marketing Tips"
- Goal: Identify active group members who are owners. They are self-qualified.

#### LinkedIn
- **Search filters:** Title contains "Owner" OR "President" OR "CEO" + Industry: "Construction" OR "HVAC" OR "Plumbing" + Location: [target city/state]
- **Tool:** LinkedIn Sales Navigator ($99/mo) -- essential for B2B prospecting
- **What to capture:** Name, title, company, location, number of employees, profile URL

### 2.2 How to Build Prospect Lists

#### Recommended Tech Stack
| Tool | Purpose | Cost |
|------|---------|------|
| Apify Google Maps Scraper | Scrape Google Maps for businesses | ~$49/mo |
| Apollo.io | Email finding, enrichment, cold email sending | $49-99/mo |
| LinkedIn Sales Navigator | Find and connect with owners | $99/mo |
| Google Sheets or Airtable | CRM/prospect tracking | Free-$20/mo |
| Instantly.io or Smartlead | Cold email sending at scale | $30-97/mo |
| PhantomBuster | LinkedIn automation | $59/mo |

#### List Building Workflow (Weekly)

**Monday: Scrape**
1. Run Apify Google Maps Scraper for 5 cities x 3 verticals (HVAC, plumbing, roofing) = 15 searches
2. Export to Google Sheets
3. De-duplicate against master list

**Tuesday: Enrich**
1. Upload business names + websites to Apollo.io
2. Apollo finds owner emails and phone numbers
3. Export enriched data back to master sheet

**Wednesday: Qualify + Score**
1. Score each prospect (see scoring criteria below)
2. Tag by tier fit (T1, T2, T3)
3. Segment into email sequences

**Thursday-Friday: Load + Launch**
1. Load qualified prospects into Instantly.io or Smartlead
2. Assign to appropriate email sequence
3. Launch new sequences

### 2.3 Prospect Qualification Scoring

Score each prospect 1-10. Pursue anyone scoring 6+.

| Criteria | Points | How to Check |
|----------|--------|--------------|
| Has a website | +1 | Google search |
| Has Google Business Profile | +1 | Google Maps |
| Fewer than 50 Google reviews | +2 | Google Maps (they need review help) |
| No after-hours answering | +2 | Call them at 7 PM (goes to voicemail = gold) |
| 5-50 employees | +2 | LinkedIn, website, or Apollo |
| Has been in business 3+ years | +1 | Google, BBB, or license database |
| Active on social media | +1 | Facebook/Instagram check |
| Runs Google Ads | +1 | Search their service -- if they show up in ads, they're spending on marketing |
| No online booking on website | +1 | Check their website |
| **Total possible** | **12** | |

**Score Interpretation:**
- 8-12: HOT -- prioritize, call within 48 hours
- 6-7: WARM -- email sequence first, call on engagement
- 3-5: COOL -- email sequence only, revisit in 90 days
- 0-2: SKIP -- too small, too new, or already have systems

### 2.4 Volume Targets

| Activity | Weekly Target | Monthly Target |
|----------|---------------|----------------|
| New prospects scraped | 500-1,000 | 2,000-4,000 |
| Prospects qualified + scored | 300-600 | 1,200-2,400 |
| New email sequences launched | 200-400 | 800-1,600 |
| Cold calls made (to email openers) | 50-100 | 200-400 |
| LinkedIn connections sent | 100-150 | 400-600 |
| Discovery calls booked | 15-25 | 60-100 |
| Demos completed | 10-15 | 40-60 |
| Deals closed | 3-5 | 12-20 |

---

## 3. COLD EMAIL CAMPAIGNS

### General Rules for All Sequences
- Send from a warmed-up domain (not your primary domain). Example: uaisresults.com or getscaleai.com
- Keep emails under 120 words
- No images, no HTML formatting, no links in email 1
- Always personalize the first line with something specific (their city, review count, business name)
- Send between 8 AM - 11 AM in the prospect's local time zone
- Wait at least 2 days between emails in a sequence
- Use Instantly.io or Smartlead for sending (they handle warmup, rotation, and deliverability)

---

### SEQUENCE 1: "The Missed Call Audit"

**Trigger:** Any HVAC/plumbing/roofing company. This is the default sequence for new prospects.

**Pre-work:** Before launching this sequence, call the prospect's business phone after 5 PM on a weekday. Note what happens. Does it ring out? Go to generic voicemail? Go to an answering service? This becomes your opening line.

---

**Email 1 (Day 1) -- The Hook**

Subject: called your shop at 6 PM last night

```
Hey {FirstName},

I called {CompanyName} last night at 6:14 PM -- got sent straight to voicemail.

No text back. No callback. Nothing.

I do this for a living (audit home services companies for missed revenue), so I wasn't surprised. But here's the thing: the average HVAC company misses 27% of inbound calls. At your average ticket price, that's probably $8,000-$15,000/month walking to your competitors.

We built an AI system that answers every call, books the appointment, and texts the customer back in under 60 seconds -- 24/7.

Would it be worth 15 minutes to see how it works?

-- {YourName}
UAIS (Using AI to Scale)
```

**Email 2 (Day 3) -- The Proof**

Subject: re: called your shop at 6 PM last night

```
{FirstName} -- quick follow-up.

One of our HVAC clients in {NearbyCity} was in the same spot -- missing after-hours calls, no follow-up system. Within 60 days:

- Recovered 23 missed leads per month
- Added $14,200/mo in new revenue
- Went from 3.8 to 4.6 stars on Google

They started with our $497/mo plan. Paid for itself in the first week.

Worth a quick call to see if we could do the same for {CompanyName}?

-- {YourName}
```

**Email 3 (Day 7) -- The Question**

Subject: quick question about {CompanyName}

```
{FirstName},

Genuine question -- when someone calls {CompanyName} after hours or on weekends, what happens to that lead?

Most contractors I talk to say the same thing: "We call them back Monday morning." By then, 78% have already called someone else.

We fix that. Our AI answers in 2 rings, books the job, and confirms via text -- while you're at your kid's game or sleeping.

15-minute demo? I'll show you exactly how it works using your own phone number.

-- {YourName}
```

**Email 4 (Day 10) -- The Risk Reversal**

Subject: free missed-call audit for {CompanyName}

```
{FirstName},

I know you're busy running crews, so I'll keep this simple.

I want to run a free missed-call audit for {CompanyName}. I'll call your business at 5 different times this week (after hours, lunch, weekends) and document exactly what happens each time.

Then I'll send you a report showing how many calls you're likely losing and what that costs you per month.

No pitch. No obligation. Just data.

Want me to run it?

-- {YourName}
```

**Email 5 (Day 14) -- The Breakup**

Subject: should I close your file?

```
{FirstName},

I've reached out a few times about helping {CompanyName} stop losing after-hours leads. Haven't heard back, so I'll assume the timing isn't right.

I'm going to close out your file on my end. If things change and you want to explore how AI can recover missed calls and automate follow-up, just reply to this email and I'll re-open it.

Either way, hope business is booming.

-- {YourName}
```

---

### SEQUENCE 2: "The Review Gap"

**Trigger:** Companies with fewer than 50 Google reviews OR a rating below 4.5 stars.

**Pre-work:** Check their Google Business Profile. Note their exact review count and star rating. Check their top competitor's review count.

---

**Email 1 (Day 1) -- The Data**

Subject: {CompanyName} has {ReviewCount} Google reviews

```
Hey {FirstName},

I was looking at {CompanyName} on Google -- you've got {ReviewCount} reviews at {StarRating} stars.

Your top competitor, {CompetitorName}, has {CompetitorReviewCount} reviews at {CompetitorStars}.

Here's why that matters: 93% of homeowners check Google reviews before calling. The company with more (and better) reviews gets the call first.

We built an AI system that automatically asks every customer for a review after their job is complete -- via text, at the perfect moment. Our clients average 15-25 new reviews per month.

Would it be worth 15 minutes to see how we could close the review gap for {CompanyName}?

-- {YourName}
UAIS (Using AI to Scale)
```

**Email 2 (Day 3) -- The Story**

Subject: re: {CompanyName} has {ReviewCount} Google reviews

```
{FirstName},

A roofing company we work with in {State} had 34 reviews when they started with us. Their main competitor had 187.

After 90 days using our review automation:
- They hit 112 reviews
- Went from #4 to #1 in Google Maps for "roofing company {City}"
- Inbound calls increased 40%

The system sends a text to every customer 2 hours after job completion. Happy customers leave a review. Unhappy ones get routed to your team privately (so you can fix it before it goes public).

Worth a conversation?

-- {YourName}
```

**Email 3 (Day 7) -- The Insight**

Subject: your 1-star review from {Month}

```
{FirstName},

I noticed {CompanyName} got a {LowStarCount}-star review back in {Month}. It mentions {BriefNonQuoteSummary}.

Here's the problem: that review is sitting there unanswered. Google's algorithm penalizes businesses with unresponded negative reviews, and 45% of consumers say they're more likely to use a business that responds to negative reviews.

Our system does two things:
1. Routes negative feedback BEFORE it hits Google (so you can fix the problem first)
2. Auto-drafts professional responses to every review (you approve with one click)

Free to chat for 10 minutes?

-- {YourName}
```

**Email 4 (Day 10) -- The Quick Win**

Subject: I'll get you 10 reviews this month -- free

```
{FirstName},

Here's my offer: let me set up our review automation for {CompanyName} at no cost for 30 days.

If you don't get at least 10 new Google reviews in that month, we part ways. If you do, we talk about a paid plan.

No setup fee. No credit card. Just results.

The only thing I need from you is a 15-minute call to connect the system to your CRM or customer list.

Interested?

-- {YourName}
```

**Email 5 (Day 14) -- The Breakup**

Subject: closing the loop on {CompanyName}

```
{FirstName},

I reached out about helping {CompanyName} get more Google reviews through automation. Haven't heard back, so I'll take the hint.

If you ever want to close the review gap with {CompetitorName}, just reply to this email. The offer stands.

-- {YourName}
```

---

### SEQUENCE 3: "The Estimate Leak"

**Trigger:** Companies doing $500K+ in revenue (bigger companies giving more estimates).

**Pre-work:** No specific pre-work needed. This sequence uses industry data.

---

**Email 1 (Day 1) -- The Stat**

Subject: 60% of your estimates aren't closing

```
Hey {FirstName},

The average home services company closes about 40% of the estimates they give. That means for every 10 estimates your team writes, 6 customers ghost you.

On a $4,000 average HVAC job, that's $24,000 in lost revenue for every 10 estimates.

The problem isn't your pricing. It's follow-up. Most companies send one email and move on. The customer meant to call back but forgot, got busy, or called the company that followed up three times.

We built an AI system that follows up on every unsold estimate -- automatically -- via text, email, and voicemail drop. No extra work for your team.

Worth 15 minutes to see how it works?

-- {YourName}
UAIS (Using AI to Scale)
```

**Email 2 (Day 4) -- The Math**

Subject: re: 60% of your estimates aren't closing

```
{FirstName},

Let me run quick math for {CompanyName}:

If your team gives 40 estimates/month at a $4,000 average ticket:
- 40% close rate = 16 jobs = $64,000/mo
- If we help you recover just 5 of the 24 lost estimates = $20,000/mo
- That's $240,000/year in recovered revenue

Our Tier 2 system costs $997/mo. That's a 20x return.

The AI follows up on Day 1, Day 3, Day 7, Day 14, and Day 30 after every estimate. Different message each time. Feels personal. Customers think your office manager is reaching out.

Quick call this week?

-- {YourName}
```

**Email 3 (Day 8) -- The Competitor Angle**

Subject: your competitors are automating this

```
{FirstName},

I work with 6 HVAC companies in {State} right now. Every single one is using AI to follow up on estimates automatically.

That means when a homeowner gets quotes from you AND one of them, here's what happens:

- Your follow-up: one phone call, maybe an email
- Their follow-up: 5-touch automated sequence over 30 days (text, email, voicemail)

Who do you think gets the callback?

I'm not trying to create urgency for the sake of it. But the companies adopting this now are pulling ahead fast.

15 minutes. I'll show you exactly what your competitors are seeing.

-- {YourName}
```

**Email 4 (Day 11) -- The Simple Ask**

Subject: one question for {FirstName}

```
{FirstName},

Simple question: what happens to an estimate after your tech writes it and the customer doesn't call back within 48 hours?

If the answer is "nothing" or "we try to call once" -- you're leaving real money on the table.

Happy to show you what automated estimate follow-up looks like in action. Takes 15 minutes.

-- {YourName}
```

**Email 5 (Day 14) -- The Breakup**

Subject: last note from me

```
{FirstName},

This is my last email about estimate follow-up for {CompanyName}. If recovering unsold estimates isn't a priority right now, I totally get it.

But if it ever becomes one, I'm here. Just reply to this thread.

All the best with the busy season ahead.

-- {YourName}
```

---

### SEQUENCE 4: "The Competitor Edge"

**Trigger:** Use when you can identify a prospect's direct competitor who is already using AI tools, chatbots, or has strong online presence.

**Pre-work:** Identify the prospect's top local competitor. Check if the competitor has a chatbot on their website, online booking, after-hours answering, or strong review presence.

---

**Email 1 (Day 1) -- The Wake-Up**

Subject: {CompetitorName} is doing something you're not

```
Hey {FirstName},

I was researching HVAC companies in {City} and noticed something interesting.

{CompetitorName} has:
- Online booking on their website
- An AI chatbot answering questions 24/7
- {CompetitorReviewCount} Google reviews (vs. your {ProspectReviewCount})
- Automated text follow-up after every call

You do better work (at least that's what your reviews say). But they're winning on speed and systems.

We help companies like {CompanyName} level the playing field with AI -- without hiring more office staff.

Worth a 15-minute conversation?

-- {YourName}
UAIS (Using AI to Scale)
```

**Email 2 (Day 3) -- The Breakdown**

Subject: re: {CompetitorName} is doing something you're not

```
{FirstName},

Here's what I mean about {CompetitorName}'s advantage:

When a homeowner needs an AC repair at 8 PM:
- They call {CompetitorName}: AI answers, books next-day appointment, sends confirmation text in 30 seconds
- They call {CompanyName}: voicemail. Maybe a callback tomorrow morning.

Who gets the job?

This isn't about who's a better technician. It's about who responds first. And right now, the data says 78% of customers hire the first company that responds.

I can get {CompanyName} set up with the same system in under a week. Want to see a demo?

-- {YourName}
```

**Email 3 (Day 7) -- The Trend**

Subject: this is happening across {City}

```
{FirstName},

This isn't just {CompetitorName}. I'm seeing it across {City}:

Home services companies are adopting AI for answering calls, following up on leads, chasing estimates, and getting reviews. The ones doing it are growing 30-40% faster than the ones who aren't.

It's not because AI is magic. It's because it eliminates the two biggest revenue killers in home services:
1. Slow response time
2. Zero follow-up

We can solve both for {CompanyName} starting at $497/mo.

15 minutes for a quick demo?

-- {YourName}
```

**Email 4 (Day 10) -- The Question**

Subject: honest question, {FirstName}

```
{FirstName},

No pitch this time -- just a genuine question.

When you think about what's holding {CompanyName} back from the next level of growth, what comes to mind?

For most contractors I talk to, it's one of three things:
1. Not enough leads
2. Leads they can't close
3. No time to follow up

If any of those resonate, I might be able to help. If not, no worries.

-- {YourName}
```

**Email 5 (Day 14) -- The Breakup**

Subject: I'll back off

```
{FirstName},

I've sent a few emails about helping {CompanyName} compete with the AI-powered companies in {City}. No reply, so I'll respect your time and stop reaching out.

If anything changes, this thread will always be here. Just hit reply.

Wishing you a strong season.

-- {YourName}
```

---

### SEQUENCE 5: "The Seasonal Play"

**Trigger:** Use 4-8 weeks before a major season (summer for AC, winter for heating, spring for roofing/landscaping).

**Pre-work:** Know the upcoming season and the prospect's trade.

---

**Seasonal Timing Guide:**
| Trade | Hot Season | Launch Sequence |
|-------|-----------|-----------------|
| HVAC (cooling) | May-September | March-April |
| HVAC (heating) | October-February | August-September |
| Roofing | March-October | January-February |
| Plumbing | Year-round (peak: winter) | October-November |
| Landscaping | March-October | January-February |
| Cleaning | Spring + holidays | February-March, October-November |

---

**Email 1 (Day 1) -- The Season is Coming**

Subject: {Season} is 6 weeks out -- is {CompanyName} ready?

```
Hey {FirstName},

{Season} season is about 6 weeks away. For HVAC companies in {City}, that means call volume is about to double.

Here's the question: when those calls start flooding in, can your team answer every one? What about the ones that come in at 7 PM? On Saturday morning? During lunch?

Last summer, the average HVAC company in {State} missed 31% of inbound calls during peak season. That's not a stat I made up -- it's from ServiceTitan's industry report.

We set up AI call answering and lead follow-up systems specifically for home services. Takes about a week to deploy. Most clients start seeing results in the first 72 hours.

Can we chat for 15 minutes before the rush hits?

-- {YourName}
UAIS (Using AI to Scale)
```

**Email 2 (Day 3) -- The Prep Story**

Subject: re: {Season} is 6 weeks out

```
{FirstName},

Last {Season}, one of our HVAC clients in {NearbyCity} set up our system two weeks before the heat wave hit. Here's what happened:

- Calls answered by AI after hours: 127 in the first month
- Appointments booked without a human touching it: 89
- Revenue from AI-booked jobs: $43,000+

He told me: "That's like hiring a full-time CSR who works 24/7 for $500/month."

The companies that prepare before peak season win. The ones that scramble during it lose calls.

Which one do you want {CompanyName} to be?

-- {YourName}
```

**Email 3 (Day 7) -- The Checklist**

Subject: your {Season} readiness checklist

```
{FirstName},

Quick {Season} readiness checklist for {CompanyName}:

[ ] After-hours calls go to AI or live agent (not voicemail)
[ ] Every missed call gets an automatic text-back within 60 seconds
[ ] Past customers get a seasonal tune-up campaign
[ ] Every estimate gets automated follow-up for 30 days
[ ] Every completed job triggers a Google review request

If you checked fewer than 3, you're leaving money on the table this {Season}.

We can get all 5 set up in a week. Want to knock it out before things get crazy?

-- {YourName}
```

**Email 4 (Day 10) -- The Urgency**

Subject: setup takes a week -- {Season} is in {Weeks} weeks

```
{FirstName},

Our system takes about 5-7 business days to set up and calibrate. {Season} season starts in roughly {Weeks} weeks.

That means if we start this week, you'll be fully operational before the rush. Wait two more weeks and you'll be scrambling.

I have 3 setup slots open this month for HVAC companies in {State}. Want one?

-- {YourName}
```

**Email 5 (Day 14) -- The Breakup**

Subject: maybe next {Season}

```
{FirstName},

Looks like the timing isn't right for {CompanyName} this season. No worries at all.

I'll reach back out before next {NextSeason} season in case things change. In the meantime, if you want to explore AI for your business at any point, just reply here.

Have a great {Season}.

-- {YourName}
```

---

## 4. COLD CALL SCRIPT

### When to Call
Call prospects who have **opened** your emails (tracked via Instantly.io or Smartlead) but haven't replied. Also call any prospect scored 8+ regardless of email engagement.

### Call Framework: O-Q-P-O-C (Open, Qualify, Pitch, Overcome, Close)

---

**OPENING (First 15 Seconds -- Make or Break)**

```
"Hey {FirstName}, this is {YourName} with UAIS. I sent you an email a couple days
ago about the after-hours calls at {CompanyName} -- did you get a chance to see it?

[If YES]: "Great -- what'd you think?"
[If NO]: "No worries, the short version is..."
[If WHO IS THIS / WHAT DO YOU WANT]: "Totally fair. I'll be quick..."
```

**Transition into the pitch (pick based on sequence they're in):**

```
"The short version is: I help HVAC companies like yours stop losing leads after
hours. I actually called your shop at 6 PM last week and got sent to voicemail --
which is exactly the problem we solve. We set up an AI system that answers every
call, books the appointment, and texts the customer back in under a minute."
```

---

**QUALIFYING QUESTIONS (Pick 3-4)**

```
1. "How many calls do you think {CompanyName} gets per day during peak season?"

2. "What happens when a call comes in after your office closes?"

3. "Do you have someone following up on estimates that don't close?"

4. "How are you getting Google reviews right now? Is it consistent?"

5. "Are you running any kind of reactivation campaign to past customers?"

6. "What's your average ticket size for a [service call / install / repair]?"

7. "How many techs are you running right now?"

8. "What CRM or scheduling software are you using?"
   (ServiceTitan, Housecall Pro, Jobber, or "nothing" -- all are fine)

9. "If I could show you a system that recovers 10-20 missed leads per month
   without you lifting a finger, would that be worth a 15-minute look?"
```

---

**THE PITCH (30-45 Seconds Max)**

```
"Here's the deal, {FirstName}. We built an AI system specifically for home services
companies. It does three things:

1. Answers your phone 24/7 -- so you never miss a lead again
2. Follows up on every estimate you give -- automatically, for 30 days
3. Gets you Google reviews after every job -- without your team asking

Our HVAC clients are averaging $10,000-$20,000 in recovered revenue per month.
The system starts at $497/month. So even if it only recovers ONE job, it pays
for itself.

What I'd love to do is set up a 15-minute demo where I show you exactly how it
works -- I'll even use your phone number so you can see the AI answer a call
to your business live on the screen."
```

---

**OBJECTION HANDLING (On the Call)**

| Objection | Response |
|-----------|----------|
| "I'm too busy right now" | "I totally get it -- that's actually why this exists. You're too busy to chase leads and follow up on estimates, so the AI does it for you. How about we do 15 minutes Thursday? I'll work around your schedule." |
| "We already have a receptionist" | "That's great. Does she work at 9 PM? On Saturdays? During lunch? Our AI handles the overflow -- the calls your team can't get to. It's not a replacement, it's a safety net." |
| "How much does it cost?" | "It starts at $497/month for the base system. But let me ask you this -- what's one missed job worth to you? If the answer is more than $497, it pays for itself from day one. Let me show you a quick demo and we can figure out the right fit." |
| "Send me some info" | "Happy to. But honestly, a 2-page PDF won't do it justice. What if I show you a live demo in 15 minutes? You'll see the AI answer a call, book a job, and send a review request -- all live. Way more useful than a brochure." |
| "I need to think about it" | "Totally fair. What specifically do you want to think through? Is it the price, the technology, or something else? I want to make sure I'm giving you what you need to make a good decision." |
| "We tried something like this before and it didn't work" | "I hear that a lot. What did you try? [Listen.] Yeah, that's different from what we do. Most of those tools are built for every industry. Ours was built ground-up for home services -- it knows your terminology, your booking flow, your seasonal patterns. That's why it works." |

---

**CLOSE TO MEETING**

```
"Here's what I'd suggest: let's do a 15-minute Zoom call where I show you the
system live. I'll answer a call to your business using the AI, show you the
follow-up sequences, and pull up what the dashboard looks like.

If you love it, great -- we'll talk about getting you set up. If not, at least
you'll see what's out there and you'll have some ideas you can use regardless.

Fair enough? I've got [Day] at [Time] or [Day] at [Time] -- which works better?"
```

---

## 5. LINKEDIN OUTREACH

### 5.1 Profile Optimization

Your LinkedIn profile should be optimized to speak directly to home services company owners. Not other marketers. Not AI people. Contractors.

**Headline:**
```
I help HVAC, plumbing & roofing companies recover $10K-$30K/month in missed
revenue using AI | Founder @ UAIS
```

**About Section:**
```
If you own a home services company, I have a question for you:

What happens when someone calls your business at 7 PM on a Tuesday?

If the answer is "voicemail" -- you're losing $5,000-$15,000 every month to
competitors who answer faster.

I'm the founder of UAIS (Using AI to Scale). We build AI systems specifically
for HVAC, plumbing, roofing, electrical, and landscaping companies. Our system:

-- Answers every call 24/7 (even at 2 AM)
-- Follows up on unsold estimates automatically
-- Gets you 15-25 new Google reviews per month
-- Reactivates past customers for seasonal campaigns

Our clients see an average 10-20x return on their investment.

If you're doing $500K+ in revenue and want to grow without hiring more office
staff, let's talk.

Book a free 15-minute demo: [Link]
```

**Banner Image:** Before/after showing a company going from 23 reviews to 147 reviews, or a screenshot of the AI dashboard with revenue numbers.

**Featured Section:** Pin a case study, a short demo video, or a testimonial video from a client.

### 5.2 Connection Request Templates

**Template 1 -- Peer Approach**
```
Hey {FirstName} -- I saw you run {CompanyName} in {City}. I work with a lot of
HVAC/plumbing companies on the tech side. Would love to connect.
```

**Template 2 -- Specific Observation**
```
{FirstName} -- noticed {CompanyName} has some great reviews on Google. I work
with home services companies on automating their lead follow-up. Thought it'd
be worth connecting.
```

**Template 3 -- Mutual Group/Connection**
```
Hey {FirstName}, we're both in the {GroupName} group. I help home services
companies scale with AI. Thought we should connect -- always good to know
people in the industry.
```

### 5.3 DM Sequence (After Connection Accepted)

**DM 1 (Day 0 -- Immediately after they accept)**
```
Hey {FirstName}, thanks for connecting. Quick question -- is {CompanyName} using
any kind of automation for answering calls after hours or following up on
estimates? Curious because it's the #1 revenue leak I see in home services.
```

**DM 2 (Day 3 -- If no reply)**
```
No worries if you're swamped, {FirstName}. I know running a {Trade} company
keeps you busy.

I put together a short video showing how one of our HVAC clients recovered
$14K/month in missed leads using AI. Would you want me to send it over?
```

**DM 3 (Day 7 -- If no reply)**
```
Last ping, {FirstName}. If you ever want to explore how AI can help {CompanyName}
answer more calls and close more estimates, I'm here. Just shoot me a message
anytime. Hope business is going well.
```

### 5.4 Content Strategy (What to Post)

Post 3-5 times per week. Mix of these content types:

**Content Pillar 1: Industry Pain Points (2x/week)**
- "I called 20 HVAC companies in Dallas after 5 PM. Here's what happened..." (document the results)
- "The average plumbing company loses $12,000/month from slow follow-up. Here's why."
- "Your receptionist goes home at 5. Your competitors' AI doesn't."

**Content Pillar 2: Results / Social Proof (1x/week)**
- Client before/after screenshots (revenue, reviews, response time)
- "Our client just hit 200 Google reviews. They had 47 when we started."
- Video testimonials from clients (even 30-second iPhone videos work)

**Content Pillar 3: Education (1x/week)**
- "3 things every HVAC company should automate before summer"
- "How to calculate how much revenue you're losing from missed calls"
- "The 5-touch estimate follow-up sequence that closes 30% more jobs"

**Content Pillar 4: Behind the Scenes (1x/week)**
- Show the AI answering a call (screen recording)
- Show the dashboard with real (anonymized) data
- Document your process for setting up a new client

---

## 6. FACEBOOK GROUP STRATEGY

### 6.1 Groups to Join

Search for and join these types of groups (aim for 15-20 groups total):

| Group Type | Example Names | Why |
|------------|---------------|-----|
| HVAC business owners | "HVAC Business Owners", "HVAC Contractors Network" | Direct access to decision makers |
| Plumbing business owners | "Plumbing Business Growth", "Master Plumbers Network" | Same |
| Roofing contractors | "Roofing Contractors of America", "Roofing Business Owners" | Same |
| General contractor groups | "Contractor Business Growth", "Home Service Business Owners" | Broader reach |
| ServiceTitan users | "ServiceTitan Users Group", "ServiceTitan Tips & Tricks" | They already invest in software -- warm |
| Housecall Pro users | "Housecall Pro Community" | Same |
| Jobber users | "Jobber Community" | Same |
| Local business groups | "{City} Small Business Network", "{City} Business Owners" | Local targeting |
| Home services marketing | "Home Services Marketing", "Contractor Marketing Tips" | People already thinking about growth |

### 6.2 Engagement Strategy (Before Selling)

**Week 1-2: Lurk and Learn**
- Read posts. Understand what people are complaining about.
- Common complaints: "Can't find good help," "Leads are drying up," "My CSRs keep quitting," "I'm working 80 hours/week."
- Note the most active members (they're the influencers).

**Week 3+: Add Value First**
- Answer questions with genuine, helpful advice. Do NOT pitch your service.
- Share useful content: "Hey, I put together a spreadsheet for calculating close rates. DM me if you want a copy."
- Become known as the person who knows about AI and automation for home services.

### 6.3 Comment Templates (For Responding to Pain Points)

**When someone posts about missing calls:**
```
This is the #1 revenue killer in home services. The data shows that 78% of
customers hire the first company that responds. If your phones go to voicemail
after 5 PM, you're handing jobs to whoever answers next.

A few options:
1. Hire an after-hours answering service ($800-1,500/mo)
2. Set up an AI receptionist that answers + books ($400-600/mo)
3. At minimum, set up a missed-call text-back so the customer gets an
   instant response

Happy to share more about how option 2 works if anyone's interested. We've
set it up for a bunch of companies in this group.
```

**When someone posts about needing more reviews:**
```
The easiest way to get reviews consistently: automate the ask.

Send a text 2 hours after every job completion. Keep it simple: "Hey
{CustomerName}, thanks for choosing us. Would you mind leaving us a quick
review? [Google link]"

Timing matters. 2 hours post-job = they're still happy and remember the
experience. Do it 2 days later and the moment is gone.

We automate this for our home services clients and they average 15-25 new
reviews/month. DM me if you want to see how the system works.
```

**When someone posts about slow sales / low close rates:**
```
What does your follow-up look like after giving an estimate?

Most companies I talk to: one phone call, maybe an email. Then they move on.

The reality is, the customer didn't say "no" -- they said "not right now."
A 5-touch follow-up sequence over 30 days (text + email + voicemail) recovers
15-25% of those "lost" estimates.

We automate this entire process. Happy to share the exact sequence we use
if anyone wants it.
```

### 6.4 DM Sequence (After They Engage With Your Comment)

**DM 1 (Immediately after they like/comment on your post or comment):**
```
Hey {FirstName}! I saw you liked my comment about [topic]. Are you dealing
with that at {CompanyName} right now?
```

**DM 2 (After they respond with their pain point):**
```
Yeah, that's really common. Almost every {Trade} company I talk to has
the same issue.

We actually built a system that handles [their specific problem]
automatically. Would you want to see a quick demo? It's 15 minutes
and I'll show you exactly how it works using real examples.
```

**DM 3 (If they go cold after DM 2):**
```
No pressure at all, {FirstName}. I know you're busy running crews.

If you ever want to explore it, just ping me here. In the meantime,
here's a quick tip that might help: [give one actionable piece of
advice related to their pain point].
```

### 6.5 Group Post Templates (For When You Have Permission to Post)

**Template 1: The Poll**
```
Quick poll for the group:

What's the BIGGEST revenue leak in your business right now?

A) Missed calls after hours
B) Estimates that don't close
C) Not enough Google reviews
D) Past customers who never come back

Drop your letter below -- I'll share a tip for each one.
```

**Template 2: The Case Study Tease**
```
One of our HVAC clients went from $45K/month to $72K/month in 90 days.

No new trucks. No new techs. No new marketing spend.

Three things changed:
1. AI started answering their phone 24/7
2. Every estimate got automated follow-up for 30 days
3. Every customer got a review request after the job

If you want the full breakdown of how we set this up, drop a comment
or DM me.
```

**Template 3: The Free Resource**
```
I put together a free "Revenue Leak Calculator" for home services companies.

You plug in your numbers (calls per day, close rate, average ticket)
and it tells you exactly how much you're losing from:
- Missed calls
- Unsold estimates
- Lack of reviews

DM me "calculator" and I'll send it over. No strings attached.
```

---

## 7. SALES CALL SCRIPT (THE DEMO)

### Pre-Call Preparation (5 Minutes Before)

- Pull up their Google Business Profile (review count, star rating, hours)
- Check their website (do they have online booking? Chat? After-hours info?)
- Review any email exchanges or notes from the cold call
- Have the ROI calculator ready with their trade's average ticket pre-loaded
- Have the demo environment ready (AI call demo, dashboard, review automation)

### Call Structure (45-60 Minutes)

---

**PHASE 1: RAPPORT + AGENDA (5 Minutes)**

```
"Hey {FirstName}, thanks for taking the time. Before we jump in, I want to
make sure we use this time well.

Here's what I was thinking for the next 45 minutes:
1. I'll ask you a few questions about {CompanyName} so I understand your
   business and what you're dealing with
2. I'll show you how the system works -- live
3. We'll run the numbers to see if it makes financial sense for you
4. And if it does, I'll walk you through how we'd get you set up

Sound good? Cool. Let's start with you. Tell me about {CompanyName} --
how long have you been at it?"
```

---

**PHASE 2: DISCOVERY (10-15 Minutes)**

Ask these questions and TAKE NOTES. Their answers drive the entire rest of the call.

**Business Overview:**
```
1. "How many techs are you running right now?"
2. "What's your revenue look like? Are you north of $500K? $1M?"
3. "What's your average ticket size for a [repair / install / service call]?"
4. "What percentage of your revenue comes from installs vs. service/repair?"
```

**Lead Flow:**
```
5. "How are most of your leads coming in right now? Google, referrals,
    Home Advisor, Angi?"
6. "How many inbound calls do you get per day during peak season?"
7. "Who's answering the phones? Office manager? CSR? You?"
8. "What happens after 5 PM? Weekends? Lunch breaks?"
```

**The Money Questions:**
```
9. "What's your close rate on estimates? Do you track it?"
10. "When someone gets an estimate and doesn't call back, what does the
     follow-up look like?"
11. "How are you handling Google reviews? Is there a process?"
12. "Are you doing anything to re-engage past customers? Seasonal campaigns?"
```

**The Pain:**
```
13. "What's the biggest bottleneck in your business right now?"
14. "If you could wave a magic wand and fix one thing, what would it be?"
15. "What have you tried before that didn't work?"
```

---

**PHASE 3: ROI CALCULATION -- LIVE ON THE CALL (5 Minutes)**

```
"Okay {FirstName}, let me share my screen and run the numbers with you.
Based on what you told me..."
```

**ROI Calculator Script:**

```
"You said you get about [X] calls per day. Industry data shows home services
companies miss about 27% of inbound calls. So that's roughly [X * 0.27]
missed calls per day, or [monthly number] per month.

At your average ticket of $[ticket], that's $[monthly missed revenue]
per month in calls that never get answered.

Now let's look at estimates. You said your team gives about [X] estimates
per month and your close rate is around [X]%. That means [Y] estimates
go unsold. At $[avg install ticket], that's $[unsold estimates value]
in quotes sitting on the table.

If we recover just [conservative number] of those missed calls and
[conservative number] of those estimates, that's $[recovered amount]
per month.

The system we're looking at costs $[price]/month. So your return is
roughly [X]x your investment.

Does that math make sense to you?"
```

**Key Formulas:**
- Missed call value = (daily calls x 0.27) x 30 x avg ticket x 0.3 (30% would have booked)
- Unsold estimate value = (monthly estimates x (1 - close rate)) x avg install ticket
- Recovery projection (conservative) = 15-20% of missed call value + 10-15% of unsold estimate value

---

**PHASE 4: THE DEMO (15 Minutes)**

**Demo Flow:**

**Step 1: AI Call Answering (5 min)**
```
"Let me show you the coolest part. I'm going to call your business number
right now using our AI system. Watch what happens."

[Call their number. If they have voicemail after hours, show the contrast.
If during hours, show how AI handles overflow.]

"Now let me show you what the AI sounds like when it's set up for your
business."

[Play the AI answering a sample HVAC call. It greets, qualifies, asks
for the address, books the appointment, sends a confirmation text.]

"That entire interaction took 90 seconds. No human involved. And the
appointment is already in your calendar."
```

**Step 2: Dashboard (5 min)**
```
"Here's what your dashboard looks like. You can see:
- Every call that came in today, who it was, what they needed
- Appointments booked by the AI
- Estimate follow-up status (who's been contacted, who responded)
- Review requests sent and reviews received
- Revenue attributed to the AI system

This is a real client dashboard -- obviously with their info anonymized.
They're tracking $23,000 in revenue this month that came directly through
the AI system."
```

**Step 3: Review Automation (3 min)**
```
"After every completed job, the system sends a text like this:
[Show sample text message]

'Hi Sarah, thanks for choosing {CompanyName} for your AC repair today!
If you had a great experience, would you mind leaving us a quick review?
[Google review link]'

It goes out automatically 2 hours after the job is marked complete in
your system. Our clients average 15-25 new reviews per month with this.
You currently have {ReviewCount} -- imagine hitting 200 in the next 6 months."
```

**Step 4: Follow-Up Sequences (2 min)**
```
"And here's the estimate follow-up. When a tech writes a quote and the
customer doesn't book within 48 hours, this sequence kicks in automatically:

Day 1: Text -- 'Hey {Customer}, just checking in on the estimate we sent...'
Day 3: Email -- Detailed follow-up with the estimate attached
Day 7: Voicemail drop -- Personal message from your company
Day 14: Text -- 'We're running a limited-time offer...'
Day 30: Final text -- 'Just wanted to make sure you got taken care of...'

Each message feels personal. Customers think your office manager is
reaching out individually. But it's all automated."
```

---

**PHASE 5: PRICING PRESENTATION (5 Minutes)**

```
"Based on what you told me, here's what I'd recommend for {CompanyName}:"
```

**If recommending Tier 1:**
```
"We'd start with our Lead Recovery Engine. This gives you the AI
receptionist, missed call text-back, follow-up sequences, and review
automation.

Setup is $1,500 -- that covers building your custom AI, training it on
your services and pricing, connecting to your systems, and testing.

Monthly is $497. That includes unlimited calls, unlimited texts, unlimited
follow-ups, and the dashboard.

Based on the numbers we ran, you're likely leaving $[X]/month on the table
right now. This pays for itself from the first recovered job."
```

**If recommending Tier 2:**
```
"For {CompanyName}, I'd recommend our Growth Machine. That includes
everything from Tier 1 plus estimate follow-up automation, past customer
reactivation campaigns, and seasonal outreach.

Setup is $3,500. Monthly is $997. Based on your volume, I'd expect this
to generate $[X]/month in recovered and reactivated revenue. That's a
[X]x return."
```

**If recommending Tier 3:**
```
"Given the size of your operation, the AI Ops Hub makes the most sense.
You get everything from Tier 1 and 2, plus dispatch optimization, automated
invoicing, and the full operations dashboard. Plus a dedicated account manager.

Setup is $7,500. Monthly is $1,997. For a company running [X] trucks,
the dispatch optimization alone typically saves $3,000-5,000/month in
reduced windshield time and better route planning."
```

---

**PHASE 6: THE CLOSE (5-10 Minutes)**

**The Assumptive Close:**
```
"So here's how we'd get started. The setup takes about 5-7 business days.
We'd start by connecting to your phone system and CRM, build out your
custom AI, train it on your services and pricing, and then do a full
test before going live.

In terms of timing, if we kicked this off this week, you'd be up and
running by [date]. That's right before {season} really picks up.

Should we get the paperwork going?"
```

**The Two-Option Close:**
```
"Based on everything we talked about, I see two paths:

Option A: We start with Tier 1 at $497/mo, get the AI receptionist and
review automation live, and you see results within the first week. Then
we add the estimate follow-up and seasonal campaigns as a Phase 2.

Option B: We go straight to Tier 2 at $997/mo and get everything
running at once.

Which feels more comfortable for you?"
```

**The Timeline Close:**
```
"Here's my concern, {FirstName}. {Season} season starts in {X} weeks.
Setup takes about a week. If we wait another month, you'll be right in
the middle of the rush trying to get this going.

The best time to set up the system is before you need it. What do you
say we lock in the setup this week?"
```

---

**PHASE 7: OBJECTION HANDLING (As Needed)**

| # | Objection | Response |
|---|-----------|----------|
| 1 | "It's too expensive" | "I understand. Let me ask you this -- how much is one missed job worth? If your average ticket is $4,000 and this system recovers just one extra job per month, you're getting an 8x return on $497. The question isn't whether you can afford it -- it's whether you can afford NOT to have it while your competitors do." |
| 2 | "I need to talk to my wife/partner" | "Totally fair. Would it help if I put together a one-page summary with the ROI calculation so you have something concrete to show them? And let's schedule a follow-up call for Thursday -- that gives you time to discuss it and we can answer any questions together." |
| 3 | "I don't trust AI to talk to my customers" | "That's a valid concern, and you're not the first person to say that. Here's how we handle it: the AI is trained specifically on YOUR business. It knows your services, your pricing, your service area. It doesn't make stuff up. And any call it can't handle gets immediately routed to you or your team. Want to hear it handle a real scenario right now?" |
| 4 | "We tried automation before and it didn't work" | "What did you try? [Listen.] I hear that a lot. The difference is, those tools are built for every industry. Ours is built ground-up for home services. It knows the difference between an AC repair call and a furnace install request. It knows your seasonal patterns. It speaks your customers' language. Want to see side by side how it's different?" |
| 5 | "I don't have time to set this up" | "That's exactly why you need this. You're stretched thin, your team is maxed, and things are falling through the cracks. The setup takes about one hour of YOUR time -- a 30-minute onboarding call and then 30 minutes to review the AI before it goes live. We handle everything else." |
| 6 | "What if it breaks or says something wrong?" | "Two safety nets: First, every AI response is based on your approved scripts and information -- it won't freelance. Second, you get a daily report of every conversation the AI had. If something doesn't look right, we adjust it immediately. We also have a human escalation protocol -- if the AI isn't sure, it says 'Let me have someone from our team call you right back' and alerts your team instantly." |
| 7 | "I'm not tech-savvy" | "You don't need to be. We handle all the technical stuff. Your interaction with the system is a simple dashboard -- think of it like checking your bank account online. And you have a dedicated point of contact who answers any questions. Our least tech-savvy client is 67 years old and runs a roofing company -- he loves it." |
| 8 | "Can I do a trial first?" | "I don't do free trials because the setup work is the same whether it's a trial or a full engagement. But here's what I will do: if you don't see a positive ROI in the first 30 days, I'll refund your first month. You'll have the data to prove it either way. Fair?" |
| 9 | "My customers want to talk to a real person" | "I hear you. And some will. That's why we built a seamless handoff. The AI handles the initial greeting, qualifying, and booking. If a customer says 'I want to talk to someone,' the AI immediately routes them to your team with context: 'Transferring you now. I've let them know you have a leak in your kitchen and you're at 123 Main St.' Your customer gets a better experience because the handoff is warm, not cold." |
| 10 | "I just need more leads, not automation" | "I get it. But here's the thing -- you might already have the leads. If you're missing 27% of calls and losing 60% of estimates, the problem isn't lead volume. It's lead conversion. Let me show you the math on your specific numbers. If we can convert even 15% more of what you already have, that might be more revenue than a $2,000/month ad campaign." |
| 11 | "My industry is different" | "What makes it different? [Listen.] That's fair. But here's what I know: every home services company I talk to has the same three problems -- missed calls, poor follow-up, and not enough reviews. Whether you're fixing ACs or replacing roofs, the fundamentals are the same. The AI is customized for your specific trade, terminology, and workflow." |
| 12 | "I want to see it work for someone in my area first" | "Understandable. I can connect you with a client in [nearby city] who's in the same trade. They've been using the system for [X] months. Or I can show you anonymized results from companies in {State}. Which would be more helpful?" |
| 13 | "What's the contract length?" | "Month to month after the setup. No long-term lock-in. If it's not working, you can cancel anytime. Most clients don't -- because the ROI is clear from month one. But I never want someone to feel trapped." |
| 14 | "I'll think about it and call you back" | "I respect that. Here's what I've found though -- when someone says 'I'll call you back,' life gets in the way and it just doesn't happen. Not because you don't want to, but because you're running a business. How about this: let's schedule a 10-minute follow-up call for [day]. That way you have time to think, and I'm not chasing you down. I'll send a calendar invite right now." |
| 15 | "Can you do it for less?" | "I wish I could, but here's the thing -- the price reflects the custom work we do for each client. Your AI is built specifically for {CompanyName}. It's trained on your services, your pricing, your service area. That's not a template. But let me reframe it: at $497/month, you need to recover ONE missed call per month to break even. Everything after that is profit. Most clients see 10-20x return." |
| 16 | "I want my team to look at it first" | "Great idea. Let's schedule a 15-minute call with you and your key person -- office manager, operations lead, whoever runs the day-to-day. I'll show them the system and answer their questions directly. That way you both have the info to make a decision together. When works for them?" |

---

## 8. FOLLOW-UP SEQUENCES

### 8.1 Post-Demo Follow-Up (Didn't Close on the Call)

**Touch 1: Same Day (Within 2 Hours of the Call)**

Channel: Email

Subject: great chatting, {FirstName} -- here's your ROI summary

```
Hey {FirstName},

Great talking with you today about {CompanyName}. As promised, here's a
quick summary of what we discussed:

YOUR NUMBERS:
- Estimated missed calls/month: {X}
- Estimated unsold estimates/month: {X}
- Missed revenue opportunity: ${X}/month

WHAT WE RECOMMENDED:
- {Tier Name}: ${setup} setup + ${monthly}/mo
- Expected ROI: {X}x in the first 90 days

NEXT STEP:
If you're ready to move forward, just reply to this email and I'll send
over the onboarding form. Setup takes 5-7 business days.

If you want to think it over, totally fine. I'll follow up in a couple days
to see where your head's at.

Talk soon,
{YourName}
```

---

**Touch 2: Day 2**

Channel: Text message

```
Hey {FirstName}, it's {YourName} from UAIS. Quick follow-up on our call
yesterday. Any questions come up that I can help with? Happy to jump on
a quick call anytime.
```

---

**Touch 3: Day 5**

Channel: Email

Subject: quick question about {CompanyName}

```
Hey {FirstName},

Following up on our conversation last week. I keep thinking about the
number we calculated -- ${X}/month in missed revenue.

That's ${X * 12} per year. And every month that goes by without a
system in place, that's another ${X} gone.

I'm not trying to pressure you. But I am trying to make sure you have
everything you need to make a decision. Is there anything holding you
back that I can address?

-- {YourName}
```

---

**Touch 4: Day 8**

Channel: Email with case study

Subject: how {ClientName} added ${Amount}/month

```
{FirstName},

Wanted to share a quick case study that might be relevant.

{ClientName} is a {Trade} company in {City}. When they started with us:
- {X} Google reviews (now {Y})
- Missing ~30% of after-hours calls (now 0%)
- Close rate on estimates: {X}% (now {Y}%)
- Monthly revenue: ${before} (now ${after})

They started with our {Tier} plan -- same one we discussed for you.

Sometimes it helps to see what's possible from someone who was in a
similar spot. Happy to connect you with them if you want to hear it
firsthand.

-- {YourName}
```

---

**Touch 5: Day 12**

Channel: Voicemail drop

Script:
```
"Hey {FirstName}, it's {YourName} from UAIS. I wanted to check in on
our conversation from last week about setting up AI for {CompanyName}.
I know you're busy, but I didn't want you to lose momentum on this,
especially with {Season} right around the corner. Give me a call back
when you get a chance -- [phone number]. Talk soon."
```

---

**Touch 6: Day 20**

Channel: Email (offer a free audit)

Subject: free offer for {CompanyName}

```
{FirstName},

I know we talked a couple weeks ago and the timing wasn't quite right.
Here's what I'd like to offer:

Let me run a full Revenue Leak Audit for {CompanyName} -- completely free.

I'll:
1. Call your business at 5 different times and document the experience
2. Analyze your Google reviews vs. your top 3 competitors
3. Mystery-shop your estimate follow-up process
4. Put it all in a report with specific dollar amounts you're losing

No strings attached. Even if you never buy anything from us, you'll
have a clear picture of where revenue is falling through the cracks.

Want me to run it?

-- {YourName}
```

---

**Touch 7: Day 30**

Channel: Email (the graceful exit)

Subject: last follow-up from me

```
{FirstName},

This is my final follow-up on our conversation about AI for {CompanyName}.
I don't want to be the annoying sales guy who doesn't take a hint.

If the timing isn't right, I completely understand. Running a {Trade}
company is demanding and adding new systems isn't always top of mind.

Here's what I'll do: I'll check back in with you in 90 days. If
things change before then -- you're losing sleep over missed calls,
your competitor launches AI, or you just want to revisit the numbers --
hit reply and I'm here.

Wishing you a great {Season} season.

-- {YourName}
```

### 8.2 When to Offer a Trial or Audit

Offer the free Revenue Leak Audit if:
- They showed genuine interest on the demo call but couldn't commit
- They have a specific objection you can address with data (e.g., "I don't think we're missing that many calls")
- They went cold after Touch 3 (the audit re-engages them with something of value)
- They said "maybe next quarter" -- the audit keeps the relationship warm

Do NOT offer a free trial of the full system. The setup work is significant. Instead, offer:
- Free Revenue Leak Audit (low effort, high perceived value)
- 30-day money-back guarantee on the first month (risk reversal, not a free trial)

### 8.3 When to Walk Away

Walk away (move to 90-day drip) if:
- They don't respond to 7 touches over 30 days
- They explicitly say "not interested" (respect it, move on)
- They can't articulate a problem you solve (they don't feel the pain)
- They're doing less than $250K/year (likely can't afford it)
- They have a bad attitude or are disrespectful (bad clients aren't worth it)

---

## 9. REFERRAL SYSTEM

### 9.1 How to Ask Existing Clients for Referrals

**When to Ask:** 30 days after onboarding, once they've seen results.

**The Ask (On a Check-In Call):**
```
"{FirstName}, I'm glad the system is working well for {CompanyName}.
Quick question -- do you know any other {Trade} company owners who
might be dealing with the same issues you had before we started?

I'm not looking for a list of 50 people. Just 1-2 names of owners
you know who are missing calls, losing estimates, or struggling
with reviews.

As a thank you, I'd knock $200 off your next month for every
introduction that turns into a call."
```

**The Ask (Via Email):**

Subject: quick favor, {FirstName}?

```
Hey {FirstName},

Hope you're loving the results from the AI system. Quick favor:

Do you know 1-2 other home services company owners who could benefit
from what we've set up for you?

Doesn't have to be HVAC -- plumbing, roofing, electrical, landscaping,
cleaning -- any home services company that's missing calls or losing
estimates.

For every referral that books a call with us, I'll credit $200 to
your account. If they sign up, you get a full month free.

Just reply with their name and best contact info and I'll take it
from there. I'll mention you by name (or not -- your call).

Thanks,
{YourName}
```

### 9.2 Referral Incentive Structure

| Referral Action | Reward |
|----------------|--------|
| Referred lead books a discovery call | $200 credit on next invoice |
| Referred lead signs up for Tier 1 | 1 month free ($497 value) |
| Referred lead signs up for Tier 2 | 1 month free ($997 value) |
| Referred lead signs up for Tier 3 | 1 month free ($1,997 value) |
| 3+ referrals that sign up in a quarter | "Founding Partner" status: permanent 10% discount |

### 9.3 Partner Program

**Target Partners:**
- Marketing agencies that serve home services companies
- Business coaches who work with contractors
- CRM consultants (ServiceTitan, Housecall Pro, Jobber)
- Accountants/bookkeepers who serve trades businesses
- Trade association leaders

**Partner Offer:**

```
"We pay 15% recurring commission for every client you refer who signs up.
That means:

- Tier 1 referral: $74.55/month for as long as they're a client
- Tier 2 referral: $149.55/month
- Tier 3 referral: $299.55/month

Send us 5 Tier 2 clients and you're earning $747/month passively.
We handle all the sales, onboarding, and support. You just make
the introduction."
```

**Partner Outreach Email:**

Subject: partnership opportunity -- home services AI

```
Hey {PartnerName},

I noticed you work with home services companies through {TheirBusiness}.
I run UAIS -- we build AI systems for HVAC, plumbing, and roofing
companies (call answering, follow-up, reviews).

We're looking for a few strategic partners who are already trusted
by home services business owners. The deal:

- You refer clients who need AI/automation
- We handle everything (sales, setup, support)
- You earn 15% recurring monthly commission

No minimums. No exclusivity. Just a way for your clients to get
better results and for you to earn on the relationship.

Want to hop on a 15-minute call to see if there's a fit?

-- {YourName}
```

---

## 10. CONTENT MARKETING PLAN

### 10.1 YouTube Video Topics (20 Ideas)

1. "I Called 50 HVAC Companies After Hours -- Here's What Happened"
2. "How One Plumber Went From 3.8 to 4.7 Stars in 90 Days"
3. "The $15,000/Month Mistake Every HVAC Company Makes"
4. "AI vs. Answering Service: Which Is Better for Contractors?"
5. "How to Calculate How Much Revenue You're Losing From Missed Calls"
6. "5 Automations Every Home Services Company Needs in 2026"
7. "I Built an AI Receptionist for a Roofing Company -- Here's the Result"
8. "Why Your Estimates Aren't Closing (And How to Fix It)"
9. "The Exact Follow-Up Sequence That Closes 30% More Estimates"
10. "How to Get 25 Google Reviews Per Month on Autopilot"
11. "What Happens When AI Answers Your HVAC Company's Phone (Live Demo)"
12. "Home Services Companies Making $1M+ All Do These 3 Things"
13. "How to Reactivate Past Customers and Add $10K/Month in Revenue"
14. "The Seasonal Marketing Playbook for HVAC Companies"
15. "I Spent $500 on AI vs. $2,000 on an Answering Service -- Here's What Won"
16. "3 Signs Your Home Services Company Is Ready for AI"
17. "How to Compete With Bigger Contractors (Without Spending More on Ads)"
18. "The Hidden Cost of Slow Response Time in Home Services"
19. "How to Systemize Your Home Services Company (Without Hiring an Office Manager)"
20. "What I Learned Working With 50+ Home Services Companies on AI"

### 10.2 LinkedIn Post Templates (10 Templates)

**Template 1: The Stat Bomb**
```
I called 50 HVAC companies in Dallas after 5 PM last week.

Here's what happened:

- 37 went to voicemail
- 8 had a generic answering service
- 4 had an automated text-back
- 1 had AI that booked the appointment

That's 74% of companies sending leads straight to their competitors.

If you're a home services company owner reading this:
Call your own business tonight at 7 PM.

What happens?

If the answer is "voicemail" -- DM me. We should talk.
```

**Template 2: The Counterintuitive Take**
```
Hot take: Most home services companies don't have a lead problem.

They have a follow-up problem.

Here's what I mean:

The average HVAC company gets 200+ inbound calls per month.
They close about 40% of their estimates.
They follow up on unsold estimates... once. Maybe.

That means 60% of leads they already PAID for just... disappear.

You don't need more leads. You need to convert the ones you have.

AI follow-up converts 15-25% of those "lost" estimates.

On a $4,000 average job, that's $12,000-$20,000/month in recovered revenue.

Without spending another dollar on marketing.
```

**Template 3: The Story**
```
6 months ago, I met a plumbing company owner named Mike.

Mike had 3 trucks, 4 techs, and was doing about $800K/year.

His biggest frustration: "I know we're missing calls. I know
estimates are falling through the cracks. But I'm too busy
running jobs to fix it."

We set up three things:
1. AI answering his phone after hours
2. Automated estimate follow-up (5 touches over 30 days)
3. Review automation after every completed job

Within 90 days:
- 34 recovered leads from after-hours calls
- 11 estimates closed that would have been lost
- Went from 28 to 89 Google reviews
- Revenue up 31%

Mike didn't hire anyone new. Didn't increase his ad spend.
He just stopped letting money slip through the cracks.

If you're in the same boat, DM me. I'll show you how it works.
```

**Template 4: The How-To**
```
How to calculate exactly how much revenue your home services
company is losing every month:

Step 1: Count your daily inbound calls (check your phone system)
Step 2: Multiply by 27% (industry average missed call rate)
Step 3: Multiply by 30 days
Step 4: Multiply by your average ticket
Step 5: Multiply by 30% (percentage that would have booked)

Example for an HVAC company:
15 calls/day x 27% = 4 missed/day
4 x 30 = 120 missed/month
120 x $350 avg ticket x 30% = $12,600/month

That's $151,200/year in revenue walking out the door.

Do the math for your business. Then DM me and I'll show you
how to fix it.
```

**Template 5: The Before/After**
```
Before UAIS:
- 23 Google reviews
- 27% of calls going to voicemail
- 38% close rate on estimates
- $52,000/month revenue

After UAIS (90 days):
- 94 Google reviews
- 0% missed calls
- 51% close rate on estimates
- $78,000/month revenue

Same number of trucks. Same number of techs.
Same marketing budget.

The only thing that changed: we stopped letting leads
fall through the cracks.

This was one HVAC company in Texas. We've seen similar
results across plumbing, roofing, and electrical.

Want to see what the numbers look like for your company?
Link in the first comment.
```

**Template 6: The Question Post**
```
Question for home services company owners:

When was the last time you called your own business
after hours?

Do it tonight. Call at 7 PM and see what happens.

If you get voicemail, that's what every potential
customer is experiencing too.

78% of them will call the next company on the list.

What did you get when you called? Drop it in the comments.
```

**Template 7: The Myth Buster**
```
"AI is going to replace my office staff."

No, it's not. Here's what it actually does:

It handles the stuff your staff CAN'T do:
- Answer calls at 9 PM on a Tuesday
- Follow up on 47 estimates simultaneously
- Send review requests after every single job
- Reactivate 2,000 past customers for seasonal campaigns

Your office manager is great at what they do.
But they can't work 24/7.
AI can.

It's not a replacement. It's a multiplier.
```

**Template 8: The Lesson Learned**
```
Biggest lesson I learned working with 50+ home
services companies:

The ones who grow fastest aren't better at their trade.
They're better at answering the phone.

That's it. That's the secret.

The fastest company to respond wins the job. Not the
cheapest. Not the most experienced. The fastest.

Speed to lead is everything in home services.

If your response time is measured in hours instead of
seconds, you're losing to someone who's faster.
```

**Template 9: The Analogy**
```
Imagine you own a restaurant.

Every night, 30% of customers walk in,
see no one at the host stand, and leave.

You'd fix that immediately, right?

That's exactly what's happening at your home
services company when calls go to voicemail.

30% of your "customers" are walking in (calling),
seeing no one (voicemail), and leaving (calling
your competitor).

The fix costs less than a part-time employee.
And it works 24/7/365.
```

**Template 10: The Direct Offer**
```
I'm looking for 5 home services companies in [State]
to beta-test our new AI call + follow-up system.

What you get:
- AI receptionist (answers 24/7)
- Missed call text-back
- Estimate follow-up automation
- Review request automation

What it costs:
- $497/month (normally $1,500 setup -- waived for beta)

What I need from you:
- 15-minute setup call
- Honest feedback after 30 days

If it doesn't generate at least $3,000 in recovered revenue
in the first month, I'll refund you in full.

DM me "BETA" if you're interested. First 5 only.
```

### 10.3 Case Study Template

Use this format for every client case study:

```markdown
# Case Study: How {CompanyName} {Achieved Result} in {Timeframe}

## The Company
- **Name:** {CompanyName}
- **Trade:** {HVAC / Plumbing / Roofing / etc.}
- **Location:** {City, State}
- **Size:** {X techs, $X annual revenue}
- **Time as UAIS client:** {X months}

## The Problem
{2-3 sentences describing their situation before UAIS. Be specific with
numbers: how many calls they were missing, their close rate, their review
count, their pain points.}

## The Solution
{Which UAIS tier they chose and why. What specific features were most
important to them.}

### What We Set Up:
1. {Feature 1 -- e.g., AI receptionist handling after-hours calls}
2. {Feature 2 -- e.g., 5-touch estimate follow-up sequence}
3. {Feature 3 -- e.g., Automated review requests post-job}

## The Results (After {X} Days)

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Monthly revenue | ${before} | ${after} | +{X}% |
| Google reviews | {before} | {after} | +{X} |
| Missed calls | {X}% | {X}% | -{X}% |
| Estimate close rate | {X}% | {X}% | +{X}% |
| Response time | {X} hours | {X} seconds | -{X}% |

## ROI Breakdown
- **Monthly investment:** ${tier price}
- **Monthly revenue recovered:** ${amount}
- **Return on investment:** {X}x

## What {OwnerName} Says
"{Direct quote from the client about their experience.}"

-- {OwnerName}, Owner, {CompanyName}
```

---

## 11. METRICS AND TRACKING

### 11.1 Pipeline Stages

| Stage | Definition | Expected Conversion |
|-------|-----------|-------------------|
| 1. Prospect | Scraped/enriched, not yet contacted | -- |
| 2. Contacted | In an active email sequence or called | 10-15% to Stage 3 |
| 3. Engaged | Replied to email, answered call, connected on LinkedIn | 30-40% to Stage 4 |
| 4. Discovery Call Booked | Meeting is on the calendar | 70-80% show rate |
| 5. Discovery Call Completed | Call happened, qualified | 50-60% to Stage 6 |
| 6. Demo/Proposal Sent | Showed the system, presented pricing | 30-40% to Stage 7 |
| 7. Negotiation | Interested but has objections or needs time | 50-60% to Stage 8 |
| 8. Closed Won | Signed up, payment received | -- |
| 9. Closed Lost | Said no or went dark after 30-day follow-up | -- |
| 10. Nurture (90-Day) | Not now but maybe later; drip every 90 days | 5-10% reactivate |

### 11.2 KPIs to Track

**Daily KPIs:**
| Metric | Target |
|--------|--------|
| New prospects added to sequences | 50-100 |
| Emails sent | 200-400 |
| Email replies received | 5-15 |
| Cold calls made | 10-20 |
| LinkedIn connection requests sent | 20-30 |
| Discovery calls booked | 1-2 |

**Weekly KPIs:**
| Metric | Target |
|--------|--------|
| Total prospects contacted | 300-500 |
| Email open rate | 40-60% |
| Email reply rate | 3-8% |
| Cold call connect rate | 15-25% |
| Discovery calls completed | 5-8 |
| Demos completed | 3-5 |
| Proposals sent | 3-5 |
| Deals closed | 1-2 |
| Revenue closed | $2,000-$10,000 MRR |

**Monthly KPIs:**
| Metric | Target |
|--------|--------|
| Total prospects contacted | 1,200-2,000 |
| Discovery calls completed | 20-30 |
| Demos completed | 12-20 |
| Deals closed | 4-8 |
| New MRR added | $4,000-$16,000 |
| Setup revenue collected | $6,000-$30,000 |
| Pipeline value (total) | $50,000-$100,000 |
| Average deal size (MRR) | $700-$1,200 |
| Sales cycle length | 14-30 days |
| Customer acquisition cost (CAC) | less than $500 |
| Churn rate | less than 5% |

### 11.3 Weekly Sales Meeting Agenda

**Every Monday, 30 Minutes:**

1. **Pipeline Review (10 min)**
   - How many deals in each stage?
   - What's expected to close this week?
   - What's stuck and why?

2. **Activity Review (5 min)**
   - Did we hit last week's activity targets?
   - Where are we short? (emails, calls, LinkedIn)

3. **Win/Loss Analysis (5 min)**
   - What closed last week and why?
   - What did we lose and why?
   - Any objections coming up repeatedly?

4. **This Week's Plan (10 min)**
   - Priority prospects to follow up with
   - Any demos scheduled?
   - Any content to publish?
   - Any referrals to pursue?

### 11.4 Monthly Sales Report Template

```
UAIS MONTHLY SALES REPORT -- {Month} {Year}

REVENUE
- New MRR added: ${amount}
- Setup fees collected: ${amount}
- Total new revenue: ${amount}
- Cumulative MRR: ${amount}

PIPELINE
- New prospects added: {number}
- Discovery calls booked: {number}
- Discovery calls completed: {number}
- Demos completed: {number}
- Proposals sent: {number}
- Deals closed: {number}
- Deals lost: {number}

CONVERSION RATES
- Email reply rate: {X}%
- Call-to-meeting rate: {X}%
- Meeting-to-demo rate: {X}%
- Demo-to-close rate: {X}%
- Overall lead-to-close rate: {X}%

TOP WINS
1. {Company} -- {Tier} -- {MRR} -- closed because {reason}
2. {Company} -- {Tier} -- {MRR} -- closed because {reason}
3. {Company} -- {Tier} -- {MRR} -- closed because {reason}

TOP LOSSES / LESSONS
1. {Company} -- lost because {reason} -- lesson: {lesson}
2. {Company} -- lost because {reason} -- lesson: {lesson}

NEXT MONTH FOCUS
- Target: {X} new deals, ${X} new MRR
- Priority: {which vertical / city / sequence to focus on}
- New experiment: {what we're testing}
```

### 11.5 Recommended CRM Setup

**If budget is tight:** Google Sheets or Airtable
- One tab/view per pipeline stage
- Columns: Company, Contact, Email, Phone, Score, Stage, Last Touch, Next Step, Notes
- Color code by tier fit (green = T3, yellow = T2, blue = T1)

**If ready to invest:** GoHighLevel ($97-297/mo) or Close.com ($49-99/mo)
- GoHighLevel is ideal because it handles CRM + email + SMS + phone + pipeline in one tool
- Built for agencies selling to local businesses
- Has built-in automation for follow-up sequences

**Pipeline Tracking Minimum:**
- Every prospect has a stage
- Every prospect has a "next step" and a "next step date"
- Move prospects through stages daily
- Review pipeline every Monday
- No prospect sits in a stage for more than 14 days without action

---

## APPENDIX: QUICK REFERENCE

### Pricing At a Glance

| | Tier 1: Lead Recovery Engine | Tier 2: Growth Machine | Tier 3: AI Ops Hub |
|--|-----|-----|-----|
| **Setup** | $1,500 | $3,500 | $7,500 |
| **Monthly** | $497/mo | $997/mo | $1,997/mo |
| **Best For** | 1-5 techs, $250K-$750K revenue | 5-20 techs, $750K-$2M revenue | 20+ techs, $2M+ revenue |
| **Key Features** | AI receptionist, follow-up, reviews | + outreach, estimate follow-up, seasonal | + dispatch, invoicing, dashboard |
| **Expected ROI** | 5-10x | 10-20x | 15-30x |

### Seasonal Campaign Calendar

| Month | Campaign | Vertical |
|-------|----------|----------|
| January | "Heating system checkup" | HVAC |
| February | "Pre-spring roof inspection" | Roofing |
| March | "Spring AC tune-up early bird" | HVAC |
| April | "Spring cleanup + landscape refresh" | Landscaping |
| May | "AC ready for summer?" | HVAC |
| June | "Mid-summer plumbing check" | Plumbing |
| July | "Peak heat -- emergency AC service" | HVAC |
| August | "Back to school -- home electrical safety" | Electrical |
| September | "Pre-winter furnace inspection" | HVAC |
| October | "Fall gutter + roof prep" | Roofing |
| November | "Holiday cleaning special" | Cleaning |
| December | "Frozen pipe prevention" | Plumbing |

### Key Stats to Memorize

- 78% of customers hire the first company that responds
- 27% of inbound calls to home services companies go unanswered
- 60% of estimates never close (without follow-up)
- 93% of consumers check Google reviews before choosing a contractor
- The average home services company loses $8,000-$15,000/month from missed calls
- Companies with 100+ Google reviews get 3x more clicks than those with fewer than 50
- 5-touch follow-up converts 15-25% of "lost" estimates
- AI answering costs $400-600/mo vs. $800-1,500/mo for a human answering service

---

*This playbook is a living document. Update it as you learn what works, what doesn't, and what your market responds to. Review and revise quarterly.*

*UAIS -- Using AI to Scale*
