# Tech Stack — Home Services AI System

## Core Infrastructure

| Category | Tool | Purpose | Cost (per client) |
|----------|------|---------|-------------------|
| **AI Voice** | Vapi.ai | AI phone answering + outbound calls | $0.05/min ≈ $25-50/mo |
| **SMS/Voice** | Twilio | Text messages, call routing, notifications | $0.008/text ≈ $10-20/mo |
| **Email** | SendGrid | Transactional + marketing emails | $0-5/mo (shared plan) |
| **Call Tracking** | CallRail | Source tracking, recording, analytics | $15/mo per number |
| **Automation** | n8n (self-hosted) | Workflow orchestration | $5/mo (VPS share) |
| **AI Processing** | Claude API | Content generation, review responses, dispatch logic | $5-15/mo |
| **CRM Integration** | ServiceTitan / HCP / Jobber API | Job management, scheduling, customer data | $0 (API included in their subscription) |
| **Review Monitoring** | Google Business API + custom | Review tracking, response posting | $0 |
| **Geo Services** | Google Maps API | Routing, proximity, address lookup | $2-5/mo |
| **Landing Pages** | Carrd or custom HTML | Campaign-specific booking pages | $0-5/mo |
| **Dashboard** | Custom HTML/JS | Client-facing performance dashboard | $0 (static hosting) |

---

## Hosting Infrastructure

### Option A: Single VPS (For 1-25 clients)
- **Provider:** DigitalOcean / Hetzner / Vultr
- **Spec:** 4 vCPU, 8GB RAM, 160GB SSD
- **Cost:** $48/mo (DigitalOcean) or $12/mo (Hetzner)
- **Runs:** n8n, custom scripts, dashboards, cron jobs
- **Capacity:** 25 clients comfortably

### Option B: Scaled VPS (For 25-100 clients)
- **Setup:** 2-3 VPS instances behind a load balancer
- **Spec:** 4 vCPU, 8GB RAM each
- **Cost:** $96-$144/mo
- **Capacity:** 100 clients

### Option C: Cloud Functions (For 100+ clients)
- **Provider:** AWS Lambda + API Gateway
- **Cost:** Pay-per-execution, ~$200-$500/mo at scale
- **Benefits:** Auto-scaling, no capacity planning
- **When:** Once you've proven the model and need to scale fast

---

## CRM-Specific Integration Details

### ServiceTitan
- **API:** REST API v2
- **Auth:** API key + tenant ID
- **Capabilities:** Create/read/update jobs, customers, invoices, technician schedules
- **Webhooks:** Job status changes, new customer, appointment created
- **Rate limits:** 50 requests/minute
- **Notes:** Most full-featured API. Supports dispatch and equipment tracking.

### Housecall Pro
- **API:** REST API
- **Auth:** OAuth 2.0
- **Capabilities:** Create/read jobs, customers, estimates, invoices
- **Webhooks:** Available for job events
- **Rate limits:** Varies
- **Notes:** Good for small-mid businesses. Simpler than ServiceTitan.

### Jobber
- **API:** GraphQL API
- **Auth:** OAuth 2.0
- **Capabilities:** Clients, jobs, quotes, invoices, scheduling
- **Webhooks:** Available via app marketplace
- **Rate limits:** 500 requests/minute
- **Notes:** GraphQL makes data fetching efficient. Good mid-market option.

### No CRM (Client uses spreadsheets/paper)
- Deploy lightweight CRM via:
  - Google Sheets + n8n (simplest)
  - Airtable (visual, easy for non-technical)
  - GoHighLevel (if they're willing to adopt)
- AI still handles all automation through this lightweight layer

---

## Phone System Integration Options

### Option 1: New Tracking Number (Simplest)
- Provision local Twilio number
- Client puts this number on Google Ads / website
- All calls route through our AI first
- Can forward to their existing number as fallback
- **Best for:** Starting Tier 1 quickly

### Option 2: Call Forwarding
- Client sets up conditional forwarding on their existing number
- "If busy" or "if no answer after 3 rings" → forward to our AI
- **Best for:** Clients who want to keep answering when available

### Option 3: SIP Integration
- Connect our AI directly to their phone system (RingCentral, Vonage, etc.)
- AI answers in parallel with their team
- Most seamless experience
- **Best for:** Tier 3 clients with existing VoIP systems

---

## AI Voice Configuration (Vapi/Bland.ai)

### Voice Selection
- Choose voice that matches trade and region
- Male voice: authoritative, trusted — good for HVAC, electrical
- Female voice: warm, professional — good for general services
- Regional accent matching: slight Southern for FL/TX, neutral for national

### Knowledge Base Per Client
```json
{
  "company_name": "Tampa Bay HVAC Pro",
  "services": [
    {"name": "AC Repair", "price_range": "$150-$800", "urgency": "same-day"},
    {"name": "AC Tune-Up", "price_range": "$79-$129", "urgency": "schedule"},
    {"name": "New AC Install", "price_range": "$4,500-$12,000", "urgency": "estimate"},
    {"name": "Furnace Repair", "price_range": "$150-$600", "urgency": "same-day"},
    {"name": "Duct Cleaning", "price_range": "$300-$600", "urgency": "schedule"}
  ],
  "service_area": "Hillsborough, Pinellas, Pasco counties",
  "hours": "Mon-Fri 8am-6pm, Emergency 24/7",
  "emergency_fee": "$89 after-hours trip charge",
  "financing": "0% for 12 months on systems over $3,000",
  "brands_serviced": ["Carrier", "Trane", "Lennox", "Goodman", "Rheem"],
  "warranty": "2-year labor warranty on all repairs",
  "escalation_number": "+18135551234"
}
```

---

## Monitoring & Alerting

### System Health Monitoring
- n8n workflow execution monitoring (built-in)
- Vapi call quality monitoring (latency, drops, errors)
- Twilio delivery reports (SMS success/failure)
- CRM API connectivity checks (every 15 minutes)

### Client-Facing Dashboard
- Real-time: calls today, leads captured, appointments booked
- Weekly: call volume trend, booking rate, revenue recovered
- Monthly: full ROI report with comparison to pre-system baseline

### Alert Triggers
| Condition | Alert | To |
|-----------|-------|-----|
| AI call failure rate >5% | Slack + SMS | Systems Builder |
| CRM API disconnected | Slack | Systems Builder |
| Zero calls in 24 hours (for active client) | Email | Account Manager |
| Negative review posted | SMS | Client + Account Manager |
| Client churn risk (declining engagement) | Email | Account Manager |

---

## Security & Compliance

### Data Handling
- All customer data stays in the client's CRM — we don't store PII
- Call recordings stored in CallRail (client's account)
- API keys encrypted at rest and in transit
- VPS access via SSH key only, no password auth

### Compliance
- **TCPA:** Consent tracked for all SMS. Opt-out on every message.
- **Recording consent:** State-by-state compliance. Two-party consent states get disclosure.
- **CAN-SPAM:** Unsubscribe link in all emails. Physical address in footer.
- **GDPR:** Not typically applicable (US home services), but data deletion available on request.
- **PCI:** We never handle payment data directly. Stripe/Square handles payment processing.

---

## Tool Costs Summary (Per Client Per Month)

| Tool | Tier 1 | Tier 2 | Tier 3 |
|------|--------|--------|--------|
| Vapi (AI voice) | $25-50 | $25-50 | $35-60 |
| Twilio (SMS/voice) | $10-20 | $15-30 | $20-35 |
| SendGrid (email) | $0-5 | $5-10 | $5-10 |
| CallRail (tracking) | $15 | $15 | $15 |
| Claude API | $5-10 | $10-15 | $15-25 |
| n8n hosting share | $5 | $5 | $5 |
| Google Maps API | $0-2 | $2-5 | $5-10 |
| **Total COGS** | **$60-107** | **$77-130** | **$100-160** |
| **Client pays** | **$497** | **$997** | **$1,997** |
| **Gross margin** | **78-88%** | **87-92%** | **92-95%** |
