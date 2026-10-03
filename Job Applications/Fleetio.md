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
date_modified: "2026-10-02 18:12"
---

## Application

> How did you hear about Fleetio and what compelled you to apply?

```
I found the listing through Matcha, which surfaces roles that match my background.

What compelled me to apply was the Marketplace team specifically. Most of my recent work has been integrations with systems I don't control -- Shopify, payment gateways, shipping and fulfillment platforms. Your marketplace is that same problem with more parties in it: fleets on one side, shops on the other, and approvals, service records, and payments passing between them. Getting that to behave correctly when one side is slow or wrong is the work I find most interesting, and I'd rather do it on a product I stay with than as a series of client projects.

It also helps that you hire in Mexico. I spend a good part of the year in Veracruz, where my wife is from, and very few US remote roles allow for that.
```

> What area of full-stack web development do you find yourself gravitating towards the most? Why?

```
Backend, and specifically the integration layer -- APIs, webhooks, and the data modeling behind them. I enjoy solving problems at the intersection of scalability, reliability, and maintainability. I really got interested in those types of problems after readying Designing Data Intensive Applications.

However, I do work across the stack. I shipped React apps both mobile and Shopify embedded apps.
```

> What project are you most proud of from your recent role? Why?

```
Payment middleware I built for a health-wearable brand. They sold through Shopify, but their payment gateway wasn't one Shopify Payments supports, and their processor's license was expiring. If checkout went down, the store stopped taking money.

I built a Node/TypeScript service that brokered payments between the store and the gateway's hosted checkout, then reconciled the result back to Shopify so orders were marked paid, voided, refunded, or cancelled correctly. Since it was touching payments, it was imperative that my code was correct. I scoped an idempotency key to each payment session and reused it across retries, so a retried request couldn't double-charge anyone.

I'm proud of it for two reasons. The first is that we made the deadline with zero interruptions. The second is that it was touching payments, so it demanded a type of correctness that I'd never been held to before. It was stressful at times, but I got through it with a lot of TDD and rigorous designing.

Oh, and coffee.
```
