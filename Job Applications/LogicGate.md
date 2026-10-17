---
type: job
applied: 2026-10-16
job_type: fulltime
channel: form
status: awaiting-reply
interviews:
source: linkedin
listing: "https://www.logicgate.ai/company/careers/?gh_jid=4743005005"
company: LogicGate
position: "Senior Software Engineer: Back-end"
contract: false
remote: true
compensation: $125,000 - $165,000 per year + variable + equity + benefits
title: LogicGate
date_created: "2026-10-16 18:33"
date_modified: "2026-10-16 18:33"
---

## Application

> What's one thing about migrations that frustrates you as a service scales and how do you architect around it?

```
The older a system gets, the less the existing data matches what the schema says. A migration might be trivial against a clean dev database, but in prod it gets complicated with years of legacy rows in production.

I ran into this at Dekstech, adding partial payments to an internal app we use to estimate projects and pay our engineers. Legacy payments had a `PAID` or `CONFIRMED` status without the corresponding flags set, so a naive backfill of the new `amountPaid` column would have produced wrong totals, and people would have gotten paid twice or not at all. I did it in stages: normalize the legacy status flags first, then backfill only the payments that were actually paid, then recompute every estimate's totals from the payment rows themselves, the source of truth. I also pulled the payment math out of the controllers into its own module with unit tests for underpayment, overpayment, and failed or cancelled submissions.

So the way I architect around it is to keep derived state recomputable from a single source of truth, break migrations into small, verifiable stages, and put schema changes through CI and code review like any other code. At Octimine, for example, I set up a peer-reviewed CI/CD pipeline for our Elasticsearch schema updates, which cut down on conflicts and made deployments faster and safer.
```
