---
type: job
applied: 2026-07-29
job_type: fulltime
recruited: false
status: ghosted
source: matcha
interviews:
listing: https://jobs.Ashbyhq.Com/certa/3c608236-953e-4902-ba27-0589b09bb028
position: Software Engineer - Partner Engineering
contract: false
remote: true
compensation:
title: Certa
date_created: 2026-07-29 18:40
date_modified: 2026-07-29 18:40
---

## Application

> Have you been involved in designing and developing the architecture of complex software systems? If yes, please confirm which part you were involved in.

```
At Octimine, I replaced a weekly Python batch job that took 48 hours minimum to run. The problem was that it was prone to breakage and sometimes would even overlap with the following week's job.

I began by analyzing the batch job and what it was doing. I saw that data came in continuously, so a batch job wasn't even required in the first place.

I suggested we migrate to a real-time, event-driven system, and I proposed Kafka Streams for this solution. Other team members suggested using AirFlow for simplicity, but looking at what the batch job was actually doing, it was clear that Kafka Streams was a better fit.  It wasn't a simple ETL job, where AirFlow specializes. The batch job was doing heavy analytics. Kafka Streams provides joins, windows, compaction, grouping, etc. out-of-the-box and would, in the end, make our lives easier.

I designed the system from source to sink and proposed it to my manager and other backend engineers. After we agreed on the plan, I began implementing the new pipeline with two other engineers.

After it was completed, the new pipeline was much more durable. All analytics were unit-tested. We had a DLQ for failed messages, and could quickly diagnose problems. Moreover, problem messages no longer halted the entire run. And, on top of all of that, customers got their data in real time!
```