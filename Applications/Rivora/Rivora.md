---
type: job
applied: 2026-09-14
job_type: contractor
channel: form
status: rejected
interviews:
  - 2026-09-18 14:00
source: wellfound
listing: https://wellfound.com/jobs?job_listing_slug=4697979-backend-engineer-5-8-years
company: Rivora
position: Backend Engineer (5-8 years)
contract: true
remote: true
compensation: $135k – $177k • No equity
title: Rivora
date_created: "2026-09-15 10:58"
date_modified: "2026-09-28 18:07"
---

## Questions

### Tell us about the last bug you fixed where a type system, type annotations, or a linter caught something before it reached users. What was the bug, and what would have broken if it had shipped?

At Dekstech, I work on an internal app we use to estimate projects and pay our engineers. I was adding the ability for managers to mark payments as paid after a discussion, which meant reworking the payments page.

The old payments page typed payments as `any`, so the compiler never actually checked them. When I typed the page against our `Payment` type, `tsc` showed ~30 errors. The frontend type had drifted from the database! It listed a `COMPLETED` status that our Prisma schema never had (the real statuses are `PAID` and `CONFIRMED`), and it was missing fields the API was already returning, like `isPaid`, `amountPaid`, and `approvalStatus`. For example, TypeScript flagged `payment.status === "PAID"` as a comparison that could never be true.

The client build runs `tsc` before `vite build`, so this failed the build instead of reaching users. I updated the types to match the schema, and everything compiled.

If it had shipped with the old types, the UI would have been written against a status the API never returns. Paid and confirmed payments would have shown the wrong status badges, and developers would never have seen the button to confirm they'd been paid.

### Describe a specific time you used an AI coding assistant (Copilot, Cursor, Claude, ChatGPT, whatever you use) on a real task recently. What did it get right, and what did you have to fix or reject?

I recently used Claude Code to build out a Node.JS app for a client's payment provider. The app needed to sync payment data between the provider and Shopify. Since it was touching payments, it was imperative that my code was correct.

I use a scope->plan->implement->review cycle built from skills. First, I give the agent a rough overview of the problem in Markdown (mostly what the client said and my own interpretations/follow-up questions). The `scope` skill formalizes that into concrete functional and non-functional requirements, and the `plan` skill turns those into an implementation plan. Both require a lot of back-and-forth with the model, but it helps me really understand the problem.

What it got right: this cycle surfaced a number of ambiguities in the provider's API documentation, which I was able to bring up to the provider and client and have reconciled. Then, once we hit the `implement` phase, it was mostly smooth sailing, since all the hard questions had already been addressed.

What I had to fix or reject: Claude wanted to hand-roll a SQL migration runner and a config loader when libraries already exist for those things. I rejected both and had it use off-the-shelf solutions. It also started editing the implementation before any test existed, so I stopped it and made it write a failing unit test first, then fix the code until the test passed.

In the end, it was a complete success, and the client was able to switch their payment provider before their existing contract ran out.

### Tell us about the last time you chose between an existing library/package and writing something yourself for the same problem. What did you pick, and why?

As mentioned in the previous answer, Claude wanted to hand-roll a custom SQL migration runner and a bespoke config loader for a client's payment app. I told it to use off-the-shelf libraries for both (`node-pg-migrate` for migrations and `envalid` for config validation).

I almost always choose to go with existing libraries, because it's less code to maintain and less surface area for bugs, especially when the libraries are well-used and thoroughly tested as was the case here.  Moreover, the app was touching payments, so it was critical that the code was correct.

That being said, I don't always pick the library. When I built my personal blog, I wrote my own static site generator instead of using someone else's. Mostly, because I wanted fine-grained control. Also since it was a personal project the stakes were much lower. It also turned out to be a great learning experience!

### Describe a time you had to work across two systems where one side didn't fully control the other, an API you didn't own, a data format shared with another service, anything like that. What broke or almost broke?

I built a Node.js/React app for a B2B coffee distributor to show the sales team lapsed or about-to-lapse customers via an Excel sheet and an interactive map.

The catch was Shopify's Admin API, which we didn't control. It only returns the last 60 days of orders. I.e., a customer who lapsed 3 months ago produces no  rows in a recent-orders query, so a live query would have silently dropped exactly the accounts the tool existed for.

To get around this, I designed a Postgres projection of customer and order data, refreshed in the background. Each refresh merges recent customers and orders with the stored projection (latest order date wins) and upserts the result. Customer provided historical seed data for the initial run, and the app runs off the projection instead of the API, keeping lapsed accounts visible beyond the 60 day window.

### Tell us about the last time you had to get productive in an unfamiliar codebase or tool within a few days, not weeks. What was your actual approach?

I was working on a contract for Teletone, an audio software company. They had  some proprietary audio file downloads (up to 30GB) sitting in S3, randomly public via ACLs. They needed them locked down. But their stack was Next.js on Vercel, Firebase/Firestore, and a Shopify Liquid theme. I hadn't used any of that before!

My first step was to start exploring the code and understanding the tech. I asked Claude questions about the codebase, recent commits, and had it ask ME questions to make sure I understood the part I was to update.

I then started experimented with the tools (installing Vercel CLI, for example), pulling down the env vars, calling the Firebase API, etc. making sure to not run any write or delete commands. I'm a big believer in learning by doing.

After I had a good understanding of how everything fit together, I started on a plan that met all the client's requirements. I worked with Claude on this and we went through a few iterations before I was happy. For example, I wanted a seamless rollback if anything didn't work.  All existing infra and data stayed in place, so that a rollback was as simple as `git revert && git push` (e.g., all S3 URLs remained in Firestore).

Within five days of starting, I had migrated their content to a single S3 bucket with prefix-based access behind CloudFront (OAC and signed cookies) and made the frontend updates to use it.

## Follow-Up

```
Hi Vera,

Thanks again for speaking with me last Friday. It sounds like you guys have a great product and a great team.

I just wanted see if there were any updates.  I'm still very interest in the role, so please let me know!

Thank you,
Chris
```

## Rejection

```
Hi Chris, thank you so much for following up.
After some careful consideration, we have decided to move forward with other candidates whose skills are more closely aligned with our current needs. However I'd love to stay in touch, and will happily reach out as more roles become available.
Wishing you the best!
Vera
```

### Follow-up

```
Hi Vera,

Thanks for letting me know.  That is totally understandable.

I'd definitely be happy to stay in touch. Any future senior backend opportunities related to in Java, Python, Node.js, AWS, distributed systems, and/or event-driven architectures may be a closer fit!

Wishing you and the team the best.

Chris
```
