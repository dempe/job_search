---
type: job
applied: 2026-09-16
job_type: fulltime
channel: form
status: ghosted
source: matcha
listing: "https://job-boards.greenhouse.io/beaconbiosignals/jobs/4407556009"
company: Beacon Biosignals
position: Senior Software Engineer
contract: false
remote: true
compensation: $150,000 – $170,000
title: Beacon Biosignals
date_created: "2026-09-16 19:05"
date_modified: "2026-09-16 19:35"
---

## Questions

### In 1-2 sentences, please tell us what drew you to apply to Beacon Biosignals.

Most of my career I've moved data around reliably, like what the Datastore team does with brain recordings. Since teaching English to underserved children, I've wanted a job with both challenging engineering problems *and* a fulfilling mission.

### In a few sentences sentences, describe a tricky database migration or schema change you led. What was the blast-radius risk and how did you mitigate it?

At Dekstech, I work on an internal app we use to estimate projects and pay our engineers. I added support for partial payments, which meant adding an `amountPaid` column to payments and changing how each estimate's paid and remaining totals are derived.

The blast radius was every payment and estimate row in the database. Payments only had the amount they were submitted for, and legacy rows had a `PAID` or `CONFIRMED` status without the corresponding boolean flags set, so a naive backfill would have produced wrong paid totals, and people would have gotten paid twice or not at all.

I did it in stages in one migration: normalize the legacy status flags first, then backfill `amountPaid` only for payments that were actually paid, then recompute every estimate's `amountPaid`, `remainingAmount`, and `paymentStatus` from the payment rows themselves, the source of truth. I also isolated the math out of the controllers into its own module with unit tests covering underpayment, overpayment, and failed or cancelled submissions.
