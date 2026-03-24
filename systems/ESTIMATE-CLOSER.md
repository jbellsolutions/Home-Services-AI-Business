# Estimate Closer System — Technical Specification

## Purpose
Automatically follow up on every unsold estimate to recover the 40-60% of quoted revenue that typically goes cold. This is the single biggest revenue leak in home services.

---

## The Problem

- Average HVAC company sends 50-80 estimates per month
- 40-60% never get followed up (24-48 estimates abandoned)
- Average estimate value: $500-$3,000 (residential), $5,000-$25,000 (commercial)
- Revenue sitting on the table: **$12,000-$48,000/month**
- Reason they don't follow up: "I forgot," "I got busy," "I assumed they went with someone else"

## The Reality
- 60% of "lost" estimates were never actually lost — the customer just got busy too
- 35% of properly followed-up estimates close within 14 days
- 80% of contractors do ZERO estimate follow-up

---

## The 6-Touch Estimate Follow-Up Sequence

| Touch | Timing | Channel | Purpose |
|-------|--------|---------|---------|
| 1 | Same day (2 hrs after estimate) | Text | Warm thank-you + questions |
| 2 | Day 2 | Email | Detailed recap + value justification |
| 3 | Day 5 | Text | Check-in + address hesitation |
| 4 | Day 10 | Phone (AI call) | Personal check-in |
| 5 | Day 21 | Text | Incentive offer |
| 6 | Day 45 | Email | Final reactivation |

### Touch Details

**Touch 1 — Same Day Thank You (Text, 2 hours after estimate)**
```
"Hi [Name], thanks for having us out today! [Tech name] put together your
estimate for [service — e.g., 'the new AC system']. Any questions about
the quote? Happy to clarify anything. — [Company]"
```

**Touch 2 — Value Recap (Email, Day 2)**
```
Subject: "Your [service] estimate from [Company]"

Hi [Name],

Thanks again for having us out to look at your [service need].

Here's a quick recap of what we recommended:
- [Service/equipment description]
- Investment: $[amount]
- [Financing option if applicable: "We offer 0% financing for 12 months"]
- [Warranty: "Includes our 2-year labor warranty"]

A few things worth noting:
- [Urgency point: "Running an inefficient AC can add $50-$100/month to your electric bill"]
- [Value point: "The [equipment] we quoted has the highest efficiency rating in its class"]
- [Trust point: "We've installed over 500 of these systems in the [city] area"]

Ready to move forward? Just reply to this email or call us at [phone].

— [Tech Name], [Company]
```

**Touch 3 — Hesitation Handler (Text, Day 5)**
```
"Hey [Name], just checking in on your [service] quote. Totally understand
if you're shopping around — happy to answer any questions or adjust the
scope if needed. What's holding you back? — [Company]"
```

**Touch 4 — AI Phone Call (Day 10)**
```
"Hi [Name], this is [AI name] from [Company]. I'm following up on the
[service] estimate [Tech] put together for you about 10 days ago.
Just wanted to check — have you had a chance to think about it?
... [Handle response: answer questions, offer scheduling, note objections]
... Great, I can get you on the schedule for [date]. Shall I book that?"
```

**Touch 5 — Incentive (Text, Day 21)**
```
"[Name], we have availability this week for [service] and I wanted to
offer you [specific incentive: $200 off / free maintenance plan for 1 year /
waived permit fee / upgraded thermostat]. Valid through [date]. Want me
to book you in? — [Company]"
```

**Touch 6 — Final Reactivation (Email, Day 45)**
```
Subject: "Still thinking about [service]?"

Hi [Name],

It's been a few weeks since we quoted your [service]. If you've already
handled it — great! If not, your quote is still valid and we'd love to
help when you're ready.

[Seasonal urgency if applicable: "With summer coming, now's the ideal
time to handle this before the rush."]

Just reply or call [phone] whenever you're ready. No pressure.

— [Company] Team
```

---

## Automation Logic

### Trigger
- Estimate created in CRM with status "Pending" or "Sent"
- Manual flag by tech: "Customer said they'd think about it"

### Stop Conditions
- Estimate status changes to "Won" / "Accepted" → Send congrats + booking confirmation
- Estimate status changes to "Lost" → Log reason, stop sequence
- Customer replies "not interested" / "went with someone else" → Stop, log reason
- Customer books directly → Stop sequence

### Segmentation by Estimate Value
| Estimate Value | Follow-Up Intensity |
|---------------|-------------------|
| <$500 | Standard 6-touch text/email only |
| $500-$2,000 | Full 6-touch including AI phone call |
| $2,000-$10,000 | Full 6-touch + owner notified for personal call at Touch 4 |
| >$10,000 | Owner handles personally with AI-drafted talking points |

---

## CRM Integration

### ServiceTitan
- Monitor estimate status via API
- Pull: customer name, phone, email, service type, estimate amount, tech name
- Update: add follow-up notes, change status on close

### Housecall Pro
- Webhook on estimate creation
- Pull: same data points
- Update: same

### Jobber
- API polling for new estimates
- Pull: same
- Update: same

---

## Performance Metrics

| Metric | Target | Without System |
|--------|--------|---------------|
| Estimates followed up | 100% | 20-40% |
| Response rate to follow-up | 40-50% | N/A |
| Recovery rate (estimates closed that were going cold) | 20-35% | 0% (never followed up) |
| Average days to close (after follow-up) | 7-14 days | Never |
| Revenue recovered per month | $8,000-$25,000 | $0 |
| Incentive cost (discounts offered) | $500-$1,500/mo | $0 |
| Net revenue recovered | $7,500-$23,500/mo | $0 |

---

## Objection Handling (Built Into AI Responses)

| Customer Says | AI/System Response |
|--------------|-------------------|
| "Too expensive" | Offer financing options, break down cost per month, compare to cost of not fixing |
| "Getting other quotes" | "Totally understand. Happy to match or beat a comparable quote. What are you seeing?" |
| "Not the right time" | "When would be better? I can set a reminder to follow up then." |
| "Need to talk to spouse" | "Of course! Would it help if I sent the estimate details in an email so you can review together?" |
| "Going with someone else" | "Thanks for letting me know. If anything changes, your quote is still valid for 60 days." (Log competitor + reason) |
| No response at all | Continue sequence. They're usually just busy, not disinterested. |

---

## Revenue Impact Calculation

**For a typical $2M HVAC company:**
- Estimates sent/month: 60
- Currently unfollowed: 36 (60%)
- With system — followed up: 60 (100%)
- Recovery rate: 25%
- Additional closes: 9 jobs/month
- Average estimate value: $1,200
- **Monthly revenue recovered: $10,800**
- **Annual revenue recovered: $129,600**
- **Cost of system: included in Tier 2 ($997/mo = $11,964/yr)**
- **ROI: 10.8x on this feature alone**
