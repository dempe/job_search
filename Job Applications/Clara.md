---
type: job
applied: 2026-02-01
interviews:
  - 2024-02-04 14:30
  - 2024-02-11 14:00
status: declined
job_type: fulltime
source: workatastartup
position: Founding Platform Engineer
contract: false
remote: false
4day: false
industry: healthcare
website:
location: San Francisco, CA
company_size: 5
channel: recruited
listing: https://www.Workatastartup.Com/jobs/89493
blog:
correspondence: workatastartup
compensation: $250K - $280K  •  0.10% - 0.40%
title: Clara
date_created: "2026-02-01 13:30"
date_modified: "2026-10-21 18:04"
---

## Application

Hiring manager (he's an engineer! I checked on LI) sent the following:

```
Hey Chris! saw your work building distributed systems at Dempewolf and the AWS infrastructure you shipped there, exactly the kind of systems thinking we need. we're building the first AI-first medical practice from the ground up, real patient care, not a demo. founding platform engineer role, you'd own the entire backend and healthcare integrations stack. YC founders, $100M+ ARR at previous company, well-funded with runway. also love that you're looking for a team where you can have real autonomy and keep shipping clean, scalable systems, that's exactly what this is. would love to chat if you're interested!

- Cuau
```

ChatGPT mentioned (rightly) that Cuau mentions many things directly from my profile. He must have looked directly at it.

```
Read the subtext in his message

This is not a generic recruiter blast.

He referenced:

distributed systems

AWS infra you shipped

autonomy

clean systems

That means one of two things is likely:

1️⃣ He actually read your background.
2️⃣ You were sourced intentionally.

Both are strong signals.

Also…

Founding platform engineer is not a casual hire. That is a high-trust role.

Translation:

You are already being evaluated as a serious candidate.

Act accordingly.
```

```
One adjustment I strongly recommend

Avoid:

“I’d love to learn more!”

It is not bad — but it is slightly candidate-energy.

We want peer energy.

Subtle difference.

You are not asking for a tour.

You are exploring mutual fit.
```

```
Hi Cuau,

Thanks for reaching out! This sounds like an interesting problem space, and I'd love to hear more about what you're building.

Happy to connect! Feel free to grab a slot on my calendar:  https://calendly.com/calendly-dempewolf/30min

Best,
Chris
```

## Interview 1

### Transcript

![[Transcripts/Clara - Interview 1]]

### Questions

Model answers, not a record of what was said.

> Can you tell me a little bit about yourself?

```
Sure. I'm a backend engineer with about 11 years of experience, and most of it has been on the data ingestion side -- pulling data from sources you don't control, normalizing it, and getting it somewhere it's useful.

At DataRank, I built the company's ingestion: a distributed framework for social media APIs with shared token pools and rate limiting, and a distributed web crawler. At SimplyMeasured, I built microservices and set up the API gateway. At Octimine, I was the senior data engineer, and I replaced a fragile weekly batch job processing about 30 million patent documents with a real-time Kafka Streams pipeline.

Since then I've been running my own company. I built an iOS app with a serverless AWS backend, and I've done contract work, mostly backend and AWS.

I'm looking for three things now: to work on a team again, because I learn the most working with other people; new problems, because I've plateaued on the problems my own company gives me; and to focus on engineering instead of sales and marketing. Ingesting messy medical data from multiple sources for an AI product is exactly the kind of problem I like.
```

> So you built the app all by yourself? Tell me about that.

```
Yes, end to end. It's called Athena Math, a mental math training app for iOS. I'd wanted to build it for a while, and after I left Octimine it was the right time.

The frontend is React Native with Expo and TypeScript. I'd never done frontend before, so that was the biggest learning curve -- React's declarative model, state management, how rendering works over time. I used Zustand for state and SQLite on the device for offline session history and performance analytics.

The backend is AWS serverless: API Gateway, Lambda, and DynamoDB, defined in SAM, with GitHub Actions for CI/CD. Its main job is purchase verification. Apple recommends against verifying purchases on the device, since anything the client says can be faked, so the backend validates Apple's signed notifications -- including the certificate chain -- before unlocking anything. It's idempotent, with SQS retries and a dead-letter queue, and CloudWatch alarms.

I released it last summer, and it converts at about 11 percent, with a lot of positive feedback from the mental math community.
```

> Did you only build the mobile application, or did you also build a web app?

```
Just the mobile app, iOS for now. Since it's React Native, Android is mostly a build and some testing away, and people have asked for it, so that's next. A web version hasn't been a priority, because mental math practice is something people do in short bursts on their phones.
```

> Can you explain exactly what the platform does? Does it help you learn?

```
It's for practicing mental arithmetic. You configure the drill -- which operations, how many digits, number ranges, time limits -- and it tracks every session, so you can see your speed and accuracy over time and where you're weakest. The existing iOS apps were either too simple or too rigid, so the goal was something simple to use but fully customizable.

On whether it "makes you smarter": a lot of brain-training apps claim general benefits, but the research mostly says skills don't transfer -- train on n-back and you get better at n-back. I'm upfront that mental math might not transfer either. The difference is that calculating in your head is a useful skill on its own. You use it every day.
```

> Did you use any LLM for that, or is it purely your own?

```
The idea is mine -- I had it long before LLMs were around. And the app itself doesn't use an LLM. Problems are generated algorithmically and answers are checked deterministically. Arithmetic has exact answers, so an LLM would only add cost, latency, and a chance of being wrong.

Where LLMs came in was building it. They were a huge help learning React Native, which I'll get into.
```

> What did you use to build it -- the languages, the tools, the IDEs?

```
TypeScript with React Native and Expo for the app, Zustand for state, and SQLite for local storage. I wrote it in VS Code, with Codex and later Claude Code as assistants.

I wanted to actually learn React Native, not just have the AI write it, so I'd write a piece myself, show it to the AI, and ask how it could be better. It would correct me and explain the better pattern, and that's how I learned the idioms.

For the backend, everything is infrastructure as code in a SAM template: Lambda, API Gateway, DynamoDB, SQS. GitHub Actions deploys it, with separate staging and production environments, and CloudFormation gives me automated rollbacks if a deploy fails.
```

> Which infrastructure-as-code tool are you using?

```
AWS SAM. CloudFormation is AWS's general-purpose infrastructure as code, and SAM is an extension of it built specifically for serverless apps. It gives you short syntax for Lambda functions, API Gateway, and DynamoDB tables, and it expands into regular CloudFormation when you deploy. So you get CloudFormation's change sets and automatic rollback, plus `sam local` for testing functions locally.

I picked it because my backend is entirely serverless on AWS. For something multi-cloud, or with more non-serverless infrastructure, I'd lean toward Terraform.
```

> I saw that you have a lot of experience with ETL. Can you tell me about your experience at Octimine?

```
Octimine did analytics on patents, and they hired me as senior data engineer. The core of the system was a weekly Python batch job processing about 30 million documents. On a good week, it took two days. On a bad week, it failed, retried, and overlapped with the next week's run, so customers didn't get their data.

The data was arriving continuously, so a batch job didn't make sense in the first place. I proposed moving to an event-driven pipeline. Airflow came up, but this was heavy analytics -- joins, aggregations, windows -- not simple ETL, so I proposed Kafka Streams, which gives you all of that out of the box.

I designed it from source to sink. A source connector read new records from the data warehouse, each analytic became a stream processor in the topology, and a sink topic fed Elasticsearch, which backed our API. Every analytic was unit tested, and a dead-letter queue meant one bad document couldn't take down the run. I also documented the whole pipeline, including recovery procedures, which cut down recurring on-call incidents.

The result was a much more durable system, and customers got their data in near real time instead of weekly.
```

> We're ingesting data from different sources -- FHIR, which is basically the standard for medical data, and also wearable devices. They have different rate limits, and they're very limited: some we can only query once per week, one once per day. But we want everything as real-time as possible. I think it's good to be event-driven instead of batch processing, but how would you go about that?

```
First, be honest about the constraint: if a source only allows one query a week, polling can't make it real-time. So the goal is to get as fresh as each source allows, and make the rest of the system event-driven no matter how the data arrives.

Step one is to use push wherever it exists. Many wearable APIs offer webhooks, and FHIR has subscriptions. A push notification costs no rate-limit budget, and then you fetch only what changed.

For sources you have to poll, I'd build a generic source manager, similar to the API manager I built at DataRank for social media APIs. Each source gets a configuration: its rate limit as a token bucket, its schedule, its backoff policy -- exponential with jitter on 429s -- and its pagination. Polls are incremental, using something like `_lastUpdated` in FHIR or a since-cursor, so each scarce call returns only changes. If the budget can't cover every patient, prioritize -- refresh patients with upcoming visits or recent activity first.

Every fetched record goes onto a queue or stream as an event, and everything downstream consumes from there. Writes are idempotent upserts keyed on resource ID and version, so retries and overlapping polls are harmless. Failures go to a dead-letter queue.

Last, track freshness per source and per patient, and expose it. If the AI is reasoning over someone's data, it should know the wearable data is from today but the lab data is a week old.
```

> We have two open roles, data engineer and platform engineer. I contacted you for the platform role, but I think you also fit the data role very well. What are your thoughts?

```
I'd prefer the data engineering role. Data ingestion and pipelines are where I've spent most of my career and where I'm strongest -- the ingestion frameworks at DataRank, the Kafka pipeline at Octimine. The problem you just described, combining rate-limited FHIR and wearable sources into something close to real-time, is exactly the kind of work I want to do.

That said, I've done a lot of the platform side too -- infrastructure as code, CI/CD, AWS -- so I'd be comfortable contributing there when the data platform needs it. But if I'm choosing, data.
```

## Interview 2

### Transcript

![[Transcripts/Clara - Interview 2]]

### Questions

Model answers, not a record of what was said.

> What's your thought about the challenge?

```
It looks fun. As I understand it, there are two inputs: FHIR bundles from your supplier, which are already deduplicated through the health information exchange, and lab reports that arrive as scanned PDFs or images. The goal is to turn the lab report into valid FHIR, merge it into the patient's record, and get a de-identified copy into Postgres the team can use for evals and training.

My plan would be:

For the bundles: validate against the FHIR spec with an off-the-shelf library like fhir.resources rather than rolling my own. Invalid bundles go to a dead-letter queue with an alert, never into the database. Valid ones are stored, and the whole bundle is written in one transaction, so a failure never leaves a partial record.

For the lab reports: send the image to a vision model with structured outputs, so the response has to match a strict schema -- test name, value, unit, reference range, date. Then map each result to a FHIR Observation that references the patient, and run it through the same validation. The risk is hallucination, so I'd check that each extracted value actually appears in the source, sanity-check units and ranges, and route anything low-confidence to human review.

For de-identification: strip direct identifiers like names, birth dates, contact details, and addresses below the state level, and replace IDs with a keyed hash like HMAC, so the same patient always maps to the same pseudonym and references still line up.

A couple of questions I'd ask up front: do you only ever get data from the one supplier, and where does de-identification need to happen -- in production, or only for the copy that leaves it?
```

> So for each resource, you're proposing a record in the database where we store that record?

```
Yes -- one row per FHIR resource. The key is the resource's ID, which also keeps references between resources resolvable. The main column is the raw resource as JSONB. Keeping the raw resource makes it the source of truth, so anything else can be re-derived later without re-ingesting.

Rather than a table per resource type -- FHIR has well over a hundred -- I'd use one table with a resource_type column and pull a few fields out into indexed columns for the most common lookups: the patient reference, the effective date, and the version. A GIN index on the JSONB covers ad-hoc queries. If something turns out to be slow, you add a generated column for it later.

Writes are upserts keyed on ID and version, so reprocessing the same bundle is harmless, and each bundle is written in a single transaction.
```

> Do you know structured outputs?

```
Yes. Structured outputs let you give the model a JSON Schema and constrain its output to match it. Instead of asking nicely for JSON and hoping, the decoding itself is restricted, so the response always parses and has the required fields and types. OpenAI exposes it as a JSON schema response format in strict mode, and with Anthropic you get the same effect by defining a tool with an input schema and requiring the model to call it.

For this challenge, that means I define a schema for a lab result -- test name, value, unit, reference range, date -- send the image, and get back data I can map straight to FHIR Observations.

The important caveat is that structured outputs guarantee the shape, not the truth. The model can still produce a perfectly valid object with the wrong number. So I'd still validate the content: check that each extracted value appears in the source, sanity-check units and ranges, validate the final FHIR, and keep a labeled set of real reports to measure extraction accuracy whenever the prompt or model changes.
```

### Preparation

```
Hey Chris,

We really enjoyed reviewing your profile, we'd love to move forward with a hands-on technical session. How does your week look? Are you available tomorrow or Wednesday?I'd like to book about an hour of your time for a practical working session. Feel free to use whatever tools make you most productive: AI assistants, your favorite Python frameworks, whatever helps you think and build.

The Goal:
We work with FHIR bundles (healthcare data in JSON format) and need to build robust data pipelines to process and prepare this data for downstream systems.
What we'd like to explore with you:

-   Parsing & organizing FHIR data - How would you approach extracting and structuring the relevant clinical information from raw FHIR bundles?
-   De-identification strategy - Healthcare data requires careful handling. How would you approach stripping PHI while preserving data utility?
-   Pipeline robustness - What strategies would you use to ensure reliable, fault-tolerant data processing at scale?
-   Database ingestion - How would you prepare and validate the processed records for a patient who are fully deidentified before an ML engineer uses this data to fine tune a model?

This isn't about writing production code in an hour - it's about thinking through the problem together and seeing how you approach data engineering decisions.
Looking forward to hearing from you.

Best,
Cuau
```

### Retrospective

Went pretty well except for technical difficulties. *Really* need to buy a new computer. Will buy a Mac Mini when I go back to AR in March.

I think they would likely want a follow-up actually, but… They are exclusively in-office, so even with a relocation package and competitive pay, this is a no-go. They basically told me there is zero chance of any hybrid setup.

## Declination

```
Hey Cuau,

That makes total sense, and I appreciate the transparency.  Unfortunately, I won't be able to commit to a full-time in-office schedule at this time.

That said, I really enjoyed the conversation and the role is a strong fit for me.  If anything changes on your side (e.g., a remote-first exception, a phased approach, or a short-term contract while we reassess relocation later in the year), please keep me in mind -- I'd love to revisit.

Thanks again.

Best,
Chris
```
