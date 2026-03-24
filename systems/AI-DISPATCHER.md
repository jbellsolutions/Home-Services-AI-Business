# AI Dispatcher System — Technical Specification

## Purpose
Automatically route incoming jobs to the right technician based on skills, location, availability, and priority. Eliminate the dispatcher bottleneck and reduce drive time, missed appointments, and scheduling conflicts.

---

## The Problem
- Average home services company: 1 dispatcher managing 5-15 techs
- Dispatcher is the #1 bottleneck in growing companies
- Manual dispatching leads to:
  - Wrong tech for the job (HVAC install guy sent to a simple thermostat issue)
  - Excessive drive time (sending a tech across town when one is 5 minutes away)
  - Double-bookings and missed appointments
  - Uneven workload (one tech overloaded, another idle)
  - Emergency calls can't be prioritized in real-time
- When the dispatcher is sick/on vacation, chaos

---

## AI Dispatcher Capabilities

### 1. Smart Job Routing
When a new job enters the system:
1. **Parse the job**: service type, location, urgency, equipment brand
2. **Match technicians** against criteria:
   - Skills/certifications (don't send a residential tech to a commercial chiller)
   - Current location (minimize drive time)
   - Availability (not already booked in that window)
   - Workload balance (spread jobs evenly across the team)
   - Customer history (same tech who was there before, if available)
3. **Rank top 3 options** and auto-assign the best match
4. **Notify the tech** via text/app with job details

### 2. Real-Time Rerouting
- If a tech finishes early → check for nearby unassigned jobs → offer it
- If a tech is running late → notify next customer with updated ETA
- If a job cancels → redistribute the slot or offer it to customers on the waitlist
- If emergency comes in → find nearest available tech, move non-urgent jobs

### 3. Schedule Optimization
- Morning: optimize the day's route for minimum drive time (traveling salesman problem)
- Throughout day: re-optimize as jobs complete, cancel, or add
- End of day: fill gaps with maintenance agreement visits or neighborhood campaigns

### 4. Technician Profiles
For each tech, the system tracks:
```
{
  "name": "Mike Johnson",
  "id": "tech_042",
  "skills": ["residential_ac", "residential_heating", "ductwork", "thermostat"],
  "certifications": ["EPA_608", "NATE_AC", "Carrier_authorized"],
  "equipment_brands": ["Carrier", "Trane", "Lennox", "Goodman"],
  "max_daily_jobs": 6,
  "home_base": {"lat": 27.9506, "lng": -82.4572},
  "current_location": {"lat": 27.9650, "lng": -82.4300},
  "availability": "available", // available, on_job, break, off_duty
  "current_job_eta_completion": "2024-03-15T14:30:00",
  "avg_job_times": {
    "ac_tuneup": 45,
    "ac_repair": 90,
    "furnace_tuneup": 45,
    "thermostat_install": 30,
    "system_install": 480
  },
  "customer_rating": 4.8,
  "jobs_today": 3,
  "jobs_remaining": 2
}
```

---

## Routing Algorithm

```
Input: New job (service_type, location, urgency, time_window, equipment_brand)

FOR each available tech:
  skill_match = tech.skills CONTAINS service_type
  cert_match = tech.certifications MATCH requirements
  brand_match = tech.equipment_brands CONTAINS job.brand (if applicable)

  IF NOT skill_match → skip
  IF NOT cert_match → skip

  distance = haversine(tech.current_location, job.location)
  drive_time = distance / avg_speed (adjusted for traffic via Google Maps API)

  availability_score = tech.max_daily_jobs - tech.jobs_today
  workload_score = normalize(availability_score)

  proximity_score = 1 / (1 + drive_time)

  IF job.urgency == "emergency":
    urgency_weight = 3.0  // prioritize nearest available
  ELSE:
    urgency_weight = 1.0

  customer_history_bonus = 0.2 IF tech previously served this customer

  TOTAL_SCORE = (proximity_score * urgency_weight * 0.4)
              + (workload_score * 0.3)
              + (tech.customer_rating * 0.2)
              + (customer_history_bonus * 0.1)

RANK techs by TOTAL_SCORE
ASSIGN to top-ranked tech
NOTIFY tech via SMS with job details
UPDATE schedule
```

---

## Integration Points

### CRM (ServiceTitan / HCP / Jobber)
- **Read:** Job queue, technician schedules, customer history
- **Write:** Job assignments, route updates, completion status
- **Webhook:** New job created → trigger routing algorithm

### Google Maps API
- Real-time driving distance and time estimates
- Route optimization for daily schedule
- Traffic-aware ETA calculations

### Twilio
- Tech notifications (job assigned, schedule changed, emergency alert)
- Customer notifications (tech on the way, ETA update, job complete)

---

## Notifications

### To Technicians
```
NEW JOB ASSIGNED:
📍 123 Oak St, Tampa FL 33609
🔧 AC Repair — not cooling
⏰ 2:00 PM - 3:30 PM window
👤 John Smith (returning customer)
📞 (813) 555-1234
📝 "Unit is running but blowing warm air. Outdoor unit making clicking noise."
🗺️ [Google Maps link]
Reply ACCEPT or ISSUE
```

### To Customers
```
YOUR APPOINTMENT:
"Hi [Name], [Tech Name] from [Company] is on the way! 🚐
ETA: ~25 minutes (arriving by 2:15 PM)
[Tech Name] specializes in [service type] and has a 4.8-star rating.
Questions? Call or text [number]."
```

### To Owner (Daily Summary)
```
DISPATCH SUMMARY — [Date]:
✅ 24 jobs dispatched | 23 completed | 1 rescheduled
🚐 Average drive time: 18 min (down from 28 min last month)
⚡ 2 emergency calls handled (avg response: 35 min)
🔧 Top tech today: Mike J (6 jobs, 4.9 avg rating)
📊 Utilization: 87% (target: 85%)
💰 Revenue dispatched: $8,400
```

---

## Performance Metrics

| Metric | Target | Without AI Dispatcher |
|--------|--------|---------------------|
| Average drive time between jobs | <20 min | 30-45 min |
| Jobs per tech per day | 5-7 | 3-5 |
| Schedule utilization | 85-90% | 65-75% |
| Emergency response time | <45 min | 1-3 hours |
| Double-booking rate | 0% | 5-10% |
| Customer ETA accuracy | ±15 min | ±45 min |
| Dispatcher hours needed/day | 0-1 (oversight only) | 8 (full-time) |

---

## Revenue Impact

**Fewer drive-time hours = more billable hours:**
- 5 techs × 30 min saved/day × 22 days = 55 hours/month freed
- At $150/hr billing rate = **$8,250/month additional capacity**

**Higher utilization = more jobs per day:**
- Going from 4 jobs/tech/day to 5.5 = 37% more revenue from same team
- On $2M revenue company = **$740,000 additional annual capacity**

**Dispatcher salary savings:**
- Full-time dispatcher: $3,000-$4,500/month
- With AI Dispatcher: 0-5 hours/week oversight (office manager handles)
- **Savings: $3,000-$4,500/month**

---

## Setup Process

1. Build technician profiles (skills, certs, home base, max capacity)
2. Define service types and skill requirements
3. Connect to CRM for job queue and scheduling
4. Set up Google Maps API for routing
5. Configure notification templates
6. Define emergency escalation rules
7. Run parallel with existing dispatcher for 1 week (AI suggests, human confirms)
8. Go live with AI handling routine dispatch, human handling exceptions
9. After 2 weeks: full AI dispatch with human oversight
