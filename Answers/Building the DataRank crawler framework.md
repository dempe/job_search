## Archy

Source: [[Archy]]

> Please tell us about a time you identified a technical bottleneck or a looming scalability issue that others had overlooked. How did you build a case for fixing it, and what was the measurable impact on the system's performance or reliability?

```
When I joined DataRank, our web crawlers were a collection of ad hoc scripts run manually across four servers. Adding a new data source meant SSH'ing in and editing scripts by hand.

I made a case for fixing it by proposing a plan: a centralized queue of URLs to be crawled, have an orchestrator and a pool of crawlers on each server such that the orchestrator would pull from the queue and distribute the work to the first crawler whose canHandle() method returned true.

After implementation, adding a new data source went from manual server edits to a simple redeploy (using Jenkins back in those days). We onboarded two junior engineers shortly after who could contribute new crawlers independently without touching server configuration.
```

## HireGlide

Source: [[HireGlide]]

>  Makes sense. Describe a project where you had to make tradeoffs between getting something out the door vs making it perfect. What did you choose and why?

```
i worked for a company that needed to gather a large amount of data from web scraping. they had a few one-off crawlers, but we needed a framework to spin up new crawlers quickly, easily, and in a distributed manner. we didn’t yet know which sources would actually matter long-term, and building a fully generic pipeline upfront would have required weeks of abstraction work with a high risk of guessing wrong. I chose to accept some duplication and tighter coupling in the initial version rather than over-abstracting early. I built a concrete pipeline optimized for the first few data sources, with clear boundaries, but intentionally deferred generalized plugin systems and advanced configurability. We shipped sooner, uncovered real usage patterns, and avoided building flexibility we didn’t need. once the requirements stabilized, we refactored the hot paths into shared components with much better confidence about what actually needed to be generic. our data analysts were happy and our customers were happy. end users care about data. they don't care if the system that got them data is perfect or not as long as they have the data they want
```

## JustPaid

Source: [[JustPaid]]

>  What is one thing you have built in the past? Please describe your product and what it did.

```
One company I worked for needed to ingest large amounts of data from the web from forums, review sites, and other sites that didn't have a readily available API.  I built a distributed web scraper in Java that had a queue of URLs to crawl.  Each worker would pull a URL off the queue (a MySQL table) and determine the correct crawler to use.

Everything was built in Java using generics, so it was really easy to spin up new data sources, allowing us to ingest more and more diverse comment data to perform product market analytics for our clients.
```
