# Lead Follow-Up Engine — Technical Specification

## Purpose
Automatically follow up with every lead that doesn't book on first contact, using a multi-touch sequence across text, email, and phone over 14 days. Recover 20-35% of leads that would otherwise go cold.

---

## The Core Problem
- 78% of sales go to the first responder
- Average home services follow-up: 1 attempt, then forgotten
- 80% of sales require 5+ follow-up touches
- Most home services companies do ZERO systematic follow-up

---

## Sequence Design

### The 7-Touch Follow-Up Sequence

| Touch | Timing | Channel | Message Type |
|-------|--------|---------|-------------|
| 1 | Immediate (within 60 sec) | Text + Email | Confirmation + intro |
| 2 | 4 hours later | Text | Availability check |
| 3 | Day 1 (next morning) | Email | Value + social proof |
| 4 | Day 3 | Text | Helpful tip related to their issue |
| 5 | Day 5 | Phone (AI call) | Quick check-in call |
| 6 | Day 7 | Text | Limited-time offer |
| 7 | Day 14 | Email | Final touch + soft close |

### Touch Details

**Touch 1 — Immediate Confirmation (Text + Email)**
```
TEXT: "Hi [Name], thanks for reaching out to [Company]! We got your request
about [service]. I have availability [tomorrow/this week]. Would [Day] at
[Time] work for you? Reply YES to confirm or suggest another time. — [Company]"

EMAIL: Subject: "[Company] — Your [Service] Request"
Body: Confirmation of their inquiry, what to expect, company credentials
(years in business, reviews, licenses), next step to book.
```

**Touch 2 — Availability Check (Text, 4 hours later)**
```
"Hey [Name], just following up on your [service] request. We have a tech
available [specific time]. Want me to lock that in? — [Company]"
```

**Touch 3 — Value + Social Proof (Email, Day 1)**
```
Subject: "Quick tip about your [AC issue / plumbing concern / etc.]"
Body: Helpful information about their specific issue + "We helped a homeowner
in [their area] with the exact same issue last week. Here's what we found..."
+ CTA to book
```

**Touch 4 — Helpful Tip (Text, Day 3)**
```
"[Name], quick tip while you're deciding: [specific helpful tip related to
their service need]. If you want us to take a look, we're available this week.
Just reply and I'll get you booked. — [Company]"
```

**Touch 5 — AI Phone Call (Day 5)**
```
AI calls: "Hi [Name], this is [AI name] from [Company]. I'm following up on
your [service] request from earlier this week. Just wanted to check — did you
still need help with that? ... Great, I can get you on the schedule for
[available time]. Does that work?"
```

**Touch 6 — Limited Offer (Text, Day 7)**
```
"[Name], we're running a [seasonal/weekly] special this week — [specific offer:
free diagnostic, $50 off, waived trip charge]. If you still need help with
[service], now's a great time. Book here: [link] — [Company]"
```

**Touch 7 — Final Touch (Email, Day 14)**
```
Subject: "Still need help with [service]?"
Body: "Hi [Name], I know life gets busy. Just wanted to reach out one more
time about your [service] request. If you've already handled it — great!
If not, we're here whenever you're ready. You can book anytime at [link]
or just reply to this email. — [Company Team]"
```

---

## Automation Logic

### Trigger Events
- New lead enters CRM without appointment booked
- Web form submission
- Missed call (no appointment resulted)
- AI Receptionist conversation where caller didn't book
- Google Business Profile message

### Stop Conditions (Immediately halt sequence)
- Lead books an appointment → send confirmation, stop
- Lead replies "stop" or "unsubscribe" → opt out, stop
- Lead replies with negative intent → flag for human, stop
- Lead replies positively → engage in real-time conversation, attempt to book
- Lead marks as spam → remove from all sequences

### Re-Engagement Triggers
- Lead who went cold opens an old email → restart with Touch 5 (phone call)
- Lead who said "not right now" → re-enter sequence in 30/60/90 days
- Seasonal trigger (their original issue is seasonal) → targeted seasonal campaign

---

## Technical Stack

| Component | Tool | Function |
|-----------|------|----------|
| Automation Engine | n8n or Make | Orchestrates the sequence timing and logic |
| SMS | Twilio | Sends/receives text messages |
| Email | SendGrid or ActiveCampaign | Sends emails, tracks opens/clicks |
| AI Phone Calls | Vapi/Bland.ai | Makes the Day 5 follow-up call |
| CRM | ServiceTitan/HCP/Jobber API | Checks booking status, updates lead records |
| AI Processing | Claude API | Personalizes messages based on lead data |

---

## Personalization Engine

Every message is personalized with:
1. **Lead name** — from initial contact
2. **Service type** — what they originally inquired about
3. **Location** — their area/neighborhood
4. **Urgency context** — what's at risk if they wait (e.g., "leaving an AC issue can lead to compressor failure")
5. **Social proof** — recent job in their area with similar issue
6. **Seasonal relevance** — tie to current weather/season

**Example personalization variables:**
```
{{first_name}} — John
{{service_type}} — AC repair
{{neighborhood}} — Westshore
{{urgency_tip}} — Running your AC when it's not cooling properly can damage the compressor
{{social_proof}} — We just fixed the same issue for a homeowner on Bay to Bay last week
{{seasonal_hook}} — With temperatures hitting 95 this week
{{offer}} — Free diagnostic (normally $89)
{{booking_link}} — https://book.company.com/schedule
```

---

## Performance Metrics

| Metric | Target | Benchmark |
|--------|--------|-----------|
| Sequence completion rate | >90% (all 7 touches sent) | Most companies: 1 touch |
| Text response rate | 25-35% | Industry avg: 45% for first text, drops after |
| Email open rate | 35-50% | Industry avg: 20% |
| Booking rate from sequence | 20-35% of leads who enter | Industry avg: 5-10% |
| Opt-out rate | <3% | If higher, adjust messaging frequency |
| Time to first response | <60 seconds | Industry avg: 47 minutes |

---

## Compliance

- **TCPA:** All texts require prior express consent (captured via web form or inbound call)
- **CAN-SPAM:** All emails include unsubscribe link and physical address
- **Opt-out:** Instant opt-out on "STOP" keyword for SMS
- **Do Not Call:** AI phone calls only to leads who initiated contact (not cold calls)
- **Recording disclosure:** State-specific consent rules for call recording
- **Frequency caps:** Maximum 1 text and 1 email per day to any lead
