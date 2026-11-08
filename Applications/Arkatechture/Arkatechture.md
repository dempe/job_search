---
type: job
applied: 2026-09-14
job_type: fulltime
channel: form
status: ghosted
interviews:
source: matcha
listing: "https://arkatechture.pinpointhq.com/en/postings/795de167-707f-4349-b41f-92945f512210"
company: Arkatechture
position: Senior Software Engineer, Technical Lead
contract: false
remote: true
compensation: $111,000 - $130,000 / year
title: Arkatechture
date_created: "2026-09-14 19:17"
date_modified: "2026-09-14 19:25"
---

## Questions

### To help us get to know you, please include your resume and answer the following question in the cover letter section of the application: Tell us about a complex data or software engineering solution you personally designed and delivered. What problem were you solving, what technologies and approach did you use, and what was the outcome? Please also briefly describe your role in guiding other engineers or improving the team's technical approach along the way. (250 words or less.) Cover Letter

At Octimine, I replaced a weekly Python batch job that took 48 hours minimum to run. It processed about 30 million patent documents per week for about 50 customers. The problem was that it was prone to breakage and sometimes would even overlap with the following week's job.

I began by analyzing the batch job and what it was doing. I saw that data came in continuously, so a batch job wasn't even required in the first place.

I suggested we migrate to a real-time, event-driven system, and I proposed Kafka Streams. Other team members suggested Airflow for simplicity, but it wasn't a simple ETL job, where Airflow specializes. The batch job was doing heavy analytics, and Kafka Streams provides joins, windows, compaction, grouping, etc. out-of-the-box.

I designed the system from source to sink and proposed it to my manager and other backend engineers. After we agreed on the plan, I implemented the new pipeline with two other engineers.

The new pipeline was much more durable. All analytics were unit-tested. We had a DLQ for failed messages and could quickly diagnose problems. And customers got their data in real time instead of waiting a week!

As the only data engineer, I made sure to document all aspects of our data ingestion pipeline, from the what and the why to the orchestration. I also urged the team to move communication out of direct messages and into public chat rooms, so others could chime in and learn from the conversation.
