# Review Manager System — Technical Specification

## Purpose
Automatically request reviews after every completed job, respond to all reviews (positive and negative) within 4 hours, and track review performance over time. Reviews are the #1 driver of local SEO and trust.

---

## The Numbers That Sell This

- 93% of consumers read online reviews before choosing a local business
- Businesses that respond to reviews earn 35% more revenue
- A 1-star increase on Google = 5-9% revenue increase
- 85% of home services companies never respond to reviews
- 53% never proactively ask for reviews
- Average home services company gets 2-3 organic reviews/month
- With a system: 10-20 reviews/month

---

## System Components

### 1. Post-Job Review Request

**Trigger:** Job marked "complete" in CRM (ServiceTitan/HCP/Jobber)

**Timing:** 2 hours after job completion (let the customer enjoy the fix, then ask)

**The 2-Step Method:**
```
Step 1 — Internal Satisfaction Check (Text):
"Hi [Name], [Tech Name] from [Company] just finished up at your home.
Quick question — how was your experience? Reply 1-5 (5 being amazing!)"

IF response >= 4:
  Step 2 — Google Review Request (Text):
  "Awesome, thank you! 🙌 Would you mind taking 30 seconds to share that
  on Google? It really helps us out: [direct Google review link]"

IF response <= 3:
  Route to owner:
  "[Name] rated their experience [score]. Job #[number]. Tech: [name].
  Service: [service]. Recommend reaching out to resolve."
  DO NOT send Google review link.
```

**Follow-Up if No Review Left (24 hours):**
```
"Hi [Name], just a gentle reminder — if you have a moment, we'd really
appreciate a quick Google review. It takes 30 seconds and helps local
families find reliable [trade] service: [link]"
```

### 2. AI Review Response

**Positive Reviews (4-5 stars):**
- Respond within 4 hours
- Personalized: reference the specific service performed
- Thank the customer by name
- Mention the technician by name
- Include a subtle keyword for SEO ("We're glad we could help with your AC repair in [neighborhood]")
- Keep it warm and genuine, not corporate

**Example:**
```
"Thank you so much, [Name]! We're thrilled to hear [Tech] took great care
of your [service]. It's always great working with homeowners in [neighborhood].
If you ever need anything in the future, we're just a call away. — [Company] Team"
```

**Negative Reviews (1-3 stars):**
- Respond within 2 hours (urgent)
- Acknowledge the issue without being defensive
- Apologize for the experience
- Offer to resolve offline (provide direct phone number)
- Never argue, never make excuses, never blame the customer
- Alert owner immediately via text before posting response

**Example:**
```
"[Name], thank you for sharing your feedback. We're sorry your experience
didn't meet the standard we hold ourselves to. We'd like to make this right.
Could you give us a call at [owner's direct number]? We'll personally make
sure this gets resolved. — [Owner Name], Owner"
```

**Owner Notification for Negative Reviews:**
```
TEXT to owner: "⚠️ New [X]-star review from [Name] on Google.
Job: [service] on [date]. Tech: [tech name].
Issue: '[brief excerpt]'
Suggested response drafted. Review at [link]. Call [Name] at [phone]."
```

### 3. Review Monitoring

- Check Google, Yelp, Facebook, BBB every 2 hours
- New review alert sent to owner's phone
- Track: review count, average rating, response rate, sentiment
- Monthly report: review growth, rating trend, top keywords, tech-specific ratings

---

## Google Review Link Generator

Direct review link format:
```
https://search.google.com/local/writereview?placeid=[PLACE_ID]
```

Setup: Extract Place ID from Google Maps API using business name + address.

Short link: Create branded short URL (e.g., review.companyname.com) that redirects to the Google review page.

---

## Technical Stack

| Component | Tool | Function |
|-----------|------|----------|
| Review Request (SMS) | Twilio | Sends review request texts |
| Review Monitoring | Google Business API + Yelp API | Detects new reviews |
| AI Response Writing | Claude API | Generates personalized review responses |
| CRM Integration | ServiceTitan/HCP/Jobber API | Triggers on job completion |
| Review Posting | Google Business API | Posts responses to Google reviews |
| Reporting | Custom dashboard | Tracks all review metrics |
| Owner Alerts | Twilio SMS | Notifies owner of new reviews |

---

## Review Request Timing by Trade

| Trade | Best Time to Ask | Why |
|-------|-----------------|-----|
| HVAC | 2 hours after completion | Customer is comfortable, enjoying fixed AC/heat |
| Plumbing | 1 hour after completion | Immediate relief from the problem |
| Roofing | 24 hours after completion | Need time to inspect from ground level |
| Electrical | 2 hours after completion | Testing lights/outlets, enjoying the fix |
| Landscaping | Same day, 4 PM | See the result in daylight |
| Cleaning | 1 hour after completion | Fresh and clean, peak satisfaction |

---

## Performance Metrics

| Metric | Target | Industry Avg |
|--------|--------|-------------|
| Review request send rate | 100% of completed jobs | 15-20% |
| Satisfaction survey response rate | 40-60% | N/A (most don't do this) |
| Google review conversion rate | 25-35% of happy customers | 5-10% |
| New reviews per month | 10-20 | 2-3 |
| Review response rate (all platforms) | 95%+ | 15% |
| Response time | <4 hours (positive), <2 hours (negative) | Days to never |
| Average rating trend | Stable or improving | Declining without management |

---

## SEO Impact

Reviews directly affect local SEO ranking:
- **Quantity:** More reviews = higher ranking in Google Maps "local pack"
- **Recency:** Recent reviews weighted more heavily
- **Response rate:** Google rewards businesses that respond
- **Keywords in reviews:** Encourage customers to mention specific services
- **Keywords in responses:** Include service + location naturally

**Target:** Move from position 4-10 in local pack to position 1-3 within 6 months through consistent review generation and response.

---

## Compliance

- Never offer incentives for reviews (violates Google TOS)
- Never ask only happy customers for reviews (FTC guidance)
- The 2-step method is compliant: ask everyone about satisfaction, then direct happy ones to Google
- Unhappy customers get routed to owner for resolution (still asked, just handled differently)
- SMS opt-out respected for review requests
- Review request is ONE ask + ONE reminder, then stop
