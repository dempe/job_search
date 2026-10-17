## Beacon Biosignals

[[Beacon Biosignals]]

> In a few sentences sentences, describe a tricky database migration or schema change you led. What was the blast-radius risk and how did you mitigate it?

```
At Dekstech, I work on an internal app we use to estimate projects and pay our engineers. I added support for partial payments, which meant adding an `amountPaid` column to payments and changing how each estimate's paid and remaining totals are derived.

The blast radius was every payment and estimate row in the database. Payments only had the amount they were submitted for, and legacy rows had a `PAID` or `CONFIRMED` status without the corresponding boolean flags set, so a naive backfill would have produced wrong paid totals, and people would have gotten paid twice or not at all.

I did it in stages in one migration: normalize the legacy status flags first, then backfill `amountPaid` only for payments that were actually paid, then recompute every estimate's `amountPaid`, `remainingAmount`, and `paymentStatus` from the payment rows themselves, the source of truth. I also isolated the math out of the controllers into its own module with unit tests covering underpayment, overpayment, and failed or cancelled submissions.
```

## LogicGate

[[LogicGate]]

> What's one thing about migrations that frustrates you as a service scales and how do you architect around it?

```
The older a system gets, the more legacy data it accumulates, which makes new migrations tougher. A migration might be trivial against a clean dev database, but in prod it gets complicated with years of legacy rows.

I recently ran into this exact scenario at Dekstech when I was adding support for partial payments to our internal app. Legacy payments had a `PAID` or `CONFIRMED` status without the corresponding flags set, so a naive backfill of the new `amountPaid` column would have produced wrong totals.

I split the migration into phases: normalize the legacy status flags, backfill, and recompute each estimate's totals from the source of truth, the payment rows.

To architect around it, *keep derived state recomputable* from a single source of truth, break migrations into small, verifiable stages, and put schema changes through CI and code review like any other code. 
```
