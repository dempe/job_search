---
type: job
applied: 2026-10-02
job_type: fulltime
recruited: false
status: awaiting-reply
interviews:
source: matcha
listing: "https://job-boards.greenhouse.io/fleetio/jobs/5253664007"
company: Fleetio
position: Senior Software Engineer, Marketplace
contract: false
remote: true
compensation:
title: Fleetio
date_created: "2026-10-02 18:01"
date_modified: "2026-10-02 18:01"
---

## Application

> What area of full-stack web development do you find yourself gravitating towards the most? Why?

```
Backend, and specifically the integration layer -- APIs, webhooks, and the data modeling behind them.

I enjoy solving problems at the intersection of scalability, reliability, and maintainability, which is where backend work lives. The part I find most interesting is the seam between systems you control and systems you don't. That's where the hard problems are: a webhook that arrives twice, a third-party API that times out halfway through a write, a payment marked captured on one side and not the other. Getting that right means thinking about idempotency, retries, reconciliation, and what the data should look like when one side is wrong.

A recent example: a B2B coffee distributor needed their sales team to see which wholesale accounts had gone quiet. The obvious approach was to query Shopify live, but Shopify's Admin API only reliably returns about 60 days of orders, so a customer who lapsed months ago produces no rows at all -- exactly the accounts the tool existed to surface. I designed a Postgres projection refreshed in the background, merging recent orders with stored history, so lapsed accounts stay visible regardless of the API window.

I do work across the stack -- I've shipped a React Native app and the React frontend for that distributor's app -- but the frontend is the newer half of my experience, and the backend is where I'm strongest.
```

> What project are you most proud of from your recent role? Why?

```
```
