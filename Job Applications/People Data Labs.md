---
type: job
applied: 2026-10-22
job_type: fulltime
channel: form
contact:
status: interview
interviews:
  - 2026-10-29 12:30 - 13:00
source: matcha
listing: "https://jobs.ashbyhq.com/people-data-labs/5108aa65-f7cc-4d41-92fe-a3a5373d705d"
company: People Data Labs
position: Senior Software Engineer, Data Acquisition
contract: false
remote: true
compensation: $160K - $200K
title: People Data Labs
date_created: "2026-10-22 15:11"
date_modified: "2026-10-29 11:24"
---

## Application

> Briefly describe your web crawling experience

[[Building the DataRank crawler framework#People Data Labs|Building the DataRank crawler framework]]

> How do you handle anti-scraping mechanisms or bot detection while crawling?

[[Handling bot detection while crawling#People Data Labs|Handling bot detection while crawling]]

> Is there anything else you'd like us to know about you? (Optional)

[[Personal background and interests#People Data Labs|Personal background and interests]]

## Interview 1

### Preparation

#### Stories

##### Crawling at scale

At DataRank, my first company, I set up the entire web scraping stack. When I joined, our crawlers were a collection of ad hoc scripts run manually across four servers. Adding a new data source meant SSH'ing in and editing scripts by hand.

I built a distributed framework around a central job queue in a MySQL table. An orchestrator on each server pulled work off the queue and announced it to the crawlers in its pool. Each crawler claimed work based on a `canHandle` regex against the URL, and crawlers could feed new pages to other crawlers in a chain for further processing. Everything was transformed into a common, canonical comment model.

That took us from 5 or 6 sites to dozens in just a few months. Adding a new source went from manual server edits to a redeploy through Jenkins, and the two junior engineers we onboarded could contribute new crawlers on their own without touching server configuration.

One tradeoff I'd make again: I didn't build a fully generic plugin system up front. I built for the first few sources with clear boundaries, then refactored the hot paths into shared components once we knew what actually needed to be generic.

##### Bot detection and anti-scraping

First, figure out why the request is failing. A 429 means exponential backoff with jitter. The site might require logging in. If the site needs JavaScript to render, use a JavaScript-capable browser.

If there's an explicit CAPTCHA or access protection, stop the crawl and check whether there's API access.

I also build a circuit breaker into my crawlers, so they don't keep hitting a site that's blocking them. At DataRank, I turned Jenkins into a live status page for the crawler fleet, backed by automated system tests, so the customer success team could see for themselves which scrapers had broken after a site change instead of routing every question through an engineer.

##### Backpressure and message-driven design

At Octimine, I replaced a fragile weekly Python batch job processing about 30 million patent documents with a real-time, event-driven Kafka Streams pipeline in Java. Message-driven design is what made it durable. Each stage consumes at its own pace from a topic, so a slow stage falls behind and catches up instead of taking the whole run down. Records that failed went to a dead-letter queue, and everything else kept flowing. In the old batch job, it kept failing and retrying until it ran into the next week's job.

At DataRank, the backpressure came from the other side: the APIs we consumed. The social media API framework I built had generic token pools, rate limiting, and retry strategies, so we stayed within each platform's limits instead of getting cut off.

More recently, on my own app's serverless backend, failed operations go onto an SQS retry queue, with idempotent processing so a retry can never apply something twice.

##### Data quality

At DataRank, the whole point of the ingestion layer was normalizing messy data from forums, review sites, and social APIs into one canonical model, so analysts were working with consistent data no matter where it came from.

At Octimine, I unit-tested every analytic in the Kafka Streams pipeline and ran those tests as regression tests in CI, so we could update analytics without risking data corruption. I also set up a peer-reviewed CI/CD pipeline for Elasticsearch schema changes.

At Dekstech, I added partial payments to an internal app, and legacy rows had a `PAID` or `CONFIRMED` status without the matching flags set, so a naive backfill would have produced wrong totals. I normalized the legacy flags first, then backfilled, then recomputed every derived total from the payment rows, the source of truth. The general principle: keep derived data recomputable from a single source of truth.

##### Browser rendering and network debugging

At Dekstech, I audited a bedding retailer's Shopify storefront for Core Web Vitals. I traced their LCP regressions and redundant tracking traffic to third-party scripts, render-blocking legacy dependencies, and duplicate pixels injected through Google Tag Manager.

On another client, what was reported as a mislabeled tracking issue turned out to be a broken integration between the storefront and a third-party fulfillment platform. And on a third, I investigated an anomalous spike in third-party API events and traced the root cause to legacy server code.

##### Reliability and observability

The one that stands out is at Octimine. The weekly batch job would fail and retry until it ran into the next week's job, which meant customers weren't getting their data. The long-term fix was the Kafka Streams pipeline with a dead-letter queue, so one bad document couldn't take the whole run down.

After every incident, I do a root-cause analysis and document how to recover, so anyone on the team can handle it next time. At Octimine, that turned into a whole set of recovery documentation, and it cut down on recurring on-call incidents.

On my own serverless backend, I set up structured logging, CloudWatch alarms, and SQS/SNS retries, so I'm alerted to failures immediately. And at DataRank, the Jenkins crawler status page meant broken scrapers were visible to the whole company, not just engineering.
