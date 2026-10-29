---
type: job
applied: 2026-10-29
job_type: contractor
channel: recruited
contact:
status: interview
interviews:
- 2026-10-30 13:00 - 13:30
source: inbound
listing: https://jobs.ashbyhq.com/aescape/28f86607-2017-4a05-bc86-b196a0f34086
jd: "[[Job Descriptions/Aescape (1)]]"
company: Aescape
position: Senior Backend Engineer
contract: true
remote: true
compensation:
title: Aescape (1)
date_created: "2026-10-29 11:11"
date_modified: "2026-10-29 17:23"
---

## Application

Dan said that I did not have to submit a formal application, but I took a look at it anyways. Many of the questions have changed slightly since my last application or are net new.

I figured that it would be a good idea to have an answer to each, even though it's not necessary.

### Questions

> Please describe your most recent production Golang experience: what you built, roughly when, and for how long.

```
My most recent production Go was at SimplyMeasured (later Sprout Social), from 2016 through mid 2018. Most of the backend there was in Go and Java. I designed and built APIs and microservices in Go and Spring Boot, sitting behind an API gateway I set up to centralize auth, rate limiting, and request transforms.

So it's been a while. Since then I've worked mostly in typed languages (TypeScript, Java, Kotlin), and I'd expect it to take me a few weeks to get fluent in Go again.
```

> Describe a third-party API integration you built and shipped in production.

```
At Dekstech, I built a greenfield Node.js middleware on Heroku connecting a client's Shopify store to their new payment provider, ahead of a hard deadline to migrate off their old processor. Customers paid through the provider's hosted checkout, and the middleware reconciled each checkout session with its Shopify order.

During scoping, I noticed the API docs warned not to treat redirects to `/payment/success` and `/payment/cancelled` as definitive, whereas the provider's CTO directly told me otherwise. I trusted the docs more on this issue as it both aligns with Stripe's stance and just makes sense — a user could leave the page before redirect, a network error could happen, or you could visit the URL directly. They eventually added a webhook for payment reconciliation at my (and my client's) urging before launch day. 

Since it was touching payments, it was imperative that my code was correct. Each payment session got its own idempotency key, reused across retries, so a retry couldn't double-charge anyone. Gateway errors were mapped to typed errors, so a decline was handled differently from a transient gateway failure. Every request boundary was validated with schema parsing, and 32 tests against a stubbed gateway proved that a declined or interrupted payment couldn't leave an order paid but unfulfilled.
```

> Please share your AI tools experience. E.g. Cursor, Claude Code, etc.

```
I mostly use Codex and Opus, but use DeepSeek for lighter weight stuff.  I use the OpenCode harness in addition to the TUIs for Opus and Codex.

As for how I actually use AI, I have a pretty detailed, constantly-evolving workflow that's really a chain of model-agnostic skills:

scope -> plan -> execute -> verify.  `scope` takes a loosely defined problem and turns it into a more formally defined problem in terms of functional and non-functional requirements, constraints, assumptions, and risks, and outputs `scope.md`.

The next phase is `plan`.  It reads `scope.md`, and builds an implementation plan in `plan.md`, making sure all requirements and dependencies are fullfilled.

There is a lot of back-and-forth with the AI on these first two phases, but it really helps narrow down *what* exactly we're trying to solve and *how* we will solve it.

Since so much time is invested in scoping and planning, the execution and verification phases usually go by pretty quickly, since we know exactly what we need to do by that point.
```

> Why Aescape?

```
```

## Interview 1

### Preparation

#### Stories

Dan mentioned that he wants to hear about my recent contracting work, so I better make sure I have those stories down pat.

##### Payment Integration App

##### Interactive Customer Map App

##### Athena Math (Focusing on Infrastructure)
