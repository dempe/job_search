---
title: Application notes record how the application reached the employer in `channel`
status: accepted
superseded_by:
---

# Context

Application notes track two different things: where the listing was found, and how the application got to the employer. `source` holds the first (`matcha`, `linkedin`, `wellfound`, ...). The second needs more than a yes/no for "was I recruited", since applications also arrive through referrals and through messaging a hiring manager directly.

# Decision

- Every note in `Job Applications/` has a `channel` field with exactly one of these values:
  - `form`: a normal application through the posting. The default.
  - `recruited`: the employer or a recruiter reached out first.
  - `referral`: someone inside the company referred the user.
  - `direct`: the user contacted the hiring manager or someone on the team themselves.
- `source` stays limited to where the listing was found. It does not encode the channel.
- `_meta/Templates/Job Template.md` and the `dapplication` skill write `channel: form`. The user changes it by hand for the other three values.

# Consequences

- Dataview queries group and sort by `channel` (see `Job Applications/_MOC Jobs.md`).
- A few older notes still have channel-like `source` values (`email`, `reference`, `previously worked there`, `inbound`). Those values don't say where the listing was found.
