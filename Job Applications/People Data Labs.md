---
type: job
applied: 2026-10-22
job_type: fulltime
channel: form
contact:
status: awaiting-reply
interviews:
source: matcha
listing: "https://jobs.ashbyhq.com/people-data-labs/5108aa65-f7cc-4d41-92fe-a3a5373d705d"
company: People Data Labs
position: Senior Software Engineer, Data Acquisition
contract: false
remote: true
compensation: $160K - $200K
title: People Data Labs
date_created: "2026-10-22 15:11"
date_modified: "2026-10-22 15:18"
---

## Application

> Briefly describe your web crawling experience

```
At DataRank, my first company, I set up the entire web scraping stack. We were creating bespoke crawlers for various websites (mostly forums) that transformed scraped content into a common, canonical comment model.

They needed a way to spin up new crawlers for new websites quickly.

I built a distributed framework that consisted of a central job queue in a MySQL table.  A orchestrator that ran on each server would pull from the queue and announce the work to available crawlers in its pool.  Crawlers would accept the work based on a `canHandle` regex rule based on the URL.  They could then feed new pages to new crawlers in a chain if needed for further processing.

This allowed us to scale our bespoke scraping framework to dozens of websites in just a few months (was only about 5 or 6 before my framework).
```

> How do you handle anti-scraping mechanisms or bot detection while crawling?

```
First, determine the cuase of the failure. A 429 requires exponential-backoff with jitter.  The site might require logging in.  Make sure you're using a Javascript-capable browser if the website requires it.

If there's an explicit Captcha or access protenction, stop the crawl and check if there's API access.

Also, I make sure that my crawlers have a circuit breaker built in so that they don't keep hitting a site that's blocking them. At DataRank, I even had a live dashboard built in Jenkins that showed crawler status (via automated system tests).  Mostly for the customer success team to get immediate info.
```

> Is there anything else you'd like us to know about you? (Optional)

```
Most of my career has been data ingestion. After DataRank, I was the senior data engineer at Octimine, where I replaced a fragile weekly Python batch job processing ~30 million documents a week with a real-time Kafka Streams pipeline in Java, including a DLQ and unit tests for every analytic.

I'm based in the US (Arkansas, Central Time) and work fully remote. I'm currently working as a contractor, but looking to re-join a team where I can have more collaboration and ownership.
```
