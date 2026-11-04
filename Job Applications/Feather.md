---
type: job
applied: 2026-04-10
interviews:
  - 2026-04-22 10:40
status: declined
job_type: fulltime
source: workatastartup
position: Founding Engineer
contract: false
remote: ture
4day: false
industry: AI
website:
location: Seattle, WA
company_size:
channel: form
listing: https://www.workatastartup.com/jobs/92516
blog:
correspondence:
compensation: $120K - $170K  •  0.50% - 1.50%
title: Feather
date_created: "2026-10-21 17:49"
date_modified: "2026-10-21 17:49"
---

## Application

```
Hi Aahan,

I'm Chris.  I'm a backend engineer with 10 years of experience.  I've mostly worked on data ingestion.  At Octimine, I converted a 2 day batch job into a real-time, event-driven analytics pipeline based in Kafka (Python and Java).  I also built a distributed data collection framework for DataRank (S13).

I'm currently running my own company doing AWS contracting work and building apps (React Native/Typescript) end-to-end on AWS serverless.

I have not done a lot of LLM work specifically, but I did set up a personal RAG in Python on my Obsidian vault, and it's something I'm genuinely interested in learning.

Would love to have a quick chat and learn more about the role!

Best,
Chris
```

## Interview 1

### Transcript

![[Transcripts/Feather - Interview 1]]

### Questions

Model answers, not a record of what was said.

> We're a voice AI platform. I don't know if you've seen them before or talked to voice AI. Have you?

```
Yes. I've talked to a few voice agents, mostly support and scheduling lines, and I've looked at how they're put together. The pipeline is basically streaming speech-to-text, an LLM deciding what to say and which tools to call, and text-to-speech back out, all under a tight latency budget so the conversation doesn't feel laggy.

What interests me as a backend engineer is everything around that loop: handling thousands of concurrent calls, telephony integration, interruptions and turn-taking, tool calls into customers' systems that have to be reliable and idempotent, and capturing transcripts and outcomes so customers can see what happened. That's where I think most of the hard engineering is, especially for enterprise customers.
```

> Run me through your career background.

```
I'm a backend engineer, and most of my career has been data ingestion and data pipelines.

I started in 2013 at DataRank, a Y Combinator startup tracking what people said online about products. I built their ingestion: a distributed crawler framework for forums, and a framework for social APIs like Facebook, Twitter, and Pinterest with token pools and rate limiting, so adding a new source took very little code.

Then I moved to Seattle and joined SimplyMeasured, which had a much bigger microservice backend. I built services in Spring Boot and Go, and built the API gateway that handled auth, rate limiting, and request transforms for all of them.

After that I was the senior data engineer at Octimine in Munich, a patent analytics startup. Their weekly batch job, written by data scientists, took days and sometimes ran into the next week. I proposed and built an event-driven pipeline on Kafka Streams, porting their Python analytics to Java, with a dead letter queue and unit tests on every analytic. It processed around 30 million documents a week.

Since then I've run my own company -- a React Native app on a serverless AWS backend -- and done contract work on Node.js payment and Shopify integrations. Now I want to get back on a team and work on hard backend problems at scale, which is what a platform handling high call volume is.
```
