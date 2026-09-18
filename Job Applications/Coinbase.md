---
type: job
applied: 2026-09-16
job_type: fulltime
recruited: false
status: awaiting-reply
interviews:
source: matcha
listing: "https://www.coinbase.com/en-mx/careers/positions/7812407"
company: Coinbase
position: Senior Software Engineer - Data Platform
contract: false
remote: true
compensation: $186,065 - $218,900 USD
title: Coinbase
date_created: "2026-09-16 21:52"
date_modified: "2026-09-17 19:32"
---

## Application

> Cover Letter

```
Hello,

I'm Chris, a backend engineer with 11 YOE. I have specialized in data ingestion, distributed systems, and cloud architecture.

At Octimine, I replaced a weekly Python batch job that took 48 hours minimum with a real-time, event-driven pipeline in Java and Kafka Streams, processing about 30 million patent documents a week. It had a DLQ for failed messages and unit tests on every analytic, so a bad message no longer halted the entire run and customers got their data as it arrived instead of once a week.

Before that, at DataRank, I architected the company's Java data ingestion -- a distributed framework with generic queuing, token pools, and rate limiting that normalized data from external APIs into a canonical model, so that adding a new source meant writing one implementation. At SimplyMeasured/Sprout Social, I wrote HBase map/reduce jobs for social analytics and set up the API gateway (in Kong) that gave clients a single interface to our microservices.

I enjoy platform work, but I should be straightforward that I haven't run Spark or Airflow in production. At Octimine I argued for Kafka Streams over Airflow, since the pipeline was analytics-heavy rather than a simple ETL job, and Kafka Streams gave us joins, windowing, and compaction out of the box. I've built the primitives these frameworks wrap, and I pick up new tools quickly.

I'm currently doing project-based contracting work, but I'm looking to return to a team. I find that's where I do my best work and learn the most.

Best,
Chris
```

> Which of the following best describes how you use AI tools today?

```
Daily, as a core part of how I build. I run a scope->plan->implement->review cycle out of a set of model-agnostic skill files that I share across Claude Code, Codex, and OpenCode, so any agent can pick up where another left off. Most of my effort goes into defining the problem and the plan; the agent does much of the implementation.

I keep human oversight over what it produces. On a recent payments integration, I rejected a hand-rolled SQL migration runner and config loader in favor of off-the-shelf libraries, and made it write a failing unit test before changing any code.
```
