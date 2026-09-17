## Rivora

[[Rivora]]

> Tell us about the last bug you fixed where a type system, type annotations, or a linter caught something before it reached users. What was the bug, and what would have broken if it had shipped?

```
At Dekstech, I work on an internal app we use to estimate projects and pay our engineers. I was adding the ability for managers to mark payments as paid after a discussion, which meant reworking the payments page.

The old payments page typed payments as `any`, so the compiler never actually checked them. When I typed the page against our `Payment` type, `tsc` showed ~30 errors. The frontend type had drifted from the database! It listed a `COMPLETED` status that our Prisma schema never had (the real statuses are `PAID` and `CONFIRMED`), and it was missing fields the API was already returning, like `isPaid`, `amountPaid`, and `approvalStatus`. For example, TypeScript flagged `payment.status === "PAID"` as a comparison that could never be true.

The client build runs `tsc` before `vite build`, so this failed the build instead of reaching users. I updated the types to match the schema, and everything compiled.

If it had shipped with the old types, the UI would have been written against a status the API never returns. Paid and confirmed payments would have shown the wrong status badges, and developers would never have seen the button to confirm they'd been paid.
```
