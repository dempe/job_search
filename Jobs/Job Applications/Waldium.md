---
type: job
applied: 2025-12-04
interviews:
  - 2025-12-11 11:00
  - 2025-12-19 11:00
status: rejected
job_type: fulltime
source: workatastartup
position: Founding Engineer
contract: false
remote: false
4day: false
industry:
website:
location: San Francisco, CA
company_size:
recruited: false
listing: https://www.Workatastartup.Com/jobs/85114
blog:
correspondence:
compensation: $120K - $200K  •  0.30% - 1.00%
title: Waldium
date_created: "2025-12-04 14:17"
date_modified: "2026-01-19 11:53"
---

## Application

```
Hi Shivam,

I'm Chris. A backend engineer with 9 YOE.  I specialize in data pipelines and distributed systems.  What really caught my eye with your listing is that I built a distributed web scraping framework for a previous employer (DataRank YC13).

I'm currently running my own company shipping React Native/Typescript apps end-to-end on AWS serverless but looking to re-join a team environment.  I'd love to hear more about the role!

Let me know if you're available for a quick chat!

Best,
Chris
```

## Technical Interview Preparation

Layout for project descriptions:

- The **goal** was `X`.
- The **constraints** were `A` and `B`.
- We **chose** `Y` because it **minimized** `Z`.
- The **tradeoff** was `W` , which we **accepted** because `V`.
- In retrospect, I'd **revisit** `Q` once the **constraints change**.

Three projects I will prepare for:

- Kafka ETL
- Current app dev
- Distributed web scraper
- (Optional backup): API gateway

### Kafka ETL

Tentative layout:

```
The goal was to move from slow, fragile batch ingestion to near–real-time data availability.
The constraints were growing volume and downstream consumers needing freshness without coordination.
We chose Kafka because it minimized coupling between producers and consumers and allowed replay.
The tradeoff was operational complexity, which we accepted because reliability and flexibility mattered more than simplicity at that scale.
In retrospect, I’d revisit parts of the schema strategy once producer contracts stabilized.
```

- **Goal**
- **Constraints**
- **Choice**
- **Minimization**
- **Tradeoff**
- **Retrospect**
- **Changing constraints**

### App Development

Tentative layout:

```
The goal was a focused, fast mental-math app that didn’t require accounts or onboarding.
The constraints were solo development time and long-term maintainability.
I chose React Native because it minimized duplicated effort across platforms.
The tradeoff was weaker platform-specific polish, which I accepted to ship and iterate.
In retrospect, I’d revisit some abstractions once feature velocity slowed.
```

- **Goal**
- **Constraints**
- **Choice**
- **Minimization**
- **Tradeoff**
- **Retrospect**
- **Changing constraints**

### Distributed Web Scraper

- **Goal**
- **Constraints**
- **Choice**
- **Minimization**
- **Tradeoff**
- **Retrospect**
- **Changing constraints**

Tentative layout:

```
The goal was to extract structured data reliably from a large number of known sites.
The constraints were highly heterogeneous HTML, site-specific behavior, and a fixed downstream data model.
We chose a framework where each site had its own crawler implementation behind a shared interface.
This minimized cross-site fragility and kept failures localized to individual crawlers.
The tradeoff was duplicated logic and higher maintenance cost, which we accepted to gain correctness and debuggability.
In retrospect, I’d revisit shared abstractions once patterns across crawlers became clearer.
```

```
When I first join the data ingestion team, we had one-off crawlers for various sites. The queue was hopelessly backed up, and was difficult to add new sites.

The goal was to allow customers (including in-house data analysts) to submit sites to be scraped and have data and analytics for those sites in ~1 week (easy to add new data sources) and to clear the backlog of URLs to crawl.

The constraints were 1) to not affect current data ingestion 2) to not spend more than 6 weeks 3) a fixed downstream data model 4) highly heterogenous HTML (sometimes requiring JavaScript execution).

We had four servers that we rented for dedicated crawling purposes. This provided me with ample parallelization ability.

I designed a new queue in MySQL.  it had the URL to be crawled, when it was added, and a priority number (1 - 5).  Aside from that, we had a DLQ for pages that did not have a suitable crawler or errored out.  We also kept a log of all URLs crawled, their associated crawler, and when they were crawled.  Transactions provided a nice means of making sure that two crawlers did not pick up the same URL.

Due to pagination or adding separate pages for products and comments, the crawlers, themselves, added items to the queue.  Apart from that, we had dedicated seeders for each website that would run periodically and add lots of URLs for specific sites to the queue.

There was a "bot controller" that 1) pulled a URL from the queue and used regexes to determine the correct cralwer to pass the URL to.  it was multi-threaded, so we had many threads running on each of the four servers.

when a crawler finished crawling a page, it transformed the data into the canonical comment model and persisted it to HBase where we later performed twice daily batch analytics jobs on the data.  if the page was crawled successfully, we updated the log.  if not, we updated the DLQ.
```

At a very high level, we basically used the Producer->Consumer pattern, where the seeders and crawlers were the producers (added to the queue) and the orchestrator was the consumer (read from the queue).

![[Pasted image 20251216215101.png]]
