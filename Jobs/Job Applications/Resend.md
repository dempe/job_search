---
type: job
applied: 2026-06-04
status: rejected
interviews:
job_type: fulltime
source: matcha
position: Backend Engineer (Infra), Core Sending
contract: false
remote: true
recruited: false
listing: https://jobs.ashbyhq.com/resend/d5bc5890-847d-4bc5-bbd7-d0d72021ff3c
compensation: $150,000 - $170,000
title: Resend
date_created: 2026-06-03 10:00
date_modified: 2026-06-04 09:56
---

## Application

> Why do you want to join Resend?<br/>
> Send an engaging message and tell us why you want to join us, what excites you about the problem we're solving, and how you envision your role at Resend.

```
There are a lot of things that excite me about this job opportunity. One thing that stands out is the very international team. I've worked on highly international teams before and found that great for diversity of opinions and styles.

I've read through your website and can tell that Resend puts a lot of thought and effort into their product, employees, and culture. That is a very, very nice looking and highly detailed website, by the way!

The problems you're solving at Resend -- async messaging pipelines, high availability, scaling databases, etc. is the type of work that I love. It's where I've spent most of my career. I'd love to continue growing my career as part of Resend.

At Resend, I envision myself as someone who is constantly looking for new problems to solve and shipping solutions.

I also envision myself collaborating a lot with others. I've worked both solo and on teams, and I consistently do my best work and learn the most when collaborating closely with others.

Thanks for reading!
```

> Tell us the most impactful project you've worked on before and what your role was in it. Share numbers that help us understand the workload (number of customers, requests per second, etc) and your impact on the project.<br/>
> Answer example: At my previous job, I led the rebuild of our payments service, handling checkout for ~2.3M monthly users at ~1,200 RPS peak.) I owned the technical design and the zero-downtime migration from a Rails monolith to a Go service with Kafka-based event distribution. After 4 months in production, p95 latency dropped from 800ms to 180ms.

```
As Senior Data Engineer at Octimine, I converted a 48-hourish batch data ingestion/analytics job (run weekly) to a real-time, event-driven analytics pipeline in Apahce Kafka. This meant that customers got data in immediately instead of waiting a week.

The data came in continuously to our data warehouse, so it did not make sense to me to use a batch job in the first place. I decided to use Kafka over something like Airflow due to the highly analytic nature of the pipeline. A Kafka Streams topology has joins, compaction, aggregates, etc. built-in and made my work a lot simpler.

We had about 50 customers. The data was all new patent data (new patents or updates to existing patents) in the US and Europe -- about 30 million documents per week.
```

> Tell us your favorite tools (editor, terminal, productivity tools, etc.).

```
I use...

- NeoVim (with various plugins/configs) for most text editing
- Emacs for task tracking in Org Mode specifically
- IntelliJ for larger projects
- Ghostty as my terminal emulator
- Obsidian for general note taking and journaling
- MacOS for my operating system
- Nix for package management, config management, and dependency management/reproducible builds (basically IaC for your personal computer)
- Zsh (heavily configured) for my shell
- Anki for studying
```
