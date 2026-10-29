## Archy

[[Archy]]

> Please tell us about a time you identified a technical bottleneck or a looming scalability issue that others had overlooked. How did you build a case for fixing it, and what was the measurable impact on the system's performance or reliability?

```
When I joined DataRank, our web crawlers were a collection of ad hoc scripts run manually across four servers. Adding a new data source meant SSH'ing in and editing scripts by hand.

I made a case for fixing it by proposing a plan: a centralized queue of URLs to be crawled, have an orchestrator and a pool of crawlers on each server such that the orchestrator would pull from the queue and distribute the work to the first crawler whose canHandle() method returned true.

After implementation, adding a new data source went from manual server edits to a simple redeploy (using Jenkins back in those days). We onboarded two junior engineers shortly after who could contribute new crawlers independently without touching server configuration.
```

## HireGlide

[[HireGlide]]

>  Makes sense. Describe a project where you had to make tradeoffs between getting something out the door vs making it perfect. What did you choose and why?

```
i worked for a company that needed to gather a large amount of data from web scraping. they had a few one-off crawlers, but we needed a framework to spin up new crawlers quickly, easily, and in a distributed manner. we didn’t yet know which sources would actually matter long-term, and building a fully generic pipeline upfront would have required weeks of abstraction work with a high risk of guessing wrong. I chose to accept some duplication and tighter coupling in the initial version rather than over-abstracting early. I built a concrete pipeline optimized for the first few data sources, with clear boundaries, but intentionally deferred generalized plugin systems and advanced configurability. We shipped sooner, uncovered real usage patterns, and avoided building flexibility we didn’t need. once the requirements stabilized, we refactored the hot paths into shared components with much better confidence about what actually needed to be generic. our data analysts were happy and our customers were happy. end users care about data. they don't care if the system that got them data is perfect or not as long as they have the data they want
```

## JustPaid

[[JustPaid]]

>  What is one thing you have built in the past? Please describe your product and what it did.

```
One company I worked for needed to ingest large amounts of data from the web from forums, review sites, and other sites that didn't have a readily available API.  I built a distributed web scraper in Java that had a queue of URLs to crawl.  Each worker would pull a URL off the queue (a MySQL table) and determine the correct crawler to use.

Everything was built in Java using generics, so it was really easy to spin up new data sources, allowing us to ingest more and more diverse comment data to perform product market analytics for our clients.
```

## People Data Labs

[[People Data Labs]]

> Briefly describe your web crawling experience

```
At DataRank, my first company, I set up the entire web scraping stack. We were creating bespoke crawlers for various websites (mostly forums) that transformed scraped content into a common, canonical comment model.

They needed a way to spin up new crawlers for new websites quickly.

I built a distributed framework that consisted of a central job queue in a MySQL table.  A orchestrator that ran on each server would pull from the queue and announce the work to available crawlers in its pool.  Crawlers would accept the work based on a `canHandle` regex rule based on the URL.  They could then feed new pages to new crawlers in a chain if needed for further processing.

This allowed us to scale our bespoke scraping framework to dozens of websites in just a few months (was only about 5 or 6 before my framework).
```

## People Data Labs (asynchronous crawling)

[[People Data Labs]]

> Have you worked with asynchronous programming in your crawlers?

```
Yes. At DataRank, each orchestrator managed a bounded thread pool of crawlers. Work ran concurrently, and when the pool was full, the orchestrator stopped pulling from the queue until crawlers freed up. That bounded pool was effectively our backpressure -- we never pulled more work than we could process.

Crawling is I/O-bound, almost all waiting on the network, so today I'd do it with async I/O instead of threads -- in Python, asyncio with an async HTTP client like aiohttp or httpx. The same principles apply: a semaphore to cap total concurrency, separate per-domain limits so one site doesn't eat the whole budget, bounded queues between stages for backpressure, and timeouts and retries on every request so one slow site can't stall everything.

I've also built asynchronous systems outside crawling: the Kafka Streams pipeline at Octimine, and an SQS-based retry system on my own app's serverless backend.
```

## People Data Labs (crawler health monitoring)

[[People Data Labs]]

> How do you monitor the health of your crawlers and their long-term reliability?

```
Crawlers break constantly, because sites change their markup. Sites also run A/B tests, so a crawler can suddenly get a version of the page it was never written for. So monitoring has to catch breakage you didn't cause.

At DataRank, I added end-to-end system tests for every crawler, which hadn't existed before, run centrally through Jenkins on a schedule. A failing test meant a site had changed. Later I turned that into a status dashboard the customer insights team could check themselves, with alerts to us including the error.

Today I'd add a few things: metrics on success rate, yield, and latency per source, so a crawler that quietly returns half as many records gets flagged even if nothing errors. Data-quality checks on the output, like required fields suddenly going null. And a failure queue with the error attached, so we can fix the crawler and replay what we missed.
```

## People Data Labs (crawling at scale)

[[People Data Labs]]

> What tools or strategies have you used for web crawling at scale?

```
The main strategy was separating the plumbing from the crawling logic, so we only ever wrote the part that was specific to a site.

At DataRank, every crawler used to be built from scratch and run by hand on a server. I built a framework with a single central job queue of URLs in MySQL. An orchestrator on each of our four servers pulled from the queue continuously, managed a thread pool of crawlers, and offered each URL to them. Each crawler had a `canHandle` rule matched against the URL, claimed the work, parsed the page, and could pass new URLs on to the next crawler in a chain asynchronously via the central job queue. Crawlers implemented standard interfaces with the boilerplate extracted out.

That scaled horizontally -- more throughput meant adding another server running an orchestrator, with no changes to the crawlers. It took us from 5 or 6 sites to dozens in a few months.

For fetching, we escalated through browsers by cost: a plain lightweight HTTP client first, then a headless browser that executes JavaScript, then a full browser through Selenium, only when the cheaper options failed. Failed URLs went to a failure queue instead of being dropped.
```

## People Data Labs (crawling tools)

[[People Data Labs]]

> Have you used any tools such as Scrapy, Selenium, or Puppeteer?

```
Selenium, yes -- heavily. It drove the browser tiers in our framework, from headless with JavaScript up to a full browser with a custom user agent when we needed it.

I haven't used Scrapy or Puppeteer in production. Our framework was custom because when we built it, around 2013, the off-the-shelf options didn't fit what we needed. If I were building it today, I'd look hard at Scrapy for the plain HTTP crawling, since it already handles scheduling, throttling, and retries, and Playwright for anything that needs a real browser. I'd rather use a well-tested framework than maintain my own plumbing, and spend our code on what's specific to our sources.
```

## People Data Labs (status dashboard timing)

[[People Data Labs]]

> Do you wish you had built the crawler status dashboard sooner?

```
Not necessarily. The status dashboard was more a problem of growth that manifested later as our collection of scrapers grew and grew.  The framework allowed us to grow and grow, and as we grew our data sources, problems became more frequent (changes in Markup, A/B testing, etc.).

We built out the tests that drove the dashboard from day 1, so, in a sense, we did start building the dashboard from the beginning.  But I think that focus on the UI manifestation would have been premature optimization.  We needed to focus on expanding our data sources after the framework was complete, and that's exactly what we did.
```
