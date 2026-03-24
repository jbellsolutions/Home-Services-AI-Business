# AI Receptionist System — Technical Specification

## Purpose
Answer every inbound call to the home services company 24/7/365, qualify the lead, book appointments, and handle emergencies — all with a human-sounding AI voice.

---

## Architecture

```
Inbound Call → CallRail (tracking) → Vapi/Bland.ai (AI voice agent)
                                           │
                                    ┌──────┼──────┐
                                    │      │      │
                              Booking  Emergency  Info Request
                                │         │          │
                            CRM API   SMS to    Answer from
                          (create job)  owner    knowledge base
                                │         │          │
                            Confirmation  Owner     Caller gets
                            text to      takes     answer, offered
                            caller       over      booking
```

## Core Capabilities

### 1. Call Answering
- Custom greeting: "Thanks for calling [Company Name], this is [AI Name]. How can I help you today?"
- Natural conversation flow — not a phone tree
- Understands: service requests, scheduling, pricing questions, emergency calls
- Handles: English + Spanish (bilingual configured per client)
- Fallback: "Let me connect you with a team member" → transfers to owner/dispatcher

### 2. Lead Qualification
During the call, the AI collects:
- Caller name and phone number (via caller ID + confirmation)
- Service address
- Problem description ("My AC isn't cooling" → categorize as AC Repair)
- Urgency level (emergency vs. routine vs. just getting quotes)
- Preferred scheduling window
- How they heard about the company

### 3. Appointment Booking
- Checks real-time availability via CRM API (ServiceTitan/HCP/Jobber)
- Offers 2-3 available time slots
- Books the appointment directly in the CRM
- Sends confirmation text to caller immediately
- Sends notification to dispatcher/owner

### 4. Emergency Handling
Trigger keywords: "no heat," "flooding," "gas smell," "sparking," "pipe burst," "no hot water" (winter)
- Immediately escalates: texts owner's cell + on-call tech
- Tells caller: "I'm sending an emergency alert to our team right now. Someone will call you back within 10 minutes."
- Logs as priority in CRM
- If no response from tech in 5 minutes: calls owner directly

### 5. FAQ Handling
Pre-loaded knowledge base per client:
- Service area boundaries
- Services offered and basic pricing ranges
- Financing options
- Warranty information
- What brands/equipment they service
- Hours of operation
- Emergency fees (after-hours surcharge, etc.)

---

## Technical Stack

| Component | Tool | Cost |
|-----------|------|------|
| AI Voice | Vapi ($0.05/min) or Bland.ai ($0.07/min) | $25-$50/mo per client |
| Call Tracking | CallRail ($45/mo base, $3/number) | $15/mo per client |
| Phone Forwarding | Twilio SIP ($0.0085/min inbound) | $5-$10/mo |
| CRM Integration | ServiceTitan/HCP/Jobber API | $0 (API included) |
| SMS Confirmations | Twilio ($0.0079/text) | $5-$10/mo |
| AI Processing | Claude API (for complex queries) | $2-$5/mo |

**Total per-client cost: $52-$90/month**

---

## Call Flow Logic

```
1. Call comes in
2. CallRail tracks source (Google Ads, organic, LSA, direct)
3. Forward to Vapi/Bland.ai AI agent
4. AI greets caller with business name
5. IF emergency keywords detected:
   → Log as emergency
   → Text owner + on-call tech immediately
   → Tell caller help is on the way
   → Stay on line until human takes over OR caller hangs up
6. IF booking request:
   → Ask qualifying questions (name, address, service, urgency)
   → Query CRM for availability
   → Offer time slots
   → Book appointment in CRM
   → Send confirmation text to caller
   → Send notification to dispatcher
7. IF info question:
   → Answer from knowledge base
   → Offer to book if appropriate
   → "Would you like to schedule a visit?"
8. IF complex/unclear:
   → "Let me connect you with someone who can help with that."
   → Transfer to owner/dispatcher
   → Log the call details for follow-up
9. After call:
   → Log full transcript in CRM
   → Tag with source, service type, urgency
   → Trigger follow-up sequence if no appointment booked
```

---

## Performance Metrics

| Metric | Target | How Measured |
|--------|--------|-------------|
| Answer rate | 100% of calls | CallRail data |
| Average answer time | <3 seconds | Vapi analytics |
| Call duration | 2-4 minutes avg | Vapi analytics |
| Booking rate (from qualified leads) | 35-50% | CRM bookings / qualified calls |
| Emergency escalation time | <60 seconds | SMS delivery timestamp |
| Caller satisfaction | <5% "transfer to human" requests | Call transcripts |
| False emergency rate | <2% | Manual review |

---

## Setup Process

1. **Gather business info** — services, pricing, service area, team, hours
2. **Write AI script** — greeting, qualifying questions, FAQ responses, emergency protocol
3. **Configure Vapi/Bland.ai** — voice selection, script upload, fallback rules
4. **Set up CallRail** — tracking numbers, call forwarding, source tracking
5. **Connect CRM** — API integration for availability check + booking
6. **Configure Twilio** — confirmation texts, emergency alerts
7. **Test** — 20 test calls covering: booking, emergency, FAQ, transfer, Spanish
8. **Go live** — activate forwarding, monitor first 48 hours
9. **Optimize** — review transcripts, adjust script, tune FAQ responses

---

## Edge Cases & Handling

| Scenario | How AI Handles |
|----------|---------------|
| Caller is angry/frustrated | Empathetic tone, offer to connect with manager, log for owner review |
| Caller wants a specific person | "Let me check if [name] is available" → transfer or take message |
| Caller is a vendor/solicitor | Politely decline, do not book, tag as "vendor" |
| Caller has existing appointment | Look up in CRM, confirm or reschedule |
| Caller wants estimate over phone | Provide range if available, offer in-home estimate booking |
| Multiple callers at once | Vapi handles concurrent calls (no busy signal) |
| Poor audio quality | "I'm sorry, I'm having trouble hearing you. Could you repeat that?" |
| Caller hangs up mid-conversation | Log partial info, trigger follow-up text to their number |
