---
type: job
applied: 2026-06-10
status: rejected
interviews:
job_type: fulltime
source: matcha
position: Senior Backend Software Engineer
contract: false
remote: true
recruited: false
listing: https://jobs.Ashbyhq.Com/Archy/9cf41704-3950-417d-be81-114c27ecf892
compensation: 160,000 - 190,000
title: Archy
date_created: 2026-06-10 20:46
date_modified: 2026-06-11 10:08
---

## Application

> Cover Letter (optional)

```
Hello,

I'm Chris, a backend engineer with 11 YOE. I have specialized in data ingestion, distributed systems, and cloud architecture.

I'm currently running a one-man contracting company doing AWS work. I've helped clients set up serverless pipelines in API Gateway, Lambda, DynamoDB with SQS queues. I've helped clients tune their EC2 and RDS instances and set up S3/CloudFront.

At Octimine, I replaced a 48-hour batch process (run weekly) with a real-time, event-driven pipeline in Kafka Streams using a Java-based stream topology, allowing customers to get their data instantly.

I got experience in microservices (mostly Spring Boot), asynchronous messaging (Kafka), and API design at SimplyMeasured/SproutSocial. I set up their API gateway in Kong.

As mentioned, I'm running my own company, but I'm looking to return to a team. I find that I do my best work and learn the most working with others.

Best,
Chris
```

> Please tell us about a time you identified a technical bottleneck or a looming scalability issue that others had overlooked. How did you build a case for fixing it, and what was the measurable impact on the system's performance or reliability?

```
When I joined DataRank, our web crawlers were a collection of ad hoc scripts run manually across four servers. Adding a new data source meant SSH'ing in and editing scripts by hand.

I made a case for fixing it by proposing a plan: a centralized queue of URLs to be crawled, have an orchestrator and a pool of crawlers on each server such that the orchestrator would pull from the queue and distribute the work to the first crawler whose canHandle() method returned true.

After implementation, adding a new data source went from manual server edits to a simple redeploy (using Jenkins back in those days). We onboarded two junior engineers shortly after who could contribute new crawlers independently without touching server configuration.
```
