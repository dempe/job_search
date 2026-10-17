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

I recently ran into this exact scenario at Dekstech when I was adding support for partial payments to our internal app. Legacy payments had a `PAID` or `CONFIRMED` status without the corresponding flags set, so a naive backfill of the new `amountPaid` column would have produced wrong totals.

Before adding a new migration, I had to normalize the legacy status flags, backfill, and recompute each estimate's totals from the source of truth, the payment rows.

To architect around it, *keep derived state recomputable* from a single source of truth, break migrations into small, verifiable stages, and put schema changes through CI and code review like any other code. 
```
