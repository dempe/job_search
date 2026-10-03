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
Backend, and specifically the integration layer -- APIs, webhooks, and the data modeling behind them. I enjoy solving problems at the intersection of scalability, reliability, and maintainability. I really got interested in those types of problems after readying Designing Data Intensive Applications.

However, I do work across the stack. I shipped React apps both mobile and Shopify embedded apps.
```

> What project are you most proud of from your recent role? Why?

```
Payment middleware I built for a health-wearable brand. They sold through Shopify, but their payment gateway wasn't one Shopify Payments supports, and their processor's license was expiring. If checkout went down, the store stopped taking money.

I built a Node/TypeScript service that brokered payments between the store and the gateway's hosted checkout, then reconciled the result back to Shopify so orders were marked paid, voided, refunded, or cancelled correctly. Since it was touching payments, it was imperative that my code was correct. I scoped an idempotency key to each payment session and reused it across retries, so a retried request couldn't double-charge anyone.

I'm proud of it for two reasons. The first is that we made the deadline with zero interruptions. The second is that it was touching payments, so it demanded a type of correctness that I'd never been held to before. It was stressful at times, but I got through it with a lot of TDD and rigorous designs.

Oh, and coffee.
```
