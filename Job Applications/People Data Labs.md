---
type: job
applied: 2026-10-22
job_type: fulltime
channel: form
contact:
status: interview
interviews:
  - 2026-10-29 12:30 - 13:00
  - 2026-11-03 14:00 - 14:45
source: matcha
listing: "https://jobs.ashbyhq.com/people-data-labs/5108aa65-f7cc-4d41-92fe-a3a5373d705d"
company: People Data Labs
position: Senior Software Engineer, Data Acquisition
contract: false
remote: true
compensation: $160K - $200K
title: People Data Labs
date_created: "2026-10-22 15:11"
date_modified: "2026-11-04 17:24"
---

## Application

> Briefly describe your web crawling experience

[[Building the DataRank crawler framework#People Data Labs|Building the DataRank crawler framework]]

> How do you handle anti-scraping mechanisms or bot detection while crawling?

[[Handling bot detection while crawling#People Data Labs|Handling bot detection while crawling]]

> Is there anything else you'd like us to know about you? (Optional)

[[Personal background and interests#People Data Labs|Personal background and interests]]

## Interview 1

### Transcript

![[Transcripts/People Data Labs - Interview 1]]

### Questions

Model answers, not a record of what was said.

> Why are you looking to leave?

[[Returning to a collaborative engineering team#People Data Labs|Returning to a collaborative engineering team]]

> What attracted you to the data acquisition role, and what have you done that overlaps with what we're doing? Have you done data acquisition in your previous jobs?

[[Data acquisition experience#People Data Labs|Data acquisition experience]]

> What tools or strategies have you used for web crawling at scale?

[[Building the DataRank crawler framework#People Data Labs (crawling at scale)|Building the DataRank crawler framework]]

> Have you used any tools such as Scrapy, Selenium, or Puppeteer?

[[Building the DataRank crawler framework#People Data Labs (crawling tools)|Building the DataRank crawler framework]]

> How did you handle anti-scraping mechanisms or bot detection while crawling?

[[Handling bot detection while crawling#People Data Labs (interview)|Handling bot detection while crawling]]

> How do you monitor the health of your crawlers and their long-term reliability?

[[Building the DataRank crawler framework#People Data Labs (crawler health monitoring)|Building the DataRank crawler framework]]

> Do you wish you had built the crawler status dashboard sooner?

[[Building the DataRank crawler framework#People Data Labs (status dashboard timing)|Building the DataRank crawler framework]]

> Have you worked with asynchronous programming in your crawlers?

[[Building the DataRank crawler framework#People Data Labs (asynchronous crawling)|Building the DataRank crawler framework]]

> Describe how you've structured unstructured or semi-structured data into a useful schema.

[[Designing the DataRank canonical data model#People Data Labs|Designing the DataRank canonical data model]]

> Are you interested in going back to data acquisition?

[[Data acquisition experience#People Data Labs (returning to data acquisition)|Data acquisition experience]]

> Are you comfortable with Python?

[[Backend language experience#People Data Labs|Backend language experience]]

### Preparation

#### Stories

##### Crawling at Scale

At DataRank, my first company, I set up the entire web scraping stack. When I joined, our crawlers were a collection of ad hoc scripts run manually across four servers. Every new data source started from scratch: its own job queue, its own threading, no reusable code, and no tests. Maintaining them meant SSH'ing in and editing scripts by hand.

I built a distributed framework around a single central job queue in a MySQL table. An orchestrator on each server pulled work off the queue continuously, handled the threading and parallelization, and announced work to the crawlers in its pool. Each crawler claimed work based on a `canHandle` regex against the URL, and crawlers could feed new pages to other crawlers in a chain. Crawlers implemented standard interfaces with the boilerplate extracted out, and everything was transformed into a common, canonical comment model.

Each site still needed custom crawling code, but the plumbing was already there. That took us from 5 or 6 sites to dozens in just a few months, and the two junior engineers we onboarded could add crawlers on their own, deployed through Jenkins.

Since crawlers broke constantly as sites changed their markup, I also added end-to-end system tests, which hadn't existed before, run from one central place. Later I turned that into a status dashboard so the customer success team could see which crawlers were broken.

One tradeoff I'd make again: I didn't build a fully generic plugin system up front. I built for the first few sources with clear boundaries, then refactored the hot paths into shared components once we knew what actually needed to be generic.

##### Bot Detection and Anti-scraping

First, figure out why the request is failing. A 429 means exponential backoff with jitter. The site might require logging in. If the site needs JavaScript to render, use a JavaScript-capable browser.

If there's an explicit CAPTCHA or access protection, stop the crawl and check whether there's API access.

I also build a circuit breaker into my crawlers, so they don't keep hitting a site that's blocking them. At DataRank, I turned Jenkins into a live status page for the crawler fleet, backed by automated system tests, so the customer success team could see for themselves which scrapers had broken after a site change instead of routing every question through an engineer.

##### Backpressure and Message-driven Design

At Octimine, I replaced a fragile weekly Python batch job processing about 30 million patent documents with a real-time, event-driven Kafka Streams pipeline in Java. Message-driven design is what made it durable. Each stage consumes at its own pace from a topic, so a slow stage falls behind and catches up instead of taking the whole run down. Records that failed went to a dead-letter queue, and everything else kept flowing. In the old batch job, it kept failing and retrying until it ran into the next week's job.

At DataRank, the backpressure came from the other side: the APIs we consumed. The social media API framework I built had generic token pools, rate limiting, and retry strategies, so we stayed within each platform's limits instead of getting cut off.

More recently, on my own app's serverless backend, failed operations go onto an SQS retry queue, with idempotent processing so a retry can never apply something twice.

##### Data Quality

At DataRank, the whole point of the ingestion layer was normalizing messy data from forums, review sites, and social APIs into one canonical model, so analysts were working with consistent data no matter where it came from.

At Octimine, I unit-tested every analytic in the Kafka Streams pipeline and ran those tests as regression tests in CI, so we could update analytics without risking data corruption. I also set up a peer-reviewed CI/CD pipeline for Elasticsearch schema changes.

At Dekstech, I added partial payments to an internal app, and legacy rows had a `PAID` or `CONFIRMED` status without the matching flags set, so a naive backfill would have produced wrong totals. I normalized the legacy flags first, then backfilled, then recomputed every derived total from the payment rows, the source of truth. The general principle: keep derived data recomputable from a single source of truth.

##### Browser Rendering and Network Debugging

At Dekstech, I audited a bedding retailer's Shopify storefront for Core Web Vitals. I traced their LCP regressions and redundant tracking traffic to third-party scripts, render-blocking legacy dependencies, and duplicate pixels injected through Google Tag Manager.

On another client, what was reported as a mislabeled tracking issue turned out to be a broken integration between the storefront and a third-party fulfillment platform. And on a third, I investigated an anomalous spike in third-party API events and traced the root cause to legacy server code.

##### Reliability and Observability

The one that stands out is at Octimine. The weekly batch job would fail and retry until it ran into the next week's job, which meant customers weren't getting their data. The long-term fix was the Kafka Streams pipeline with a dead-letter queue, so one bad document couldn't take the whole run down.

After every incident, I do a root-cause analysis and document how to recover, so anyone on the team can handle it next time. At Octimine, that turned into a whole set of recovery documentation, and it cut down on recurring on-call incidents.

On my own serverless backend, I set up structured logging, CloudWatch alarms, and SQS/SNS retries, so I'm alerted to failures immediately. And at DataRank, the Jenkins crawler status page meant broken scrapers were visible to the whole company, not just engineering.

## Interview 2

### Transcript

![[Transcripts/People Data Labs - Interview 2]]

### Questions

Model answers, not a record of what was said.

> Introduce yourself.

```
I've spent most of my 11 years in data ingestion -- what you call acquisition. At DataRank, I was the second engineer at a five-person startup, and I built the web crawling framework and a sister framework for social media APIs, all normalized into one canonical model. At SimplyMeasured, I moved more into API design and microservices in Go and Spring Boot.

After a couple of years teaching English in Mexico, I came back as a senior data engineer at Octimine in Munich, where I replaced a fragile weekly batch job over about 30 million patent documents with a real-time Kafka Streams pipeline. For the last few years I've run my own company -- an iOS app with a serverless AWS backend, and contract work building Node.js apps and AWS infrastructure for clients.
```

> Pick something relevant that you've worked on and take me through it: the business case and why you built it, the architecture of the solution, the role you played, and any challenge you faced and how you overcame it.

```
At Octimine, we sold patent analytics -- things like citation counts and how technologically similar two patents are -- through an API and a UI. All of it came from a weekly Python batch job that ran for over 48 hours. When it failed, it restarted from scratch, and sometimes it ran into the next week's run. That meant a lot of hours spent babysitting it, and customers getting stale data. Meanwhile the data was arriving in our provider's Postgres warehouse continuously, in partial updates -- a title one day, citations another -- so recomputing everything once a week didn't fit the data at all.

I made the case for an event-driven pipeline and built it in Kafka Streams. A source connector read the warehouse's write-ahead log, so every change landed in a source topic. We deserialized the XML into one canonical record per patent family, then fanned out to independent processors, one per analytic. Each one emitted a partial update to Elasticsearch, keyed by family ID, applied with doc_as_upsert, so Elasticsearch was an eventually consistent view of everything. Failed records went to a dead-letter topic instead of stopping the run, and every analytic had unit tests that ran as regression tests in CI. Because the analytics were decoupled, one breaking didn't take down the others -- you fixed it and replayed.

I designed and built it. I left Germany before it cut over to production -- I gave my six months' notice and finished in staging -- but in staging it was clearly more reliable than the batch job.
```

> You said the original job was janky and took a lot of time to support. What specifically about the original architecture made it janky and difficult to support?

```
Three things. First, it was one long monolithic run -- thousand-line Python scripts with no tests -- so any failure meant restarting the whole 48-hour job. Second, it recomputed everything every week, even though only a small fraction of patents had changed, so the cost and the failure surface scaled with the whole dataset instead of with what changed. Third, nothing was isolated: a bad record or one broken analytic could fail everything downstream, and because it wasn't written by software engineers, figuring out where it failed and what state it left behind took real digging.

Before the rewrite, I split it into phases in CI, so we could restart just the stage that failed, like the Postgres and Elasticsearch loads, instead of the whole thing. That bought time, but the real fix was making the work incremental and isolated, which is what the streaming design did.
```

> The data comes in as XML. What did the transformed data model end up looking like?

```
Everything was keyed by patent family ID. A family is the same invention filed in different countries and languages, so for analytics, the family is the unit that matters, not the individual publication.

Each family record had the raw, non-derived fields -- title, abstract, IPC classification codes, citations, dates -- in one canonical structure. Since updates arrived in pieces, each field was latest-value-wins: a new citation update replaced the old one without touching the title. The derived analytics were separate, computed downstream from that record, and written to Elasticsearch as their own fields on the same family document.
```

> When you say normalized, do you mean normalized in the database sense, or something else?

```
Something else -- I should have said canonical or standardized. I meant converting the XML into one consistent shape per patent family, with the same field names and formats no matter which update it came from. It wasn't database normalization; if anything, the Elasticsearch documents were deliberately denormalized, with everything about a family in one document so the API could read it in a single lookup.
```

> You mentioned Postgres as your warehouse, but you're also loading Elasticsearch. What was the purpose of each, and how did you use them?

```
The Postgres warehouse belonged to our data provider. It was the source of truth for raw patent data, and we didn't choose it -- we consumed changes from it.

Elasticsearch was our serving layer. It powered the API and the UI, because customers were searching across patents and filtering by classification and other fields, which is what Elasticsearch is built for. The pipeline's job was to keep it current.

There was also an internal Postgres. The batch job had used it as scratch space between stages, so the new pipeline didn't need it, but the data scientists relied on it for analysis. So we kept it, with a clear agreement: it was best-effort, and if you needed the latest production data, Elasticsearch was the source.
```

> You didn't get to see it go all the way to production. Did you face any particular challenges building the new system, and how did you work through them?

```
The hardest one was the technological-distance analytic, which scores how similar two patents are so customers doing competitive analysis can find related patents. It needed two inputs from different places: backward citations, which lived in Neo4j for graph traversal, and IPC codes from the family record.

The first problem was keys. Citations referenced individual publication numbers, but everything else was keyed by family ID, so they couldn't join. The fix is to re-key citations to family ID through a publication-to-family mapping, so both sides are co-partitioned on the same key before the join.

The second was windowing. I'd built it as a stream-stream join, and those only match records that arrive within the same time window. If citations arrived in week one and IPC codes in week three, they never joined. The right design is a table-table join: materialize each input as a KTable, the latest value per family ID, backed by a compacted changelog topic. Then an update to either side recomputes the score against the current value of the other, no matter when it arrived. I'd identified that as the fix but hadn't finished it when I left.
```

> How do you feel about the work acquisition does, as I've described it? Does it sound like something that fits well with what you're interested in working on?

```
Yes, very much. Crawling, standardizing, light enrichment, and then building update queues to tell the crawlers what to do next is the same loop I built at DataRank. Our crawlers fed new URLs back into the central queue, and everything landed in one canonical model. The difference is scale, and doing the standardization in Spark streaming, which is new to me and something I'd like to learn.

It's also the part of the data stack I've enjoyed most. The sources change under you, the data's messy, and the job is making it come out complete and correct.
```

> Have you worked hands-on with web crawling yourself? Talk to me about what you were crawling.

```
Yes, it was my first big project. At DataRank, we collected what people said online about consumer products -- forums, review sites, niche communities like fishing or video game forums -- so brands could do sentiment and demographic analysis. For example, we found that people talking about ranch dressing were often also talking about Tabasco, and Walmart's insights team ran a trial pairing them that helped sales.

When I joined, crawlers were ad hoc scripts, each run by hand on one of four servers. I built a framework with one central URL queue in MySQL. An orchestrator on each server pulled from the queue and offered each URL to a pool of crawlers, which claimed it with a regex-based canHandle rule. Crawlers could push new URLs back onto the queue, so pagination and follow-up pages were processed asynchronously. That let us write only the site-specific parsing, and it took us from 5 or 6 sites to dozens in a few months.
```

> With agents trying to crawl everything these days, sites are putting up more and more barriers to crawling. Did you face any challenges in being able to crawl what you wanted, and how did you overcome them?

```
Back then, the main problem wasn't blocking -- it was breakage. Sites changed their markup or ran A/B tests, so a crawler would suddenly get a page it was never written for. I handled that with end-to-end system tests for every crawler, run centrally in Jenkins, which later became a status dashboard. For rate limits, we used exponential backoff with jitter, and for login walls, we automated the login.

Today the barriers are much stronger, and I'd handle it in tiers: start with plain HTTP, escalate to a headless browser like Playwright only when a page needs JavaScript, keep per-domain rate limits and a circuit breaker so a crawler that's getting blocked backs off instead of making it worse, and rotate proxies and user agents where it's appropriate. Each site's success rate and yield should be monitored, since it's whack-a-mole -- what worked last month stops working. And if a site explicitly forbids crawling, that's a stop. Then it's a conversation about an API or a data partnership.
```

> How does AI fit into your ideal workflow as a developer today?

```
I use a four-step flow: scope, plan, execute, review. Scoping turns a loose problem into explicit requirements, constraints, assumptions, and risks. Planning turns that into an implementation plan that covers every requirement. Those two steps get most of the back-and-forth with the AI, so execution is usually straightforward. During execution, I make it work test-first -- a failing test for each task, then the code, then make it pass -- and the review step checks the result against the original requirements.

It's the same process I used before AI, just faster. And I own everything I put up for review, whether I typed it or an agent did. If I can't explain a line, it doesn't go in the PR.
```

> What would you rate your level of proficiency with Python?

```
About a 7. I'm comfortable writing idiomatic Python and I've used it throughout my career -- batch processing at Octimine, data pipelines in CI, parts of the API gateway at SimplyMeasured, an Anki add-on I published. But my day-to-day lately has been TypeScript and Java, so I'm brushing up before the coding round.
```

> We host a bit on-prem, and occasionally that means SSHing into a system, finding logs, and figuring out what's going on if something's not working. What would you rate your level of proficiency with Linux?

```
About an 8. I live in a terminal, and I've done exactly that kind of work: at DataRank, our crawlers ran on four on-prem servers, and at Dekstech, I set up a client's production EC2 environment -- reverse proxy, process management, SSL, deploys. So SSHing in, reading logs with journalctl, grep, and tail, checking processes, disk, and memory, and restarting services is routine for me. Where I'm thinner is deep kernel or network tuning.
```

> Do you have any experience with Spark and/or Databricks, specifically in production?

```
No, neither in production. The closest experience I have is Java MapReduce jobs over HBase at SimplyMeasured, and Kafka Streams at Octimine, which has a lot of the same concepts: partitioning by key, co-partitioning before joins, repartitioning being expensive, and stateful aggregations. So I understand why a shuffle costs what it does. The PySpark API and Databricks tooling would be new, and it's the first thing I'd ramp up on.
```

> Have you used pandas at all?

```
Not in any real way. Most of my data work has been in SQL, Java, and Kafka Streams. The DataFrame model -- select, filter, group by, join, aggregate -- maps closely to SQL, which I'm comfortable with, so I'd expect to pick up pandas and the PySpark DataFrame API quickly.
```

### Preparation

#### Hiring Manager Interview with Jake Berry

Tuesday, Nov 3, 2:00–2:45 (45 min).

##### Who Jake Is

- Manages data acquisition and the Platform team (build tools, CI/CD, AWS infrastructure, logging and monitoring). The recruiter also said he manages SRE.
- He's also a hands-on data engineer in PySpark. He rewrote PDL's core entity resolution in PySpark, cut days off build time by better task sequencing and job tuning, and led customer-centric data quality improvements.
- Self-rated expert in application architecture, AWS (serverless, EC2, CloudFormation), and AWS analytics (Glue, EMR, Athena, Redshift). Intermediate in Python and SQL.
- Values: hiring and keeping strong people, playing to people's strengths, clear priorities, learning from failure, curiosity and tinkering, working sustainably. He's spent years managing enterprise and ERP systems, so he'll care about systems that are maintainable and easy to operate.

##### What He'll Probably Dig Into

- **The crawler framework, in depth.** The orchestrator and `canHandle`, the shared queue, how the system tests caught breakage, what I'd do differently today (async I/O, Scrapy/Playwright instead of my own plumbing).
- **Data quality.** This is his area. Lead with storing raw data so a fixed parser could re-run without a re-crawl (I missed this on the screen). Then the canonical model with source IDs for dedupe and traceability, and the Octimine analytics regression tests.
- **Reliability and operations.** He runs Platform/SRE. The Octimine batch-to-Kafka-Streams story (DLQ), the recovery documentation that cut recurring incidents, monitoring crawlers for silent degradation (yield dropping, required fields going null), not just errors.
- **CI/CD and build time.** He cut days of build time, so he'll appreciate:
  - the peer-reviewed CI/CD pipeline for Elasticsearch schema changes at Octimine
  - adding recurring tasks to CI/CD there
  - GitHub Actions + SAM with automated deploys and rollbacks
  - Jenkins at DataRank

##### AWS: Know What I Built Cold, and Don't Bluff the Rest

He's the expert in the room. He won't need me to know every service. He'll notice if I overclaim.

Know these well, including *why* I chose each:
- Serverless backend (Athena Math): Lambda, API Gateway, DynamoDB, SQS/SNS, CloudWatch alarms, SAM/CloudFormation, GitHub Actions.
  - Idempotent writes for duplicate notifications, conditional writes for out-of-order notifications (lifetime beats subscription, later subscription wins), SQS retries with a DLQ.
  - Be ready for Lambda tradeoffs: timeouts, cold starts, concurrency limits, when I'd move to containers instead.
- EC2 production deploy at Dekstech: reverse proxy, process management, SSL, migrations, repeatable deploys.
- CloudFront + OAC with signed cookies replacing public S3 ACLs.
- AWS Certified Developer – Associate (2024).

Gap: Glue, EMR, Athena, Redshift, and Spark. I haven't used them in production. Read up on the basics so I can follow the conversation, and say plainly that they're new to me:
- S3 as a data lake, partitioned Parquet, Athena querying S3 directly, Glue as catalog and ETL, EMR as managed Spark.
- Spark basics: partitions, shuffles, why joins are expensive, why sequencing and tuning jobs saves time.
- Closest real experience: Java HBase MapReduce jobs at SimplyMeasured, and Kafka Streams joins, windowing, and compaction at Octimine.

##### Questions for Jake

- What's the biggest reliability problem on the data acquisition side right now? (The recruiter said to ask him.)
- What does on-call look like for this team?
- How do you find out a crawler is broken or quietly degraded today?
- How do you measure data quality for acquisition, and how does it flow back from entity resolution? (He rewrote it.)
- How do data acquisition and Platform split ownership of crawler infrastructure?
- What would a strong first 90 days look like for this role?

#### Live Python Coding Round

The step after this interview. 1 hour on CoderPad: about 15 minutes of conversation, then two exercises in order (finish the first to get the second). Not finishing isn't held against me.

##### What to Practice

I don't know the exercises. For a data acquisition team, plausible themes are parsing and cleaning messy records, deduplicating or merging records about the same person, counting and grouping, processing a stream or file, and maybe a rate-limited or concurrent fetcher.

- Standard library until it's automatic:
  - `collections` (`Counter`, `defaultdict`, `deque`)
  - `heapq`, `itertools`, `dataclasses`
  - `json`, `csv`, `re`
  - generators, `sorted(…, key=…)`
- Live-coding habits: restate the problem, ask about edge cases, get a simple version working first, then improve it. Talk through it. Test with quick `assert`s on small inputs.
- Timed practice: a few medium, data-processing-style problems at about 25 minutes each, in a plain editor without autocomplete.
