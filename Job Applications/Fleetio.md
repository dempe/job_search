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
Backend, and specifically the integration layer -- APIs, webhooks, and the data modeling behind them. I enjoy solving problems at the intersection of scalability, reliability, and maintainability.

However, I do work across the stack. I shipped a React Native app and the React frontend for that distributor's app -- but the frontend is the newer half of my experience, and the backend is where I'm strongest.
```

> What project are you most proud of from your recent role? Why?

```
Payment middleware I built for a health-wearable brand. They sold through Shopify, but their payment gateway wasn't one Shopify Payments supports, and their processor's license was expiring. If checkout went down, the store stopped taking money.

I built a Node/TypeScript service that brokered payments between the store and the gateway's hosted checkout, then reconciled the result back to Shopify so orders were marked paid, voided, refunded, or cancelled correctly. Since it was touching payments, it was imperative that my code was correct. I scoped an idempotency key to each payment session and reused it across retries, so a retried request couldn't double-charge anyone, and mapped the gateway's errors by type so a decline was handled differently from a transient failure. I covered the flow with 32 tests against a stubbed gateway, specifically to prove that a declined or interrupted payment couldn't leave an order sitting in a paid-but-unfulfilled state.

I'm proud of it for two reasons. The first is that the deadline was real and we made it -- checkout stayed live. The second is the kind of correctness it required: most of the work was reasoning about what happens when one of the two systems fails partway through, and that's the work I find most satisfying.
```
