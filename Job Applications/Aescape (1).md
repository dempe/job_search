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
date_modified: "2026-11-04 17:20"
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

During scoping, I noticed the API docs warned not to treat redirects to `/payment/success` and `/payment/cancelled` as definitive, whereas the provider's CTO directly told me otherwise. I trusted the docs more on this issue as it both alignedWe were able to integrate the call to the webhook and test it in time for launch. with Stripe's stance and just makes sense — a user could leave the page before redirect, a network error could happen, or you could visit the URL directly. They eventually added a webhook for payment reconciliation at my (and my client's) urging before launch day. We built and tested the webhook handler in time for launch.

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

### Transcript

![[Transcripts/Aescape (1) - Interview 1]]

### Questions

Model answers, not a record of what was said.

> Tell me about what you've been working on recently.

```
For the past year, most of my work has come through Dekstech, a Shopify agency whose clients' backends have outgrown what a theme can do. They brought me in for some AWS work, liked it, and started giving me the backend projects.

The two that are most relevant here are greenfield apps I built from start to finish. One is a payment middleware connecting a client's Shopify store to a new third-party payment provider that Shopify didn't support, built against a hard deadline because their old processor contract was expiring. The other is an interactive customer map for a B2B distributor's sales team, which shows lapsed accounts and sweeps their region for new prospects. Both are Node.js on Heroku with Postgres, both integrate with Shopify's API, and both meant working against vendor APIs I didn't control.

Outside of that, I run my own iOS app, Athena Math, on a serverless AWS backend I built -- API Gateway, Lambda, DynamoDB, and SQS with a dead-letter queue -- which is where most of my thinking about retries and idempotency comes from.
```

> On the greenfield payment integration, what was the state of things when they gave it to you? How did you approach it, how did it go, and were there any tough problems you ran into?

```
It was truly greenfield -- no code, a new payment provider that looked like a young company, and a deadline because the old processor's contract was ending. I had direct contact with the provider's CTO, and their API docs.

The hard problem showed up while I was reading the docs. Like Stripe, the provider redirects the customer to a success or cancelled page after checkout, and the docs warned not to treat those redirects as proof of payment -- the customer can close the tab first, the network can drop, or anyone can visit the URL directly. But the docs didn't say what to use instead. When I asked the CTO, he told me to use the redirect.

I didn't want to block on it, so I built with payment confirmation behind one interface, which made swapping the source a small change later. Then I took the risk to the client in plain terms: orders could be marked paid when they weren't, or the other way around. He agreed, we went back to the provider together, and they moved a webhook up from their backlog. That's the right model -- we host the endpoint, and the provider calls it when a payment succeeds or is cancelled. We had the handler built and tested in time for launch.

Since it was touching payments, it was imperative that my code was correct. Each payment session had an idempotency key reused across retries, the webhook handler was idempotent on the payment ID so a duplicate delivery was a no-op, gateway errors were mapped to typed errors so a decline was handled differently from a transient failure, and 32 tests against a stubbed gateway proved an interrupted payment couldn't leave an order paid but unfulfilled.
```

> How did you hand it over at the end?

```
I build the handoff in as I go, so it isn't a scramble at the end. Every significant decision gets a short decision record in the repo -- what we chose and why, like the webhook instead of the redirect -- so whoever inherits it knows why it's built that way, not just how.

Everything was test-driven, so there's a test for each requirement, and that suite doubles as documentation of what the system is supposed to do.

Then I wrote two kinds of docs. One was for the store owner, who isn't technical: what the system does and what to do when something looks wrong. The other was for whatever engineer takes it over: how to run it, deploy it, debug it, and maintain it. That one lives in the repo so the next developer finds it where they'd look.

That's how I'd approach the handoff here too, adapted to your template and to the team taking it over.
```

> When was the last time you used Go?

```
Professionally, 2016 to mid 2018 at SimplyMeasured, which was later acquired by Sprout Social. Most of the backend there was Go and Java. I built APIs and microservices in Go behind an API gateway I set up for auth, rate limiting, and request transforms, so a lot of network-facing service code -- which is close to what these integrations are.

So it's been a while, and I won't pretend otherwise. Since then I've worked in other typed languages -- TypeScript, Java, Kotlin -- and Go is one of the quickest languages to get back into: the language is small, and gofmt and the standard library make Go code look the same everywhere. Before starting, I'd work through some exercises and read your service template, so I'd be productive in Go from the first week.
```

> When you're onboarding with a new client, are there things clients do that really set you up for success? What would a great onboarding and transition look like for you?

```
Mostly it's access and answers early. On day one: access to the repo, the service template, and the environments, plus whatever partner documentation and sandbox credentials exist for the first booking platform. Vendor sandboxes are often the slowest thing to get, and they block everything else.

Next, a named person for decisions -- for this, it sounds like Bill and Craig -- and a regular check-in, so questions don't pile up.

And a clear definition of done for each integration: which booking events have to sync, what the source of truth is when the two systems disagree, and what the team needs at handoff. With most of my clients I've had to draw that out myself, since they weren't technical. I write up what I think they need and ask them to correct it. With an engineering team as technical as yours, that should go much faster.
```

> Are you looking to continue doing contract work, or are you looking for full-time work now?

```
Honestly, both. Long term, I'm drawn to full-time for collaboration and ownership -- staying with the systems I build. But a greenfield engagement like this is the kind of contract work I like most, and a contract that could extend or convert is a good fit for what I want either way.

What matters for you: if I sign on for this, I finish it. Three integrations and a clean handoff is the commitment, and I'm not going to leave halfway through. If it turns into an extension or a full-time role, I'd be very interested.
```

### Preparation

#### Stories

Dan mentioned that he wants to hear about my recent contracting work, so I better make sure I have those stories down pat.

##### Payment Integration App

##### Interactive Customer Map App

##### Athena Math (Focusing on Infrastructure)
