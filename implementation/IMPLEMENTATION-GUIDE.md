# Home Services AI Agent System -- Implementation Guide

**Version:** 2.0
**Last Updated:** 2026-03-24
**Purpose:** Step-by-step deployment playbook for setting up AI agent systems for home services clients (HVAC, plumbing, roofing, electrical, garage doors, etc.)

> This guide is designed so that any systems builder on the team can pick up a new client folder and deploy the full stack without guessing. Follow it linearly for new clients. Use the section index for maintenance and troubleshooting.

---

## Table of Contents

1. [Onboarding Checklist](#1-onboarding-checklist)
2. [Tier 1 Deployment (Days 1-7)](#2-tier-1-deployment-days-1-7)
3. [Tier 2 Deployment (Days 8-21)](#3-tier-2-deployment-days-8-21)
4. [Tier 3 Deployment (Days 14-30)](#4-tier-3-deployment-days-14-30)
5. [Tech Stack Setup](#5-tech-stack-setup)
6. [Quality Assurance](#6-quality-assurance)
7. [Client Training](#7-client-training)
8. [Ongoing Operations](#8-ongoing-operations)
9. [Cost Structure Per Client](#9-cost-structure-per-client)
10. [Scaling Playbook](#10-scaling-playbook)

---

## 1. Onboarding Checklist

Complete this checklist BEFORE scheduling the deployment start date. Nothing moves forward until every required item is collected. Use the intake form (Google Form or Notion template) to capture everything in one session -- ideally a 45-minute onboarding call.

### 1.1 Business Information (Required)

| Item | Details to Collect | Notes |
|---|---|---|
| Legal business name | Exactly as registered | Used for invoicing integrations |
| DBA / brand name | What customers see | Used in AI scripts and review responses |
| Primary phone number | Main business line | Will be forwarded or ported |
| Business address | Full street address | For GBP and service area config |
| Service area | List of cities, zip codes, or mile radius | Be specific -- "30-mile radius from 75201" |
| Services offered | Full list with sub-services | E.g., "HVAC: install, repair, maintenance, duct cleaning" |
| Business hours | Mon-Sun with hours | Include after-hours emergency policy |
| License numbers | State contractor license, EPA, etc. | Needed for GBP and compliance |
| Years in business | Number | Used in AI scripts for trust building |
| Owner name(s) | First and last | For escalation and AI Co-Founder briefings |
| Owner direct cell | Phone number | Emergency escalation only |
| Owner email | Email address | For reports and dashboard access |

### 1.2 Tech Access (Required)

| Item | Details to Collect | Action |
|---|---|---|
| CRM login | Username, password, admin access | Request API key immediately |
| CRM type | ServiceTitan / Housecall Pro / Jobber / Other | Determines integration path |
| Google Business Profile | Owner email with GBP access | Request manager-level access for our service account |
| Google Business Profile ID | From GBP dashboard URL | Needed for API calls |
| Website URL | Primary domain | For form integration and SEO audit |
| Website platform | WordPress / Wix / Squarespace / Custom | Determines form embed method |
| Website admin login | CMS credentials | For installing tracking scripts and forms |
| Phone system | Current provider (RingCentral, Grasshopper, landline, cell) | Determines forwarding method |
| Phone system login | Admin credentials | For configuring forwarding |
| Email provider | Gmail / Outlook / Other | For sending domain verification |
| Domain registrar | GoDaddy / Namecheap / Cloudflare / Other | For DNS records (SPF, DKIM, DMARC) |
| Domain registrar login | Admin credentials | For email deliverability setup |
| Existing review platform accounts | Yelp, Angi, HomeAdvisor, Thumbtack | For review monitoring |
| Social media accounts | Facebook, Instagram, Nextdoor | For future outreach integration |

### 1.3 Current Tools Inventory

Run through this with the client to understand what they already use:

**CRM-Specific Questions:**

- **ServiceTitan:** Do you have the API add-on enabled? What is your tenant ID? Do you use their phone integration (ServiceTitan Phones)? Are memberships/maintenance agreements managed in ST?
- **Housecall Pro:** What plan are you on (Basic/Essentials/MAX)? Is online booking enabled? Do you use HCP payments? Are you on their Zapier integration?
- **Jobber:** What plan (Core/Connect/Grow)? Do you use Jobber Payments? Is client hub enabled? Do you have API access (Grow plan required)?
- **Other CRM:** Name it, get login, determine if it has an API or Zapier connection.

**Other Tools:**
- Accounting: QuickBooks Online / Xero / FreshBooks / Wave / None
- Accounting login credentials
- Payment processing: Square / Stripe / CRM-native / Check only
- Marketing: Any existing email tool (Mailchimp, Constant Contact)?
- Scheduling: Any standalone scheduling tool?
- Answering service: Currently using a live answering service? Name and contract terms?
- Fleet tracking: GPS tracking on trucks?

### 1.4 Pricing Information

| Item | Details |
|---|---|
| Service call / dispatch fee | E.g., "$89 diagnostic fee" |
| Common repair price ranges | By service type (e.g., "AC repair: $150-$800") |
| Installation/replacement ranges | By equipment type (e.g., "AC unit install: $4,500-$12,000") |
| Maintenance plan pricing | Monthly/annual cost and what it includes |
| Financing available? | Yes/No, through whom (Synchrony, GreenSky, Wisetack) |
| Warranty terms | Labor warranty, equipment warranty |
| Emergency/after-hours surcharge | Dollar amount or percentage |
| Free estimates offered? | Which services get free estimates? |
| Price match policy | Any guarantee language to use? |
| Promotional offers | Current running specials |

### 1.5 Team Information

For each technician/installer, collect:

| Field | Purpose |
|---|---|
| Full name | Dispatch and scheduling |
| Cell phone number | For dispatch notifications |
| Email address | For schedule notifications |
| Skills/certifications | Skill-based routing (e.g., "EPA 608 Universal, NATE certified") |
| Service types | What jobs can they handle? |
| Typical availability | Regular schedule (e.g., "Mon-Fri 7a-5p") |
| Service area preference | Any geographic preferences or restrictions |
| Apprentice or lead? | Determines job complexity assignment |

Also collect:
- Office manager name, phone, email
- Dispatcher name (if separate from owner), phone, email
- Who approves estimates over $X amount?

### 1.6 Emergency Escalation Protocol

Define the escalation chain clearly:

```
Level 1: AI handles (booking, FAQ, follow-up, reviews)
Level 2: Office manager handles (scheduling conflicts, complaints, complex questions)
Level 3: Owner handles (jobs over $X, legal issues, major complaints, media inquiries)
```

Get from client:
- Dollar threshold for owner escalation (e.g., "any job over $10,000")
- Types of calls that should ALWAYS go to a human immediately
- After-hours emergency protocol (true emergencies like gas leaks, flooding)
- Preferred notification method for escalations (call, text, email)

### 1.7 Brand Voice Notes

Ask the client these questions and document the answers:

- "If your business was a person, how would they talk? Formal or friendly? Country or corporate?"
- "What do your best customers say about you?"
- "What makes you different from the competitor down the street?"
- "Any words or phrases you always use? Any you hate?"
- "Do you have a tagline or motto?"

Document as a Brand Voice Card:

```
Tone: [Friendly and professional / Southern hospitality / No-nonsense expert / etc.]
Personality: [Neighbor you trust / The expert's expert / Family business warmth]
Always say: ["We'll take care of you" / "Your comfort is our priority"]
Never say: ["Cheap" / "We're the best" / competitor names]
Signature phrases: [Client-specific phrases they use in ads or on calls]
```

### 1.8 Onboarding Sign-Off

Before proceeding to deployment:

- [ ] All required business info collected
- [ ] CRM API access confirmed working
- [ ] GBP manager access granted and verified
- [ ] Phone system access confirmed
- [ ] Website admin access confirmed
- [ ] Domain registrar access confirmed (for email DNS)
- [ ] Pricing sheet completed and approved by client
- [ ] Team roster with contact info completed
- [ ] Escalation protocol documented and approved by client
- [ ] Brand voice card completed
- [ ] Client signed service agreement
- [ ] First invoice paid / payment method on file
- [ ] Client added to project management board (ClickUp/Notion)
- [ ] Internal Slack channel created: #client-[businessname]

---

## 2. Tier 1 Deployment (Days 1-7)

Tier 1 is the foundation. It covers the AI Receptionist, phone integration, CRM connection, follow-up sequences, and review management. The client should be live and answering calls via AI by Day 7.

### 2.1 Day-by-Day Deployment Schedule

| Day | Focus | Deliverables |
|---|---|---|
| Day 1 | Infrastructure setup | Accounts created, API keys generated, domains verified, hosting provisioned |
| Day 2 | AI Receptionist build | Voice agent configured, scripts written, call flows mapped |
| Day 3 | Phone system integration | Call forwarding active, tracking numbers provisioned, SIP configured |
| Day 4 | CRM integration | Bidirectional sync working, booking flow tested |
| Day 5 | Follow-up sequences | SMS and email sequences built, triggers connected |
| Day 6 | Review management + GBP | Review monitoring live, GBP optimized, response templates loaded |
| Day 7 | Testing and go-live | 20 test calls, full QA pass, client sign-off, flip the switch |

### 2.2 Day 1: Infrastructure Setup

**Account Creation (allow 2-3 hours):**

1. **Vapi account** (or Bland.ai -- see Tech Stack section for decision criteria)
   - Create account at dashboard.vapi.ai
   - Add payment method
   - Generate API key: Settings > API Keys > Create
   - Note the API key in the client's credential vault (1Password/Bitwarden)
   - Purchase a phone number in the client's area code: Phone Numbers > Buy Number

2. **Twilio account** (for SMS)
   - Create account or use sub-account under master account
   - Verify business identity (A2P 10DLC registration -- this takes 1-3 days, start immediately)
   - Purchase phone number in client's area code for SMS
   - Generate API credentials: Console > Account > API keys > Create API key
   - Note Account SID, Auth Token, and API Key
   - Register messaging service: Messaging > Services > Create
   - Add purchased number to messaging service

3. **SendGrid account** (or ActiveCampaign)
   - Create account or add sender identity under agency account
   - Verify sending domain: Settings > Sender Authentication > Authenticate Domain
   - Add DNS records to client's domain registrar:
     - CNAME record for SendGrid domain verification
     - CNAME record for DKIM
     - TXT record for SPF (merge with existing SPF if present)
   - Create API key: Settings > API Keys > Create with "Mail Send" and "Marketing" permissions
   - Wait for domain verification (usually 15-60 minutes)

4. **n8n instance** (or Make.com)
   - If self-hosted: Create new n8n instance on VPS (see Hosting section)
   - If cloud: Create workspace or add to agency workspace
   - Install required nodes/modules for this client
   - Create environment variables for all API keys

5. **CallRail account** (if using call tracking)
   - Create company under agency account
   - Purchase tracking number(s) in client's area code
   - Configure number pool if using dynamic number insertion on website

6. **Claude API key**
   - Generate from console.anthropic.com
   - Use agency account, tag usage to client for cost tracking
   - Set up usage alerts at $50, $100, $200/month thresholds

7. **Hosting** (if self-hosting n8n or custom endpoints)
   - Provision VPS: Hetzner CX31 (4 vCPU, 8GB RAM) or equivalent
   - Or use Railway/Render for managed hosting
   - Point subdomain: client-slug.youragency.com
   - Install SSL via Let's Encrypt / Caddy
   - Deploy n8n via Docker Compose (see Tech Stack section)

8. **Credential Vault Entry**
   - Create entry in 1Password/Bitwarden vault: "Client - [Business Name]"
   - Store ALL API keys, logins, phone numbers, account IDs
   - Share vault entry with team members who need access

### 2.3 Day 2: AI Receptionist Setup

**Voice Agent Configuration (Vapi):**

Step 1 -- Create the Assistant:
- Dashboard > Assistants > Create Assistant
- Name: "[Client Name] Receptionist"
- Model: Claude 3.5 Sonnet (best balance of quality and speed for voice)
- Temperature: 0.3 (keep it consistent and on-script)
- Max tokens: 300 (voice responses should be concise)

Step 2 -- Voice Selection:
- Go to Voice settings in the assistant config
- Provider recommendation: ElevenLabs or PlayHT
- For HVAC/plumbing: Use a warm, professional male or female voice
- Test 3-4 voices with the client's greeting script
- Client gets final voice approval
- Set voice speed to 1.0x (natural pace, adjust after testing)

Step 3 -- System Prompt (the core script):

```
You are the AI receptionist for [Business Name], a [services] company serving [service area].

YOUR ROLE:
- Answer incoming calls professionally
- Determine the caller's need (service request, estimate, emergency, existing appointment, other)
- Book appointments for service and estimates
- Provide basic pricing information
- Transfer to a human when needed

BUSINESS DETAILS:
- Company: [Business Name]
- Phone: [number]
- Hours: [hours]
- Service area: [cities/zips]
- Services: [full list]

GREETING:
"Thank you for calling [Business Name], this is [AI Name]. How can I help you today?"

CALL FLOW:

1. IDENTIFY NEED:
   Ask what service they need help with. Listen for keywords:
   - Emergency words (gas leak, flooding, no heat in winter, no AC in summer): Flag as EMERGENCY
   - Repair words (broken, not working, leaking, strange noise): Route to SERVICE BOOKING
   - Install/replace words (new unit, upgrade, replacement): Route to ESTIMATE BOOKING
   - Maintenance words (tune-up, check-up, maintenance plan): Route to MAINTENANCE BOOKING
   - Existing appointment (reschedule, cancel, when is my): Route to APPOINTMENT LOOKUP

2. COLLECT INFORMATION (for all service requests):
   - Full name
   - Service address (confirm it's in our service area)
   - Phone number (confirm we have this right)
   - Email address
   - Brief description of the issue
   - Preferred date/time (offer next available)
   - "Is this your home or a rental property?"
   - "How did you hear about us?"

3. PRICING GUIDANCE:
   [Insert pricing card from onboarding]
   - Always frame as ranges: "Our diagnostic fee is $[X], and most [service] repairs run between $[low] and $[high]"
   - For installations: "Every home is different, so we provide free on-site estimates. Typical [equipment] installations range from $[low] to $[high]"
   - NEVER give a firm quote on the phone -- always position as "we'll give you an exact price on-site"

4. EMERGENCY PROTOCOL:
   If the caller describes a genuine emergency:
   - "I understand this is urgent. Let me get our emergency team on this right away."
   - Collect name, address, phone, brief description
   - Transfer to emergency number: [owner/dispatcher cell]
   - If no answer after 30 seconds, send emergency SMS alert and tell caller: "I've sent an urgent alert to our team. Someone will call you back within [X] minutes."

5. TRANSFER TRIGGERS (send to human immediately):
   - Caller explicitly asks for a person/the owner
   - Complaint or angry caller (after one attempt to help)
   - Legal question or threat
   - Insurance claim question
   - Commercial/large project inquiry over $[threshold]
   - Anything you genuinely cannot answer after two attempts

6. CLOSING:
   After booking: "Great, you're all set for [date/time]. You'll receive a confirmation [text/email] shortly. Is there anything else I can help you with?"
   After providing info: "Is there anything else I can help you with today?"
   Always end with: "Thank you for calling [Business Name]. Have a great [day/evening]!"

PERSONALITY:
[Insert brand voice card from onboarding]

RULES:
- Never make up information. If you don't know, say "Let me have someone from our team get back to you on that."
- Never badmouth competitors.
- Never promise specific arrival times unless confirmed in the CRM.
- Always confirm the service address is within our service area before booking.
- Keep responses concise -- this is a phone call, not an essay.
- If the caller is having trouble understanding you, slow down and use shorter sentences.
```

Step 4 -- Function Calls / Tool Use:
Configure the assistant to call your n8n webhooks for:
- `book_appointment` -- Sends booking data to CRM
- `check_availability` -- Queries CRM for open slots
- `lookup_customer` -- Searches CRM by phone number
- `send_emergency_alert` -- Triggers SMS to owner/dispatcher
- `log_call` -- Records call summary to CRM

Step 5 -- Post-Call Actions:
Configure Vapi server URL to point to your n8n webhook:
- On call end, Vapi sends full transcript + extracted data
- n8n workflow processes: create/update CRM record, trigger follow-up sequence, log call summary

### 2.4 Day 3: Phone System Integration

Choose the integration method based on the client's current setup:

**Option A: Call Forwarding (Simplest -- recommended for most clients)**

1. Get a new tracking number from CallRail or Vapi in the client's area code
2. On the client's existing phone system, set up conditional forwarding:
   - All calls forward to the Vapi number
   - If Vapi doesn't answer in 30s, falls back to the client's cell/office
3. Update Google Business Profile with the tracking number as primary
4. Keep the original number as the business's canonical number for existing customers
5. Add the tracking number to the website header and contact page

Setup steps for common phone systems:
- **RingCentral:** Admin > Phone System > Auto-Receptionist > Set forwarding rule
- **Grasshopper:** Settings > Call Forwarding > Add Vapi number as first in sequence
- **Cell phone:** Carrier-specific forwarding (*72 + number on most carriers)
- **Landline:** Call carrier to set up remote call forwarding

**Option B: SIP Trunking (For clients with existing PBX)**

1. Get SIP credentials from Vapi: Phone Numbers > [number] > SIP settings
2. Add Vapi as a SIP trunk on the client's PBX
3. Route inbound calls to Vapi trunk as the first destination
4. Configure failover to existing extensions
5. Test bidirectional audio quality

**Option C: Number Porting (When client wants to keep their number on our system)**

1. Submit port request through Vapi or Twilio
2. Port takes 7-14 business days -- set up forwarding as interim solution
3. Once ported, the client's original number rings directly to Vapi
4. Configure failover to the client's cell

**CallRail Setup (if using):**

1. Create tracking number pool (5 numbers minimum for dynamic insertion)
2. Install CallRail JavaScript snippet on client's website
3. Configure dynamic number insertion (DNI) settings:
   - Source: All web visitors OR specific campaigns
   - Landing page vs. session-based tracking
4. Set call destination to Vapi phone number
5. Enable call recording (with proper disclosure)
6. Configure whisper message: "CallRail tracking. Source: [source]"
7. Set up integrations: CallRail > Integrations > Connect to Google Analytics, Google Ads (if applicable)

**Phone Testing:**
- Call from 3 different phone numbers (landline, cell, VoIP)
- Test during business hours and after hours
- Verify caller ID displays correctly
- Confirm transfer to human works
- Test failover (what happens if Vapi is down)

### 2.5 Day 4: CRM Integration

#### ServiceTitan Integration

**Prerequisites:**
- ServiceTitan API access enabled (requires Enterprise plan or API add-on)
- Tenant ID from client
- API key from ServiceTitan developer portal

**Setup Steps:**

1. Authenticate with ServiceTitan API:
   - Endpoint: `https://api.servicetitan.io/connect/token`
   - Use client_credentials grant type
   - Store access token and refresh token in n8n credentials

2. Build n8n workflows for:

   **Create Booking:**
   ```
   Trigger: Vapi call ends with booking data
   Steps:
   1. Search customer by phone: GET /crm/v2/customers?phone=[number]
   2. If not found: POST /crm/v2/customers (create new)
   3. Get available slots: GET /dispatch/v2/capacity
   4. Create job: POST /jpm/v2/jobs
   5. Create appointment on job: POST /jpm/v2/appointments
   6. Confirm via SMS to customer
   ```

   **Customer Lookup:**
   ```
   Trigger: Vapi function call during live call
   Steps:
   1. GET /crm/v2/customers?phone=[number]
   2. If found: Return name, address, service history summary
   3. Return to Vapi for AI to use in conversation
   ```

   **Update Job Notes:**
   ```
   Trigger: Vapi call ends
   Steps:
   1. Find or create customer
   2. Find active job/booking
   3. PATCH /jpm/v2/jobs/[id] -- add call transcript summary to notes
   ```

3. Map ServiceTitan fields:
   - Business Unit ID (map to service type: HVAC, Plumbing, etc.)
   - Job Type ID (map to: Service Call, Estimate, Maintenance)
   - Campaign ID (map to lead source from CallRail)
   - Tag IDs (for AI-booked, source tracking)

4. Test the full loop:
   - Make a test call
   - Confirm customer created in ServiceTitan
   - Confirm job/appointment shows on dispatch board
   - Confirm notes contain call summary

#### Housecall Pro Integration

**Prerequisites:**
- HCP API access (Essentials or MAX plan)
- OAuth2 credentials from HCP developer portal

**Setup Steps:**

1. OAuth2 setup:
   - Register app in HCP developer portal
   - Get client_id and client_secret
   - Authorization URL: `https://api.housecallpro.com/oauth/authorize`
   - Token URL: `https://api.housecallpro.com/oauth/token`
   - Complete OAuth flow and store refresh token

2. Build n8n workflows for:

   **Create Job:**
   ```
   Trigger: Vapi call ends with booking data
   Steps:
   1. Search customer: GET /customers?phone=[number]
   2. If not found: POST /customers
   3. Create estimate or job: POST /jobs
   4. Schedule: PATCH /jobs/[id]/schedule
   5. Send confirmation
   ```

   **Customer Lookup:**
   ```
   GET /customers?phone=[number]
   Return: name, address, job history count, outstanding balance
   ```

3. HCP-specific notes:
   - HCP uses "jobs" not "appointments" -- a job can have multiple scheduled visits
   - Tags are crucial for tracking AI-booked jobs: add "AI-Booked" tag
   - HCP has built-in SMS -- decide whether to use HCP SMS or Twilio (recommend Twilio for consistency)
   - If client uses HCP Online Booking, make sure AI doesn't double-book

#### Jobber Integration

**Prerequisites:**
- Jobber Grow plan (required for API access)
- GraphQL API access from Jobber developer portal

**Setup Steps:**

1. OAuth2 setup:
   - Register app at developer.getjobber.com
   - Get client_id and client_secret
   - Auth URL: `https://api.getjobber.com/api/oauth/authorize`
   - Token URL: `https://api.getjobber.com/api/oauth/token`

2. Jobber uses GraphQL. Key queries/mutations:

   **Create Client + Request:**
   ```graphql
   mutation {
     clientCreate(input: {
       firstName: "John"
       lastName: "Smith"
       phones: [{ number: "5551234567", primary: true }]
       emails: [{ address: "john@email.com", primary: true }]
       billingAddress: { street1: "123 Main", city: "Dallas", province: "TX", postalCode: "75201" }
     }) {
       client { id }
     }
   }
   ```

   **Create Request (leads/inquiries):**
   ```graphql
   mutation {
     requestCreate(input: {
       clientId: "[id]"
       title: "AC Repair - No cooling"
       details: "Customer reports AC not blowing cold. Unit is 8 years old."
     }) {
       request { id }
     }
   }
   ```

3. Jobber-specific notes:
   - Jobber distinguishes between Requests (leads), Quotes, Jobs, and Invoices
   - AI-booked calls should create Requests that the office converts to Jobs
   - Use Jobber's built-in automation for follow-up if the client prefers

### 2.6 Day 5: Follow-Up Sequence Configuration

**SMS Sequences (via Twilio):**

Build these sequences in n8n with time-delay nodes:

**Sequence 1: Appointment Confirmation**
```
Trigger: Job booked in CRM
Immediately: "Hi [Name], this is [Business]. Your [service] appointment is confirmed for [date] at [time]. Reply YES to confirm or call us at [number] to reschedule."
24 hours before: "Reminder: [Business] will be at [address] tomorrow at [time] for your [service] appointment. Our tech [Tech Name] will call 30 min before arrival."
1 hour before: "Your [Business] tech is on the way! Expected arrival: [time]. Questions? Call [number]."
```

**Sequence 2: Post-Service Follow-Up**
```
Trigger: Job marked complete in CRM
2 hours after: "Hi [Name], thanks for choosing [Business]! How was your experience today? Reply with any feedback -- we'd love to hear from you."
24 hours after: "Happy with your [service]? A quick Google review helps us help more homeowners like you: [review link]. Thank you, [Name]!"
7 days after: (Only if no review left) "Hi [Name], we hope your [equipment] is running great! If you have a minute, we'd really appreciate a Google review: [review link]"
```

**Sequence 3: Estimate Follow-Up (for estimates not yet approved)**
```
Trigger: Estimate created in CRM but not approved
24 hours after: "Hi [Name], this is [Business]. Did you have any questions about the estimate we provided for [service]? We're happy to walk through the options. Call us at [number] or reply here."
72 hours after: "Hi [Name], just checking in on your [service] estimate. We have availability this week if you'd like to move forward. Any questions at all? [number]"
7 days after: "Hi [Name], your estimate for [service] is still available. We're currently offering [seasonal promo if applicable]. Want to schedule? Reply or call [number]."
14 days after: "Hi [Name], just a final note -- we'd love to help with your [service] project. Your estimate is valid for 30 days. Reach us anytime at [number]. - [Business]"
```

**Email Sequences (via SendGrid):**

Build parallel email sequences for each SMS sequence above, but with richer content:

**Post-Service Email (24 hours after job complete):**
```
Subject: How did we do, [Name]?
From: [Business Name] <hello@[domain]>

Body:
- Thank them for their business
- Recap what was done
- Include maintenance tips for their specific service
- CTA: Leave a Google review (button)
- CTA: Refer a friend (link to referral program)
- Footer: Contact info, unsubscribe link
```

**Estimate Follow-Up Email (48 hours after estimate):**
```
Subject: Your [Service] Estimate from [Business Name]
From: [Business Name] <hello@[domain]>

Body:
- Recap the estimate
- Address common concerns (financing available, warranty info)
- Include a testimonial from a similar job
- CTA: Approve estimate (link/button)
- CTA: Schedule a call to discuss (link)
```

**n8n Workflow Architecture for Sequences:**

```
[CRM Webhook] --> [Router: Determine Sequence Type]
  |-> [Appointment Confirmation Branch]
  |     |-> [Send SMS Immediately] -> [Wait 24h] -> [Send Reminder SMS] -> [Wait] -> [Send Day-Of SMS]
  |-> [Post-Service Branch]
  |     |-> [Wait 2h] -> [Send Thank You SMS] -> [Wait 22h] -> [Send Review SMS + Email] -> [Wait 6d] -> [Check Review Status] -> [If No Review: Send Final SMS]
  |-> [Estimate Follow-Up Branch]
        |-> [Wait 24h] -> [Check: Estimate Approved?] -> [If No: Send SMS] -> [Wait 48h] -> [Send Email] -> [Wait 4d] -> [Send SMS] -> [Wait 7d] -> [Send Final SMS]
```

**Important: Compliance**
- All SMS must include opt-out language: "Reply STOP to opt out"
- Handle STOP responses by removing from sequences and flagging in CRM
- Maintain a suppression list in n8n or your SMS platform
- A2P 10DLC registration must be complete before sending (started on Day 1)

### 2.7 Day 6: Review Management + GBP Optimization

**Review Monitoring Setup:**

1. Google Business API:
   - Enable the Google Business Profile API in Google Cloud Console
   - Create service account with Business Profile Manager role
   - Download JSON key file
   - Store in credential vault and n8n

2. Review monitoring n8n workflow:
   ```
   [Scheduled Trigger: Every 30 minutes]
   --> [GET reviews from GBP API, sorted by updateTime desc]
   --> [Filter: New reviews since last check]
   --> [Router: By star rating]
       |-> [5 stars]: Auto-respond with template (rotate through 5-8 templates)
       |-> [4 stars]: Auto-respond with appreciation template
       |-> [3 stars]: Alert team + draft response for manual review
       |-> [1-2 stars]: URGENT alert to owner + draft response + do NOT auto-post
   --> [Log review to tracking sheet/database]
   --> [Update last-check timestamp]
   ```

3. Review response templates (create 5-8 per rating tier):

   **5-Star Template Examples:**
   ```
   "Thank you so much, [Name]! We're thrilled that [tech name] took great care of your [service type]. Your comfort is our top priority. We appreciate you trusting [Business Name]!"

   "[Name], this made our day! Our team works hard to provide the best [service] experience in [city], and it's great to know it shows. Thank you for the kind words!"
   ```

   **Negative Review Draft (for human approval):**
   ```
   "[Name], we're sorry to hear about your experience. This isn't the standard we hold ourselves to. Our owner [Owner Name] would like to speak with you directly -- please call us at [number] at your convenience. We want to make this right."
   ```

4. Review generation triggers:
   - Automatically built into the post-service SMS/email sequence (Day 5)
   - Direct review link format: `https://search.google.com/local/writereview?placeid=[PLACE_ID]`
   - Get Place ID from Google Places API or GBP dashboard

**Google Business Profile Optimization:**

Complete this checklist for every client:

- [ ] Business name matches legal name exactly (no keyword stuffing)
- [ ] Primary category is correct and specific (e.g., "HVAC contractor" not just "Contractor")
- [ ] Add all relevant secondary categories (up to 9)
- [ ] Business description: 750 characters, include service area and key services, natural tone
- [ ] Service area configured with correct cities/zip codes
- [ ] All service types listed with descriptions
- [ ] Business hours accurate (including special hours for holidays)
- [ ] Phone number is the tracking number (from CallRail or Vapi)
- [ ] Website URL is correct
- [ ] Appointment URL configured (if using online booking)
- [ ] Photos: Minimum 10 high-quality photos (team, trucks, completed work, office)
- [ ] Logo uploaded (high resolution, square format)
- [ ] Cover photo uploaded (action shot of team at work)
- [ ] Products/services section filled out with pricing ranges
- [ ] Q&A section: Pre-populate 10-15 common questions with answers (from your own account)
- [ ] Attributes enabled: Women-led, veteran-owned, etc. (if applicable)
- [ ] Messaging enabled (route to AI or office)

**Ongoing GBP Posting Schedule (set up now, automate later in Tier 2):**
- 3 posts per week minimum
- Mix of: seasonal tips, completed job photos, special offers, team spotlights
- Use Google Business API to auto-post from templates

### 2.8 Day 7: Testing Protocol and Go-Live

**Testing Protocol -- 20 Test Calls:**

Make or coordinate 20 test calls covering these scenarios:

| Test # | Scenario | What to Verify |
|---|---|---|
| 1 | Standard AC repair request | Full booking flow, CRM entry created |
| 2 | Plumbing emergency (water leak) | Emergency escalation, owner alerted |
| 3 | New system estimate request | Estimate booking flow, follow-up triggered |
| 4 | Existing customer calling back | Customer lookup works, history referenced |
| 5 | After-hours call | After-hours greeting, next-day callback promised |
| 6 | Caller outside service area | Politely declined, alternative suggested |
| 7 | Caller asking for pricing | Ranges given, not firm quotes |
| 8 | Caller wants to reschedule | Appointment lookup and modification |
| 9 | Angry/upset caller | Empathy shown, human transfer triggered |
| 10 | Caller asks for owner by name | Transfer to owner/office |
| 11 | Spanish-speaking caller | Language handling (transfer or bilingual response) |
| 12 | Maintenance plan inquiry | Plan details, booking for sign-up |
| 13 | Financing question | Financing options explained |
| 14 | Very long/rambling caller | AI stays on track, guides to resolution |
| 15 | Caller with poor cell reception | Audio quality handling |
| 16 | Rapid-fire questions | AI handles multiple topics |
| 17 | Competitor comparison question | Handled without badmouthing |
| 18 | Warranty question | Accurate info provided |
| 19 | Multiple services needed | Both captured and booked |
| 20 | Hang-up/short call | Proper logging, no ghost booking |

For each test call, score on:
- Greeting accuracy (0-5)
- Need identification speed (0-5)
- Information collection completeness (0-5)
- Tone/personality match to brand (0-5)
- CRM entry accuracy (0-5)
- Follow-up triggered correctly (0-5)

**Minimum passing score: 4.0 average across all calls.** If below, fix issues and retest.

**Additional Tests:**

- [ ] Form submission on website creates CRM entry and triggers sequence
- [ ] Review request SMS sends correctly with working review link
- [ ] Review monitoring catches a test review within 30 minutes
- [ ] Review auto-response posts correctly for 4-5 star reviews
- [ ] Negative review triggers alert without auto-posting
- [ ] Estimate follow-up sequence fires correctly with proper timing
- [ ] SMS opt-out (STOP) is handled correctly
- [ ] Call failover works if Vapi is unavailable
- [ ] All emails pass deliverability check (use mail-tester.com, target 9+/10)

**Go-Live Checklist:**

- [ ] All 20 test calls passed with 4.0+ average
- [ ] CRM integration confirmed bidirectional
- [ ] Follow-up sequences tested end-to-end
- [ ] Review management confirmed working
- [ ] GBP optimization complete
- [ ] Client listened to 3+ test call recordings and approved
- [ ] Failover/escalation numbers confirmed working
- [ ] A2P 10DLC registration approved (SMS can send)
- [ ] Email deliverability confirmed (SPF, DKIM, DMARC passing)
- [ ] Monitoring dashboards set up (see QA section)
- [ ] Client signed go-live approval
- [ ] Call forwarding activated to Vapi number
- [ ] Old answering service cancelled (if applicable)
- [ ] Internal team notified: "#client-[name] is LIVE"

---

## 3. Tier 2 Deployment (Days 8-21)

Tier 2 adds proactive revenue generation: cold outreach, estimate follow-up acceleration, neighborhood targeting, seasonal campaigns, and referral programs.

### 3.1 Cold Outreach System (Days 8-10)

**Prospect List Building:**

1. Define ideal customer profile with client:
   - Homeowners (not renters) in service area
   - Home value range (e.g., $200K-$800K)
   - Home age (older homes need more service)
   - HVAC system age (10+ years = replacement candidate)

2. Source prospect data:
   - **Property data providers:** ATTOM Data, PropertyRadar, BatchLeads
   - Pull: Owner name, mailing address, property address, home value, year built, email (if available)
   - Target: 2,000-5,000 prospects per campaign
   - **Local business databases (for commercial):** Apollo.io, ZoomInfo (if client serves commercial)

3. Email verification:
   - Run all emails through ZeroBounce or NeverBounce
   - Remove invalid, catch-all, and disposable addresses
   - Target: 95%+ deliverability rate on the final list
   - Cost: ~$2-5 per 1,000 verifications

4. List segmentation:
   - Segment by: home age, home value, zip code, system age (if available)
   - Create 3-5 segments for personalized messaging

**Email Outreach Sequence Configuration:**

Use a dedicated outreach tool (Instantly.ai or Smartlead) -- NOT SendGrid (to protect transactional email reputation).

1. Warm up sending domains:
   - Purchase 2-3 secondary domains (e.g., [businessname]-hvac.com, [businessname]-services.com)
   - Set up email accounts on each: hello@, info@, team@
   - Configure SPF, DKIM, DMARC on each domain
   - Run warm-up for 14 days (Instantly handles this automatically)
   - Start with 20 emails/day, ramp to 50/day per account

2. Outreach sequence (5-email series over 21 days):

   **Email 1 (Day 0) -- Value Lead:**
   ```
   Subject: Quick question about your [City] home
   Body: Seasonal value offer (e.g., "AC tune-up season is here -- want a $49 check-up before the heat hits?")
   CTA: Reply or book link
   ```

   **Email 2 (Day 3) -- Social Proof:**
   ```
   Subject: Your neighbors in [Neighborhood] trust us
   Body: Reference specific work done in their area, include a review quote
   CTA: Reply or call
   ```

   **Email 3 (Day 7) -- Educational:**
   ```
   Subject: [3 signs your AC won't survive this summer]
   Body: Helpful tips content, position as expert
   CTA: Free diagnostic offer
   ```

   **Email 4 (Day 14) -- Offer:**
   ```
   Subject: Exclusive for [Neighborhood] homeowners
   Body: Time-limited offer (10% off, free add-on service)
   CTA: Book now link, expires in 7 days
   ```

   **Email 5 (Day 21) -- Breakup:**
   ```
   Subject: Last note from [Business Name]
   Body: "Didn't hear back -- no worries. We're here when you need us."
   CTA: Save our number
   ```

3. Reply handling:
   - Route all replies to n8n webhook
   - AI (Claude) classifies reply intent: interested, not interested, unsubscribe, question
   - Interested replies: Create lead in CRM, trigger AI follow-up call or manual callback
   - Unsubscribe: Remove from all lists immediately
   - Questions: AI drafts response, human reviews before sending

### 3.2 Estimate Follow-Up Integration (Days 10-12)

Connect to the client's quoting/estimating workflow to accelerate conversions:

1. **CRM Webhook for Estimate Events:**
   - ServiceTitan: Listen for estimate status changes via webhooks
   - HCP: Poll estimates endpoint every 15 minutes for status changes
   - Jobber: Listen for quote state changes via webhooks

2. **Estimate Follow-Up Automation (n8n):**
   ```
   [Estimate Created] --> [Wait 4 hours] --> [AI reviews estimate details]
   --> [Generate personalized follow-up message]
   --> [Send SMS: "Hi [Name], your estimate for [service] is ready. Total: $[amount]. Questions? I'm here to help."]
   --> [Wait 24h] --> [Check: Approved?]
   --> [If No: Send detailed email with estimate PDF, financing options, FAQ]
   --> [Wait 48h] --> [Check: Approved?]
   --> [If No: AI makes follow-up phone call via Vapi outbound]
   --> [Wait 5d] --> [Check: Approved?]
   --> [If No: Send "price valid for 30 days" reminder + any seasonal discount]
   --> [Wait 7d] --> [Final human outreach -- task assigned to office manager]
   ```

3. **AI Outbound Estimate Follow-Up Call Script:**
   ```
   "Hi, is this [Name]? This is [AI Name] from [Business Name].
   I'm following up on the estimate we provided for [service description].
   I wanted to see if you had any questions about the options we presented.
   [Listen for objections/questions]
   [Handle common objections: price, timing, need to think about it]
   [If interested: Book the job or transfer to office to finalize]
   [If not ready: Offer to send financing info or schedule a callback in a week]"
   ```

### 3.3 Neighborhood Targeting Setup (Days 12-14)

When a technician completes a job, automatically target the surrounding neighborhood:

1. **Geolocation Trigger:**
   - When a job is marked complete in CRM, capture the service address
   - Use Google Geocoding API to get lat/long
   - Query property database for 50-100 nearest homeowners within 0.5-mile radius
   - Filter: homeowners only, not already customers, not recently contacted

2. **Neighborhood Campaign (n8n workflow):**
   ```
   [Job Completed Webhook] --> [Geocode Address] --> [Query Nearby Homeowners]
   --> [Filter: Not Existing Customers] --> [Deduplicate Against Recent Outreach]
   --> [Generate Personalized Mailer/Email]
   --> [Route: Email if available, Direct Mail if not]
   ```

3. **Neighborhood Templates:**

   **Email:**
   ```
   Subject: We just helped your neighbor on [Street Name]!
   Body: "Hi [Name], we just completed a [service type] for a homeowner on
   [Street Name]. Since we're already in your neighborhood, we wanted to offer
   you a complimentary [inspection/tune-up/assessment]. Would this week work?"
   ```

   **Direct Mail Postcard (via Lob API or PostcardMania):**
   ```
   Front: "Your [Street Name] neighbor just got a new [AC/furnace/roof]!"
   Back: Before/after photo (if authorized), special offer, QR code to booking page
   ```

4. **Frequency Capping:**
   - Same address: No more than once per 90 days
   - Same neighborhood: No more than once per 30 days
   - Track all touches in the prospect database

### 3.4 Seasonal Campaign Calendar (Days 14-17)

Pre-load 12 months of seasonal campaigns. The AI handles execution -- you set the calendar once per year and adjust quarterly.

**Campaign Calendar Template:**

| Month | Campaign Theme | Service Focus | Offer | Channel |
|---|---|---|---|---|
| January | "New Year, New Comfort" | Heating system check-ups | Free thermostat with tune-up | Email + SMS to existing |
| February | "Love Your Home" | Indoor air quality | $50 off duct cleaning | Email + cold outreach |
| March | "Spring Into Savings" | AC tune-ups before summer | $49 AC tune-up (reg. $89) | All channels |
| April | "Allergy Season Prep" | Air filtration, duct cleaning | Free air quality test | Email + neighborhood |
| May | "Beat the Heat" | AC repair/replacement prep | Free AC diagnostic | Cold outreach + ads |
| June | "Summer Survival" | Emergency AC repair push | Priority service for members | SMS to existing |
| July | "Cool Savings" | System replacement for aging units | $500 off new system install | Email + outbound calls |
| August | "Back to School Comfort" | Maintenance agreements | First month free on maint. plan | All channels |
| September | "Fall Furnace Prep" | Heating tune-ups | $49 furnace tune-up | Email + SMS |
| October | "Winterize Your Home" | Full system inspection | Bundled HVAC + plumbing check | Cold outreach |
| November | "Holiday Comfort" | Emergency service availability | Extended warranty promo | Email to existing |
| December | "Year-End Deals" | System replacement | Financing at 0% for 12 months | All channels |

**Setup in n8n:**

1. Create a "Campaign Scheduler" workflow:
   - Scheduled trigger fires on the 1st of each month
   - Reads campaign details from a Google Sheet or Airtable
   - Generates email/SMS content using Claude API with campaign theme and offer
   - Queues the campaign in the appropriate channel (email, SMS, outbound calls)

2. For each campaign, pre-create:
   - Email template (HTML in SendGrid)
   - SMS template (in n8n)
   - Landing page or offer page on client's website (if applicable)
   - Tracking UTMs for attribution

3. Campaign performance tracking:
   - Emails sent, opened, clicked
   - SMS sent, responses
   - Bookings attributed to campaign
   - Revenue generated
   - All logged to reporting dashboard

### 3.5 Referral Program Deployment (Days 17-21)

1. **Define Referral Terms with Client:**
   - Reward for referrer: $50 credit, gift card, or account credit
   - Reward for new customer: $25 off first service
   - Minimum job value to qualify (e.g., $200+)
   - Double-sided or single-sided rewards

2. **Referral Tracking System:**
   - Generate unique referral codes per customer: [CUSTOMER_INITIALS]-[4_DIGITS]
   - Create referral landing page: [domain]/refer or [domain]/friends
   - Track: referrer, referee, code used, job booked, job completed, rewards issued

3. **Automated Referral Workflows (n8n):**

   **After every completed job (via CRM webhook):**
   ```
   [Job Complete] --> [Wait 3 days]
   --> [Send Referral SMS: "Thanks again, [Name]! Know someone who needs [service]?
       Share your personal code [CODE] and you'll both get a reward. Details: [link]"]
   --> [Send Referral Email with shareable link and code]
   ```

   **When a referral code is used:**
   ```
   [New booking with referral code] --> [Validate code]
   --> [Tag new customer as "Referral" in CRM]
   --> [Send SMS to referrer: "Great news! [Friend Name] just booked with us using your code.
       Your $50 reward will be applied to your next service!"]
   --> [Create credit in CRM or accounting system]
   ```

4. **Referral Program Materials:**
   - Referral card (PDF for tech to leave behind): code + instructions
   - Email template with shareable link
   - Social media post template for customers to share

---

## 4. Tier 3 Deployment (Days 14-30)

Tier 3 adds operational intelligence: AI dispatch, invoicing automation, customer lifecycle management, financial dashboards, and the AI Co-Founder briefing.

### 4.1 AI Dispatcher Configuration (Days 14-18)

The AI Dispatcher assigns the right technician to the right job based on skills, location, and availability.

**Technician Profile Setup:**

For each tech, create a profile in your dispatch database (Airtable, Supabase, or CRM tags):

```json
{
  "tech_id": "tech_001",
  "name": "Mike Johnson",
  "phone": "+15551234567",
  "skills": ["hvac_install", "hvac_repair", "hvac_maintenance", "epa_608", "nate_certified"],
  "max_skill_level": "senior",
  "service_types": ["residential_hvac", "light_commercial_hvac"],
  "home_zip": "75201",
  "preferred_zones": ["zone_north", "zone_central"],
  "max_daily_jobs": 5,
  "availability": {
    "monday": {"start": "07:00", "end": "17:00"},
    "tuesday": {"start": "07:00", "end": "17:00"},
    "wednesday": {"start": "07:00", "end": "17:00"},
    "thursday": {"start": "07:00", "end": "17:00"},
    "friday": {"start": "07:00", "end": "16:00"},
    "saturday": "off",
    "sunday": "on_call"
  },
  "current_location_zip": null,
  "truck_stocked_for": ["residential_ac", "residential_furnace"],
  "notes": "Prefers north side. Good with elderly customers. Spanish-speaking."
}
```

**Service Area Zone Mapping:**

1. Divide the client's service area into zones:
   - Zone definitions: Group zip codes into 4-8 logical zones by geography
   - Consider: Highway access, tech home locations, traffic patterns
   - Example: Zone North (75201-75210), Zone South (75211-75220), etc.

2. Assign zone preferences to each tech

3. Create travel time matrix:
   - Use Google Distance Matrix API
   - Pre-calculate typical travel times between zone centers
   - Cache results (recalculate monthly)

**AI Dispatch Logic (n8n workflow):**

```
[New Job Needs Assignment]
--> [Get job details: service type, skill required, address, urgency, time preference]
--> [Geocode job address, determine zone]
--> [Query available techs for that date/time]
--> [Filter by: skill match, zone preference, availability]
--> [Score remaining candidates:]
      - Skill match: +10 if primary skill, +5 if secondary
      - Zone match: +10 if preferred zone, +5 if adjacent, +0 if other
      - Current location proximity: +10 if same zone today, +5 if adjacent
      - Workload: +10 if under daily max, -10 if at max
      - Customer preference: +5 if returning tech for existing customer
--> [Assign highest-scoring tech]
--> [Send assignment notification via SMS]
--> [Update CRM dispatch board]
--> [If no tech available: Alert office manager for manual assignment]
```

**Dispatch Notification to Tech (SMS):**
```
"New job assigned:
[Customer Name] - [Service Type]
[Address]
[Date] at [Time Window]
Issue: [Brief description]
Notes: [Any special notes]
Reply OK to confirm or ISSUE to flag a problem."
```

### 4.2 Invoicing Automation (Days 18-20)

**QuickBooks Online Integration:**

1. Connect via OAuth2:
   - Register app at developer.intuit.com
   - Get client_id, client_secret
   - Complete OAuth flow, store refresh token
   - API base: `https://quickbooks.api.intuit.com/v3/company/[realmId]`

2. n8n workflow -- Auto-Invoice on Job Completion:
   ```
   [CRM: Job Marked Complete with total]
   --> [Check: Customer exists in QBO?]
   --> [If not: POST /customer (create)]
   --> [POST /invoice: Create invoice with line items from job]
   --> [POST /invoice/[id]/send: Email invoice to customer]
   --> [Update CRM: Mark invoice sent, link invoice ID]
   ```

3. Line item mapping:
   - Map CRM job types/services to QBO items
   - Include labor, materials, and service fees as separate line items
   - Apply tax rates based on service address jurisdiction

4. Payment tracking:
   ```
   [Scheduled: Every 2 hours]
   --> [GET payments created since last check]
   --> [For each payment: Update CRM job status to "Paid"]
   --> [Trigger thank-you SMS/email]
   ```

**Xero Integration (if client uses Xero instead):**

1. Connect via OAuth2 at developer.xero.com
2. Similar workflow structure, using Xero API endpoints:
   - POST /Invoices to create
   - POST /Invoices/[id]/Email to send
   - GET /Payments to track payments

### 4.3 Customer Lifecycle System (Days 20-24)

**Maintenance Agreement Tracking:**

1. Create maintenance agreement database (Airtable/Supabase):
   ```
   Fields:
   - customer_id (linked to CRM)
   - plan_type (basic/premium/ultimate)
   - start_date
   - renewal_date
   - monthly_rate
   - visits_included (e.g., 2 per year)
   - visits_completed_this_year
   - next_visit_due
   - equipment_covered (array of equipment IDs)
   - auto_renew (boolean)
   - payment_method
   - status (active/expired/cancelled)
   ```

2. Maintenance reminder workflows:

   **Visit Due Reminder (n8n):**
   ```
   [Daily trigger at 8 AM]
   --> [Query: Agreements where next_visit_due is within 30 days]
   --> [For each: Send SMS/email to schedule]
   --> [If no response in 7 days: AI outbound call to schedule]
   --> [If no response in 14 days: Alert office manager]
   ```

   **Renewal Reminder (n8n):**
   ```
   [Daily trigger at 8 AM]
   --> [Query: Agreements where renewal_date is within 60 days AND auto_renew = false]
   --> [60 days out: Send renewal email with plan comparison]
   --> [30 days out: Send SMS reminder + call from AI]
   --> [14 days out: Office manager personal call]
   --> [7 days out: Final email with "renew before [date] to keep your rate"]
   ```

**Equipment Lifecycle Tracking:**

1. For each serviced piece of equipment, track:
   - Equipment type and model
   - Installation date / estimated age
   - Last service date
   - Service history (all jobs on this equipment)
   - Estimated remaining life
   - Replacement recommendation threshold

2. Replacement opportunity workflow:
   ```
   [Quarterly trigger]
   --> [Query: Equipment older than 10 years (HVAC) / 15 years (water heater) / etc.]
   --> [Cross-reference: Has customer been contacted about replacement in last 6 months?]
   --> [If not: Generate personalized replacement outreach]
   --> [Send educational email about efficiency gains, rebates, financing]
   --> [Track: Opens, clicks, responses, conversions]
   ```

### 4.4 Financial Dashboard Build (Days 24-27)

**Data Sources:**

Connect these data sources into a unified dashboard (Google Looker Studio, Metabase, or custom):

| Data Source | Metrics Pulled | Update Frequency |
|---|---|---|
| CRM | Jobs booked, completed, revenue, avg ticket | Real-time via webhook |
| Phone system (CallRail/Vapi) | Calls received, answered, booked, missed | Daily sync |
| Email platform (SendGrid) | Emails sent, opened, clicked, replied | Daily sync |
| SMS platform (Twilio) | SMS sent, delivered, responses | Daily sync |
| Review platforms (Google) | New reviews, avg rating, response time | Every 30 min |
| Accounting (QBO/Xero) | Revenue, invoiced, collected, outstanding | Daily sync |
| Outreach (Instantly) | Emails sent, opens, replies, meetings | Daily sync |

**KPI Dashboard Sections:**

1. **Revenue Overview:**
   - Total revenue (MTD, QTD, YTD)
   - Revenue vs. last month, vs. same month last year
   - Average ticket size
   - Revenue by service type
   - Revenue by lead source

2. **Lead Flow:**
   - Total inbound calls
   - Calls answered by AI vs. missed
   - Call-to-booking conversion rate
   - Bookings by source (phone, web, referral, outreach)
   - Estimates generated vs. approved (close rate)

3. **Customer Health:**
   - New customers this month
   - Repeat customers this month
   - Active maintenance agreements
   - Customer retention rate
   - Net Promoter Score (from post-service surveys)

4. **Marketing Performance:**
   - Cost per lead by channel
   - Email campaign performance
   - SMS campaign performance
   - Review generation rate
   - Google Business Profile views and actions

5. **Operational Efficiency:**
   - Average response time (call to booking)
   - Estimate follow-up conversion rate
   - Technician utilization rate
   - Jobs per tech per day
   - Revenue per tech per day

**Dashboard Build Steps:**

1. Create a central database (Supabase or PostgreSQL) as the data warehouse
2. Build n8n ETL workflows that sync data from each source to the warehouse
3. Connect Looker Studio (free) or Metabase (self-hosted free) to the warehouse
4. Build dashboard pages for each KPI section above
5. Set up automated email delivery: Weekly summary every Monday at 7 AM
6. Set up alerts: Revenue drops >20% WoW, review rating drops below 4.5, missed call rate >15%

### 4.5 AI Co-Founder Briefing (Days 27-30)

The AI Co-Founder briefing is a weekly or daily AI-generated executive summary that tells the business owner exactly what they need to know.

**Daily Briefing (SMS, sent at 7 AM):**
```
"Good morning, [Owner Name]. Here's your [Business Name] snapshot:
Yesterday: [X] calls, [Y] booked, $[Z] revenue
This week so far: $[total] revenue ([+/-X%] vs last week)
Action needed: [1-2 items requiring attention]
Great news: [1 positive highlight]"
```

**Weekly Briefing (Email, sent Monday at 7 AM):**
```
Subject: [Business Name] Weekly Briefing - Week of [Date]

EXECUTIVE SUMMARY:
[2-3 sentence AI-generated overview of the week]

BY THE NUMBERS:
- Revenue: $[X] (vs $[Y] last week, [+/-Z%])
- Jobs completed: [X]
- New customers: [X]
- Avg ticket: $[X]
- Close rate (estimates): [X%]
- Reviews received: [X] (avg [X.X] stars)

WINS:
- [Specific positive example]
- [Specific positive example]

NEEDS ATTENTION:
- [Specific issue with recommended action]
- [Specific issue with recommended action]

OPPORTUNITIES:
- [AI-identified opportunity]
- [AI-identified opportunity]

NEXT WEEK PREVIEW:
- [X] jobs scheduled
- [Campaign name] launching on [date]
- [Any seasonal notes]
```

**n8n Workflow for Briefing Generation:**
```
[Scheduled trigger: Daily 6:30 AM / Weekly Monday 6:30 AM]
--> [Query all data sources for relevant period]
--> [Compile raw data into structured JSON]
--> [Send to Claude API with briefing prompt template]
--> [Claude generates natural-language briefing]
--> [Daily: Send via Twilio SMS to owner]
--> [Weekly: Send via SendGrid email to owner + office manager]
```

---

## 5. Tech Stack Setup

Detailed setup instructions for each tool in the stack.

### 5.1 Vapi (AI Phone Agent)

**When to choose Vapi:** Best for most clients. Superior voice quality, better function-calling support, more customizable.

**Setup:**

1. Create account: dashboard.vapi.ai
2. Billing: Add payment method, set budget limits
3. Phone number:
   - Dashboard > Phone Numbers > Buy Number
   - Select area code matching client
   - Cost: ~$2/month per number
4. Create assistant (see Day 2 detailed instructions above)
5. Configure server URL for webhooks:
   - Settings > Server URL: `https://n8n.yourdomain.com/webhook/vapi-[client-slug]`
   - Events to receive: call.ended, call.phone-call-control, function-call
6. Test: Make test call to purchased number

**Vapi Pricing Model:**
- Per-minute pricing: ~$0.05-0.15/min depending on voice provider and LLM
- Typical client: 200-400 minutes/month = $10-60/month

### 5.2 Bland.ai (AI Phone Agent -- Alternative)

**When to choose Bland:** Budget-sensitive clients, simpler call flows, or when you need enterprise batch calling.

**Setup:**

1. Create account: app.bland.ai
2. Get API key: Settings > API Keys
3. Create a "Pathway" (Bland's visual call flow builder):
   - Build the call flow as a decision tree
   - Each node = a prompt/response pair
   - Connect nodes with conditions
4. Phone number: Request via API or dashboard
5. Configure webhook for call results:
   - POST to your n8n endpoint with call transcript and extracted data

### 5.3 Twilio (SMS and Voice Infrastructure)

**Setup:**

1. Create account: twilio.com/try-twilio
2. Upgrade from trial (required for production)
3. A2P 10DLC registration (CRITICAL -- do this Day 1):
   - Console > Messaging > Compliance > Registrations
   - Register your agency as the ISV
   - Register each client as a Brand
   - Register Campaign: Use case = "Customer Care" + "Marketing"
   - Approval takes 1-5 business days
   - Without this, SMS will be blocked or heavily filtered

4. Phone number purchase:
   - Console > Phone Numbers > Buy a Number
   - Select area code, enable SMS capability
   - Cost: $1.15/month per number

5. Messaging Service:
   - Console > Messaging > Services > Create
   - Add purchased number(s) to service
   - Enable sticky sender (same number for same customer)
   - Configure opt-out handling: Enabled (automatic STOP processing)

6. Webhook configuration for inbound SMS:
   - Phone Number > Configure > Messaging webhook
   - URL: `https://n8n.yourdomain.com/webhook/twilio-inbound-[client-slug]`

**Twilio Pricing:**
- SMS: $0.0079 per outbound segment, $0.0075 per inbound
- Typical client: 500-1,500 SMS/month = $4-12/month

### 5.4 SendGrid (Transactional and Marketing Email)

**Setup:**

1. Create account or sub-user under agency account
2. Domain authentication (CRITICAL for deliverability):
   - Settings > Sender Authentication > Authenticate Domain
   - Add provided DNS records to client's domain:
     - 3 CNAME records for SendGrid authentication
     - Update existing SPF TXT record to include SendGrid
   - Verify domain (may take up to 48 hours, usually 15 minutes)

3. Create API key:
   - Settings > API Keys > Create API Key
   - Permissions: Mail Send (full), Marketing (full), Stats (read)

4. Email templates:
   - Create templates for each sequence (appointment confirmation, review request, estimate follow-up, etc.)
   - Use SendGrid Dynamic Templates with Handlebars variables
   - Design responsive HTML templates or use their drag-and-drop editor
   - All templates must include: unsubscribe link, physical mailing address, brand logo

5. Suppression management:
   - Configure suppression groups for different email types
   - Global unsubscribes, bounces, and spam reports are handled automatically

**SendGrid Pricing:**
- Free tier: 100 emails/day (not enough for production)
- Essentials: $19.95/month for 50,000 emails
- Typical client: 1,000-3,000 emails/month = well within Essentials plan

### 5.5 n8n (Automation Orchestration)

**Self-Hosted Setup (Recommended for cost control):**

1. Provision VPS:
   - Hetzner CX31: 4 vCPU, 8GB RAM, 80GB disk -- approximately $9/month
   - Or DigitalOcean: $24/month for similar specs
   - Or Railway: Pay-per-use, starts ~$5/month

2. Install via Docker Compose:

   ```yaml
   # docker-compose.yml
   version: '3.8'
   services:
     n8n:
       image: n8nio/n8n:latest
       restart: always
       ports:
         - "5678:5678"
       environment:
         - N8N_HOST=n8n.yourdomain.com
         - N8N_PORT=5678
         - N8N_PROTOCOL=https
         - WEBHOOK_URL=https://n8n.yourdomain.com/
         - N8N_ENCRYPTION_KEY=${N8N_ENCRYPTION_KEY}
         - DB_TYPE=postgresdb
         - DB_POSTGRESDB_HOST=postgres
         - DB_POSTGRESDB_DATABASE=n8n
         - DB_POSTGRESDB_USER=n8n
         - DB_POSTGRESDB_PASSWORD=${POSTGRES_PASSWORD}
       volumes:
         - n8n_data:/home/node/.n8n
       depends_on:
         - postgres

     postgres:
       image: postgres:15
       restart: always
       environment:
         - POSTGRES_DB=n8n
         - POSTGRES_USER=n8n
         - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
       volumes:
         - postgres_data:/var/lib/postgresql/data

     caddy:
       image: caddy:2
       restart: always
       ports:
         - "80:80"
         - "443:443"
       volumes:
         - ./Caddyfile:/etc/caddy/Caddyfile
         - caddy_data:/data

   volumes:
     n8n_data:
     postgres_data:
     caddy_data:
   ```

   Caddyfile:
   ```
   n8n.yourdomain.com {
     reverse_proxy n8n:5678
   }
   ```

3. Deploy:
   ```bash
   export N8N_ENCRYPTION_KEY=$(openssl rand -hex 32)
   export POSTGRES_PASSWORD=$(openssl rand -hex 16)
   docker compose up -d
   ```

4. Create admin account at https://n8n.yourdomain.com
5. Install community nodes as needed

**Workflow Organization:**

Create one folder per client, with these standard workflows:
- `[Client] - AI Receptionist Handler` (processes Vapi call data)
- `[Client] - Appointment Sequence` (confirmation + reminders)
- `[Client] - Post-Service Sequence` (follow-up + review request)
- `[Client] - Estimate Follow-Up` (multi-step estimate conversion)
- `[Client] - Review Monitor` (check + respond to reviews)
- `[Client] - CRM Sync` (bidirectional data sync)
- `[Client] - Outbound Campaigns` (seasonal + neighborhood)
- `[Client] - Dispatch Logic` (tech assignment -- Tier 3)
- `[Client] - Invoice Automation` (billing -- Tier 3)
- `[Client] - Briefing Generator` (daily/weekly reports -- Tier 3)

### 5.6 CallRail (Call Tracking)

**Setup:**

1. Create company under agency account
2. Purchase tracking numbers:
   - Source Tracking: 1 number per marketing source (Google Ads, website, direct mail)
   - Dynamic Number Insertion: Pool of 5-10 numbers for website visitor tracking
3. Install JavaScript on client's website:
   ```html
   <script src="//cdn.callrail.com/companies/[COMPANY_ID]/[hash]/swap.js"></script>
   ```
4. Configure call destinations: Route to Vapi phone number
5. Configure integrations:
   - Google Analytics 4
   - Google Ads (if running PPC)
   - CRM (if CallRail has direct integration)
6. Set up call scoring: Enable CallRail's AI call scoring for automatic lead qualification

**CallRail Pricing:**
- Essentials: $45/month (10 local numbers, 250 minutes)
- Typical client needs: $45-$95/month

### 5.7 Google Business API

**Setup:**

1. Google Cloud Console:
   - Create project: `[agency-name]-gbp`
   - Enable APIs: Google Business Profile API, Places API
   - Create service account: IAM > Service Accounts > Create
   - Download JSON key
   - Grant service account access to client's GBP (Manager role)

2. API endpoints used:
   - Reviews: GET reviews from location
   - Review replies: POST reply to specific review
   - Posts: POST local post to location
   - Insights: GET report insights for location

3. Rate limits: 60 requests per minute per project -- sufficient for monitoring

### 5.8 CRM APIs

See Day 4 section for detailed CRM integration instructions. Summary:

| CRM | Auth Method | API Style | Key Consideration |
|---|---|---|---|
| ServiceTitan | Client Credentials | REST | Requires API add-on (~$50/month) |
| Housecall Pro | OAuth2 | REST | Rate limits: 100 requests/min |
| Jobber | OAuth2 | GraphQL | Requires Grow plan for API access |

### 5.9 Claude API (AI Processing)

**Setup:**

1. Organization account at console.anthropic.com
2. Create API key per client (for cost tracking) or use one key with metadata tagging
3. Model selection:
   - Voice agent (real-time): Claude 3.5 Sonnet (fast, cost-effective)
   - Content generation (emails, follow-ups): Claude 3.5 Sonnet
   - Complex analysis (briefings, dispatch optimization): Claude Sonnet 4
4. Usage monitoring:
   - Set up billing alerts at console.anthropic.com
   - Track usage per client via API metadata or separate keys
   - Typical usage: $15-50/month per client

### 5.10 Hosting

**Recommended Architecture:**

```
[Hetzner VPS - ~$9/month]
  Docker containers:
    - n8n (automation engine)
    - PostgreSQL (n8n database)
    - Caddy (reverse proxy + SSL)
    - Supabase (optional: client data warehouse)
  Domain: n8n.youragency.com
  SSL: Auto via Caddy/Let's Encrypt
```

**Scaling Path:**
- 1-10 clients: Single VPS (CX31)
- 10-30 clients: Upgrade to CX41 (8 vCPU, 16GB) or split across 2 VPS
- 30+ clients: Move to managed n8n cloud ($50/month) or Kubernetes cluster

**Backup Strategy:**
- Daily PostgreSQL backup to S3/B2 (via cron + pg_dump)
- n8n workflow export: Weekly via API
- Credential vault: Separate backup system (1Password handles this)

---

## 6. Quality Assurance

### 6.1 Testing Checklist per Component

**AI Receptionist:**
- [ ] Greeting matches brand voice
- [ ] Call routing logic works for all service types
- [ ] Emergency escalation triggers correctly
- [ ] Customer lookup returns correct data
- [ ] Booking creates CRM entry with all fields
- [ ] Post-call summary is accurate
- [ ] Transfer to human works within 15 seconds
- [ ] After-hours handling is correct
- [ ] Out-of-service-area calls handled gracefully
- [ ] Latency is under 1.5 seconds per response

**Phone System:**
- [ ] Inbound calls ring to Vapi within 2 rings
- [ ] Caller ID displays correctly to the AI
- [ ] Call recording is working and compliant (disclosure played)
- [ ] Failover to human works when Vapi is down
- [ ] CallRail attribution is tracking sources correctly
- [ ] Transfer to human preserves caller context

**CRM Integration:**
- [ ] New customer created with all fields populated
- [ ] Existing customer matched by phone number
- [ ] Job/booking appears on dispatch board
- [ ] Job notes contain call summary
- [ ] Lead source is tagged correctly
- [ ] No duplicate customers created

**Follow-Up Sequences:**
- [ ] SMS sends within expected timeframe
- [ ] Email sends within expected timeframe
- [ ] SMS content is personalized correctly
- [ ] Email content is personalized correctly
- [ ] Links in SMS/email work correctly
- [ ] Opt-out (STOP) removes from sequences
- [ ] Sequences stop when condition is met (e.g., appointment confirmed)

**Review Management:**
- [ ] New reviews detected within 30 minutes
- [ ] 5-star auto-response posts within 1 hour
- [ ] 4-star auto-response posts within 1 hour
- [ ] 3-star and below triggers alert without auto-posting
- [ ] Response templates rotate (not the same every time)
- [ ] Review request SMS contains working Google review link

### 6.2 Call Quality Scoring Rubric

Score each call 1-5 on each dimension:

| Dimension | 1 (Poor) | 3 (Acceptable) | 5 (Excellent) |
|---|---|---|---|
| **Greeting** | Wrong business name, robotic | Correct but flat | Warm, branded, natural |
| **Need ID** | Took 3+ attempts | Got it in 2 attempts | Got it in first exchange |
| **Information Gathering** | Missed 3+ fields | Missed 1-2 fields | All fields captured |
| **Tone** | Off-brand, awkward | Neutral, professional | Matches brand voice perfectly |
| **Accuracy** | Wrong info given | Correct but vague | Correct and specific |
| **Efficiency** | Call over 5 min for simple booking | 3-4 minutes | Under 3 minutes |
| **CRM Entry** | Missing/wrong data | Most fields correct | All fields accurate |
| **Follow-Up** | Not triggered | Triggered but delayed | Triggered instantly |

**Scoring:**
- 35-40: Excellent -- no changes needed
- 28-34: Good -- minor tweaks to prompts
- 20-27: Needs work -- revise scripts and test again
- Below 20: Major issues -- rebuild the call flow

### 6.3 First-Week Monitoring Protocol

**Day 1 (Go-Live Day):**
- Monitor ALL calls in real-time for the first 4 hours
- Listen to every call recording within 2 hours of the call
- Fix any issues immediately
- Check CRM entries match call data
- Verify sequences are firing

**Days 2-3:**
- Listen to every call recording within 4 hours
- Compile daily report: calls handled, bookings made, issues found
- Make prompt/script adjustments based on real calls
- Check sequence timing and content

**Days 4-5:**
- Listen to a sample of 50% of calls
- Focus on any calls that resulted in transfers or abandoned bookings
- Check review response accuracy
- Verify estimate follow-up sequence

**Days 6-7:**
- Listen to a sample of 25% of calls
- Compile first-week report with:
  - Total calls: [X]
  - AI-handled successfully: [X] ([X%])
  - Transferred to human: [X] ([X%])
  - Bookings made: [X]
  - Issues found and fixed: [list]
  - Prompt changes made: [list]
  - Client satisfaction notes
- Share report with client

### 6.4 Common Issues and Fixes

| Issue | Likely Cause | Fix |
|---|---|---|
| AI says "I don't know" too often | System prompt missing information | Add the missing info to the knowledge base in the prompt |
| Calls feel robotic | Temperature too low, voice speed wrong | Increase temp to 0.4, adjust voice speed, add personality directives |
| Wrong service area responses | Zip code list incomplete | Update service area definition with ALL zip codes |
| CRM entries missing data | n8n workflow not extracting all fields | Add extraction steps, validate data before CRM write |
| SMS not sending | A2P registration not approved, or number not in messaging service | Check Twilio console for errors, verify 10DLC status |
| Emails going to spam | DNS records misconfigured | Run mail-tester.com, fix SPF/DKIM/DMARC |
| Calls dropping/silence | Voice provider latency | Switch voice provider in Vapi, check server health |
| Double bookings | Race condition in availability check | Add mutex/lock logic to booking workflow |
| Review responses wrong tone | Template not matching brand | Revise templates with client, increase template variety |
| Estimate follow-up fires after approval | CRM status update delayed | Add a status check before each follow-up step |

---

## 7. Client Training

The entire point of this system is that the client should barely touch anything. Training should be minimal and focused on "how to read your results" rather than "how to operate the system."

### 7.1 What the Client Needs to Know

**Essential knowledge (15-minute briefing):**

1. "Your AI receptionist is live. It answers your calls, books appointments, and follows up with customers automatically."
2. "You'll get a daily text summary and a weekly email report."
3. "If the AI can't handle something, it will call/text you or your office manager."
4. "Your reviews are being monitored. Positive reviews get auto-responses. Negative reviews get flagged for your approval before we respond."
5. "If you need anything changed, message us in Slack or email [support@youragency.com]."

**What they should NOT do:**
- Do not change phone forwarding settings
- Do not modify CRM automation rules
- Do not respond to reviews that the AI has already responded to
- Do not change GBP settings without notifying us

### 7.2 Dashboard Walkthrough

Record a 15-minute Loom video personalized for each client:

**Script outline:**

```
[0:00-2:00] "Hi [Name], this is a quick walkthrough of your dashboard."
[2:00-5:00] Revenue section: "Here's your revenue overview. This shows [current numbers]."
[5:00-8:00] Lead flow: "Here's where your leads are coming from and how they convert."
[8:00-11:00] Reviews: "Here's your review performance. You can see the latest reviews here."
[11:00-13:00] Marketing: "Here's how your campaigns are performing."
[13:00-15:00] "Any questions, reach out to us at [contact]. We'll also walk through this together on our monthly call."
```

Send the video link via email with the dashboard login credentials.

### 7.3 Monthly Report Reading Guide

Include this one-pager with every monthly report:

```
HOW TO READ YOUR MONTHLY REPORT

REVENUE: This is your total billed revenue for the month. Compare to last month
and last year. A healthy business grows 10-20% year over year.

NEW CUSTOMERS: How many first-time customers you served. This shows if your
marketing is working.

REPEAT RATE: What percentage of your customers have used you before. Target: 40%+.
This means customers trust you enough to come back.

AVERAGE TICKET: How much the average job costs. If this is declining, we may need
to adjust your pricing or upsell strategy.

REVIEW SCORE: Your average Google rating. Anything above 4.7 is excellent.
Below 4.5, we need to address the issues.

CLOSE RATE: What percentage of estimates convert to jobs. Target: 50%+.
Below 40%, we need to improve estimate follow-up.

COST PER LEAD: How much you're spending to get each new lead. Lower is better.
Target: Under $50 for most home services.

ROI: For every $1 you spend on our service, here's how much revenue it generates.
Target: 5x or higher.
```

### 7.4 Emergency Contacts and Escalation

Provide the client with a simple card:

```
SUPPORT CONTACTS

For system issues (AI not working, missed calls, wrong bookings):
Email: support@[youragency].com
Phone: [your support number]
Response time: Within 2 hours during business hours

For urgent issues (system down, major malfunction):
Text: [your cell]
Response time: Within 30 minutes

For billing questions:
Email: billing@[youragency].com

Monthly strategy call: [Scheduled day/time] via Zoom
```

---

## 8. Ongoing Operations

### 8.1 Weekly Maintenance Tasks

Perform every Monday morning (30 minutes per client):

- [ ] Review AI call quality: Listen to 5-10 random calls from the past week
- [ ] Check CRM for any data issues (duplicates, missing fields)
- [ ] Verify all sequences are firing correctly (spot check 2-3)
- [ ] Check review response accuracy and timeliness
- [ ] Review Twilio delivery reports for SMS failures
- [ ] Check email bounce rates and spam complaints
- [ ] Verify n8n workflows are running without errors (check execution log)
- [ ] Address any client requests from the week
- [ ] Update client Slack channel with weekly summary

### 8.2 Monthly Optimization Checklist

Perform during the first week of each month (2 hours per client):

- [ ] Generate and review monthly performance report
- [ ] Compare KPIs to previous month and same month last year
- [ ] Update AI scripts based on common call patterns (review transcripts)
- [ ] Refresh review response templates
- [ ] Update pricing in AI knowledge base (ask client if prices changed)
- [ ] Review and adjust follow-up sequence timing based on conversion data
- [ ] Check and update technician roster (new hires, departures)
- [ ] Launch monthly seasonal campaign
- [ ] Review outreach list quality and refresh if needed
- [ ] Update GBP with new photos, posts, and any business changes
- [ ] Check API usage and costs against budget
- [ ] Send monthly report to client
- [ ] Schedule monthly strategy call with client

### 8.3 Quarterly Business Review Template

**Meeting Duration:** 45 minutes
**Attendees:** Client owner, office manager (optional), your account manager

**Agenda:**

```
1. RESULTS REVIEW (15 min)
   - Revenue impact: Total revenue attributed to our system
   - Lead generation: Leads generated, conversion rates
   - Customer satisfaction: Review ratings, NPS, complaints
   - Cost efficiency: Your investment vs. revenue generated (ROI)

2. SYSTEM HEALTH (10 min)
   - Call quality trends
   - Sequence performance (what's working, what's not)
   - Any technical issues resolved
   - Upcoming tech changes or updates

3. STRATEGIC PLANNING (15 min)
   - What's working best? Do more of it.
   - What needs improvement? Action plan.
   - New services or offerings to add?
   - Seasonal opportunities in the next quarter
   - Expansion ideas (new service areas, new services)

4. ACTION ITEMS (5 min)
   - Document 3-5 action items with owners and deadlines
   - Schedule next QBR
```

### 8.4 Handling Client Requests and Changes

**Common requests and how to handle them:**

| Request | Process | Timeline |
|---|---|---|
| "Add a new service" | Update AI script, CRM categories, pricing | 1-2 business days |
| "Change our hours" | Update AI script, GBP, website, CRM | Same day |
| "New technician joined" | Add to dispatch roster, CRM, skill mapping | Same day |
| "Tech left the company" | Remove from all systems | Immediate |
| "We changed our pricing" | Update AI script, pricing cards, estimate templates | Same day |
| "Run a special promotion" | Create campaign in n8n, update AI script, GBP post | 2-3 business days |
| "We got a bad review" | Draft response, get client approval, post | Within 4 hours |
| "Calls aren't getting booked" | Audit last 20 calls, identify issue, fix | Within 24 hours |
| "We want to expand service area" | Update all systems with new zip codes | 1-2 business days |
| "Can you change the AI's voice?" | Swap voice in Vapi, test, client approval | 1 business day |

**Response time commitments:**
- Critical (system down): 30 minutes
- Urgent (impacting bookings): 2 hours
- Standard (changes/updates): 1-2 business days
- Non-urgent (nice-to-haves): 5 business days

---

## 9. Cost Structure Per Client

### 9.1 Infrastructure Costs Breakdown

| Tool | Cost Per Client/Month | Notes |
|---|---|---|
| Vapi (AI phone) | $15-60 | Based on ~200-400 min/month at $0.07-0.15/min |
| Twilio (SMS) | $5-15 | $1.15/number + ~500-1500 SMS at $0.0079 each |
| SendGrid (email) | $2-5 | Pro-rated from $19.95/month plan across clients |
| n8n (hosting) | $3-8 | VPS cost divided by number of clients |
| CallRail | $45-95 | Per-client account or pro-rated agency account |
| Claude API | $15-50 | Voice + content generation + briefings |
| Outreach tool (Instantly) | $5-15 | Pro-rated from agency plan |
| Google Cloud (APIs) | $0-5 | Most APIs free within limits |
| Database (Supabase) | $0-5 | Free tier for most clients, $25/month pro-rated |
| Domain/SSL | $1-2 | Pro-rated across clients |

### 9.2 Expected Monthly COGS by Tier

| | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| **AI Phone** | $30 | $40 | $50 |
| **SMS/Voice Infra** | $10 | $15 | $15 |
| **Email** | $3 | $8 | $10 |
| **Hosting/Compute** | $5 | $5 | $8 |
| **Call Tracking** | $45 | $45 | $45 |
| **AI Processing** | $15 | $25 | $45 |
| **Outreach Tools** | $0 | $10 | $10 |
| **Miscellaneous** | $5 | $10 | $15 |
| **Total COGS** | **$113** | **$158** | **$198** |

### 9.3 Margin Analysis

| | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| **Monthly Price to Client** | $997 | $1,997 | $3,497 |
| **Monthly COGS** | $113 | $158 | $198 |
| **Gross Profit** | $884 | $1,839 | $3,299 |
| **Gross Margin** | 88.7% | 92.1% | 94.3% |
| **Labor (est. hrs/month)** | 4 hrs | 8 hrs | 12 hrs |
| **Labor Cost (at $50/hr)** | $200 | $400 | $600 |
| **Net Margin After Labor** | $684 (68.6%) | $1,439 (72.1%) | $2,699 (77.2%) |

**Notes:**
- Labor hours decrease as you build SOPs and templates (by client 10, Tier 1 takes 2 hrs/month)
- COGS are conservative estimates -- actual may be 10-20% lower with optimization
- Setup costs (one-time): ~$500-800 in labor per client for initial deployment, recovered in first month

---

## 10. Scaling Playbook

### 10.1 Growth Milestones: 10 to 50 to 150 Clients

**Phase 1: 1-10 Clients (Founder Mode)**

Focus: Get the system working perfectly. Every client is a learning opportunity.

- You (the founder) do everything: sales, deployment, operations
- Spend 60% of time on delivery, 40% on sales
- Refine the deployment process with every client
- Document everything as you go (this guide is the start)
- Target: 2-3 new clients per month
- Revenue: $10K-30K MRR
- Time to reach: Months 1-4

**Phase 2: 10-25 Clients (First Hire)**

Focus: Systematize operations so you can focus on sales.

- Hire #1: Part-time Virtual Assistant / Operations Coordinator ($2,000-3,000/month)
  - Responsibilities: Weekly maintenance, call monitoring, sequence management
  - Train them on this guide
  - They handle Day 2-7 operations with your oversight
  - You handle: Sales, Day 1 setup, complex troubleshooting, client strategy

- Process improvements:
  - Create client onboarding template in Notion/ClickUp
  - Build n8n workflow templates that clone for each new client
  - Create a CRM-specific setup checklist (one per CRM type)
  - Standardize the QA testing protocol (hire a freelancer for test calls)

- Revenue: $30K-75K MRR
- Time to reach: Months 4-8

**Phase 3: 25-50 Clients (Account Manager)**

Focus: Client relationship management becomes a dedicated role.

- Hire #2: Account Manager ($4,000-6,000/month)
  - Responsibilities: Client communication, monthly reports, QBRs, upsells
  - Owns the client relationship post-deployment
  - Handles all client requests and change management
  - You handle: Sales, system architecture, complex technical issues

- Hire #3: Systems Builder / Automation Engineer ($3,000-5,000/month)
  - Responsibilities: New client deployments, CRM integrations, workflow building
  - Follows this guide for all deployments
  - Handles technical troubleshooting
  - Builds new features and improvements

- Process improvements:
  - Client portal: Self-service dashboard where clients see their metrics
  - Automated onboarding: Intake form auto-creates project boards and task lists
  - Template library: Pre-built n8n workflows for every CRM type
  - SOPs for every recurring task (documented in Notion/Confluence)

- Revenue: $75K-150K MRR
- Time to reach: Months 8-14

**Phase 4: 50-150 Clients (Department Heads)**

Focus: Build departments, not tasks.

- Team structure:
  ```
  Founder/CEO
  ├── Head of Sales (hire at ~60 clients)
  │   ├── Sales Rep 1
  │   └── Sales Rep 2
  ├── Head of Operations (promote Account Manager or hire)
  │   ├── Account Manager 1 (25 clients each)
  │   ├── Account Manager 2
  │   └── Account Manager 3
  ├── Head of Engineering (promote Systems Builder or hire)
  │   ├── Systems Builder 1
  │   ├── Systems Builder 2
  │   └── QA Specialist
  └── Admin / Finance
  ```

- Revenue: $150K-500K MRR
- Time to reach: Months 14-24

### 10.2 When to Hire

| Hire | Trigger | Cost | ROI |
|---|---|---|---|
| VA / Ops Coordinator | 10 clients OR 20+ hrs/week on operations | $2-3K/month | Frees 20 hrs/week for sales |
| Account Manager | 25 clients OR client churn above 5% | $4-6K/month | Reduces churn, enables upsells |
| Systems Builder | 25 clients OR deployment backlog > 2 weeks | $3-5K/month | Doubles deployment capacity |
| Sales Rep | 50 clients OR founder spending <20% on sales | $3-5K/month + commission | Doubles new client acquisition |
| QA Specialist | 40+ clients OR quality complaints increasing | $2-3K/month | Maintains call quality at scale |
| Head of Ops | 60+ clients | $6-8K/month | Strategic operations leadership |
| Head of Sales | 60+ clients | $6-8K/month + override | Strategic sales leadership |

### 10.3 Templates and SOPs for Repeatable Deployment

Build and maintain these templates:

**Deployment Templates (clone for each new client):**

1. **n8n Workflow Templates** (one set per CRM type):
   - `TEMPLATE-ServiceTitan-Receptionist.json`
   - `TEMPLATE-ServiceTitan-Sequences.json`
   - `TEMPLATE-ServiceTitan-Reviews.json`
   - `TEMPLATE-HCP-Receptionist.json`
   - `TEMPLATE-HCP-Sequences.json`
   - (etc. for each CRM)
   - Import template, search-and-replace client variables, activate

2. **Vapi Assistant Template:**
   - Base system prompt with `[PLACEHOLDER]` variables
   - Clone assistant, replace variables, adjust voice
   - Time to customize: 30 minutes

3. **Email Templates** (SendGrid Dynamic Templates):
   - Appointment confirmation
   - Post-service follow-up
   - Review request
   - Estimate follow-up (4-email series)
   - Seasonal campaign (12 templates)
   - Referral program
   - Clone and brand for each client: 1 hour

4. **GBP Optimization Checklist:**
   - Step-by-step with screenshots
   - Pre-written Q&A templates
   - Post templates for each industry vertical

**SOP Documents:**

| SOP | Purpose | Owner |
|---|---|---|
| SOP-001: Client Onboarding | End-to-end onboarding process | Account Manager |
| SOP-002: Tier 1 Deployment | Days 1-7 technical deployment | Systems Builder |
| SOP-003: Tier 2 Deployment | Days 8-21 marketing deployment | Systems Builder |
| SOP-004: Tier 3 Deployment | Days 14-30 operations deployment | Systems Builder |
| SOP-005: Weekly Maintenance | Recurring weekly tasks | VA / Ops |
| SOP-006: Monthly Optimization | Recurring monthly tasks | Account Manager |
| SOP-007: QBR Preparation | Quarterly review preparation | Account Manager |
| SOP-008: Call Quality Audit | How to score and improve calls | QA / VA |
| SOP-009: Client Offboarding | How to cleanly offboard a client | Account Manager |
| SOP-010: Emergency Response | System outage response protocol | Systems Builder |
| SOP-011: New CRM Integration | How to add support for a new CRM | Systems Builder |
| SOP-012: Sales Process | From lead to signed contract | Sales |

### 10.4 Client Management Tools and Processes

**Recommended Stack for Managing Your Clients:**

| Tool | Purpose | Cost |
|---|---|---|
| ClickUp or Notion | Project management, SOPs, client boards | $10-15/user/month |
| Slack | Internal communication + client channels | Free-$12.50/user/month |
| 1Password Teams | Credential management | $7.99/user/month |
| Loom | Client training videos | $12.50/user/month |
| Google Workspace | Email, Docs, Sheets, Drive | $7.20/user/month |
| Stripe or GoCardless | Client billing (recurring) | 2.9% + $0.30 per transaction |
| PandaDoc or DocuSign | Contracts and proposals | $19-35/user/month |

**Client Board Structure (ClickUp/Notion):**

Each client gets a board with these columns/statuses:

```
ONBOARDING > TIER 1 BUILD > TIER 1 LIVE > TIER 2 BUILD > TIER 2 LIVE > TIER 3 BUILD > TIER 3 LIVE > STEADY STATE
```

Each column has sub-tasks matching this implementation guide. When a new client signs, clone the template board and assign the systems builder.

**Client Health Scoring:**

Score each client monthly on a 1-5 scale:

| Metric | Weight | Scoring |
|---|---|---|
| Revenue trend | 25% | 5=Growing, 3=Flat, 1=Declining |
| Engagement | 20% | 5=Active partner, 3=Hands-off but happy, 1=Unresponsive |
| NPS/satisfaction | 20% | 5=Promoter, 3=Passive, 1=Detractor |
| System health | 20% | 5=All green, 3=Minor issues, 1=Frequent problems |
| Payment history | 15% | 5=Always on time, 3=Occasional late, 1=Chasing payments |

**Action triggers:**
- Score 4.0+: Upsell opportunity, ask for referral
- Score 3.0-3.9: Standard service, monitor
- Score 2.0-2.9: At-risk, schedule call, create improvement plan
- Score below 2.0: Escalate to founder, potential offboarding

---

## Appendix A: Quick Reference -- Deployment Timelines

```
WEEK 1:
  Mon: Infrastructure setup (Day 1)
  Tue: AI Receptionist build (Day 2)
  Wed: Phone system integration (Day 3)
  Thu: CRM integration (Day 4)
  Fri: Follow-up sequences (Day 5)

WEEK 2:
  Mon: Review management + GBP (Day 6)
  Tue: Testing + go-live (Day 7)
  Wed-Fri: Cold outreach setup (Tier 2, Days 8-10)

WEEK 3:
  Mon-Wed: Estimate follow-up + neighborhood targeting (Days 10-14)
  Thu-Fri: Seasonal campaigns + referral program (Days 14-17)

WEEK 4:
  Mon-Thu: AI Dispatch + invoicing + lifecycle (Tier 3, Days 18-24)
  Fri: Dashboards + briefings (Days 24-27)

WEEK 5:
  Mon-Tue: Final Tier 3 deliverables (Days 27-30)
  Wed: Full system QA
  Thu: Client training
  Fri: Handoff to steady-state operations
```

## Appendix B: Credential Checklist

Copy this for each client and check off as you collect:

```
CLIENT: ___________________________
DATE STARTED: _____________________

[ ] Vapi API Key
[ ] Vapi Phone Number
[ ] Twilio Account SID
[ ] Twilio Auth Token
[ ] Twilio Phone Number
[ ] Twilio Messaging Service SID
[ ] SendGrid API Key
[ ] SendGrid Sending Domain Verified
[ ] n8n Instance URL
[ ] n8n Login Credentials
[ ] CallRail Company ID
[ ] CallRail API Key
[ ] Google Cloud Service Account JSON
[ ] GBP Account ID
[ ] GBP Location ID
[ ] CRM Type: _______________
[ ] CRM API Key / OAuth Tokens
[ ] CRM Tenant/Company ID
[ ] QuickBooks OAuth Tokens (Tier 3)
[ ] Claude API Key
[ ] Client Website CMS Login
[ ] Client Domain Registrar Login
[ ] Client Phone System Login
[ ] Outreach Tool Login (Tier 2)
[ ] All stored in credential vault: [ ] Yes
```

## Appendix C: Emergency Playbook

**If Vapi goes down:**
1. CallRail/phone system failover routes to client's cell within 30 seconds
2. Alert client: "AI phone system is temporarily down, calls routing to your phone"
3. Check Vapi status page: status.vapi.ai
4. If extended outage: Switch to Bland.ai backup or route to answering service

**If n8n goes down:**
1. Check VPS health: SSH in, check Docker containers
2. `docker compose restart` usually fixes it
3. If data issue: Restore PostgreSQL from latest backup
4. Calls still work (Vapi handles independently), but follow-ups will queue

**If CRM API breaks:**
1. Check CRM status page for outages
2. Check if OAuth tokens need refreshing
3. n8n will queue failed executions -- they auto-retry when API returns
4. If extended: Switch to manual booking notifications via SMS to office

**If SMS not delivering:**
1. Check Twilio console for error logs
2. Common issue: A2P 10DLC campaign suspended -- contact Twilio support
3. Backup: Switch to email-only follow-up temporarily
4. If carrier filtering: Adjust message content to avoid spam triggers

---

*This is a living document. Update it every time you learn something new from a deployment. The goal is that any team member can pick this up and deploy a client from start to finish without asking questions.*
