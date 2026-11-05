---
type: interview
application: "[[Job Applications/Waldium]]"
company: Waldium
round: 2
date: 2025-12-19 11:00
kind:
interviewers:
outcome:
title: Waldium - Interview 2
date_created: "2026-11-04 18:10"
date_modified: "2026-11-04 18:10"
---

### Transcript

![[Transcripts/Waldium - Interview 2]]

### Questions

Model answers, not a record of what was said.

> Could you highlight two or three big projects you've worked on over the years, whether at your current consultancy or a previous company? When did you solve something deeply technical and challenging?

```
Three come to mind.

At DataRank I built a distributed crawling framework. It used a MySQL work queue, site-specific crawlers chosen by regex, and HBase for storage, and it took us from a hopelessly backed-up queue of one-off scripts to a system where analysts could add a new site and get data within about a week.

At Octimine I replaced a weekly Python batch job with a Kafka Streams pipeline. It handled about 30 million patent documents a week and made data available in near real time instead of days later. I added a dead-letter queue and ran the unit tests in CI as regression tests, so a bad record or a bad change couldn't silently corrupt the index.

At SimplyMeasured I built the API gateway in front of our microservices, which centralized auth and routing. And more recently, in my own company, I built and shipped an iOS app end to end on a serverless AWS backend, including server-side purchase verification.

The crawler is the one most relevant to you, so I'm happy to go deep on it.
```

> Let's dive into the distributed crawler and the API crawler. What was it for, how did you build it, and how did you approach the problem?

```
DataRank was about five people, and I was the second engineer. We sold insight into what people were saying online about a topic, so we needed two kinds of ingestion: social APIs like Facebook and Twitter, and web content like forums and review sites. Everything had to land in one comment model, because all of our analytics ran against it. When I joined, the web side was a pile of one-off crawlers, and the backlog was huge.

The goal was to let analysts and customers add a new site and see data within about a week, without disrupting existing ingestion. We had four rented servers and no cloud. So I put the work queue in MySQL, which we already ran: each row had the URL, a priority, and a timestamp, and transactions guaranteed that only one worker could claim a URL. A multithreaded orchestrator on each server pulled URLs and dispatched each one to the crawler whose canHandle regex matched it. Crawlers parsed the page into the comment model, wrote it to HBase, and enqueued follow-up URLs like the next page or a comment thread. Per-site seeders kept the queue full, and failures went to a dead-letter table. A crawl log with checksums told us when a page had actually changed.

The API side was a separate framework. It took the same topics and ran them as queries against each platform, using pools of tokens so we could stay within each platform's rate limits.

The tradeoff was one crawler per site, which meant more code to maintain. We accepted it because failures stayed local to one site, and parsing precision mattered more than generality for our data model.
```

> Was this a proactive or reactive crawling system? Did you set the crawler loose on the web in general, seed it with certain links, or did you always have to give it a link and it crawled that page and some associated pages?

```
Reactive and seeded. We never crawled the open web. Customers told us which topics and sites they cared about, and we wrote a seeder per site that found the URLs that held the data -- listing pages, forum indexes, product pages. Our analysts could also drop specific URLs onto the queue directly.

From there it was bounded discovery. A crawler could enqueue new URLs, but only the kinds it expected -- the next page of a thread, or a product's comment pages -- and only on sites we had crawlers for. Anything no crawler could handle went to the dead-letter table instead of growing the crawl. Seeders also ran on a schedule, and the checksum log meant re-crawls only produced new records when the content had actually changed.
```

> What exactly was this [DataRank crawler framework] for? Was it for building an internal search engine, or for extracting structured data so your analysts or customers could build BI dashboards?

```
Structured data for analytics. The product answered "what are people saying about X?" Customers defined topics, first with Boolean queries and later with a custom query language, and we matched them against everything we collected.

Everything went into HBase in one comment model: the text, author, timestamp, source, and the page it belonged to. MapReduce jobs on top ran NLP -- sentiment, entity and co-occurrence analysis -- and wrote the results to Elasticsearch, which backed our API and the customer dashboards. One example: Walmart's customer insights team found that people kept mentioning a hot sauce together with ranch dressing. They ran a campaign shelving the two together, and it worked.

So search was part of the stack, but the goal was aggregated insight rather than finding individual documents.
```

> What would you say were the distinctions between crawling an API versus crawling the web? When you say crawling an API, is there some recursive part -- pagination, or moving through Facebook's social graph to someone's friends?

```
They're different problems. Web crawling is discovery: you start from a page, follow links, and have to work out what's on each page and how to parse it. The structure is implicit and different on every site, and it changes without warning.

With an API, the schema is documented and the data is already structured, so there's no parsing guesswork. The hard parts move elsewhere: authentication, rate limits, and quotas. Our API work was really querying, not crawling. We ran each customer's topics as searches against each platform and paged through the results with cursors. There was some light recursion -- pulling the comments or replies under a matching post -- but no traversal of the social graph.

So the engineering focus was different. For the web it was parser robustness and the queue. For the APIs it was a pool of tokens so we could spread requests across accounts, backoff when we got throttled, and saving the pagination cursor so a failed job could resume where it stopped instead of starting over.
```

> Let's say I want to ingest NASA data sets that have no API. A page lists 20 data sets, and each one is about 10 PDFs zipped together -- say, images of lunar rock samples with metadata about them. How would you build an automated system to fetch all of that and store it? What structure would you want at the end, and where would it live -- still in object storage, a relational database, relational with links to the objects, a document store? Assume you have oracles, like AI agents, that can do things like PDF parsing and structured extraction.

```
I'd work backwards from what the app developer needs. At the end I want a relational table in Postgres -- one row per sample, with typed columns for the fields we're sure of, like sample ID, mission, collection site, rock type, and weight -- plus a JSONB column for fields that vary between data sets. The images and PDFs stay in S3, and each row points to them by key. That gives the app real queries and joins, keeps the large binaries out of the database, and lets the schema grow without a migration for every new field.

The pipeline has stages, each idempotent and each recording its progress in a manifest table:

First, fetch. Scrape the index page for data set links, download each zip into an S3 raw area keyed by a content hash, and record the source URL, ETag, and hash. Re-runs skip anything unchanged.

Second, unpack. Extract the PDFs and images into S3, with one manifest row per file.

Third, schema discovery, which is a one-time oracle step. Give the oracle a sample of documents and have it propose the schema. A human reviews that schema once, and that review is the contract.

Fourth, extraction. For each PDF, the oracle takes the document and the schema and returns JSON, a confidence score, and where in the document each value came from. We validate the JSON against the schema. Anything that fails or comes back with low confidence goes to a review queue instead of the table.

Fifth, load. Upsert into Postgres keyed on sample ID.

I'd always keep the raw files and record which model and prompt version produced each row. When the extraction gets better, we can re-run that stage over everything without re-crawling.
```

> What if getting the PDF or data set requires agentic behavior, like entering a code, logging in, or getting past a CAPTCHA? What would an agent-first ETL pipeline look like compared to a traditional one, and what are the inputs and outputs we'd need from the agents?

```
I'd treat the agent as a fetcher with a narrow contract. Its input is a starting URL, a goal like "download every data set on this page," and the credentials it's allowed to use. Its output is the same thing a traditional fetcher returns: a list of files written to S3, with the source URL for each, plus a log of the actions it took so we can audit and replay them. Everything downstream doesn't care whether a script or an agent did the fetching.

A login or a confirmation click is fine -- that's our own account doing what a person would do. A CAPTCHA is a different case. It's there specifically to stop automation, so I wouldn't build the system around beating one. I'd look for a bulk download or API, ask the provider for access, or have the agent pause and hand that step to a human.

The bigger difference with agent-first ETL is where the judgment sits. A traditional pipeline hard-codes the navigation and the parsing rules. Here an agent does navigation, schema discovery, and extraction, so every agent step needs a validation step after it -- schema checks, confidence thresholds, sample audits -- because agent output isn't deterministic. And I'd still run agents per item from a queue, with retries and a dead-letter queue, exactly like any other worker.
```

> What would the tradeoffs be between a batch pipeline and an event streaming pipeline here, for ingesting and structuring these PDFs? If I just needed it done, how would you explain the benefits of each approach to me?

```
For a fixed set of 20 data sets, batch. It's simpler to build, easy to re-run from scratch when we improve the extraction, and easy to reason about cost: run it, check the results, done.

If the source keeps growing -- new data sets show up and people want them quickly -- I'd make it event-driven. When a new file lands, it triggers the next stage. But I'd do that with a plain queue, one message per document, not a stream processor like Kafka Streams. Each PDF is processed independently, so there's no windowing or aggregation that would need stream processing. A queue gives us parallel workers, retries, and a dead-letter queue for the documents that fail.

I'd only reach for real streaming, like the Kafka pipeline I built at Octimine, when we need continuous aggregates over a high-volume feed, or many independent consumers of the same events.

So, to you as the stakeholder: batch gets you correct data the cheapest way. Event-driven gets you fresh data, at the cost of more moving parts. And the stages can be identical either way, so we can start with batch and switch later without rewriting them.
```

> Our data sources might include Google Drive, Slack, GitHub, and Jira or Linear. They're all accessible by APIs, but very different structurally. Even forgoing the AI part, how would you effectively build "Elasticsearch" over them? Would you pull all the data into a centralized store, push each search down to the source APIs, or put a unifying abstraction over them so the querying system doesn't know where things come from? These sources are constantly being updated.

```
I'd put a unified abstraction on top, but not commit to all-push or all-pull underneath.

The abstraction: every source exposes the same small interface -- list, read, search, and resolve a reference. Each result has a common envelope: source, ID, URL, title, author, timestamps, permissions, the text, and the parent it belongs to, like the channel, repo, or folder. The query side never knows where a result came from.

Under that, I'd index centrally where search quality matters and the volume is manageable. Slack threads, docs, and tickets go into one index, kept fresh incrementally -- Slack's Events API, Drive's changes feed, GitHub webhooks, Jira webhooks -- with a periodic full re-sync to catch anything the events missed. The upside is fast, consistently ranked search across everything, which pushing down can't give you, because every source's search API ranks differently and some are weak. The cost is that we become the steward of a copy of the customer's data, with sync lag and storage.

For things that are huge or change constantly, like the full contents of a code repo, I'd index lightweight metadata and push the reads down to the source at query time.

Permissions have to travel with every document. Results get filtered to what the asking user can see in the source system. In a product like this, that's not optional.
```

> At what granularity would you structure the Elasticsearch documents? Would one document be a GitHub repo, a file, a class, or a function? One Google Doc, or a subsection of it? A Slack thread, a full channel, or a paginated channel? What are the tradeoffs, and are there auxiliary indices you'd need to build?

```
I'd chunk each source along its natural structure, and keep a link back to the parent.

Code: one document per symbol -- a class, function, or method -- parsed with a real parser like tree-sitter, so we never split a function in half. Each chunk carries its file path, its enclosing class, and its signature. Files are too big and too mixed to rank well. Single lines have no context.

Google Docs and Confluence: split by heading section, with the doc title and heading path attached to every chunk. A whole doc is too coarse. A paragraph loses its meaning.

Slack: one document per thread. A thread is the unit of a conversation. A whole channel mixes unrelated topics, and single messages are often meaningless on their own, like "yep, that fixed it." Long threads get windowed.

Jira and Linear: one document per ticket, with its comments.

The tradeoff with granularity: small chunks rank precisely and fit in a context window, but lose their surroundings. Large chunks keep context but rank badly. Storing the parent ID gets us both -- match on small chunks, then expand to the parent when we need context.

For auxiliary indices, I'd build three. First, a symbol index of code definitions and references, like a light LSP or ctags. Second, an entity and mention index mapping names like class names, ticket IDs, and people to every document that mentions them. Third, an embedding index alongside BM25, so we can do hybrid search, because natural-language questions and exact identifiers need different kinds of matching.
```

> If we treat agents as oracles, what would they do? Would they scan the full GitHub repo, every doc in your drive, every Slack channel and thread? Would we use the same chunking strategy for all three sources or different ones? We can't naively chunk the first 50 characters, then the next 50, and so on.

```
Different chunking per source, and deterministic wherever the structure is already known. Code has an AST, docs have headings, and Slack has threads. Parsers are cheap, fast, and predictable, so I wouldn't pay an LLM to rediscover structure we can parse.

Where the oracle earns its keep is on top of the chunks, at ingestion. For each chunk, it writes a short summary, extracts the entities and references it mentions -- "this thread is about the retry logic in PaymentClient" -- and tags it. Those become the edges between sources: the Slack thread that discusses a class, and the ticket that changed it. That's what a keyword index alone can't do.

I wouldn't have agents scan whole repos or drives on every query. That's slow and expensive, and large context windows still lose detail in the middle. Ingestion does the per-chunk work once, incrementally as things change. At query time, the agent searches and reads only what it needs.

The one case for the oracle doing the chunking itself is unstructured long text, like a doc with no headings or a giant transcript, where it can split on topic changes.
```

> Say I have a question about a specific class. A keyword search finds where it's mentioned, but what if an instance is used somewhere without the class name -- say a singleton exported at the end of a file and passed around elsewhere? How would you do a multi-step search rather than a one-level search -- by building an index on ingestion, a special kind of query, or something else?

```
Both, but mostly at ingestion, because that's where it's cheap and deterministic.

At ingestion, I'd build a symbol graph of the code with a real parser, the way an IDE does: definitions, references, imports, and exports. So if the file that defines PaymentClient exports a singleton called client, the graph records that client is an instance of PaymentClient, and every file importing client gets an edge back to the class. Then "find everything related to this class" becomes a graph traversal: its definition, everything that references it directly, everything that references its instances, and its subclasses and implementations. Mentions in Slack, docs, and tickets link to the same graph through the entity index.

At query time, the search is iterative. Search, read the results, notice a new identifier, search again, and stop when the question is answered or a budget runs out. The agent drives that loop, but it calls tools backed by the graph -- go to definition, find references, find mentions -- rather than plain keyword search.

The graph handles the precise, structural hops. The agent handles the fuzzy ones, like a Slack thread that says "the payments thing" without naming the class.
```

> Say the question is how class Chris and class Shivam relate. You get 30 documents mentioning each one, and you have an LLM oracle that can reason over context. How would you build this mini RAG system? If the oracle were a person who could scan the files, how would you instruct them?

```
I'd give the agent the question and a small set of tools, and let it loop.

The tools would be: search across all sources, go to definition, find references, and read a document. The instructions would be roughly: "First, find where each class is defined, and work out the language and how relationships show up in it -- inheritance, interfaces, composition, or one class calling the other. Read both definitions. Then check the direct relationships: does one extend, implement, hold, or call the other? Then look at the documents where both appear together, and at the code paths that connect them. Then check Slack and tickets for why they relate. Stop when you can answer, and cite the document behind every claim."

On the system side, I wouldn't dump all 60 documents into context. I'd rank them first: documents that mention both classes come first, then the definitions, then call sites. The agent reads the top few, and decides whether it needs more. That keeps the context small and focused, and it's the same pattern Cursor and Claude Code use -- search, read, refine, and answer with citations.

Then evaluation. I'd build a set of questions with known answers, so we can tell whether a change to the chunking, ranking, or prompt actually makes answers better.
```

> Have you used Cursor or Claude Code?

```
Yes, I use Claude Code every day. Beyond asking it to write code, I've built custom skills for it -- multi-step workflows with strict rules that read context from a set of notes and produce structured output. I use it with a plan-first workflow: write the scope, have it plan, review the plan, then let it execute, with tests first so its output is checked.

What I've learned is that the quality comes almost entirely from the context and constraints you give it. Watching it work is useful for what you're building, too. It searches, reads a few files, searches again with what it learned, and only then answers. That's exactly the multi-hop retrieval loop we just talked about.
```

> Across the pillars -- the retrieval infrastructure, the knowledge base and agentic search, and the AI editor and writing part -- which interests you most, and which would you be happiest and most productive in?

```
I'd be most productive on retrieval infrastructure: the connectors, ingestion, indexing, and keeping everything in sync. That's what I've done at every job, so I'd be useful there in the first week.

What I'm most excited about is the agentic search on top of it, and those two meet. The agent is only as good as the tools and the indexes underneath it. So my ideal is to own the retrieval layer, and grow into agentic search by building the tools the agent calls and measuring how well it answers. The editor is the part I'd be least useful in early on, though at a company this size I'd expect to pitch in anywhere.
```

> This is a very small, scrappy founding engineering role, without the perks of a company with 20, 50, or 100 people. How do you feel about that -- is it something you're actively looking for, open to, or on the fence about?

```
It's what I'm looking for. My best years were at DataRank, a YC company where I was the second engineer, and at Octimine, which was a small team. In both, I owned whole systems end to end, and decisions happened in a conversation instead of a doc review. I interned at Walmart, so I've also seen the other end, where every small change needs a design document and sign-offs.

I'm also running my own company right now, so scrappy is normal. I do the engineering, the infrastructure, the support, and the business side. Talking to customers or sitting in on a sales call doesn't bother me. Hearing the problem firsthand is how you avoid building the wrong thing.
```

> Have you used Confluence before? Do you like it?

```
I've used it, and I don't have fond memories of it. The problem isn't the editor. It's that docs live apart from the work, so nobody updates them, they drift out of date, and search can't tell you which page is still true. People stop trusting it, and then they stop writing in it.

What's worked best for me is keeping docs next to the code -- decision records in the repo, versioned with the change that motivated them -- so updating the doc is part of the same pull request. That's really the problem you're describing: the knowledge already exists in code, Slack, and tickets. A tool that assembles and maintains docs from where the work actually happens fixes the root cause instead of asking people for more discipline.
```

### Preparation

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
