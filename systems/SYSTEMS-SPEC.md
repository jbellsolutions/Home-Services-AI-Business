# Home Services AI Platform -- Technical Systems Specification

**Version:** 2.0
**Date:** 2026-03-24
**Status:** Architecture Definition
**Classification:** Internal -- Confidential

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Overall System Architecture](#2-overall-system-architecture)
3. [Tech Stack Summary](#3-tech-stack-summary)
4. [System 1: AI Receptionist](#4-system-1-ai-receptionist)
5. [System 2: Speed-to-Lead Responder](#5-system-2-speed-to-lead-responder)
6. [System 3: Lead Follow-Up Engine](#6-system-3-lead-follow-up-engine)
7. [System 4: Review Manager](#7-system-4-review-manager)
8. [System 5: Estimate Closer](#8-system-5-estimate-closer)
9. [System 6: Cold Outreach System](#9-system-6-cold-outreach-system)
10. [System 7: Neighborhood Targeting](#10-system-7-neighborhood-targeting)
11. [System 8: Seasonal Campaign Engine](#11-system-8-seasonal-campaign-engine)
12. [System 9: AI Dispatcher](#12-system-9-ai-dispatcher)
13. [System 10: Customer Lifecycle Manager](#13-system-10-customer-lifecycle-manager)
14. [System 11: Financial Dashboard](#14-system-11-financial-dashboard)
15. [Data Model](#15-data-model)
16. [Infrastructure Costs Per Client](#16-infrastructure-costs-per-client)
17. [Security and Compliance](#17-security-and-compliance)
18. [Scaling Considerations](#18-scaling-considerations)
19. [Deployment and Onboarding](#19-deployment-and-onboarding)

---

## 1. Executive Summary

This document defines the complete technical architecture for an AI-powered operations platform designed for home services companies (HVAC, plumbing, roofing, electrical, pest control, garage doors, etc.). The platform consists of 11 interconnected systems that replace or augment the client's front-office operations: answering phones, responding to leads, following up on estimates, managing reviews, dispatching technicians, running marketing campaigns, and tracking financial performance.

Each system is deployed per-client as a managed service. The platform is built on a composable automation backbone (n8n self-hosted) with AI inference (Claude API / OpenAI), voice AI (Vapi), messaging (Twilio), email (SendGrid), and CRM integration (ServiceTitan, Housecall Pro, Jobber, or GoHighLevel).

Core philosophy: **We do not replace their software -- we make it work harder.**

---

## 2. Overall System Architecture

```
+-----------------------------------------------------------------------------------+
|                           CLIENT-FACING CHANNELS                                  |
|  Phone  |  Web Forms  |  GBP Messages  |  Facebook  |  Email  |  SMS  |  Mailers |
+----+--------+---------------+--------------+----------+--------+-------+----------+
     |        |               |              |          |        |       |
     v        v               v              v          v        v       v
+-----------------------------------------------------------------------------------+
|                        INGESTION & ROUTING LAYER (n8n)                            |
|                                                                                   |
|  Webhook receivers  |  Polling workers  |  Event listeners  |  Cron triggers      |
+----------+-----------+------------------+-------------------+---------------------+
           |
           v
+-----------------------------------------------------------------------------------+
|                          AI PROCESSING LAYER                                      |
|                                                                                   |
|  Claude API (Anthropic)     -- Intent classification, message generation,         |
|                                conversation management, data extraction           |
|  Vapi                       -- Inbound/outbound voice AI agents                   |
|  OpenAI Whisper (via Vapi)  -- Speech-to-text for call transcription              |
+-----------------------------------------------------------------------------------+
           |
           v
+-----------------------------------------------------------------------------------+
|                       AUTOMATION & ORCHESTRATION (n8n)                             |
|                                                                                   |
|  System 1: AI Receptionist          System 7: Neighborhood Targeting              |
|  System 2: Speed-to-Lead            System 8: Seasonal Campaigns                  |
|  System 3: Lead Follow-Up           System 9: AI Dispatcher                       |
|  System 4: Review Manager           System 10: Customer Lifecycle                 |
|  System 5: Estimate Closer          System 11: Financial Dashboard                |
|  System 6: Cold Outreach                                                          |
+-----------------------------------------------------------------------------------+
           |
           v
+-----------------------------------------------------------------------------------+
|                         DELIVERY LAYER                                            |
|                                                                                   |
|  Twilio (SMS/MMS/Voice)  |  SendGrid (Email)  |  Vapi (Outbound Calls)           |
|  Facebook Graph API      |  Google Business API |  Direct Mail API (PostGrid)     |
+-----------------------------------------------------------------------------------+
           |
           v
+-----------------------------------------------------------------------------------+
|                      CRM & DATA LAYER                                             |
|                                                                                   |
|  ServiceTitan API  |  Housecall Pro API  |  Jobber API  |  GoHighLevel API        |
|  Supabase (PostgreSQL) -- Platform database, analytics, logs                      |
|  Redis (Upstash) -- Caching, rate limiting, session state                         |
|  Cloudflare R2 -- Call recordings, document storage                               |
+-----------------------------------------------------------------------------------+
           |
           v
+-----------------------------------------------------------------------------------+
|                      MONITORING & REPORTING                                       |
|                                                                                   |
|  Grafana -- System health dashboards                                              |
|  PostHog -- Event tracking, funnel analytics                                      |
|  Client Dashboard (Next.js) -- Per-client reporting portal                        |
|  Internal Admin (Next.js) -- Multi-tenant management console                      |
+-----------------------------------------------------------------------------------+
```

### Inter-System Data Flow

```
System 2 (Speed-to-Lead)
    |-- new lead not booked --> System 3 (Follow-Up Engine)
    |-- lead booked job ------> System 9 (Dispatcher)

System 1 (AI Receptionist)
    |-- booked appointment ---> CRM --> System 9 (Dispatcher)
    |-- caller not booked ----> System 3 (Follow-Up Engine)

System 9 (Dispatcher)
    |-- job assigned ----------> Technician notification
    |-- job completed ---------> System 4 (Review Manager)
    |-- job completed ---------> System 7 (Neighborhood Targeting)
    |-- job completed ---------> System 10 (Customer Lifecycle)
    |-- job completed ---------> System 11 (Financial Dashboard)

System 4 (Review Manager)
    |-- review collected ------> System 11 (Financial Dashboard)

System 5 (Estimate Closer)
    |-- estimate accepted -----> CRM --> System 9 (Dispatcher)

System 8 (Seasonal Campaigns)
    |-- campaign responses ----> System 2 (Speed-to-Lead)

System 6 (Cold Outreach)
    |-- positive reply --------> CRM --> System 3 (Follow-Up Engine)

System 10 (Customer Lifecycle)
    |-- maintenance booking ---> CRM --> System 9 (Dispatcher)

ALL SYSTEMS
    |-- costs + events --------> System 11 (Financial Dashboard)
```

---

## 3. Tech Stack Summary

### Core Infrastructure

| Component | Technology | Purpose | Monthly Cost (per client) |
|---|---|---|---|
| Automation Engine | n8n (self-hosted on Railway/Hetzner) | Workflow orchestration for all 11 systems | $2-5 (shared) |
| AI Inference | Claude API (Anthropic claude-sonnet-4-20250514) | Text generation, classification, extraction | $15-40 |
| Voice AI | Vapi (primary) or Bland.ai (fallback) | Inbound/outbound phone AI agents | $50-200 |
| SMS/Voice Routing | Twilio | SMS send/receive, call forwarding, number provisioning | $30-80 |
| Email Delivery | SendGrid (Pro plan) | Transactional + marketing email | $10-25 |
| Database | Supabase (Pro) | PostgreSQL, auth, realtime, edge functions | $3-8 (shared) |
| Cache/Queue | Redis (Upstash) | Rate limiting, job queues, temp state | $1-3 (shared) |
| File Storage | Cloudflare R2 | Call recordings, documents, images | $2-5 |
| Hosting | Railway or Hetzner VPS | n8n, Next.js apps, cron workers | $5-10 (shared) |
| Monitoring | Grafana Cloud (free tier) + PostHog | Alerting, system health, analytics | $0-5 (shared) |

### CRM Integrations (client chooses one)

| CRM | API Type | Key Endpoints Used |
|---|---|---|
| ServiceTitan | REST API v2 | /jobs, /customers, /estimates, /bookings, /dispatch, /invoices, /memberships |
| Housecall Pro | REST API | /jobs, /customers, /estimates, /invoices, /schedules |
| Jobber | GraphQL API | queries: jobs, clients, quotes, invoices, schedules |
| GoHighLevel | REST API v2 | /contacts, /opportunities, /calendars, /conversations, /pipelines |

### External Service APIs

| Service | Purpose | API |
|---|---|---|
| Google Business Profile | Message monitoring, review monitoring | Google My Business API v4.9 |
| Facebook/Instagram | Lead form ingestion, message monitoring | Facebook Graph API v19.0, Webhooks |
| Google Maps Platform | Geocoding, distance calculation, neighborhood targeting | Geocoding API, Distance Matrix API |
| PostGrid | Direct mail / postcard sending | PostGrid Print & Mail API |
| Apollo.io | B2B contact data for cold outreach | Apollo REST API v1 |
| Instantly.ai | Cold email sending infrastructure | Instantly REST API |
| ZeroBounce | Email verification | ZeroBounce API |
| OpenWeatherMap | Weather-triggered campaign triggers | OneCall API 3.0 |
| Google Sheets | Lightweight reporting, client-accessible data | Google Sheets API v4 |

---

## 4. System 1: AI Receptionist

### Purpose and Function

24/7 AI-powered phone answering that books appointments, handles common questions, performs emergency triage, and transfers to a human when needed. Replaces after-hours answering services ($200-500/mo) and handles overflow during business hours. The AI receptionist knows the client's services, pricing ranges, service area, and scheduling availability.

### Technical Architecture

```
Inbound Call (Twilio Number)
    |
    v
Twilio SIP Trunk --> Vapi Voice Agent
    |
    |-- Vapi Configuration:
    |     model: claude-sonnet-4-20250514 (via Anthropic provider in Vapi)
    |     voice: Vapi stock "jennifer" or ElevenLabs "Rachel" (voice_id in Vapi config)
    |     firstMessage: "Thanks for calling {company_name}, this is {agent_name}.
    |                    How can I help you today?"
    |     systemPrompt: per-client prompt stored in Supabase clients.settings
    |     endCallMessage: "Thanks for calling {company_name}. Have a great day!"
    |     tools: [book_appointment, transfer_call, lookup_customer, check_availability]
    |     serverUrl: https://{n8n_host}/webhook/vapi-{client_id}
    |     maxDurationSeconds: 600
    |     silenceTimeoutSeconds: 30
    |     recordingEnabled: true (respects two-party consent states)
    |
    v
Vapi Function Calls (POST to serverUrl --> n8n webhook)
    |
    |-- book_appointment:
    |     n8n receives: {date, time, service_type, customer_name, phone, address}
    |     n8n calls: CRM API POST /bookings
    |     n8n returns to Vapi: {confirmation_number, scheduled_datetime}
    |
    |-- transfer_call:
    |     n8n receives: {reason, urgency}
    |     n8n calls: Twilio REST API - create conference, dial on-call number
    |     Vapi performs warm transfer with context announcement
    |
    |-- lookup_customer:
    |     n8n receives: {phone_number}
    |     n8n calls: CRM API GET /customers?phone={phone}
    |     n8n returns: {name, address, service_history, membership_status, open_estimates}
    |
    |-- check_availability:
    |     n8n receives: {date, service_type}
    |     n8n calls: CRM API GET /availability?date={date}&service={type}
    |     n8n returns: {available_slots: ["9:00 AM", "1:00 PM", "3:30 PM"]}
    |
    v
Post-Call Processing (Vapi webhook: call.ended --> n8n)
    |
    |-- Extract from Vapi payload: transcript, recording_url, duration, cost
    |-- Claude API call: classify outcome + generate summary
    |     Input: full transcript
    |     Output: {outcome, summary, customer_name, service_needed, sentiment_score}
    |     Outcomes: booked | info_request | emergency | transfer | voicemail | spam
    |-- INSERT into Supabase calls table
    |-- Upload recording to Cloudflare R2 (PUT /recordings/{client_id}/{call_id}.mp3)
    |-- UPDATE CRM contact record with call notes via API
    |-- If outcome = emergency AND no transfer completed:
    |     Twilio API: send SMS to emergency_contacts (from clients.settings)
    |     Retry call transfer every 2 minutes for 10 minutes
    |-- Send call summary notification:
    |     SMS to owner (if after hours): "AI took a call from {name} for {service}. {outcome}."
    |     Email to office (always): full summary + transcript link
```

### Data Flow

1. **Input:** Inbound phone call to Twilio-provisioned local number. Client forwards their main business line to this number (conditional forwarding after X rings, outside business hours, or all calls).
2. **Processing:** Vapi manages the real-time voice conversation using Claude as the reasoning engine. During the conversation, Vapi makes synchronous function calls to n8n webhooks for CRM lookups and booking actions. The system prompt includes the client's service area zip codes, pricing guidelines (ranges only), service menu, hours, technician names, and escalation rules.
3. **Output:** Appointment booked in CRM, call transcript and recording saved, summary notification sent to client. If not booked, lead is passed to System 3 (Follow-Up Engine).

### Integration Points

| Integration | Protocol | Details |
|---|---|---|
| Twilio | SIP trunk to Vapi; REST API for transfers | Provisions one local number per client. Number ported or forwarded from client's existing line. |
| Vapi | REST API for config; webhooks for events | Hosts voice agent. POST /assistant to create/update. Webhooks: function-call, call.ended, transcript.update. |
| CRM | REST/GraphQL API | Real-time during conversation: customer lookup, availability check, booking creation. Latency requirement: < 2 seconds per API call. |
| Claude API | REST API via Vapi provider config | Vapi sends conversation turns to Claude. We also call Claude directly for post-call classification. |
| Supabase | PostgreSQL + REST API | Call logs, transcripts, recording metadata, per-call cost tracking. |
| Cloudflare R2 | S3-compatible API | Call recording storage. Presigned URLs for playback in dashboard. |

### Automation Triggers

| Trigger | Source | Condition |
|---|---|---|
| Inbound call received | Twilio SIP | Always active, 24/7/365 |
| Conditional forwarding | Client's phone system | After X rings (configurable), outside business hours, all lines busy |
| Outbound AI call | System 3 integration | Lead follow-up: Vapi POST /call with outbound agent config |
| Configuration update | Admin dashboard | Owner updates hours, services, pricing -- pushes to Vapi via API |

### Human Escalation Rules

| Condition | Detection Method | Action |
|---|---|---|
| Caller says "speak to a person" / "real person" / "manager" | Vapi transcript keyword detection | Warm transfer to on-call staff via Twilio conference |
| Emergency detected (gas leak, flooding, no heat in winter, fire) | Claude intent classification in system prompt | Immediate transfer + SMS alert to owner + emergency contacts |
| Caller is angry/frustrated | Claude sentiment analysis (sentiment < -0.7) | Transfer to office manager with context |
| Booking requires custom pricing (> configurable threshold) | Function call returns price_exceeds_threshold | Take message, flag for callback within 1 hour |
| 3+ failed tool calls in one conversation | n8n error counter | Transfer to office or take detailed voicemail |
| Language not English/Spanish | Vapi language detection | Transfer to office with language note |
| Caller on "VIP list" | CRM lookup returns vip_flag = true | Transfer immediately to owner/designated person |

### Key Metrics

| Metric | Source | Target |
|---|---|---|
| Call answer rate | Vapi analytics API | > 98% |
| Average handle time | Vapi call duration field | < 3 minutes |
| Booking conversion rate | CRM bookings / total non-spam calls | > 35% |
| Transfer rate (to human) | Calls transferred / total calls | < 15% |
| Customer satisfaction (post-call survey) | Twilio IVR 1-5 rating after call | > 4.2/5 |
| Cost per call | (Vapi cost + Twilio cost + Claude cost) / total calls | < $1.50 |
| Emergency detection accuracy | Manual audit sample | > 95% |
| Emergency response time (detection to human contact) | Timestamp diff in system_logs | < 60 seconds |
| Voicemail rate | Calls going to voicemail / total calls | < 5% |
| Transcript accuracy | Manual audit sample | > 90% |

---

## 5. System 2: Speed-to-Lead Responder

### Purpose and Function

Monitors all digital lead sources (website forms, Google Business Profile messages, Facebook messages and lead ads, Yelp leads, Thumbtack leads, Angi leads) and responds within 60 seconds via the channel the lead arrived on plus a parallel SMS and email. Industry data shows that responding to a lead within 5 minutes makes you 21x more likely to convert compared to waiting 30 minutes. This system targets sub-60-second response.

### Technical Architecture

```
Lead Sources (all feed into n8n):
    |
    +-- Website Form Submit
    |     Webhook: POST https://{n8n_host}/webhook/lead-{client_id}
    |     Setup: WordPress plugin (WPForms/Gravity Forms webhook addon),
    |            or custom JS: fetch(webhookUrl, {method:'POST', body: formData})
    |     Payload: {name, phone, email, service, address, source: "website"}
    |
    +-- Google Business Profile Message
    |     Method A: Google Business Messages API webhook (Pub/Sub push)
    |       Subscribe: projects/{project}/subscriptions/{sub}
    |       Push endpoint: https://{n8n_host}/webhook/gbp-{client_id}
    |     Method B: Polling (fallback if webhook setup fails)
    |       n8n Cron: every 30 seconds
    |       GET /v4/accounts/{account}/locations/{location}/questions
    |       GET conversations via Business Communications API
    |
    +-- Facebook Lead Ad
    |     Facebook Webhooks: subscribe to page leadgen events
    |     App subscription: POST /{page_id}/subscribed_apps?subscribed_fields=leadgen
    |     Webhook: POST https://{n8n_host}/webhook/fb-lead-{client_id}
    |     On webhook: GET /{leadgen_id}?fields=field_data to fetch form fields
    |
    +-- Facebook Messenger
    |     Facebook Webhooks: subscribe to page messages
    |     Webhook: POST https://{n8n_host}/webhook/fb-msg-{client_id}
    |     Payload: messaging[0].message.text, messaging[0].sender.id
    |
    +-- Yelp Lead (email-based)
    |     SendGrid Inbound Parse: MX record on leads.{client-domain}.com
    |     Parse webhook: POST https://{n8n_host}/webhook/email-lead-{client_id}
    |     n8n extracts: sender, subject, body text, identifies Yelp format
    |
    +-- Thumbtack Lead (email-based)
    |     Same SendGrid Inbound Parse pipeline
    |     n8n identifies Thumbtack email format, extracts lead data
    |
    +-- Angi Lead (email-based)
    |     Same SendGrid Inbound Parse pipeline
    |     n8n identifies Angi email format, extracts lead data
    |
    v
n8n: Lead Normalization Node (Function/Code node)
    |
    |-- Extract and normalize: first_name, last_name, phone (E.164 format),
    |   email, service_needed, address, source, raw_message, timestamp
    |-- Phone normalization: strip formatting, add +1, validate with Twilio Lookup API
    |     GET /v2/PhoneNumbers/{phone}?Fields=line_type_intelligence
    |     Reject VoIP/landline for SMS (flag for call-only follow-up)
    |-- Deduplicate: SELECT FROM contacts WHERE client_id = X
    |   AND (phone = Y OR email = Z) AND created_at > NOW() - INTERVAL '24 hours'
    |   If duplicate: update existing record, do not start new sequence
    |-- Geocode address: Google Maps Geocoding API
    |     GET /geocode/json?address={address}&key={api_key}
    |-- Service area check: is geocoded lat/lng within client's service area polygons?
    |   (stored in clients.settings.service_area as GeoJSON)
    |
    v
Claude API: Intent Classification + Response Generation
    |
    |-- Endpoint: POST https://api.anthropic.com/v1/messages
    |-- Model: claude-sonnet-4-20250514
    |-- System prompt includes: client's service catalog, pricing ranges, current
    |   promotions, brand voice guidelines, service area, hours
    |-- User message: "Classify this lead and generate a response:\n{lead_data}"
    |-- Output (structured JSON via tool_use):
    |   {
    |     "intent": "service_request",     // emergency | service_request |
    |                                       // estimate_request | question | spam
    |     "urgency": "standard",           // emergency | urgent | standard | low
    |     "service_category": "ac_repair", // mapped to client's service catalog
    |     "response_sms": "Hi {name}, thanks for reaching out to {company}!
    |                      We can help with your AC issue. We have availability
    |                      tomorrow. Want me to schedule a time? Reply YES or
    |                      call us at {phone}.",
    |     "response_email_subject": "Your AC Service Request - {company}",
    |     "response_email_body": "<html>...(branded template)...</html>",
    |     "response_channel": "Thanks for your message! We'd love to help with
    |                          your {service}. We just sent you a text with
    |                          scheduling options.",
    |     "follow_up_plan": "standard_14day"
    |   }
    |
    v
Multi-Channel Response (n8n parallel execution, all within 60 seconds):
    |
    +-- SMS via Twilio:
    |     POST https://api.twilio.com/2010-04-01/Accounts/{sid}/Messages.json
    |     From: client's Twilio number
    |     To: lead's phone
    |     Body: response_sms (< 160 chars ideal, up to 1600 chars with concatenation)
    |     StatusCallback: https://{n8n_host}/webhook/sms-status-{client_id}
    |
    +-- Email via SendGrid:
    |     POST https://api.sendgrid.com/v3/mail/send
    |     from: {client_name} <noreply@{client-domain}.com>
    |     to: lead's email
    |     template_id: client's branded template in SendGrid
    |     dynamic_template_data: {name, service, company, phone, booking_link}
    |
    +-- Original channel reply (if applicable):
    |     GBP: POST Business Messages API reply to conversation
    |     Facebook Messenger: POST /{page_id}/messages
    |       {recipient: {id: sender_id}, message: {text: response_channel}}
    |     Facebook Lead Ad: no direct reply channel (SMS/email only)
    |
    v
CRM Record Creation (n8n):
    |
    +-- Check if contact exists: GET /customers?phone={phone}
    |   If exists: update existing contact, add new lead/opportunity
    |   If new: POST /contacts with all captured data
    +-- Create opportunity/lead: POST /opportunities
    |   {contact_id, source, service_type, value_estimate, status: "new"}
    +-- Attach notes: lead source, AI classification, messages sent, timestamps
    |
    v
Enqueue for System 3 (n8n):
    |-- INSERT INTO sequences (
    |     client_id, contact_id, sequence_type: follow_up_plan,
    |     current_step: 1, status: 'active',
    |     next_fire_at: NOW() + INTERVAL '24 hours'  -- step 2 fires tomorrow
    |   )
    |-- (Step 1 = the instant response we just sent)
```

### Data Flow Summary

1. **Input:** Form submission, platform message, or lead notification from any digital source.
2. **Processing:** n8n receives webhook/poll, normalizes lead data, deduplicates, validates phone, geocodes address, checks service area. Claude classifies intent and generates personalized responses.
3. **Output:** Response sent via SMS + email + original channel (all within 60 seconds). Contact and opportunity created in CRM. Lead enrolled in follow-up sequence.

### Integration Points

| Integration | Protocol | Details |
|---|---|---|
| Website forms | Webhook POST to n8n | Client adds webhook URL to their form plugin. We provide a lightweight JS snippet as fallback. |
| Google Business Profile | Pub/Sub push or 30s polling | Requires OAuth 2.0 with `business.manage` scope. Per-client OAuth tokens stored encrypted in Supabase. |
| Facebook Graph API | Webhooks (leadgen + messages) | Requires Facebook App with `pages_messaging` and `leads_retrieval` permissions. Page access tokens stored encrypted. |
| SendGrid Inbound Parse | Webhook on email receipt | MX record on subdomain routes inbound email to n8n. Parses Yelp/Angi/Thumbtack email formats. |
| Twilio | REST API for SMS send; webhooks for replies | Per-client Twilio number. SMS replies trigger n8n webhook for continued AI conversation. |
| Twilio Lookup | REST API for phone validation | Validates phone type (mobile/landline/VoIP) before SMS. $0.005/lookup. |
| CRM | REST/GraphQL API | Contact creation, opportunity creation, data enrichment. |
| Google Maps Geocoding | REST API | Address validation and geocoding. $0.005/request. |
| Supabase | PostgreSQL | Lead storage, deduplication queries, sequence enrollment. |

### Automation Triggers

| Trigger | Source | Latency Target |
|---|---|---|
| Website form submission | Webhook POST | < 30 seconds |
| GBP message received | Pub/Sub push or 30s polling | < 60 seconds |
| Facebook lead ad submitted | Webhook (leadgen event) | < 30 seconds |
| Facebook Messenger message | Webhook (messages event) | < 30 seconds |
| Yelp/Angi/Thumbtack lead email | SendGrid Inbound Parse webhook | < 90 seconds |
| SMS reply from lead | Twilio webhook | < 15 seconds |

### Human Escalation Rules

| Condition | Action |
|---|---|
| Lead requests in-person estimate for job > $5,000 | SMS notification to owner/sales manager immediately |
| Emergency service needed (flooding, gas, no heat) | Trigger System 1 outbound AI call to lead + alert owner |
| Lead replies "stop" / "unsubscribe" / "opt out" | Immediately halt all messaging, update contacts.opted_out_sms = true |
| Lead asks complex technical question AI cannot answer | Queue for human callback within 1 hour, send holding message |
| Lead is outside service area | Polite decline message, do not enroll in sequence |
| Spam detected (Claude classification) | Log and discard, do not create CRM record |
| Lead replies indicating they already booked with competitor | Mark as lost, stop sequence, log competitive intelligence |

### Key Metrics

| Metric | Target |
|---|---|
| Average first-touch response time | < 60 seconds |
| Lead-to-contact rate (lead engaged with our response) | > 40% |
| Lead-to-booking rate (booked from first response) | > 20% |
| Channel coverage (% of lead sources with auto-response active) | > 95% |
| Cost per lead response (Twilio + SendGrid + Claude) | < $0.50 |
| Phone validation accuracy | > 98% |
| Duplicate detection rate | > 95% |
| False spam classification rate | < 2% |

---

## 6. System 3: Lead Follow-Up Engine

### Purpose and Function

Automatically follows up with leads who did not book on first contact. Runs a multi-touch sequence over 14 days using SMS, email, and AI phone calls. Sequences are personalized based on lead source, service type, urgency, and prior interactions. Industry data shows that 80% of sales require 5+ follow-ups, but 44% of salespeople give up after one.

### Technical Architecture

```
Entry Points:
    |
    +-- System 2: Lead not booked after initial response
    +-- CRM status change: "needs follow-up" tag applied
    +-- Manual enrollment: office staff tags contact in CRM
    +-- System 5: Estimate follow-up (separate sequence type)
    +-- System 10: Reactivation (separate sequence type)
    |
    v
Supabase: sequences table
    |-- id, client_id, contact_id
    |-- sequence_type: standard_14day | hot_lead_3day | estimate_followup_60day |
    |                  maintenance_reminder | winback_campaign | reactivation
    |-- current_step: integer (0-indexed)
    |-- total_steps: integer
    |-- status: active | paused | completed | converted | opted_out | failed
    |-- next_fire_at: timestamptz
    |-- started_at, completed_at, last_response_at
    |-- conversion_value: numeric (filled when converted)
    |-- metadata: jsonb (source, service_type, lead_score, etc.)
    |
    v
n8n Cron Worker: "Sequence Processor"
    |-- Schedule: every 5 minutes
    |-- Query: SELECT s.*, c.* FROM sequences s
    |          JOIN contacts c ON s.contact_id = c.id
    |          WHERE s.next_fire_at <= NOW()
    |          AND s.status = 'active'
    |          AND c.opted_out_sms = false
    |          ORDER BY s.next_fire_at ASC
    |          LIMIT 50  -- batch size per run
    |
    v
For each due sequence step, load step definition from sequence_definitions table:
    |
    +-- Step type: SMS
    |     Claude API: generate personalized SMS
    |       System prompt: "Generate a follow-up SMS for a {trade} company.
    |         Context: {lead_name} inquired about {service} on {date}.
    |         Previous messages: {message_history}. This is touch #{step} of {total}.
    |         Step theme: {step_template_theme}. Keep under 160 characters.
    |         Brand voice: {brand_voice_guide}."
    |     Twilio API: POST /2010-04-01/Accounts/{sid}/Messages.json
    |       From: client's number, To: lead's phone, Body: generated SMS
    |     Log: INSERT INTO messages (channel: 'sms', direction: 'outbound', ...)
    |
    +-- Step type: EMAIL
    |     Claude API: generate personalized email subject + body
    |       Longer context window: include all prior touchpoints, lead data
    |     SendGrid API: POST /v3/mail/send
    |       Using client's dynamic template with merge fields
    |     Log: INSERT INTO messages (channel: 'email', direction: 'outbound', ...)
    |
    +-- Step type: AI_CALL
    |     Check: is it between 9 AM and 7 PM in lead's timezone?
    |       If no: reschedule to next valid window
    |     Vapi API: POST /call
    |       {
    |         assistantId: client's outbound follow-up assistant,
    |         customer: {number: lead_phone},
    |         phoneNumberId: client's Vapi phone number,
    |         assistantOverrides: {
    |           model: {messages: [{role: "system", content: follow_up_prompt}]},
    |           firstMessage: "Hi {name}, this is {agent} from {company}.
    |             I'm following up on your {service} inquiry from {date}."
    |         }
    |       }
    |     On call.ended webhook: process transcript, update sequence
    |
    +-- Step type: VOICEMAIL_DROP
    |     Slybroadcast API: POST /vmb.php
    |       audio_url: pre-recorded message URL (per client, stored in R2)
    |       phone: lead's phone number
    |     Or: Twilio AMD (Answering Machine Detection) + play recording
    |
    v
After step execution:
    |-- UPDATE sequences SET
    |     current_step = current_step + 1,
    |     next_fire_at = NOW() + step_definition.delay_interval
    |-- If current_step >= total_steps:
    |     UPDATE sequences SET status = 'completed', completed_at = NOW()
    |     Move lead to nurture list (System 10)
```

### Response Monitoring (always running, parallel to sequence processor)

```
SMS Reply Received:
    Twilio webhook --> n8n
    |-- Look up: SELECT * FROM contacts WHERE phone = {from_number} AND client_id = X
    |-- Look up: SELECT * FROM sequences WHERE contact_id = Y AND status = 'active'
    |-- Claude API: classify response
    |     Input: reply text + conversation history
    |     Output: {classification, suggested_action}
    |     Classifications:
    |       interested     --> pause sequence, attempt AI booking or notify human
    |       not_interested --> mark sequence as 'completed', log reason
    |       question       --> Claude generates answer, send reply, continue sequence
    |       stop/optout    --> IMMEDIATELY: update opted_out_sms = true, halt sequence
    |       angry          --> pause sequence, alert office manager
    |       appointment    --> attempt booking via CRM, mark converted
    |       competitor     --> mark lost, log competitor name if mentioned
    |-- Log inbound message to messages table

Email Reply Received:
    SendGrid Inbound Parse webhook --> n8n
    |-- Same classification and routing logic as SMS
    |-- Note: email replies less common, often more detailed

AI Call Completed:
    Vapi call.ended webhook --> n8n
    |-- Analyze transcript with Claude
    |-- If booking made during call: mark converted, log revenue
    |-- If callback requested: create CRM task, pause sequence
    |-- If not interested: advance or complete sequence
```

### Standard 14-Day Sequence Definition

| Day | Step # | Channel | Content Theme | Delay After |
|---|---|---|---|---|
| 0 | 1 | SMS | Instant response (handled by System 2) | 24 hours |
| 1 | 2 | Email | Welcome + service info + booking link + "what to expect" | 24 hours |
| 2 | 3 | SMS | "Did you get a chance to review? We have availability this week." | 48 hours |
| 4 | 4 | AI Call | Friendly follow-up, answer questions, try to book | 72 hours |
| 7 | 5 | Email | Social proof: 2-3 recent Google reviews + before/after photos | 0 hours |
| 7 | 6 | Voicemail Drop | Personal message from "the owner" thanking them for considering | 72 hours |
| 10 | 7 | SMS | Limited-time offer or seasonal discount code | 96 hours |
| 14 | 8 | Email | Case study / educational content about their service need | 0 hours |
| 14 | 9 | SMS | Final touch: "We're here when you're ready. Save our number!" | -- |
| 14 | 10 | (internal) | Tag in CRM: move to "nurture" list for System 10 | -- |

### Hot Lead 3-Day Sequence (for high-intent leads)

| Day | Step # | Channel | Content Theme |
|---|---|---|---|
| 0 | 1 | SMS | Instant response (System 2) |
| 0 | 2 | AI Call | Call within 5 minutes of lead submission |
| 1 | 3 | SMS | "Wanted to make sure you saw my text yesterday..." |
| 1 | 4 | Email | Detailed service info + financing options if applicable |
| 2 | 5 | SMS | Urgency: "We have one slot left this week for {service}" |
| 3 | 6 | AI Call | Final attempt, offer to answer any questions |

### Integration Points

| Integration | Purpose |
|---|---|
| Supabase | Sequence state machine, message history, contact data |
| Twilio | SMS send (outbound), SMS receive (inbound webhook), voicemail detection |
| SendGrid | Email send (transactional API), email receive (Inbound Parse), open/click tracking |
| Vapi | Outbound AI calls with follow-up-specific agent configuration |
| Slybroadcast (optional) | Ringless voicemail drops ($0.04/drop) |
| CRM | Read lead history, update contact status, create tasks for human callbacks, booking creation |
| Claude API | Message personalization, response classification, conversation management |

### Human Escalation Rules

| Condition | Action |
|---|---|
| Lead replies requesting human contact | Pause sequence, create urgent task in CRM, SMS to assigned rep within 5 min |
| Lead expresses complaint or dissatisfaction | Pause sequence, alert owner via SMS + email with full context |
| Lead indicates they hired a competitor | Mark as lost, stop sequence, log competitor name and reason |
| 3+ unanswered outbound AI calls | Switch to SMS/email only for remaining steps |
| Lead is high-value (estimated job > $10,000) | Notify owner after step 2, recommend personal outreach |
| Lead replies with question AI cannot answer | Human callback queued, holding message sent, sequence paused for 48 hours |
| Lead asks about pricing and estimate > $5,000 | Route to sales manager, provide all conversation context |

### Key Metrics

| Metric | Target |
|---|---|
| Sequence completion rate (reach final step without opt-out) | > 70% |
| Reply rate (any response on any channel) | > 25% |
| Sequence-to-booking conversion rate | > 12% |
| Opt-out rate (per sequence) | < 5% |
| Average number of touches before conversion | 3-5 |
| Revenue attributed to follow-up sequences | Tracked per sequence in Supabase |
| AI call connection rate (reached a human) | > 40% |
| AI call booking rate (of connected calls) | > 15% |
| Average cost per sequence (all channels) | < $5.00 |
| Time from lead to first human reply (when escalated) | < 30 minutes |

---

## 7. System 4: Review Manager

### Purpose and Function

Automate the collection of Google reviews after every job completion, respond to all reviews (positive and negative) with AI-generated personalized responses, and monitor review sentiment across all platforms. Google reviews are the #1 factor in local search ranking -- a steady stream of 5-star reviews directly drives more leads.

### Technical Architecture

```
Trigger: Job marked "complete" in CRM
    |
    v
n8n: Review Request Trigger
    |-- Source A: CRM webhook (job.status_changed = "completed")
    |     ServiceTitan: POST webhook on job status change
    |     Housecall Pro: POST webhook on job completed
    |     Jobber: GraphQL subscription or polling
    |-- Source B: n8n Cron polling (every 15 minutes)
    |     GET /jobs?status=completed&completed_after={last_check_timestamp}
    |
    v
n8n: Pre-Send Checks
    |-- Wait 2 hours (configurable per client in clients.settings.review_delay_hours)
    |   Implemented: n8n "Wait" node or schedule next_fire_at in Supabase
    |-- Check: Did this customer already receive a review request in last 90 days?
    |   SELECT FROM messages WHERE contact_id = X AND system_source = 'review_request'
    |   AND created_at > NOW() - INTERVAL '90 days'
    |   If yes: skip (avoid badgering repeat customers)
    |-- Check: Is there an open complaint, callback, or warranty claim for this job?
    |   Query CRM for open issues on this job_id
    |   If yes: skip and flag for manual review
    |-- Check: Customer satisfaction score (if CRM captures post-job survey)?
    |   If score < 7/10: skip automatic request, alert owner
    |-- Check: Is contact opted out of SMS?
    |   If yes: email only
    |
    v
Review Request Sequence:
    |
    +-- Step 1 (2 hours post-job): SMS via Twilio
    |     Message: "Hi {first_name}, thanks for choosing {company_name}!
    |              {tech_name} enjoyed helping you today. Would you mind
    |              leaving us a quick review? It really helps!
    |              {google_review_link}"
    |     google_review_link: https://search.google.com/local/writereview?placeid={place_id}
    |     Log: INSERT INTO messages (system_source: 'review_request', step_number: 1)
    |
    +-- Step 2 (24 hours later, if no review detected):
    |     Detection: Check Google reviews API for new review from this customer
    |       Match by: reviewer name similarity to contact name (fuzzy match)
    |       Or: new review within 24h window with matching service mention
    |     If no review found:
    |       Email via SendGrid:
    |         Branded HTML template with:
    |         - Star rating visual (click 5 stars --> Google review link)
    |         - Technician photo (if available)
    |         - "One click to leave a review" CTA button
    |         - Direct Google review link
    |
    +-- Step 3 (72 hours later, if still no review):
    |     SMS via Twilio:
    |       "Hi {first_name}, quick reminder -- if you have a moment, we'd
    |        really appreciate a review of your recent {service_type} service.
    |        {google_review_link}"
    |     (Final request -- no more after this)
    |
    v
Review Monitoring Engine (always running, all clients):
    |
    +-- Google Business Profile API (every 30 minutes per client):
    |     GET /v4/accounts/{account}/locations/{location}/reviews
    |       ?pageSize=50&orderBy=updateTime desc
    |     Compare against stored reviews in Supabase
    |     Detect new reviews: review not in reviews table by platform_review_id
    |
    +-- Yelp (daily):
    |     Yelp Fusion API: GET /v3/businesses/{business_id}/reviews
    |     Limited to 3 most recent (API limitation)
    |     Supplement with web scraping via Firecrawl if needed
    |
    +-- Facebook (every 2 hours):
    |     Graph API: GET /{page_id}/ratings?fields=reviewer,rating,review_text
    |
    v
New Review Detected:
    |
    +-- Save to Supabase:
    |     INSERT INTO reviews (client_id, platform, platform_review_id, rating,
    |       review_text, reviewer_name, created_at)
    |
    +-- Match to customer (optional):
    |     Fuzzy name match against contacts table
    |     If matched: link review to contact_id, enrich with service history
    |
    +-- Claude API: Generate Response
    |     POST /v1/messages
    |     System prompt:
    |       "You are a review response writer for {company_name}, a {trade}
    |        company. Write a response to this review. Be genuine, warm, and
    |        professional. Match the company's brand voice: {voice_guide}.
    |
    |        Response rules by rating:
    |        5-star: Thank warmly, mention specific service if identifiable,
    |                invite them to call for future needs.
    |        4-star: Thank sincerely, acknowledge they had a good experience,
    |                mention we strive for 5-star service.
    |        3-star: Thank for feedback, acknowledge room for improvement,
    |                express desire to do better, offer owner's direct contact.
    |        1-2 star: Express sincere empathy, do NOT get defensive,
    |                  take responsibility, offer to make it right,
    |                  provide owner's direct phone number,
    |                  ask them to give you a chance to fix it."
    |
    |     User message: "Rating: {rating}/5\nReview: {review_text}\n
    |                    Customer history: {service_history if matched}"
    |     Output: generated response text (100-200 words)
    |
    +-- Response Posting:
    |     If client has auto_approve_reviews = true (in clients.settings):
    |       Google: POST /v4/accounts/{account}/locations/{location}
    |               /reviews/{review_id}/reply
    |               Body: {comment: generated_response}
    |       (Yelp and Facebook: responses queued for manual posting --
    |        API limitations on automated responses)
    |     If auto_approve = false:
    |       Store response in reviews.our_response with status = 'pending'
    |       Send approval request to owner via SMS + email:
    |         "New {rating}-star review from {reviewer_name}:
    |          '{truncated_review_text}'
    |          Our suggested response: '{truncated_response}'
    |          Reply APPROVE to post, or EDIT to modify."
    |       If no response in 4 hours: auto-post (configurable)
    |
    +-- Negative Review Escalation (1-2 stars):
    |     Immediate SMS to owner: "ALERT: New {rating}-star review on Google
    |       from {reviewer_name}: '{first_50_chars}...'
    |       AI response drafted. Check dashboard or reply APPROVE."
    |     Immediate email to owner: full review + AI response + action items
    |     If review contains keywords: "BBB", "lawyer", "attorney",
    |       "health department", "sue", "report":
    |       Flag as LEGAL_RISK in Supabase
    |       Alert owner + recommend professional/legal response review
    |     Response target: posted within 1 hour of review
```

### Integration Points

| Integration | Protocol | Details |
|---|---|---|
| CRM | Webhook or polling | Job completion events, customer data, technician name, service history |
| Google Business Profile API | REST API v4 with OAuth 2.0 | Review fetching (GET), review response posting (POST). Requires `business.manage` scope. |
| Yelp Fusion API | REST API | Review fetching only (limited to 3 recent). No automated response posting. |
| Facebook Graph API | REST API | Review/rating fetching. Response posting via /{rating_id}/comments. |
| Twilio | REST API | SMS review requests, owner notification, approval handling |
| SendGrid | REST API v3 | Email review requests with branded templates, owner notification emails |
| Claude API | REST API | Review response generation, sentiment analysis |
| Supabase | PostgreSQL | Review storage, response tracking, analytics, approval workflow state |
| Firecrawl (optional) | REST API | Supplement Yelp data via web scraping when API is insufficient |

### Automation Triggers

| Trigger | Source | Action |
|---|---|---|
| Job completed in CRM | Webhook or polling | Start review request sequence (2h delay) |
| New review posted on Google | 30-min polling cycle | Generate and post/queue AI response |
| New review posted on Yelp | Daily polling cycle | Generate response, queue for manual posting |
| New review posted on Facebook | 2-hour polling cycle | Generate and post AI response |
| Negative review (1-2 stars) | Review detection pipeline | Immediate owner alert + priority response |
| Review response approval timeout (4h) | Supabase scheduled check | Auto-post if client has fallback_auto_approve = true |
| Owner replies "APPROVE" via SMS | Twilio webhook | Post the pending response via GBP API |

### Human Escalation Rules

| Condition | Action |
|---|---|
| 1-star review mentioning legal action | Alert owner immediately, recommend attorney review before responding |
| Review mentions specific employee by name (negatively) | Alert owner + flag for HR, do not auto-post response |
| 3+ negative reviews in 7 days | Alert owner with trend analysis, suggest operational review meeting |
| Client has auto_approve = false | All responses held for manual approval (SMS/email approval flow) |
| Review in language other than English | Alert owner, do not auto-respond |
| Fake/spam review detected (no matching customer) | Alert owner, suggest flagging review on Google |

### Key Metrics

| Metric | Target |
|---|---|
| Review request send rate (% of completed jobs) | > 90% |
| Review conversion rate (requests sent to reviews received) | > 15% |
| Average star rating of new reviews | > 4.5 stars |
| Time to respond to new reviews | < 2 hours (auto-approve) / < 6 hours (manual) |
| Response rate (% of reviews with a response) | 100% |
| Net new reviews per month | +8-15 per client |
| Negative review response time | < 1 hour |
| Google review link click-through rate | > 30% |
| Cost per review collected | < $2.00 |

---

## 8. System 5: Estimate Closer

### Purpose and Function

Follow up on estimates/quotes that were delivered but not accepted. Runs a 6-touch sequence over 60 days designed to convert unsold estimates into booked jobs. For most home services companies, 40-60% of estimates go unsold. Recovering even 10% of these represents significant revenue. A typical HVAC replacement estimate is $5,000-15,000 -- recovering one per month per client justifies the entire platform cost.

### Technical Architecture

```
Trigger: Estimate status = "sent" or "viewed" but not "accepted" in CRM
    |
    v
n8n: Estimate Detection
    |-- Method A: CRM webhook on estimate.status_changed
    |-- Method B: n8n Cron every 15 minutes:
    |     Query CRM: GET /estimates?status=sent&sent_after={60_days_ago}
    |     Compare against sequences table: any new unsold estimates?
    |
    v
n8n: Estimate Enrichment
    |-- Pull estimate details from CRM:
    |     Line items, total amount, customer info, technician notes
    |     Equipment proposed (brand, model, efficiency rating)
    |     Photos/documentation attached to estimate
    |-- Pull customer history from CRM:
    |     Previous jobs, lifetime value, communication history
    |     Number of previous estimates (serial shopper detection)
    |-- Classify estimate category:
    |     routine_maintenance (< $500)
    |     repair ($500-$2,500)
    |     replacement ($2,500-$15,000)
    |     new_install ($5,000-$25,000+)
    |-- Calculate priority score:
    |     score = estimate_value * recency_weight * customer_ltv_weight
    |     High priority: replacement/install with existing customer
    |     Medium priority: repair with new customer
    |     Low priority: routine maintenance
    |
    v
Enroll in Estimate Closer Sequence:
    INSERT INTO sequences (
      sequence_type: 'estimate_followup_60day',
      metadata: {estimate_id, estimate_value, category, priority_score,
                 tech_name, line_items_summary, financing_eligible}
    )
```

### 60-Day Estimate Closer Sequence

| Day | Step | Channel | Content Theme | Special Logic |
|---|---|---|---|---|
| 1 | 1 | SMS | "Hi {name}, checking in on the estimate for {service}. Any questions I can answer?" | If estimate > $3,000: include financing pre-qual link |
| 3 | 2 | Email | Detailed estimate summary + why this service matters + customer testimonial relevant to their service | Include before/after photos of similar completed job |
| 7 | 3 | AI Call | "Hi, this is {agent} from {company}, following up on your {service} estimate..." Goal: answer questions, overcome objections, book | Vapi outbound call with estimate-specific system prompt |
| 14 | 4 | SMS | Seasonal urgency or limited-time offer. "We're running a {seasonal} special -- save {$X} on your {service} if you book this month." | If within client's discount authority: include real offer |
| 30 | 5 | Email | Educational content: risks of delaying {service}, cost of waiting, efficiency loss calculations | For HVAC: "Your old system costs $X more per year in energy" |
| 45 | 6 | SMS | Final discount offer: "We'd love to earn your business. Here's a {$X} discount valid this week. Call or reply to book." | Maximum pre-approved discount applied |
| 60 | 7 | SMS | "Your estimate is expiring soon. We're here when you're ready -- just reply or call." Mark sequence complete. | Move to System 10 nurture list |

### Special Features

```
Financing Integration (for estimates > $3,000):
    |
    +-- Hearth API: POST /v1/applications/prequalify
    |     Input: {customer_name, email, loan_amount: estimate_total}
    |     Output: {prequalified: true, offers: [{monthly_payment, term, apr}]}
    |     Include in Step 1 SMS: "Payments as low as ${monthly}/mo available"
    |     Include in Step 2 Email: full financing breakdown table
    |
    +-- Alternative: GreenSky or Service Finance
    |     Similar API pattern, different endpoints

Pre-Approved Discount Authority:
    |-- Configured per client in clients.settings.estimate_closer:
    |     {
    |       max_discount_percentage: 10,
    |       max_discount_dollars: 500,
    |       discount_start_step: 4,  // only offer discounts from step 4 onward
    |       requires_approval_above: 1000  // dollar amounts above this need owner OK
    |     }
    |-- AI generates discount messaging within these bounds
    |-- Each discount offer generates a unique promo code:
    |     stored in campaigns table, tracked for redemption

Competitor Intelligence:
    |-- If lead replies mentioning a competitor:
    |     Claude classifies: {competitor_name, competitor_price_mentioned, objection}
    |     Log to Supabase: competitor_intelligence table
    |     Alert sales manager: "Lead {name} comparing with {competitor}
    |       at ${price}. Your estimate was ${our_price}."
    |     Sequence pauses, human takes over

Serial Shopper Detection:
    |-- If customer has 3+ unsold estimates in 12 months:
    |     Flag as "serial shopper" in metadata
    |     Adjust messaging: focus on value/quality, not discounts
    |     Alert owner: "This customer has requested 3 estimates without booking"
```

### Integration Points

| Integration | Purpose |
|---|---|
| CRM | Estimate data (line items, amounts, status, tech notes), customer records, job creation on acceptance |
| Twilio | SMS touchpoints from client's business number |
| SendGrid | Email touchpoints with estimate summary embedded in branded template |
| Vapi | Outbound AI call for step 3 with estimate-specific prompt |
| Hearth / GreenSky API | Financing pre-qualification for high-value estimates |
| Claude API | Message personalization, objection handling, competitor intelligence analysis |
| Supabase | Sequence tracking, discount code management, competitor intelligence, conversion analytics |

### Key Metrics

| Metric | Target |
|---|---|
| Unsold estimates contacted (within 24h) | > 95% |
| Estimate recovery rate (converted / total unsold) | > 8-15% |
| Average days from estimate to conversion | 7-14 days |
| Revenue recovered per month per client | Track individually (target: 1-3 recovered estimates/month) |
| Discount utilization rate (offers used / offers made) | < 30% |
| AI call connection rate | > 40% |
| Financing pre-qualification click rate | > 15% |
| Competitor mentions captured | Track all |
| Cost per recovered estimate | < $50 |
| ROI (recovered revenue / system cost) | > 20:1 |

---

## 9. System 6: Cold Outreach System

### Purpose and Function

Generate B2B leads by running automated email outreach campaigns to property managers, realtors, general contractors, HOA boards, and commercial facility managers. Positions the client as the preferred vendor for ongoing service contracts. A single commercial account (property management company, HOA, restaurant chain) can be worth $10,000-100,000+ per year in recurring revenue.

### Technical Architecture

```
Phase 1: Prospect List Building
    |
    +-- Apollo.io API:
    |     POST /v1/mixed_people/search
    |     Body: {
    |       person_titles: ["property manager", "facility manager",
    |                       "maintenance director", "building manager"],
    |       person_locations: ["United States"],
    |       person_location_city: ["{client_city}"],
    |       person_location_state: ["{client_state}"],
    |       organization_industry_tag_ids: [
    |         "real_estate", "property_management",
    |         "construction", "facilities_services"
    |       ],
    |       page: 1, per_page: 100
    |     }
    |     Returns: name, email, title, company, linkedin_url, phone
    |
    +-- Google Maps API (supplementary):
    |     GET /maps/api/place/textsearch/json
    |       ?query=property+management+companies+near+{city}+{state}
    |     Returns: business names, addresses, phone numbers, websites
    |     Then: scrape websites for contact emails or use Apollo enrichment
    |
    +-- Manual Upload:
    |     Client provides CSV of prospects (e.g., their existing commercial contacts)
    |     n8n parses CSV, normalizes data, deduplicates
    |
    v
Phase 2: Prospect Enrichment + Verification
    |
    +-- Apollo.io Enrichment (if not already from Apollo):
    |     POST /v1/people/match
    |     Body: {email: prospect_email, reveal_personal_emails: false}
    |     Returns: verified email, title, company details
    |
    +-- Email Verification:
    |     ZeroBounce API: POST /v2/validate
    |       Body: {api_key, email: prospect_email}
    |       Accept only: status = "valid"
    |       Reject: "invalid", "catch-all", "spamtrap", "abuse"
    |     Cost: $0.008/verification
    |     Alternative: NeverBounce API at similar pricing
    |
    +-- Deduplicate against CRM:
    |     Query CRM: GET /contacts?email={prospect_email}
    |     If exists: skip (already a known contact)
    |
    +-- Score prospects:
    |     score = company_size_weight(1-5) * proximity_weight(1-5) * title_relevance(1-5)
    |     Store in prospects table with score
    |
    v
Phase 3: Email Sequence Execution
    |
    +-- Sending Infrastructure (separate from SendGrid):
    |     Platform: Instantly.ai ($30/mo) or Smartlead ($39/mo)
    |     Reason: dedicated cold email infrastructure with:
    |       - Domain warmup (automated 2-4 week warmup cycle)
    |       - Deliverability monitoring (inbox placement tracking)
    |       - Send limits (auto-throttle based on domain health)
    |       - Separate IP/domain reputation from transactional email
    |     Sending domain: mail.{clientname}services.com (NOT client's primary domain)
    |     SPF record: v=spf1 include:instantlymail.com -all
    |     DKIM: configured via Instantly.ai DNS instructions
    |     DMARC: v=DMARC1; p=none; (monitoring mode during warmup)
    |
    +-- Domain Warmup Schedule:
    |     Week 1: 5 emails/day (to seed list of warm contacts)
    |     Week 2: 15 emails/day
    |     Week 3: 30 emails/day
    |     Week 4+: 50-100 emails/day (production volume)
    |
    v
Email Sequence (4 emails over 14 days):
    |
    +-- Email 1 (Day 1): Personalized Introduction
    |     Claude API generates unique email per prospect:
    |       Input: prospect data (name, title, company, company_size, property_types)
    |       + client data (company_name, services, service_area, differentiators)
    |       + template theme: "introduce ourselves, highlight relevant value prop"
    |     Example output:
    |       Subject: "Quick question about {company}'s maintenance setup"
    |       Body: "Hi {first_name}, I noticed {company} manages several properties
    |              in {area}. We specialize in {trade} for commercial properties
    |              and currently serve [X] property management companies in the area.
    |              Would it make sense to set up a quick call to see if we could
    |              help streamline your {trade} maintenance? Best, {client_owner}"
    |     IMPORTANT: each email is unique (not a template with merge fields)
    |                to maximize deliverability and avoid spam filters
    |
    +-- Email 2 (Day 3): Case Study / Social Proof
    |     Theme: "Sharing how we helped a similar company"
    |     Include: specific metrics, property type match, testimonial
    |
    +-- Email 3 (Day 7): Specific Offer
    |     Theme: "Free inspection / maintenance audit / no-obligation assessment"
    |     CTA: Reply to this email or use this Calendly link
    |
    +-- Email 4 (Day 14): Breakup Email
    |     Theme: "I'll assume the timing isn't right. No worries."
    |     Soft CTA: "If anything changes, we're a quick reply away."
    |     Psychologically effective: breakup emails often get highest reply rates
    |
    v
Phase 4: Response Handling
    |
    +-- Instantly.ai / Smartlead detects replies automatically
    |-- Webhook to n8n: POST /webhook/cold-reply-{client_id}
    |
    +-- Claude API: classify reply
    |     Input: reply text + original sequence context
    |     Output: {classification, next_action}
    |     Classifications:
    |       positive_interest --> Create lead in CRM, assign to sales, notify client
    |       meeting_request   --> Send Calendly link or book directly, notify client
    |       not_interested    --> Remove from sequence, mark declined, thank them
    |       out_of_office     --> Reschedule next touch for their return date
    |       wrong_person      --> Ask for referral to right contact
    |       bounce            --> Remove, mark invalid
    |       unsubscribe       --> Remove immediately, add to suppression list
    |
    +-- For positive replies:
    |     CRM: POST /contacts (create new contact)
    |     CRM: POST /opportunities (create lead/opportunity, source: "cold_outreach")
    |     SMS to client owner: "New B2B lead! {name} at {company} is interested.
    |       They manage {X} properties. Reply: '{first_50_chars}'"
    |     Email to client: full reply + conversation history + recommended next steps
```

### Integration Points

| Integration | Protocol | Details |
|---|---|---|
| Apollo.io | REST API v1 | Prospect discovery and enrichment. $49/mo (Basic) or $99/mo (Professional) per shared account. 200-300 credits/month at Basic. |
| Instantly.ai | REST API + webhooks | Cold email sending, domain warmup, reply detection. $30/mo per sending account. |
| ZeroBounce | REST API v2 | Email verification before sending. $0.008/verification. |
| CRM | REST/GraphQL | Create contacts and leads from positive responses. |
| Claude API | REST API | Unique email generation per prospect, reply classification. |
| Supabase | PostgreSQL | Prospect storage, sequence tracking, response analytics, suppression list. |
| Calendly (optional) | Booking link only | Meeting scheduling link embedded in emails. |

### Automation Triggers

| Trigger | Action |
|---|---|
| New prospect list uploaded or generated | Start email verification, then enroll verified prospects |
| Client requests campaign for specific vertical | Generate targeted prospect list from Apollo |
| Monthly refresh (1st of month) | Re-search Apollo for new prospects in service area |
| Positive reply detected | Create CRM lead, pause sequence, notify sales |
| Domain reputation drops below threshold | Pause sending, alert internal team, investigate |
| Bounce rate exceeds 3% on any send day | Pause campaign, re-verify remaining prospects |

### Compliance Requirements

| Requirement | Implementation |
|---|---|
| CAN-SPAM: physical address | Every email includes client's business address in footer |
| CAN-SPAM: unsubscribe | One-click unsubscribe link in every email, processed within 1 day |
| CAN-SPAM: accurate headers | From name and address accurately represent the client |
| B2B only | All targets are business contacts at business email addresses |
| Suppression list | Global suppression list checked before every send |
| Separate sending domain | Never cold-email from client's primary domain |

### Key Metrics

| Metric | Target |
|---|---|
| Email deliverability rate (inbox, not spam) | > 95% |
| Email open rate | > 45% |
| Reply rate (all replies) | > 5% |
| Positive reply rate | > 2% |
| Meeting booked rate | > 1% |
| Meetings booked per month per client | 3-8 |
| Deals closed from outreach per quarter | 2-5 per client |
| Bounce rate | < 3% |
| Spam complaint rate | < 0.1% |
| Average deal size from cold outreach | $5,000-50,000/year (recurring contracts) |
| Cost per meeting booked | < $50 |

---

## 10. System 7: Neighborhood Targeting

### Purpose and Function

After completing a job, automatically market to nearby homeowners in the same neighborhood. Uses the social proof of "we just helped your neighbor" with hyper-targeted direct mail postcards and geo-fenced digital ads. The proximity and social proof dramatically increase response rates compared to general marketing. Typical direct mail response rate: 1-2%. Neighborhood-targeted with social proof: 3-5%.

### Technical Architecture

```
Trigger: Job completed in CRM + customer approved marketing use
    |
    v
n8n: Neighborhood Campaign Workflow
    |
    +-- Step 1: Validate eligibility
    |     - Is this job type suitable for neighborhood marketing?
    |       (Yes: AC install, roof replacement, plumbing repair. No: warranty callback.)
    |     - Did customer consent to marketing use? (check CRM or default opt-in)
    |     - Is job value above minimum threshold? (configurable, default: $500)
    |
    +-- Step 2: Geocode job address
    |     Google Maps Geocoding API:
    |       GET /maps/api/geocode/json?address={job_address}&key={key}
    |       Response: {lat, lng, formatted_address, address_components}
    |     Extract: neighborhood name from address_components (sublocality)
    |
    +-- Step 3: Define target radius
    |     Default: 0.3 miles (urban), 0.5 miles (suburban), 1.0 mile (rural)
    |     Configured per client based on market density
    |
    +-- Step 4: Generate target mailing list
    |
    |     Option A: USPS EDDM (Every Door Direct Mail) -- simplest
    |       PostGrid EDDM API: select carrier routes within radius
    |       No individual addresses needed -- deliver to every door on route
    |       Cost: $0.20-0.30 per piece (postage only) + printing
    |
    |     Option B: Targeted list via property data API
    |       ATTOM Data API: GET /property/address
    |         ?latitude={lat}&longitude={lng}&radius=0.5&propertytype=SFR
    |         Filter: owner-occupied, single family, home built before {year}
    |       Or: PropertyRadar API with similar filtering
    |       Cost: $0.05-0.10 per record
    |       Advantage: can target specific property characteristics
    |
    +-- Step 5: Generate campaign creative
    |
    |     +-- Direct Mail Postcard (PostGrid):
    |     |     Template: 6x9 or 4x6 postcard
    |     |     Front:
    |     |       Headline: "We Just Helped Your Neighbor on {street_name}!"
    |     |       Before/after photo (if available from CRM job photos)
    |     |       Company logo and branding
    |     |     Back:
    |     |       Service description relevant to job type
    |     |       Neighborhood-specific discount: "Save ${X} -- {neighborhood} special"
    |     |       Unique promo code: e.g., "OAK25" (tracked per campaign)
    |     |       QR code --> landing page: {client-domain}.com/neighbors/{campaign_id}
    |     |       Phone number (Twilio tracking number for attribution)
    |     |       Google review count: "Rated 4.9 stars (200+ reviews)"
    |     |
    |     |     PostGrid API: POST /v1/postcards
    |     |       {
    |     |         to: [{address_line1, city, state, zip}],  // from mailing list
    |     |         front_html: rendered_template_front,
    |     |         back_html: rendered_template_back,
    |     |         size: "6x9",
    |     |         mail_type: "first_class"  // or "standard" for lower cost
    |     |       }
    |     |     Cost: $0.75-1.25/piece (print + postage + PostGrid fee)
    |     |     Volume: 100-300 pieces per completed job (based on density)
    |     |
    |     +-- Facebook/Instagram Geo-Targeted Ad:
    |     |     Facebook Marketing API:
    |     |     POST /act_{ad_account_id}/campaigns
    |     |       {name: "Neighborhood - {street} - {date}",
    |     |        objective: "LEAD_GENERATION" or "MESSAGES",
    |     |        special_ad_categories: ["HOUSING"] // required for geo-targeting}
    |     |     POST /act_{ad_account_id}/adsets
    |     |       {targeting: {
    |     |          geo_locations: {custom_locations: [
    |     |            {latitude: lat, longitude: lng, radius: 1, distance_unit: "mile"}
    |     |          ]},
    |     |          age_min: 30, age_max: 65,
    |     |          home_ownership: ["homeowners"]  // if available under housing rules
    |     |        },
    |     |        daily_budget: 1000,  // $10/day in cents
    |     |        billing_event: "IMPRESSIONS",
    |     |        optimization_goal: "LEAD_GENERATION"}
    |     |     POST /act_{ad_account_id}/adcreatives
    |     |       {body: "Just completed a {service} project in {neighborhood}!
    |     |              Ask about our neighbor discount.",
    |     |        image_url: job_photo_url or stock_photo_url,
    |     |        call_to_action: {type: "CALL_NOW" or "LEARN_MORE"}}
    |     |     Budget: $5-15/day for 7 days per campaign ($35-105 total)
    |     |     Leads from ad --> feed into System 2 (Speed-to-Lead)
    |
    +-- Step 6: Create tracking infrastructure
    |     Landing page: Next.js dynamic route /{client}/neighbors/{campaign_id}
    |       Displays: service info, neighborhood discount, booking form, reviews
    |       Tracking: PostHog pageview event with campaign_id
    |     Tracking number: Twilio number dedicated to this campaign (or pool)
    |       Calls --> System 1 (AI Receptionist) with campaign attribution
    |     Promo code: unique per campaign, stored in campaigns table
    |       When redeemed at booking: attribute revenue to campaign
    |
    v
Step 7: Campaign Tracking + Attribution
    |
    +-- Store in Supabase campaigns table:
    |     campaign_type: 'neighborhood', status: 'active',
    |     audience_count, total_cost (postcard printing + postage + ad spend),
    |     promo_code, tracking_phone, landing_page_url
    +-- Track conversions:
    |     Promo code used at booking --> campaign attributed revenue
    |     Tracking number call --> campaign attributed lead
    |     Landing page form submit --> campaign attributed lead
    |     Facebook ad lead --> campaign attributed lead
    +-- Monthly ROI calculation:
    |     campaign_revenue / campaign_cost = ROI ratio
```

### Integration Points

| Integration | Purpose | Cost |
|---|---|---|
| CRM | Job completion trigger, customer address, service type, job photos | Included |
| Google Maps Geocoding API | Address to coordinates, neighborhood name extraction | $0.005/req |
| PostGrid API | Postcard design, printing, and mailing | $0.75-1.25/piece |
| Facebook Marketing API | Geo-targeted ad campaign creation and management | Ad spend: $35-105/campaign |
| ATTOM Data API (optional) | Property owner data for targeted mailing lists | $0.05-0.10/record |
| Supabase | Campaign tracking, attribution, ROI calculation | Included |
| Next.js landing pages | Per-campaign tracking pages | Included (shared hosting) |
| Twilio | Campaign tracking phone numbers | $1/mo per number |
| PostHog | Landing page analytics, conversion tracking | Included (free tier) |

### Key Metrics

| Metric | Target |
|---|---|
| Campaigns triggered per month | 15-40 (depends on job volume) |
| Direct mail pieces sent per campaign | 100-300 |
| Direct mail response rate | 2-5% |
| Facebook ad CTR | > 2% |
| Landing page conversion rate | > 10% |
| Cost per lead from neighborhood campaigns | < $35 |
| Average campaign cost (mail + ads) | $150-400 |
| ROI per campaign (revenue / cost) | > 5:1 |
| Time from job completion to campaign launch | < 48 hours |

---

## 11. System 8: Seasonal Campaign Engine

### Purpose and Function

Execute pre-built marketing campaigns triggered by season, calendar date, weather events, or business milestones. Ensures consistent outbound marketing without manual effort from the client. Most home services companies do zero proactive marketing -- they wait for the phone to ring. This system makes outreach automatic and timely.

### Technical Architecture

```
Campaign Template Library (stored in Supabase: campaign_templates table):
    |
    +-- HVAC Templates:
    |     - spring_ac_tuneup:    trigger_date: "03-15", end_date: "04-30"
    |     - summer_efficiency:   trigger_date: "06-01", end_date: "07-15"
    |     - fall_heating_prep:   trigger_date: "09-15", end_date: "10-31"
    |     - winter_emergency:    trigger_date: "11-15", end_date: "12-15"
    |     - filter_reminder:     trigger: recurring every 90 days per customer
    |
    +-- Plumbing Templates:
    |     - spring_sump_pump:    trigger_date: "03-01", end_date: "04-15"
    |     - summer_sprinkler:    trigger_date: "08-01", end_date: "09-30"
    |     - fall_winterize:      trigger_date: "10-01", end_date: "11-15"
    |     - winter_pipe_freeze:  trigger: weather (temp < 32F for 24h)
    |     - water_heater_flush:  trigger: recurring every 12 months per customer
    |
    +-- Roofing Templates:
    |     - spring_inspection:   trigger_date: "03-15", end_date: "05-15"
    |     - fall_gutter:         trigger_date: "09-15", end_date: "11-15"
    |     - post_hail:           trigger: weather (hail event detected)
    |     - post_storm:          trigger: weather (wind > 60mph or tornado warning)
    |
    +-- Electrical Templates:
    |     - spring_generator:    trigger_date: "04-01", end_date: "05-31"
    |     - holiday_lighting:    trigger_date: "10-01", end_date: "11-15"
    |     - surge_protection:    trigger: weather (lightning storm season)
    |
    +-- Universal Templates (all trades):
    |     - new_year_special:    trigger_date: "01-02", end_date: "01-15"
    |     - tax_refund:          trigger_date: "02-15", end_date: "04-15"
    |     - spring_cleaning:     trigger_date: "03-15", end_date: "04-30"
    |     - memorial_day:        trigger_date: "05-20", end_date: "05-31"
    |     - july_4th:            trigger_date: "06-25", end_date: "07-08"
    |     - labor_day:           trigger_date: "08-25", end_date: "09-08"
    |     - holiday_gift_cards:  trigger_date: "11-15", end_date: "12-20"
    |     - referral_program:    trigger: always active, boost quarterly
    |
    v
Trigger Engine:
    |
    +-- Date-Based Triggers (n8n Cron, daily at 6:00 AM per client's timezone):
    |     Query: SELECT * FROM campaign_templates
    |            WHERE client_id = X
    |            AND trigger_type = 'date'
    |            AND trigger_date <= CURRENT_DATE
    |            AND end_date >= CURRENT_DATE
    |            AND NOT EXISTS (SELECT 1 FROM campaigns WHERE template_id = T
    |                           AND EXTRACT(YEAR FROM started_at) = EXTRACT(YEAR FROM NOW()))
    |     If match found: initiate campaign
    |
    +-- Weather-Based Triggers (n8n Cron, every 6 hours):
    |     OpenWeatherMap OneCall API 3.0:
    |       GET /data/3.0/onecall?lat={lat}&lon={lng}&appid={key}
    |     Check against trigger conditions:
    |       - temp_min < 32F for 24+ hours --> pipe_freeze_prevention
    |       - hail detected in alerts[] --> roof_inspection_post_hail
    |       - wind_speed > 60mph in alerts[] --> storm_damage_inspection
    |       - heat_index > 100F for 3+ days --> ac_emergency_campaign
    |       - lightning storms --> surge_protection_campaign
    |     If triggered: check cooldown (no same campaign within 30 days)
    |     Cost: OpenWeatherMap OneCall: $0 for 1,000 calls/day (free tier) or $40/mo
    |     Alternative: Tomorrow.io API for more granular weather events
    |
    +-- Business Event Triggers:
    |     - Membership renewal month approaching (query CRM)
    |     - Client hits review milestone (100, 200, 500 reviews)
    |     - Slow week detected (< 50% of average job volume) --> flash sale campaign
    |
    v
Audience Selection (per campaign):
    |
    +-- Query CRM + Supabase for eligible contacts:
    |     Base: all customers + leads in client's database
    |     Filters (applied via n8n Function node):
    |       - opted_in = true (not opted out of marketing)
    |       - not_contacted_last_30_days = true (avoid over-communication)
    |       - in_service_area = true
    |       - relevant_to_campaign = true (e.g., has AC system for AC campaign)
    |
    +-- Segment audience for personalization:
    |     past_customers: "As a valued {company} customer..."
    |     leads_never_booked: "We'd love to earn your business..."
    |     membership_holders: "Your membership includes a discount on..."
    |     at_risk (18+ months since last service): "We miss you! Special offer..."
    |     equipment_age_targeted: "Your {equipment} was installed in {year}..."
    |
    v
Campaign Execution (n8n workflow per campaign):
    |
    +-- SMS Blast:
    |     Twilio Messaging Service (for throughput):
    |       - Configure: Messaging Service with number pool
    |       - Send rate: up to 10 msg/sec with Messaging Service
    |       - Each SMS personalized by segment via Claude API
    |     Content example:
    |       "Hi {name}, spring is here! Time for an AC tune-up. As a past
    |        customer, you get $25 off. Book now: {booking_link}
    |        Reply STOP to opt out."
    |
    +-- Email Blast:
    |     SendGrid Marketing API:
    |       POST /v3/marketing/singlesends
    |       {
    |         name: campaign_name,
    |         send_to: {segment_ids: [segment_id]},
    |         email_config: {
    |           design_id: client's seasonal template,
    |           subject: "Spring AC Tune-Up -- $25 Off for Valued Customers"
    |         }
    |       }
    |       POST /v3/marketing/singlesends/{id}/schedule
    |       {send_at: scheduled_timestamp}
    |     Content: branded HTML with seasonal creative, offer, booking CTA
    |
    +-- Direct Mail (premium campaigns only):
    |     PostGrid API: same pattern as System 7
    |     Reserved for high-value campaigns (replacement season, big promotions)
    |     Audience: past customers with equipment > 10 years old
    |
    +-- Social Media Content:
    |     Claude API: generate 3-5 social post variations
    |     Store in Supabase for client to post (or auto-post via Buffer API)
    |     Content: seasonal tips, promotional offers, before/after photos
    |
    v
Response Handling:
    |-- All responses route to System 2 (Speed-to-Lead) for instant handling
    |-- Promo codes tracked: when used at booking, attribute to campaign
    |-- UTM-tagged links: track web traffic from email clicks
    |-- Twilio keyword triggers: "TUNEUP" auto-reply with booking link
    |-- Call tracking: dedicated campaign number routes to System 1
```

### Integration Points

| Integration | Purpose | Cost |
|---|---|---|
| OpenWeatherMap / Tomorrow.io | Weather data for trigger conditions | $0-40/mo |
| CRM | Customer and lead lists, segmentation data, service history, equipment records | Included |
| Twilio | SMS campaign delivery via Messaging Service | $0.0079/SMS |
| SendGrid Marketing API | Email campaign creation and scheduling | Included in plan |
| PostGrid | Direct mail for premium campaigns | $0.75-1.25/piece |
| Claude API | Content personalization per segment | ~$0.50-2.00/campaign |
| Buffer API (optional) | Social media scheduling | $15/mo (shared) |
| Supabase | Campaign templates, audience management, performance tracking | Included |
| PostHog | Campaign link tracking, conversion funnels | Included |

### Key Metrics

| Metric | Target |
|---|---|
| Campaigns executed per quarter per client | 4-8 |
| SMS delivery rate | > 97% |
| SMS response rate (replied or clicked) | > 8% |
| Email open rate | > 25% |
| Email click rate | > 3% |
| Campaign booking rate (% of audience that books) | > 3% |
| Revenue per campaign | > $5,000 (varies by trade and offer) |
| Weather-triggered campaign activation time | < 4 hours from weather event detection |
| Cost per campaign (SMS + email + AI) | $50-200 (excluding direct mail) |
| Campaign ROI | > 10:1 |

---

## 12. System 9: AI Dispatcher

### Purpose and Function

Intelligently route and schedule incoming jobs to technicians based on skills, certifications, current location, schedule density, job priority, and parts availability. Reduces average drive time between jobs, improves technician utilization, increases first-time fix rates, and ensures the right tech handles the right job. Manual dispatching is one of the biggest operational bottlenecks in home services.

### Technical Architecture

```
Trigger: New job created or rescheduled in CRM
    |
    v
n8n: Dispatch Decision Workflow
    |
    +-- Step 1: Pull job details from CRM
    |     GET /jobs/{job_id}
    |     Extract:
    |       service_type: "ac_repair"
    |       priority: "standard" | "urgent" | "emergency"
    |       estimated_duration: 120 (minutes)
    |       customer_address: "123 Oak St, Springfield, IL 62701"
    |       preferred_window: "morning" | "afternoon" | "anytime" | specific time
    |       equipment_info: "Carrier Infinity 2-stage, model 24ACC636A003, installed 2018"
    |       special_requirements: ["permit_needed", "specific_parts", "two_person_job"]
    |       customer_notes: technician notes from CRM
    |
    +-- Step 2: Pull technician roster from Supabase + CRM
    |
    |     Supabase: technicians table (per client)
    |       id, name, phone, skills[], certifications[], max_daily_jobs,
    |       vehicle_inventory[] (parts on truck), home_base_address,
    |       hourly_rate, avg_job_duration_by_type{}, customer_rating
    |
    |     CRM: GET /schedules?date={today}&technician_id=all
    |       Returns: each tech's booked jobs with times and addresses
    |
    |     Combine into technician_profiles[]:
    |       {
    |         id, name, skills, certifications,
    |         current_schedule: [{job_id, start, end, address}],
    |         available_slots: [{start, end}],  // calculated gaps
    |         current_location: last_job_address or home_base,
    |         jobs_remaining_today: max_daily - booked_count,
    |         has_required_parts: boolean,
    |         performance: {avg_rating, first_fix_rate, avg_duration}
    |       }
    |
    +-- Step 3: Calculate drive times
    |     Google Maps Distance Matrix API:
    |       GET /maps/api/distancematrix/json
    |         ?origins={tech1_location}|{tech2_location}|...
    |         &destinations={job_address}
    |         &departure_time=now
    |         &key={api_key}
    |     Returns: drive_time_seconds and distance_meters for each tech
    |     Cost: $0.005 per origin-destination pair
    |     Cache: store recent lookups in Redis (TTL: 4 hours)
    |
    +-- Step 4: AI optimization scoring
    |     Claude API: POST /v1/messages
    |     System prompt:
    |       "You are a dispatch optimizer for a {trade} company.
    |        Score each available technician for this job on a 0-100 scale.
    |
    |        Scoring weights:
    |        - Skill match (30%): tech must have required skills/certifications
    |        - Drive time (25%): shorter is better, penalize > 30 min heavily
    |        - Schedule fit (20%): fits cleanly in existing schedule gaps
    |        - Workload balance (15%): prefer techs with fewer jobs today
    |        - Customer match (10%): returning tech for repeat customer bonus
    |
    |        Hard constraints (disqualify tech if any fail):
    |        - Missing required certification
    |        - No available time slot that fits
    |        - Already at max daily jobs
    |        - Job requires two-person crew but no partner available
    |
    |        Business rules:
    |        - Senior techs get replacements/installs (> $3,000 jobs)
    |        - Apprentices need supervision for gas work or electrical
    |        - Emergency jobs override all schedule constraints
    |        - VIP customers get the tech with highest rating"
    |
    |     User message: JSON with job_details + all technician_profiles
    |
    |     Output (structured JSON):
    |       {
    |         "recommended": {
    |           "tech_id": "T003",
    |           "tech_name": "Mike Rodriguez",
    |           "score": 92,
    |           "reason": "Best skill match for Carrier systems, 18-min drive,
    |                      has capacitor in vehicle inventory, clean schedule gap 1-3 PM",
    |           "estimated_arrival": "1:15 PM",
    |           "estimated_drive_minutes": 18
    |         },
    |         "alternatives": [
    |           {"tech_id": "T001", "name": "Dave Smith", "score": 78,
    |            "reason": "Qualified but 35-min drive, better for afternoon slot",
    |            "tradeoff": "Longer drive time, but higher customer rating"},
    |           {"tech_id": "T005", "name": "Sarah Chen", "score": 65,
    |            "reason": "Available but less experience with Carrier systems",
    |            "tradeoff": "Less brand experience, may need phone support"}
    |         ],
    |         "schedule_impact": "No conflicts. Mike has a 3-hour gap between
    |                            his 10 AM and 3:30 PM jobs.",
    |         "parts_check": {
    |           "needed": ["capacitor 45/5 MFD", "contactor"],
    |           "on_truck": true,
    |           "supply_house_nearby": "Ferguson?"
    |         },
    |         "confidence": 0.92
    |       }
    |
    +-- Step 5: Assignment action
    |
    |     If confidence >= 0.85 AND no hard constraint warnings:
    |       AUTO-ASSIGN:
    |       CRM API: PUT /jobs/{job_id} {assigned_technician_id: tech_id}
    |       SMS to technician (Twilio):
    |         "New job assigned: {service_type} at {address}.
    |          Customer: {name}. Arrive by: {time}. Notes: {notes}
    |          Directions: {google_maps_link}"
    |       SMS to customer (Twilio):
    |         "Great news! Your technician {tech_name} is scheduled to arrive
    |          {time_window}. They'll call when they're on the way."
    |       Log: INSERT INTO dispatch_events (assignment_method: 'auto', ...)
    |
    |     If confidence < 0.85 OR edge case detected:
    |       SUGGEST TO DISPATCHER:
    |       Slack or SMS notification to office manager:
    |         "Dispatch suggestion for Job #{job_id}:
    |          Recommended: {tech_name} (score: {score})
    |          Reason: {reason}
    |          Alternatives: {alt1_name}, {alt2_name}
    |          Reply 1 to approve, 2 for {alt1}, 3 for {alt2}, or assign manually."
    |       Dashboard card with approve/reassign buttons
    |       Timeout: if no response in 15 minutes, auto-assign top recommendation
    |
    v
Real-Time Monitoring (continuous):
    |
    +-- Job duration tracking:
    |     CRM webhook: job.status_changed to "in_progress" --> log start time
    |     CRM webhook: job.status_changed to "completed" --> log end time
    |     Compare actual vs. estimated duration
    |     If running > 30 min over estimate:
    |       Alert dispatcher: "Job #{id} running long. Next customer may be affected."
    |       Auto-notify next customer: "Your technician is finishing up a job
    |         and may arrive 30 minutes later than scheduled. Sorry for the delay!"
    |
    +-- Schedule re-optimization (triggered by any schedule change):
    |     If job cancelled or rescheduled:
    |       Re-run optimization for remaining unassigned jobs
    |       Suggest backfill for newly open time slots
    |     If emergency job comes in:
    |       Find nearest qualified tech regardless of schedule
    |       Offer to reschedule their current next job
```

### Integration Points

| Integration | Purpose | Cost |
|---|---|---|
| CRM | Job data, tech schedules, assignment updates, status tracking | Included |
| Google Maps Distance Matrix API | Drive time calculations | $0.005/element |
| Claude API | Optimization scoring and reasoning | ~$0.02/dispatch decision |
| Twilio | Tech and customer notifications | $0.0079/SMS |
| Supabase | Tech skills matrix, performance history, dispatch logs | Included |
| Redis (Upstash) | Drive time caching, rate limiting | Included |
| Slack (optional) | Dispatcher notifications for non-auto assignments | Free |

### Key Metrics

| Metric | Target |
|---|---|
| Average drive time between jobs | < 25 minutes |
| First-time fix rate (right tech, right parts) | > 85% |
| Technician utilization rate (billable hours / available hours) | > 75% |
| Auto-dispatch rate (no human intervention needed) | > 60% |
| Customer on-time arrival rate | > 90% |
| Drive time reduction vs. manual dispatch | > 15% |
| Dispatch decision time (trigger to assignment) | < 2 minutes (auto) / < 15 min (suggested) |
| Daily jobs per technician | Increase by 0.5-1.0 vs. manual dispatch |
| Customer "running late" notification rate | 100% of delays > 15 min |

---

## 13. System 10: Customer Lifecycle Manager

### Purpose and Function

Manage ongoing customer relationships after the initial job. Handles maintenance reminders, seasonal outreach, membership/service agreement management, equipment warranty tracking, referral programs, and win-back campaigns for inactive customers. The cheapest lead is a repeat customer -- acquiring a new customer costs 5-7x more than retaining an existing one.

### Technical Architecture

```
Data Ingestion (continuous):
    |
    +-- CRM Sync (n8n Cron every 30 minutes):
    |     Pull: customer records, job history, equipment installed,
    |           membership status, invoices, upcoming appointments
    |     Store/update in Supabase: contacts, equipment, memberships tables
    |
    +-- Communication History (Supabase):
    |     All messages sent by all systems are logged
    |     Used to prevent over-communication (30-day cooldown between campaigns)
    |
    v
Customer Segmentation Engine (n8n daily at 5 AM):
    |
    |-- For each client, run segmentation query:
    |
    |   Active Customers (job in last 12 months):
    |     SEGMENT_MEMBER:    has active membership/service agreement
    |     SEGMENT_NONMEMBER: no membership, had service in last 12 months
    |     SEGMENT_EQUIPMENT_OLD: has equipment > 10 years old
    |     SEGMENT_MULTISYSTEM: has 2+ types of equipment (cross-sell opportunity)
    |
    |   At-Risk Customers (12-24 months since last job):
    |     SEGMENT_AT_RISK: no service in 12-24 months
    |
    |   Churned Customers (24+ months since last job):
    |     SEGMENT_CHURNED: no service in 24+ months
    |
    |   VIP Customers (top 20% by lifetime value):
    |     SEGMENT_VIP: lifetime_value > 80th percentile
    |
    |   Store segments in contacts.tags[] array in Supabase
    |
    v
Lifecycle Automation Sequences:
    |
    +-- 1. Maintenance Reminders (Cron: daily check at 8 AM)
    |     Query: SELECT * FROM equipment
    |            WHERE next_service_due <= NOW() + INTERVAL '14 days'
    |            AND contact_id NOT IN (active sequence for maintenance_reminder)
    |
    |     Maintenance schedules by equipment type:
    |       AC/Furnace tune-up:     every 6 months (spring AC, fall furnace)
    |       Filter change:          every 90 days
    |       Water heater flush:     every 12 months
    |       Sump pump test:         every 6 months (spring/fall)
    |       Duct cleaning:          every 2-3 years
    |       Roof inspection:        every 12 months
    |       Generator service:      every 12 months
    |       Drain cleaning:         every 12-24 months
    |
    |     Sequence (3 touches):
    |       Day -14: SMS -- "{name}, your {equipment} is due for maintenance.
    |                       Book your tune-up: {booking_link}"
    |       Day -7:  Email -- Detailed: why maintenance matters, what's included,
    |                         special member pricing if applicable
    |       Day 0:   SMS -- "Last reminder: your {equipment} maintenance is due.
    |                        Don't wait until it breaks! {booking_link}"
    |
    +-- 2. Membership Management
    |     Query: SELECT * FROM memberships WHERE status = 'active'
    |
    |     Renewal reminders:
    |       Day -60: Email -- "Your {membership_name} renews in 60 days. Here's
    |                         what you've saved this year: ${savings_amount}"
    |       Day -30: SMS -- "Membership renewing soon. Questions? Reply here."
    |       Day -7:  SMS -- "Your {membership_name} renews on {date}.
    |                        No action needed -- we've got you covered!"
    |
    |     Payment failed:
    |       CRM webhook: membership.payment_failed
    |       Day 0: SMS -- "We had trouble processing your membership payment.
    |                      Update your card here: {payment_update_link}"
    |       Day 3: Email -- Same message + explain what happens if not updated
    |       Day 7: SMS -- "Final notice: your membership will lapse on {date}
    |                      without an updated payment method."
    |
    |     Usage tracking:
    |       Monthly email: "Your {membership_name} includes 2 tune-ups/year.
    |                       You have {remaining} remaining. Book now: {link}"
    |
    |     Upsell (for basic members):
    |       After each service visit:
    |       Email: "Love your {basic} membership? Upgrade to {premium} for
    |               ${diff}/month more and get {additional_benefits}."
    |
    +-- 3. Equipment Lifecycle Tracking
    |     Supabase: equipment table
    |       (contact_id, type, brand, model, install_date, warranty_expiry,
    |        last_service, next_service_due, estimated_lifespan_years)
    |
    |     Warranty expiring (60 days before):
    |       Email: "Your {brand} {equipment} warranty expires on {date}.
    |              Consider an extended warranty or service agreement for
    |              continued peace of mind."
    |
    |     Equipment age milestones:
    |       At 10 years: Email -- "Your {equipment} is 10 years old.
    |                    Average lifespan is {lifespan} years. Here's what to watch for..."
    |       At 75% of lifespan: SMS -- "Your {equipment} has served you well for
    |                    {age} years. Let's talk about your replacement options
    |                    before it fails. {booking_link}"
    |       At 90% of lifespan: AI Call (Vapi outbound) -- discuss replacement
    |                    timing, financing, energy savings of new models
    |
    +-- 4. Win-Back Campaigns (for SEGMENT_AT_RISK and SEGMENT_CHURNED)
    |
    |     At-Risk (12-24 months, quarterly check):
    |       Day 1:  SMS -- "Hi {name}, it's been a while! Everything running
    |                       smoothly with your {trade} systems? We're here if needed."
    |       Day 7:  Email -- "We miss you" + what's new at the company + offer
    |       Day 14: SMS -- "Exclusive returning customer offer: ${X} off any service.
    |                       Valid this month. {booking_link}"
    |
    |     Churned (24+ months, annual attempt):
    |       Day 1:  Email -- "It's been over 2 years since we last served you.
    |                         A lot has changed! We've added {new_services},
    |                         earned {review_count} 5-star reviews, and
    |                         we'd love to earn your business again."
    |       Day 7:  SMS -- "Special come-back offer: free inspection +
    |                       20% off any repair. Reply BOOK to schedule."
    |
    +-- 5. Event-Triggered Communications
    |
    |     Customer birthday (if DOB in CRM):
    |       SMS: "Happy birthday, {name}! Here's a gift from us: $25 off
    |             your next service. Enjoy your day! - Team {company}"
    |
    |     Job anniversary (1 year after major install):
    |       SMS: "It's been 1 year since we installed your new {equipment}!
    |             How's everything running? Reply if you have any questions."
    |
    |     Referral program (14 days after every completed job):
    |       SMS: "Loved our service? Refer a friend and you both get $50 off!
    |             Share this link: {referral_link}"
    |       Track: referral_code per customer, attribute new leads
    |
    |     Post-season thank you (end of busy season):
    |       Email: "Thanks for trusting us this {season}. As a thank you,
    |               here's 10% off your next service."
```

### Integration Points

| Integration | Purpose |
|---|---|
| CRM | Customer data, job history, membership status, equipment records, billing |
| Twilio | SMS for reminders, offers, birthday messages, referral links |
| SendGrid | Email for longer lifecycle communications, membership management |
| Vapi | Outbound AI calls for equipment replacement discussions |
| Supabase | Equipment tracking, lifecycle stage, communication log, segmentation |
| Stripe (optional) | Membership billing integration, payment retry for failed payments |
| Claude API | Personalization of all communications based on customer history |

### Key Metrics

| Metric | Target |
|---|---|
| Customer retention rate (year-over-year) | > 70% |
| Maintenance reminder booking rate | > 20% |
| Membership renewal rate | > 80% |
| Win-back campaign conversion (at-risk customers) | > 8% |
| Win-back campaign conversion (churned customers) | > 3% |
| Repeat customer rate (booked 2+ times in 12 months) | > 40% |
| Referral rate (customers who refer at least 1 person) | > 5% |
| Customer lifetime value growth (YoY) | > 15% |
| Equipment replacement lead generation | 2-5 per month per client |
| Membership upsell conversion rate | > 10% |
| Average communications per customer per quarter | 4-8 (across all channels) |
| Over-communication complaints | < 1% |

---

## 14. System 11: Financial Dashboard

### Purpose and Function

Provide real-time financial visibility for the home services company owner and our internal team. Tracks revenue, expenses, cost per lead, technician profitability, marketing ROI, and daily P&L. Most small home services companies operate with zero financial visibility beyond their bank balance. This dashboard gives them CFO-level insights automatically.

### Technical Architecture

```
Data Collection Layer (n8n scheduled workers):
    |
    +-- CRM Financial Sync (every 30 minutes):
    |     Revenue:
    |       GET /invoices?status=paid&date_from={last_sync}
    |       GET /payments?date_from={last_sync}
    |       Aggregate: daily revenue, payment methods, outstanding AR
    |     Jobs:
    |       GET /jobs?date_from={last_sync}
    |       Aggregate: booked, completed, cancelled, rescheduled, avg ticket
    |     Estimates:
    |       GET /estimates?date_from={last_sync}
    |       Aggregate: sent, accepted, declined, total value, close rate
    |     Customers:
    |       GET /customers?created_after={last_sync}
    |       Aggregate: new vs returning, total active base
    |     Technicians:
    |       GET /timesheets or /jobs with tech assignment
    |       Calculate: revenue per tech, hours worked, avg ticket, callback rate
    |
    +-- Marketing Spend Sync (daily at 11 PM):
    |     Google Ads API:
    |       GET /customers/{id}/googleAds:searchStream
    |       Query: "SELECT metrics.cost_micros, metrics.impressions,
    |               metrics.clicks, metrics.conversions FROM campaign
    |               WHERE segments.date = '{yesterday}'"
    |     Facebook Ads API:
    |       GET /act_{id}/insights?date_preset=yesterday
    |       Fields: spend, impressions, reach, actions, cost_per_action_type
    |     Google Local Services:
    |       GET /v1/accounts/{id}/reports
    |       Aggregate: spend, leads, cost per lead
    |     Platform costs (from Supabase aggregation):
    |       Twilio: sum(messages.cost + calls.cost_twilio) for date
    |       Vapi: sum(calls.cost_vapi) for date
    |       SendGrid: monthly plan cost / days in month
    |       PostGrid: sum(campaign direct mail costs) for date
    |
    +-- System Performance Metrics (real-time, stored in Supabase):
    |     System 1 (AI Receptionist):
    |       calls_handled, avg_duration, booking_rate, transfer_rate, total_cost
    |     System 2 (Speed-to-Lead):
    |       leads_processed, avg_response_time, channel_breakdown, cost
    |     System 3 (Follow-Up):
    |       sequences_active, replies_received, conversions, cost
    |     System 4 (Reviews):
    |       reviews_collected, avg_rating, response_rate
    |     System 5 (Estimate Closer):
    |       estimates_in_sequence, recovered_count, recovered_revenue
    |     Systems 7/8 (Campaigns):
    |       campaigns_active, audience_reached, bookings_attributed, ROI
    |
    v
Data Processing (n8n + Supabase SQL functions):
    |
    +-- Daily P&L Calculation (runs at 12:01 AM for previous day):
    |
    |     INSERT INTO daily_financials (client_id, date, ...)
    |     VALUES (
    |       revenue:         SUM(paid_invoices.amount),
    |       cogs:            SUM(parts_cost + labor_cost + subcontractor_cost),
    |                        -- pulled from CRM job cost fields
    |       gross_profit:    revenue - cogs,
    |       marketing_spend: SUM(google_ads + facebook_ads + lsa + direct_mail),
    |       platform_cost:   SUM(twilio + vapi + sendgrid + api_costs),
    |       overhead:        client_configured_daily_overhead,
    |       net_profit:      gross_profit - marketing_spend - platform_cost - overhead,
    |       jobs_completed:  COUNT(jobs WHERE status = 'completed'),
    |       new_leads:       COUNT(contacts WHERE created_at = date),
    |       new_customers:   COUNT(contacts WHERE first_job_date = date),
    |       avg_ticket:      revenue / jobs_completed
    |     )
    |
    +-- Unit Economics (calculated on demand, cached):
    |     cost_per_lead =       total_marketing_spend / total_leads
    |     cost_per_booking =    total_marketing_spend / total_bookings
    |     customer_acq_cost =   total_marketing_spend / new_customers
    |     revenue_per_lead =    total_revenue / total_leads
    |     roas =                total_revenue / total_ad_spend
    |     ltv_to_cac_ratio =    avg_lifetime_value / customer_acq_cost
    |
    +-- Technician Profitability (daily):
    |     Per tech:
    |       revenue_generated =  SUM(invoice.amount WHERE tech = X)
    |       cost =               hourly_rate * hours_worked + truck_cost_per_day
    |       profit =             revenue_generated - cost
    |       revenue_per_hour =   revenue_generated / hours_worked
    |       jobs_per_day =       COUNT(jobs WHERE tech = X AND date = Y)
    |       avg_ticket =         revenue_generated / jobs_count
    |       callback_rate =      callbacks / total_jobs (30-day rolling)
    |
    +-- Channel Attribution (daily):
    |     Per source (google_ads, facebook, lsa, referral, organic, repeat, outreach):
    |       leads, bookings, revenue, spend, cost_per_lead, roi
    |     Attribution model: first-touch (source of first contact gets credit)
    |
    v
Dashboard Delivery:
    |
    +-- Client Dashboard (Next.js + Supabase + Recharts/Tremor):
    |     URL: https://app.{ourdomain}.com/{client_slug}
    |     Auth: Supabase Auth (email magic link or password)
    |     Mobile-responsive (owners check on their phone)
    |
    |     Pages:
    |
    |     /overview (default):
    |       - Today's P&L card: revenue | profit | jobs | avg ticket
    |       - Week/month trend sparklines
    |       - Key alerts: "3 estimates aging past 14 days", "Review count
    |         dropped below 4.5 average this week"
    |       - AI-generated daily insight: "Your Tuesday revenue was 40% above
    |         average, driven by 2 replacement jobs from the fall campaign."
    |
    |     /leads:
    |       - Lead funnel: total leads --> contacted --> booked --> completed
    |       - By source: pie chart + table
    |       - Speed-to-lead performance: avg response time trend
    |       - Follow-up sequence performance: conversion by step
    |
    |     /marketing:
    |       - Campaign performance table: each campaign with spend, leads, revenue, ROI
    |       - Channel comparison: Google vs Facebook vs LSA vs Organic vs Referral
    |       - Cost per lead trend (monthly)
    |       - ROAS trend (monthly)
    |
    |     /technicians:
    |       - Leaderboard: ranked by revenue, jobs, rating, first-fix rate
    |       - Per-tech detail: revenue, hours, avg ticket, callback rate, utilization
    |       - Schedule efficiency: avg drive time, jobs per day
    |
    |     /reviews:
    |       - Review count + avg rating trend (monthly)
    |       - Recent reviews feed with AI responses
    |       - Platform breakdown: Google vs Yelp vs Facebook
    |       - Review request conversion funnel
    |
    |     /ai-systems:
    |       - System health status (green/yellow/red per system)
    |       - Call logs: recent AI calls with transcripts, outcomes, costs
    |       - Message logs: recent SMS/email with delivery status
    |       - Sequence status: active, paused, completed counts
    |       - Platform cost breakdown: Vapi, Twilio, Claude, SendGrid
    |
    +-- Daily Email Report (SendGrid, 7:00 AM owner's timezone):
    |     Subject: "{company_name} Daily Report -- {date}"
    |     Content:
    |       Yesterday's Revenue: ${amount} ({trend} vs avg)
    |       Jobs Completed: {count}
    |       New Leads: {count} (top source: {source})
    |       Avg Ticket: ${amount}
    |       Review Score: {rating} ({new_reviews} new)
    |       Action Items: {AI-generated list of 2-3 items}
    |       Link: "View full dashboard: {dashboard_url}"
    |
    +-- Weekly SMS Summary (Twilio, Monday at 8:00 AM):
    |     "Last week at {company}: ${revenue} revenue, {new_customers} new
    |      customers, {reviews} new reviews (avg {rating}). Full report:
    |      {dashboard_url}"
    |
    +-- Google Sheets Sync (optional, for spreadsheet-oriented clients):
    |     Google Sheets API v4: daily data append to shared spreadsheet
    |     Tabs: Daily P&L, Leads, Marketing, Technicians
    |
    v
Alerting (real-time, via n8n + Supabase triggers):
    |
    +-- Revenue alerts:
    |     Daily revenue < 50% of 30-day average --> SMS to owner
    |     "Slow day alert: revenue is tracking ${X} below your daily average."
    |
    +-- Cost alerts:
    |     Cost per lead > 2x 30-day average --> SMS to owner + internal team
    |     "Cost per lead spike: ${X} today vs ${Y} average. Check campaigns."
    |
    +-- Operational alerts:
    |     Technician callback rate > 15% (30-day rolling) --> internal alert
    |     Cancellation rate > 20% (7-day rolling) --> alert owner
    |
    +-- System alerts:
    |     Any system error rate > 5% --> PagerDuty/Slack to internal team
    |     Vapi call failure rate > 2% --> immediate internal alert
    |     CRM API connection failure --> immediate internal alert
```

### Integration Points

| Integration | Purpose |
|---|---|
| CRM API | Revenue, job, estimate, customer, technician data extraction |
| Google Ads API | Campaign spend and performance data |
| Facebook Marketing API | Ad spend and performance data |
| Google LSA API | Local services ad spend and lead data |
| Supabase | Central data warehouse, real-time queries, auth for dashboard |
| Next.js + Vercel/Railway | Dashboard frontend hosting |
| Recharts or Tremor | Chart components for dashboard visualizations |
| SendGrid | Daily email reports |
| Twilio | Weekly SMS summaries |
| Google Sheets API | Optional data export for spreadsheet users |
| PostHog | Dashboard usage analytics |

### Key Metrics Tracked by the Dashboard

| Category | Metrics |
|---|---|
| Revenue | Daily/weekly/monthly revenue, average ticket, revenue per tech, revenue by service type |
| Leads | Total leads, cost per lead, lead-to-booking rate, by source, by channel |
| Marketing | ROAS, cost per acquisition, campaign ROI, ad spend by channel, organic vs paid split |
| Operations | Jobs completed, cancellation rate, utilization rate, drive time, first-fix rate |
| Customer | New vs repeat ratio, lifetime value, churn rate, membership count, referral rate |
| Reviews | New reviews, average rating trend, response rate, review request conversion |
| AI Platform | Calls handled, response times, automation rate, system costs, error rates |
| Financial | Gross margin, net profit, overhead ratio, break-even point, revenue forecast |

---

## 15. Data Model

### Primary Database: Supabase (PostgreSQL)

```sql
-- ============================================================
-- CORE TABLES
-- ============================================================

-- Our client (the home services company)
CREATE TABLE clients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    trade TEXT NOT NULL,  -- hvac, plumbing, roofing, electrical, pest_control
    crm_type TEXT NOT NULL,  -- servicetitan, housecallpro, jobber, ghl
    crm_api_key TEXT,  -- encrypted via Supabase Vault
    crm_base_url TEXT,
    twilio_phone TEXT,  -- E.164 format
    twilio_account_sid TEXT,  -- encrypted
    twilio_auth_token TEXT,  -- encrypted
    sendgrid_api_key TEXT,  -- encrypted
    vapi_assistant_id TEXT,
    vapi_outbound_assistant_id TEXT,
    google_place_id TEXT,
    google_oauth_tokens JSONB,  -- encrypted, for GBP API
    facebook_page_id TEXT,
    facebook_access_token TEXT,  -- encrypted
    service_area_zips TEXT[],
    service_area_geojson JSONB,  -- GeoJSON polygon for precise area matching
    timezone TEXT DEFAULT 'America/New_York',
    settings JSONB NOT NULL DEFAULT '{}',
    -- settings includes:
    --   review_delay_hours, auto_approve_reviews, emergency_contacts[],
    --   business_hours, discount_authority, brand_voice_guide,
    --   service_catalog[], pricing_ranges{}, tech_roster[],
    --   daily_overhead_estimate, membership_types[]
    status TEXT DEFAULT 'active',  -- active, paused, onboarding, churned
    onboarded_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Customer/lead contact
CREATE TABLE contacts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    crm_contact_id TEXT,  -- external ID in their CRM
    first_name TEXT,
    last_name TEXT,
    phone TEXT,  -- E.164 format
    phone_type TEXT,  -- mobile, landline, voip
    email TEXT,
    address_line1 TEXT,
    address_line2 TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    lat NUMERIC(10, 7),
    lng NUMERIC(10, 7),
    source TEXT,  -- google_ads, facebook, website, gbp, yelp, referral, cold_outreach
    source_detail TEXT,  -- specific campaign or form
    lifecycle_stage TEXT DEFAULT 'lead',  -- lead, prospect, customer, member, at_risk, churned
    lifetime_value NUMERIC(10, 2) DEFAULT 0,
    first_job_date DATE,
    last_job_date DATE,
    total_jobs INTEGER DEFAULT 0,
    membership_status TEXT,  -- active, expired, none
    opted_out_sms BOOLEAN DEFAULT FALSE,
    opted_out_email BOOLEAN DEFAULT FALSE,
    opted_out_calls BOOLEAN DEFAULT FALSE,
    opted_out_at TIMESTAMPTZ,
    opt_out_reason TEXT,
    tags TEXT[] DEFAULT '{}',
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- SYSTEM 1 & 3: CALLS
-- ============================================================

CREATE TABLE calls (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id),
    contact_id UUID REFERENCES contacts(id),
    direction TEXT NOT NULL,  -- inbound, outbound
    system_source TEXT,  -- ai_receptionist, lead_followup, estimate_closer
    vapi_call_id TEXT,
    twilio_call_sid TEXT,
    phone_from TEXT,
    phone_to TEXT,
    duration_seconds INTEGER,
    transcript TEXT,
    summary TEXT,  -- AI-generated summary
    outcome TEXT,  -- booked, transferred, voicemail, info_request, emergency, spam, no_answer
    sentiment_score NUMERIC(3, 2),  -- -1.0 to 1.0
    recording_url TEXT,  -- Cloudflare R2 URL
    booking_created BOOLEAN DEFAULT FALSE,
    transfer_reason TEXT,
    cost_vapi NUMERIC(8, 4),
    cost_twilio NUMERIC(8, 4),
    cost_llm NUMERIC(8, 4),
    cost_total NUMERIC(8, 4),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- SYSTEMS 2/3/4/5/7/8/10: MESSAGES
-- ============================================================

CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id),
    contact_id UUID REFERENCES contacts(id),
    channel TEXT NOT NULL,  -- sms, email, facebook, gbp, direct_mail
    direction TEXT NOT NULL,  -- outbound, inbound
    system_source TEXT NOT NULL,  -- speed_to_lead, follow_up, review_request,
                                 -- estimate_closer, seasonal_campaign, lifecycle, etc.
    sequence_id UUID REFERENCES sequences(id),
    step_number INTEGER,
    subject TEXT,  -- for email
    body TEXT,
    status TEXT DEFAULT 'sent',  -- queued, sent, delivered, opened, clicked,
                                 -- replied, failed, bounced, unsubscribed
    twilio_message_sid TEXT,
    sendgrid_message_id TEXT,
    cost NUMERIC(8, 4),
    metadata JSONB DEFAULT '{}',  -- delivery_report, open_timestamp, click_url, etc.
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- SYSTEMS 3/5/10: SEQUENCES
-- ============================================================

CREATE TABLE sequences (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id),
    contact_id UUID NOT NULL REFERENCES contacts(id),
    sequence_type TEXT NOT NULL,  -- standard_14day, hot_lead_3day,
                                 -- estimate_followup_60day, maintenance_reminder,
                                 -- winback, membership_renewal, equipment_lifecycle
    current_step INTEGER DEFAULT 0,
    total_steps INTEGER NOT NULL,
    status TEXT DEFAULT 'active',  -- active, paused, completed, converted, opted_out, failed
    next_fire_at TIMESTAMPTZ,
    paused_reason TEXT,
    started_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    converted_at TIMESTAMPTZ,
    conversion_value NUMERIC(10, 2),
    conversion_type TEXT,  -- booked_job, accepted_estimate, renewed_membership
    metadata JSONB DEFAULT '{}',  -- source_details, estimate_id, equipment_id, etc.
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Sequence step definitions (templates)
CREATE TABLE sequence_definitions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sequence_type TEXT NOT NULL,
    step_number INTEGER NOT NULL,
    channel TEXT NOT NULL,  -- sms, email, ai_call, voicemail_drop
    delay_from_previous INTERVAL NOT NULL,  -- e.g., '24 hours', '3 days'
    content_theme TEXT,  -- brief description for Claude to use as guidance
    template TEXT,  -- optional: static template with {merge_fields}
    metadata JSONB DEFAULT '{}',
    UNIQUE(sequence_type, step_number)
);

-- ============================================================
-- SYSTEM 4: REVIEWS
-- ============================================================

CREATE TABLE reviews (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id),
    contact_id UUID REFERENCES contacts(id),  -- matched customer, if found
    platform TEXT NOT NULL,  -- google, yelp, facebook
    platform_review_id TEXT,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    reviewer_name TEXT,
    our_response TEXT,
    response_status TEXT DEFAULT 'pending',  -- pending, auto_posted, approved, manual, skipped
    response_posted_at TIMESTAMPTZ,
    sentiment_score NUMERIC(3, 2),
    is_negative BOOLEAN GENERATED ALWAYS AS (rating <= 2) STORED,
    legal_risk_flag BOOLEAN DEFAULT FALSE,
    metadata JSONB DEFAULT '{}',
    review_date TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- SYSTEM 6: COLD OUTREACH PROSPECTS
-- ============================================================

CREATE TABLE prospects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id),
    first_name TEXT,
    last_name TEXT,
    email TEXT NOT NULL,
    company TEXT,
    title TEXT,
    phone TEXT,
    linkedin_url TEXT,
    source TEXT,  -- apollo, google_maps, manual_upload
    score INTEGER,  -- 1-100 priority score
    email_verified BOOLEAN DEFAULT FALSE,
    email_verification_result TEXT,  -- valid, invalid, catch_all, etc.
    sequence_status TEXT DEFAULT 'pending',  -- pending, active, replied, converted,
                                            -- declined, bounced, unsubscribed
    last_email_sent_at TIMESTAMPTZ,
    reply_received_at TIMESTAMPTZ,
    reply_classification TEXT,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- SYSTEMS 7/8: CAMPAIGNS
-- ============================================================

CREATE TABLE campaigns (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id),
    campaign_type TEXT NOT NULL,  -- neighborhood, seasonal, cold_outreach, winback
    template_id UUID,  -- reference to campaign_templates
    name TEXT NOT NULL,
    status TEXT DEFAULT 'draft',  -- draft, scheduled, active, completed, paused
    channel TEXT,  -- sms, email, direct_mail, facebook_ad, multi_channel
    audience_count INTEGER DEFAULT 0,
    audience_segment TEXT,  -- description of targeting criteria
    promo_code TEXT,
    tracking_phone TEXT,  -- Twilio number for call attribution
    landing_page_url TEXT,
    total_spend NUMERIC(10, 2) DEFAULT 0,  -- actual cost
    total_revenue_attributed NUMERIC(10, 2) DEFAULT 0,
    leads_generated INTEGER DEFAULT 0,
    bookings_generated INTEGER DEFAULT 0,
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    metadata JSONB DEFAULT '{}',  -- job_address for neighborhood, weather_event for seasonal, etc.
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE campaign_templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    trade TEXT NOT NULL,  -- hvac, plumbing, roofing, all
    campaign_type TEXT NOT NULL,
    name TEXT NOT NULL,
    trigger_type TEXT NOT NULL,  -- date, weather, event, recurring
    trigger_config JSONB NOT NULL,  -- {start_date, end_date} or {weather_condition, threshold}
    channels TEXT[] NOT NULL,  -- ['sms', 'email']
    sms_template TEXT,
    email_subject_template TEXT,
    email_body_template TEXT,
    default_offer TEXT,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- SYSTEM 9: DISPATCH
-- ============================================================

CREATE TABLE technicians (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id),
    crm_tech_id TEXT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    skills TEXT[] DEFAULT '{}',  -- ['ac_repair', 'furnace_install', 'duct_work']
    certifications TEXT[] DEFAULT '{}',  -- ['epa_608', 'nate_hvac', 'gas_license']
    max_daily_jobs INTEGER DEFAULT 6,
    hourly_rate NUMERIC(8, 2),
    home_base_address TEXT,
    home_base_lat NUMERIC(10, 7),
    home_base_lng NUMERIC(10, 7),
    vehicle_inventory TEXT[] DEFAULT '{}',  -- common parts on truck
    avg_rating NUMERIC(3, 2),
    first_fix_rate NUMERIC(5, 2),  -- percentage
    is_active BOOLEAN DEFAULT TRUE,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE dispatch_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id),
    crm_job_id TEXT NOT NULL,
    technician_id UUID REFERENCES technicians(id),
    technician_name TEXT,
    assignment_method TEXT NOT NULL,  -- auto, suggested, manual_override
    ai_confidence NUMERIC(3, 2),  -- 0.00 to 1.00
    ai_score INTEGER,  -- 0-100
    drive_time_minutes INTEGER,
    reason TEXT,  -- why this tech was chosen
    alternatives JSONB,  -- [{tech_id, name, score, reason}]
    schedule_impact TEXT,
    parts_check JSONB,  -- {needed[], on_truck: bool}
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- SYSTEM 10: EQUIPMENT TRACKING
-- ============================================================

CREATE TABLE equipment (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id),
    contact_id UUID NOT NULL REFERENCES contacts(id),
    type TEXT NOT NULL,  -- ac, furnace, water_heater, sump_pump, roof, generator
    brand TEXT,
    model TEXT,
    serial_number TEXT,
    install_date DATE,
    estimated_lifespan_years INTEGER,
    warranty_expiry DATE,
    last_service_date DATE,
    next_service_due DATE,
    service_interval_days INTEGER,  -- e.g., 180 for biannual
    condition TEXT,  -- good, fair, poor, needs_replacement
    notes TEXT,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- SYSTEM 11: FINANCIAL DATA
-- ============================================================

CREATE TABLE daily_financials (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id),
    date DATE NOT NULL,
    revenue NUMERIC(12, 2) DEFAULT 0,
    cogs NUMERIC(12, 2) DEFAULT 0,
    gross_profit NUMERIC(12, 2) DEFAULT 0,
    marketing_spend_google NUMERIC(10, 2) DEFAULT 0,
    marketing_spend_facebook NUMERIC(10, 2) DEFAULT 0,
    marketing_spend_lsa NUMERIC(10, 2) DEFAULT 0,
    marketing_spend_direct_mail NUMERIC(10, 2) DEFAULT 0,
    marketing_spend_other NUMERIC(10, 2) DEFAULT 0,
    marketing_spend_total NUMERIC(10, 2) DEFAULT 0,
    platform_cost NUMERIC(10, 2) DEFAULT 0,  -- our fees (Twilio+Vapi+etc)
    overhead NUMERIC(10, 2) DEFAULT 0,
    net_profit NUMERIC(12, 2) DEFAULT 0,
    jobs_completed INTEGER DEFAULT 0,
    jobs_booked INTEGER DEFAULT 0,
    jobs_cancelled INTEGER DEFAULT 0,
    new_leads INTEGER DEFAULT 0,
    new_customers INTEGER DEFAULT 0,
    avg_ticket NUMERIC(10, 2) DEFAULT 0,
    cost_per_lead NUMERIC(10, 2) DEFAULT 0,
    reviews_received INTEGER DEFAULT 0,
    avg_review_rating NUMERIC(3, 2),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(client_id, date)
);

-- ============================================================
-- SYSTEM HEALTH & AUDIT LOG
-- ============================================================

CREATE TABLE system_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID REFERENCES clients(id),
    system_name TEXT NOT NULL,  -- ai_receptionist, speed_to_lead, follow_up, etc.
    event_type TEXT NOT NULL,  -- success, error, escalation, timeout, warning
    severity TEXT DEFAULT 'info',  -- debug, info, warning, error, critical
    details JSONB DEFAULT '{}',
    error_message TEXT,
    duration_ms INTEGER,  -- execution time
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- INDEXES
-- ============================================================

CREATE INDEX idx_contacts_client_phone ON contacts(client_id, phone);
CREATE INDEX idx_contacts_client_email ON contacts(client_id, email);
CREATE INDEX idx_contacts_lifecycle ON contacts(client_id, lifecycle_stage);
CREATE INDEX idx_contacts_last_job ON contacts(client_id, last_job_date);

CREATE INDEX idx_sequences_next_fire ON sequences(next_fire_at)
    WHERE status = 'active';
CREATE INDEX idx_sequences_client_contact ON sequences(client_id, contact_id);
CREATE INDEX idx_sequences_status ON sequences(client_id, status);

CREATE INDEX idx_messages_client_contact ON messages(client_id, contact_id);
CREATE INDEX idx_messages_created ON messages(client_id, created_at);

CREATE INDEX idx_calls_client_date ON calls(client_id, created_at);
CREATE INDEX idx_calls_contact ON calls(contact_id);

CREATE INDEX idx_reviews_client_platform ON reviews(client_id, platform);
CREATE INDEX idx_reviews_client_date ON reviews(client_id, review_date);
CREATE INDEX idx_reviews_negative ON reviews(client_id) WHERE is_negative = TRUE;

CREATE INDEX idx_daily_financials_lookup ON daily_financials(client_id, date);

CREATE INDEX idx_equipment_next_service ON equipment(client_id, next_service_due);
CREATE INDEX idx_equipment_warranty ON equipment(client_id, warranty_expiry);

CREATE INDEX idx_campaigns_client_status ON campaigns(client_id, status);

CREATE INDEX idx_prospects_client_status ON prospects(client_id, sequence_status);
CREATE INDEX idx_prospects_email ON prospects(client_id, email);

CREATE INDEX idx_dispatch_client_date ON dispatch_events(client_id, created_at);

CREATE INDEX idx_system_logs_client_date ON system_logs(client_id, created_at);
CREATE INDEX idx_system_logs_errors ON system_logs(client_id, event_type)
    WHERE event_type = 'error';

-- ============================================================
-- ROW LEVEL SECURITY
-- ============================================================

ALTER TABLE contacts ENABLE ROW LEVEL SECURITY;
ALTER TABLE calls ENABLE ROW LEVEL SECURITY;
ALTER TABLE messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE sequences ENABLE ROW LEVEL SECURITY;
ALTER TABLE reviews ENABLE ROW LEVEL SECURITY;
ALTER TABLE campaigns ENABLE ROW LEVEL SECURITY;
ALTER TABLE daily_financials ENABLE ROW LEVEL SECURITY;
ALTER TABLE equipment ENABLE ROW LEVEL SECURITY;
ALTER TABLE technicians ENABLE ROW LEVEL SECURITY;
ALTER TABLE dispatch_events ENABLE ROW LEVEL SECURITY;

-- Policy pattern: users can only see data for their client_id
-- (client_id derived from auth.jwt() -> user_metadata -> client_id)
CREATE POLICY "client_isolation" ON contacts
    FOR ALL USING (client_id = (auth.jwt() -> 'user_metadata' ->> 'client_id')::uuid);
-- (Repeat for all tables above)
```

### Data Retention Policy

| Data Type | Hot Storage | Cold Storage | Total Retention |
|---|---|---|---|
| Call recordings (audio files) | 90 days (R2) | 2 years (R2 IA class) | 2 years |
| Call transcripts | 2 years (Supabase) | Archive to S3 | 5 years |
| SMS/email message bodies | 2 years (Supabase) | Archive to S3 | 5 years |
| Financial data | Indefinite (Supabase) | -- | Indefinite |
| Contact data | Indefinite (Supabase) | -- | Indefinite (unless opt-out) |
| Campaign data | Indefinite (Supabase) | -- | Indefinite |
| System logs | 90 days (Supabase) | -- | Auto-purge via pg_cron |
| Prospect data (cold outreach) | 12 months (Supabase) | -- | Auto-purge stale records |
| Equipment records | Indefinite (Supabase) | -- | Indefinite |
| Review data | Indefinite (Supabase) | -- | Indefinite |

---

## 16. Infrastructure Costs Per Client

### Monthly Cost Breakdown

| Service | Low Usage | Medium Usage | High Usage |
| | (15 calls/day, small market) | (30 calls/day, mid market) | (60+ calls/day, large market) |
|---|---|---|---|
| **Vapi (voice AI)** | $75 | $150 | $300 |
| **Twilio (SMS + voice routing)** | $40 | $75 | $150 |
| **Claude API (Anthropic)** | $20 | $40 | $80 |
| **SendGrid (email)** | $10 | $15 | $25 |
| **n8n hosting (shared)** | $5 | $5 | $10 |
| **Supabase (shared)** | $5 | $8 | $12 |
| **Cloudflare R2 (storage)** | $3 | $5 | $8 |
| **Google APIs (Maps, GBP)** | $5 | $10 | $15 |
| **Cold email (Instantly.ai)** | $15 | $30 | $50 |
| **Apollo.io (shared)** | $5 | $10 | $15 |
| **PostGrid (direct mail)** | $50 | $150 | $400 |
| **Monitoring (shared)** | $2 | $2 | $5 |
| **Domain/DNS/SSL** | $2 | $2 | $2 |
| | | | |
| **Total Platform COGS** | **$237** | **$502** | **$1,072** |
| **Suggested Client Price** | **$1,500/mo** | **$2,500/mo** | **$4,000/mo** |
| **Gross Margin** | **84.2%** | **79.9%** | **73.2%** |

### One-Time Setup Costs

| Item | Labor Hours | Client Setup Fee |
|---|---|---|
| CRM API integration + testing | 4-8 hours | -- |
| Vapi agent configuration + prompt engineering + testing | 4-6 hours | -- |
| Twilio number provisioning + forwarding setup | 1 hour | -- |
| SendGrid authentication (DKIM/SPF/DMARC) | 1 hour | -- |
| Cold email domain setup + warmup (2-4 weeks) | 2 hours setup + monitoring | -- |
| System prompts + brand customization | 4-6 hours | -- |
| Client dashboard provisioning | 1 hour | -- |
| Data import (customer list, equipment, etc.) | 2-4 hours | -- |
| Testing (20+ call scenarios, all lead sources, full sequence) | 4-8 hours | -- |
| Training call with client | 1 hour | -- |
| **Total** | **24-40 hours** | **$1,500-2,500** |

### Cost Scaling Notes

- **Vapi:** $0.05-0.15/minute. Average call: 2.5 min = $0.125-0.375/call. At 30 calls/day: $112-337/mo.
- **Twilio SMS:** $0.0079/segment outbound + $0.0079/segment inbound. At 500 messages/month: ~$8.
- **Twilio voice:** $0.014/min outbound + $0.0085/min inbound. Minimal if Vapi handles voice.
- **Claude API (Sonnet):** ~$0.003 per 1K input tokens, $0.015 per 1K output tokens. Average call classification: ~$0.01. Average message generation: ~$0.005. At 1,000 AI operations/month: $10-20.
- **SendGrid Pro:** $19.95/mo for 50K emails. Shared across clients.
- **PostGrid:** $0.75-1.25/postcard. 200 postcards/month: $150-250. This is the biggest variable cost.

---

## 17. Security and Compliance

### TCPA Compliance (Telephone Consumer Protection Act)

| Requirement | Implementation |
|---|---|
| Express written consent for marketing SMS | Consent captured on website form (checkbox: "I agree to receive text messages from {company}"). Timestamp + source stored in contacts.metadata.tcpa_consent. |
| Opt-out handling | All marketing SMS includes "Reply STOP to opt out." Twilio Advanced Opt-Out auto-handles STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, QUIT. n8n webhook updates contacts.opted_out_sms = true, contacts.opted_out_at = NOW(). |
| Transactional vs. marketing distinction | Appointment confirmations and reminders are transactional (no consent needed). Follow-up sequences and campaigns are marketing (consent required). |
| Calling hours | n8n enforces 8 AM - 9 PM in contact's local timezone. Timezone inferred from zip code mapping table. Outbound AI calls only between 9 AM - 7 PM. |
| Do Not Call list | Monthly DNC list scrub via DNCList.com API ($200/year) or manual upload. Applied before outbound call sequences and campaigns. |
| Autodialer disclosure | Vapi agents disclose: "This call may be recorded for quality purposes." Required at call start. |
| Prior express consent for automated calls | Website forms include: "By submitting, I consent to receive calls, including automated or AI-assisted calls, from {company_name} at the number provided." |

### Call Recording Consent

| Consent Type | States | Implementation |
|---|---|---|
| One-party consent | 38 states + DC | Recording enabled by default. Agent discloses: "This call may be recorded." |
| All-party consent | 12 states: CA, CT, FL, IL, MA, MD, MI, MT, NH, OR, PA, WA | Vapi agent asks: "Do you mind if I record this call for quality purposes?" If caller declines: Vapi config `recordingEnabled: false` toggled mid-call via server event. |
| State detection | Automatic | Caller's phone number area code maps to state via lookup table. Two-party states flagged in Vapi assistant configuration per client based on service area. |
| Storage security | All states | Recordings encrypted at rest (Cloudflare R2 server-side encryption, AES-256). Access requires authenticated presigned URL. Access logged in system_logs. Auto-deleted per retention policy. |

### CAN-SPAM Compliance (Email)

| Requirement | Implementation |
|---|---|
| Physical mailing address | Client's business address in every email footer (SendGrid template footer block) |
| Unsubscribe mechanism | One-click unsubscribe in every marketing email (SendGrid List-Unsubscribe header). Processed immediately via webhook. |
| Unsubscribe processing time | Instant (automated). CAN-SPAM requires within 10 business days; we do it in seconds. |
| Accurate subject lines | Claude generation prompt includes: "Subject line must accurately represent the email content. No deceptive or misleading subjects." |
| Identification as ad (when required) | Marketing campaign emails include "Promotional" label where applicable |
| Sender identification | From name and email accurately represent the client's business |

### Cold Email Compliance

| Requirement | Implementation |
|---|---|
| B2B exemption | All cold outreach targets business contacts at business email addresses only |
| Physical address in every email | Client's business address in footer |
| Opt-out in every email | One-click unsubscribe link, processed within 24 hours |
| Accurate headers | From name/email represents the client accurately |
| Separate sending domain | Dedicated domain (mail.{clientname}services.com), never client's primary |
| SPF/DKIM/DMARC configured | Verified before any sending begins |
| Volume limits | Max 50/day during warmup, max 200/day production |
| Suppression list management | Global suppression list checked before every send |

### Data Security

| Layer | Implementation |
|---|---|
| Encryption in transit | TLS 1.3 enforced on all connections: API calls, webhooks, dashboard |
| Encryption at rest | Supabase: AES-256 (transparent). R2: AES-256 (server-side). |
| Secrets management | All API keys stored via Supabase Vault (pgcrypto) or n8n encrypted credentials. Never in workflow code, environment variables, or logs. |
| Access control | Per-client RLS in Supabase. Dashboard auth via Supabase Auth. Internal admin requires separate auth + MFA. |
| PII handling | Phone and email hashed (SHA-256) in system_logs and analytics. Full PII only in contacts table behind RLS. |
| Audit trail | All system actions logged to system_logs with client_id, timestamp, actor, event details |
| Backup | Supabase: automatic daily backups with 7-day PITR (Point-in-Time Recovery). Database size monitored. |
| Vulnerability scanning | Dependencies scanned via npm audit / Dependabot. n8n kept on latest stable. |
| Incident response | Documented runbook for data breaches. Notification to affected clients within 72 hours per GDPR-like best practices. |

### HIPAA Considerations

Home services companies are generally NOT subject to HIPAA. However, if a client serves medical facilities:
- No PHI (Protected Health Information) is stored in our system
- Call transcripts are sanitized (no medical details captured)
- This is documented in our service agreement

---

## 18. Scaling Considerations

### Phase 1: 1-50 Clients

| Component | Architecture | Monthly Cost |
|---|---|---|
| n8n | Single instance on Hetzner CX31 (8 vCPU, 16 GB RAM, $15/mo) | $15 |
| Supabase | Single Pro project (8 GB RAM, 100 GB storage, $25/mo) | $25 |
| Redis | Upstash free tier (10K commands/day) | $0 |
| Dashboard | Next.js on Vercel (Pro plan, $20/mo) | $20 |
| Monitoring | Grafana Cloud free tier + UptimeRobot free | $0 |
| R2 Storage | Cloudflare R2 (10 GB free, then $0.015/GB/mo) | $5 |
| **Total shared infra** | | **$65/mo** |
| **Per-client infra share** | $65 / 25 clients (avg) | **$2.60** |

**Key constraints at this phase:**
- n8n handles ~50 clients if workflows are efficient (no unnecessary polling, proper batching)
- Supabase handles millions of rows comfortably
- Single engineer can manage platform + onboard 2-3 clients/month
- Manual monitoring with alerts is sufficient

### Phase 2: 50-150 Clients

| Component | Architecture | Monthly Cost |
|---|---|---|
| n8n | 2 instances: primary (webhooks + crons) + worker (execution). Hetzner CX41 each. | $60 |
| Supabase | Pro Large (16 GB RAM, 500 GB storage) or self-hosted on Hetzner | $75 |
| Redis | Upstash Pro ($10/mo) for job queues | $10 |
| Dashboard | Vercel Pro with caching | $20 |
| Monitoring | Grafana Cloud paid ($15/mo) + PagerDuty ($20/mo) | $35 |
| R2 Storage | 100 GB+ | $10 |
| **Total shared infra** | | **$210/mo** |
| **Per-client infra share** | $210 / 100 clients (avg) | **$2.10** |

**Key decisions at this phase:**
- Split n8n into webhook receiver and worker instances (n8n queue mode with Redis)
- Implement automated onboarding scripts (Terraform or Pulumi)
- Hire dedicated infrastructure engineer
- Add read replicas for dashboard queries to avoid impacting automation workloads
- Implement proper log aggregation (Loki)

### Phase 3: 150-500 Clients

| Component | Architecture | Monthly Cost |
|---|---|---|
| n8n | Kubernetes cluster: 1 main + 3-5 workers, auto-scaling | $200 |
| Database | Self-hosted PostgreSQL cluster (Patroni) on Hetzner dedicated servers, or CockroachDB | $150 |
| Redis | Redis Cluster (3 nodes) on Hetzner or Upstash Enterprise | $50 |
| Dashboard | Next.js on Vercel Enterprise or self-hosted on K8s | $50 |
| Monitoring | Full stack: Grafana + Prometheus + Loki + Tempo | $100 |
| R2/S3 | 1 TB+ | $25 |
| **Total shared infra** | | **$575/mo** |
| **Per-client infra share** | $575 / 300 clients (avg) | **$1.92** |

**Key decisions at this phase:**
- Kubernetes for n8n workers (auto-scale on queue depth)
- Database sharding strategy (by client_id range or geography)
- Negotiate volume pricing: Anthropic enterprise, Twilio ISV partner, Vapi enterprise
- Build self-serve onboarding portal (client completes wizard, systems auto-provision)
- Implement multi-region deployment for latency (US East + US West)
- Hire platform team (3-5 engineers), client success team (3-5 people)

### CRM API Rate Limit Management

| CRM | Rate Limit | Strategy |
|---|---|---|
| ServiceTitan | 100 requests/min | Token bucket in Redis per client. Queue non-urgent reads. Webhooks preferred over polling. |
| Housecall Pro | 60 requests/min | Same pattern. Batch operations where API supports it. |
| Jobber | 5 requests/sec | GraphQL batching (multiple queries in one request). |
| GoHighLevel | 100 requests/min | Webhook-first architecture. Cache frequently accessed data in Supabase. |

### AI Cost Optimization

| Strategy | Impact | Phase |
|---|---|---|
| Use Claude Haiku for classification, Sonnet for generation | 50-70% cost reduction on classification tasks | Phase 1 |
| Cache common FAQ responses per client | 20-30% reduction in API calls | Phase 1 |
| Batch non-urgent AI work (daily reports, campaign content) | Spread costs, avoid rate limits | Phase 1 |
| Prompt optimization (shorter system prompts, fewer examples) | 10-20% token reduction | Phase 2 |
| Response caching for identical review response patterns | 10-15% reduction | Phase 2 |
| Negotiate Anthropic enterprise pricing | 20-40% cost reduction | Phase 3 |
| Fine-tune smaller model for classification tasks | 60-80% cost reduction on those tasks | Phase 3 |

---

## 19. Deployment and Onboarding

### New Client Onboarding Checklist

```
PHASE 1: DISCOVERY & INFORMATION GATHERING (Day 1)
================================================================
[ ] Client trade type and full service menu
[ ] CRM type and admin API credentials
[ ] Business phone number(s) and current call flow
[ ] Business hours (standard + emergency)
[ ] Service area (zip codes or city boundaries)
[ ] Google Business Profile admin access
[ ] Facebook Business Page admin access
[ ] Company logo (SVG/PNG), brand colors (hex), brand voice description
[ ] Pricing guide / rate sheet (ranges, not exact)
[ ] Emergency escalation contacts (names + cell phones, ordered priority)
[ ] Technician roster: names, skills, certifications, phone numbers
[ ] Existing customer list export (CSV from CRM)
[ ] Current marketing channels and approximate spend
[ ] Equipment brands they service / install
[ ] Membership / service agreement details (if any)
[ ] Competitors they frequently encounter
[ ] Owner's preferred communication (SMS vs email for alerts)

PHASE 2: SYSTEM PROVISIONING (Day 1-2)
================================================================
[ ] Create client record in Supabase (clients table)
[ ] Provision Twilio local phone number (area code matching client's market)
[ ] Configure Twilio: SMS webhook, voice forwarding, recording settings
[ ] Create SendGrid authenticated sender for client's domain
    - Add DNS records: CNAME for DKIM, TXT for SPF
    - Verify sender identity
[ ] Create SendGrid dynamic templates (review request, follow-up, seasonal)
[ ] Create Vapi inbound assistant:
    - Write system prompt (trade-specific + company-specific)
    - Configure function tools (book_appointment, transfer, lookup, availability)
    - Set voice, first message, end message
    - Configure recording based on consent state(s)
    - Set server URL to n8n webhook
[ ] Create Vapi outbound assistant (for follow-up and estimate closer calls)
[ ] Test CRM API connection:
    - Verify read access to customers, jobs, estimates, schedules
    - Verify write access to bookings, contacts, notes
    - Confirm webhook configuration (if available)
[ ] Set up cold email sending domain:
    - Register: mail.{clientname}services.com
    - Configure SPF, DKIM, DMARC
    - Create Instantly.ai account, begin warmup (2-4 week process)
[ ] Create client dashboard account (Supabase Auth user)
[ ] Import customer data into contacts table
[ ] Import equipment data into equipment table
[ ] Configure all client-specific settings in clients.settings JSONB

PHASE 3: SYSTEM CONFIGURATION (Day 2-4)
================================================================
[ ] System 1 (AI Receptionist):
    - Finalize system prompt with service menu, pricing, FAQ answers
    - Test 20+ inbound call scenarios (booking, inquiry, emergency, transfer,
      after-hours, spam, Spanish, angry caller, complex question)
    - Test CRM booking creation end-to-end
    - Test emergency escalation chain
    - Test call recording and transcript saving
[ ] System 2 (Speed-to-Lead):
    - Configure webhook receivers for all active lead sources
    - Test website form submission end-to-end
    - Test GBP message detection and response
    - Test Facebook lead ad capture (if active)
    - Verify SMS and email delivery to test contacts
    - Verify CRM record creation
[ ] System 3 (Lead Follow-Up):
    - Customize sequence templates for client's trade and brand voice
    - Configure timing (respect client's timezone)
    - Test full 14-day sequence on test contact (compressed timeline)
    - Test response handling (interested, not interested, stop)
[ ] System 4 (Review Manager):
    - Connect Google Business Profile (OAuth flow)
    - Test review request SMS and email delivery
    - Test review detection (post a test review)
    - Test AI response generation and posting
    - Configure auto-approve vs manual-approve per client preference
[ ] System 5 (Estimate Closer):
    - Configure CRM estimate status triggers
    - Customize 60-day sequence for client's trade
    - Set discount authority limits
    - Configure financing integration (if applicable)
[ ] System 6 (Cold Outreach):
    - Define target verticals for client's market
    - Build initial prospect list from Apollo (100-200 prospects)
    - Verify all emails via ZeroBounce
    - Write personalized email sequence with Claude
    - (Delay actual sending until domain warmup completes)
[ ] System 7 (Neighborhood Targeting):
    - Configure radius and density settings for client's market
    - Design postcard template with client branding
    - Set up PostGrid account and verify template
    - Create landing page template
[ ] System 8 (Seasonal Campaigns):
    - Load trade-specific campaign templates
    - Configure weather trigger location (lat/lng for client's service area)
    - Customize offer amounts for each campaign
    - Set audience filters based on client's customer base
[ ] System 9 (Dispatcher):
    - Build technician skills matrix in technicians table
    - Configure dispatch rules (who handles what, seniority rules)
    - Test drive time calculation for client's service area
    - Set auto-dispatch confidence threshold
[ ] System 10 (Customer Lifecycle):
    - Set up maintenance schedules by equipment type
    - Configure membership management (if applicable)
    - Set equipment lifecycle milestones
    - Configure win-back campaign timing
[ ] System 11 (Financial Dashboard):
    - Map CRM financial fields to our data model
    - Configure Google Ads and Facebook Ads connections (if applicable)
    - Set daily overhead estimate with client
    - Test daily P&L calculation accuracy
    - Verify dashboard data display

PHASE 4: TESTING (Day 4-5)
================================================================
[ ] Full end-to-end test: inbound call --> booking --> dispatch --> job complete
    --> review request --> financial dashboard update
[ ] Full end-to-end test: web form lead --> speed-to-lead --> follow-up
    sequence --> booking
[ ] SMS delivery test to 3 real phone numbers (mobile, landline, VoIP)
[ ] Email delivery test (check inbox placement, not spam)
[ ] Review request and response flow (real Google review)
[ ] Emergency escalation: simulated emergency call
[ ] Opt-out handling: reply STOP, verify all systems respect it
[ ] Dashboard: verify all metrics populate correctly
[ ] Load test: simulate 10 concurrent calls (Vapi handles this)
[ ] CRM sync: verify data flows both directions accurately
[ ] Error handling: simulate API failures, verify fallbacks activate

PHASE 5: LAUNCH (Day 5-7)
================================================================
[ ] Enable call forwarding from client's main number to AI number
[ ] Activate all webhook receivers (go live on lead sources)
[ ] Enable follow-up sequences (process any pending leads)
[ ] Enable review request automation
[ ] Enable seasonal campaign engine
[ ] Send client: launch confirmation email + dashboard login credentials
[ ] Schedule 48-hour check-in call with client
[ ] Schedule week-1 review call with client
[ ] Internal: add client to monitoring dashboard
[ ] Internal: set up alerts for this client's systems
[ ] Monitor all systems manually for first 72 hours
[ ] Document any client-specific customizations or exceptions
```

---

## Appendix A: API Rate Limits Reference

| Service | Rate Limit | Our Strategy |
|---|---|---|
| Claude API (Anthropic) | Tier-dependent (up to 4,000 RPM at Tier 4) | Queue non-urgent requests; burst for real-time voice conversations |
| Vapi | 100 concurrent calls per account | Monitor concurrency; upgrade tier at 60% sustained utilization |
| Twilio SMS | 1 msg/sec per long code number; 10 msg/sec via Messaging Service | Use Messaging Service with number pool for campaigns |
| Twilio Voice | 1 concurrent call per number | One dedicated number per client; no contention |
| SendGrid | 10,000 emails/day (Pro plan) | Batch campaign sends overnight; transactional emails are priority |
| Google Business Profile API | 60 QPM per project | Queue requests; poll reviews at 30-min intervals per client |
| Facebook Graph API | 200 calls/user-token/hour | Cache responses (15-min TTL); use batch requests |
| Google Maps Geocoding | 50 QPS, 40,000/month | Cache all geocode results in Supabase permanently |
| Google Maps Distance Matrix | 10 elements/sec, 40,000/month | Cache drive times in Redis (4-hour TTL) |
| Apollo.io | 50 QPM (Basic), 100 QPM (Professional) | Batch prospect searches overnight |
| Instantly.ai | 50-200 emails/day per sending account | Respect warmup schedule; never exceed daily limits |
| PostGrid | 1,000 RPM | Batch postcard creation; well within limits |
| OpenWeatherMap | 1,000 calls/day (free) | 6-hourly checks; well within limits |

## Appendix B: Error Handling and Failover Matrix

| System | Failure Mode | Detection | Failover |
|---|---|---|---|
| AI Receptionist | Vapi service down | Health check every 60s | Twilio fallback: route to voicemail with promise callback |
| AI Receptionist | Claude API timeout | Vapi function call timeout (5s) | Vapi scripted fallback: basic booking IVR |
| Speed-to-Lead | n8n webhook down | UptimeRobot HTTP check | Secondary webhook URL on different n8n instance |
| Speed-to-Lead | GBP API unavailable | Polling returns error 3x | Alert internal team; queue retry every 15 min |
| Lead Follow-Up | SMS delivery failure | Twilio status callback (undelivered) | Log error; retry once after 30 min; if carrier error, email-only |
| Lead Follow-Up | Email bounce | SendGrid event webhook (bounce) | Mark contact, remove from email sequences, continue SMS-only |
| Review Manager | GBP review API down | Polling returns error | Increase poll interval; alert if down > 2 hours |
| Estimate Closer | CRM API rate limited | 429 response code | Exponential backoff: 1s, 2s, 4s, 8s, max 60s |
| Cold Outreach | Instantly.ai deliverability drops | Open rate < 20% for 3 days | Pause sending; alert internal team; investigate domain health |
| Neighborhood Targeting | PostGrid API error | HTTP error response | Queue and retry; alert if > 3 failures |
| Dispatcher | Google Maps API down | Timeout or error response | Use cached drive times; fall back to straight-line distance estimate |
| Dispatcher | Claude API slow/down | Response time > 10s | Fall back to rule-based assignment (skill match + proximity) |
| Financial Dashboard | CRM data sync fails | Missing data detected in daily check | Alert internal team; use last known data + "data pending" flag |
| All Systems | Supabase down | Connection refused | Redis cache serves critical data (contacts, active sequences). Supabase 99.9% SLA. |
| All Systems | n8n workflow error | n8n error trigger workflow | Log to system_logs, alert Slack channel, retry if transient |

## Appendix C: Glossary

| Term | Definition |
|---|---|
| CRM | Customer Relationship Management software (ServiceTitan, Housecall Pro, Jobber, GoHighLevel) |
| GBP | Google Business Profile (formerly Google My Business) |
| LSA | Google Local Services Ads |
| ROAS | Return on Ad Spend (revenue / ad spend) |
| CAC | Customer Acquisition Cost |
| LTV | Customer Lifetime Value |
| EDDM | Every Door Direct Mail (USPS program for reaching every address on a mail route) |
| TCPA | Telephone Consumer Protection Act (US law regulating automated calls/texts) |
| RLS | Row Level Security (PostgreSQL feature for data isolation) |
| PITR | Point-in-Time Recovery (database backup restoration to any moment) |
| E.164 | International phone number format (+1XXXXXXXXXX for US) |
| AMD | Answering Machine Detection (Twilio feature) |

---

*End of Technical Systems Specification*
*Document version 2.0 -- March 2026*
*To be updated as systems are built, tested, and refined during implementation.*
