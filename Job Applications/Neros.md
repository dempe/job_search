---
type: job
applied: 2026-10-23
job_type: fulltime
channel: form
contact:
status: awaiting-reply
interviews:
source: linkedin
listing: "https://job-boards.greenhouse.io/nerostechnologies/jobs/5265805007?gh_src=a44e27377us"
company: Neros
position: Senior Software Engineer
contract: false
remote:
compensation: $180,000 – $252,000 USD
title: Neros
date_created: "2026-10-23 13:59"
date_modified: "2026-10-23 13:59"
---

## Application

> Any additional information you would like to share?

```
A lot of my work has been building against interfaces I didn't control. At DataRank, I built a distributed Java framework for consuming social media APIs with generic token pools and rate limiting, so we could quickly add new APIs. More recently, I built a Node.js/React app for a B2B distributor on top of Shopify's Admin API, which only returns the last 60 days of orders. A live query would have silently dropped exactly the lapsed accounts the tool existed for, so I designed a Postgres projection refreshed in the background to keep them visible.

On a payment integration, scoping surfaced several ambiguities in the provider's API docs that I got resolved with the provider before writing code. I covered the payment flow with 32 tests against a stubbed gateway, proving a declined or interrupted payment could not strand an order in a paid-but-unfulfilled state. Since it was touching payments, it was imperative that my code was correct.

I'm currently working as a contractor, but looking to re-join a team where I can have more collaboration and ownership.
```
