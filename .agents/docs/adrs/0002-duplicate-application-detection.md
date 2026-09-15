---
title: Duplicate application detection by filename and applied date
status: accepted
superseded_by:
---

# Context

The `dapplication` skill creates a new application note per JD. Re-applying to a company shortly after a previous application is almost always a mistake. Existing notes are an imperfect source for detecting this:

- Numbering is inconsistent (`Close (0)`/`Close (1)`, `Walmart (1)`–`(3)` with no bare note).
- `title` sometimes disagrees with the filename (`Close (1).md` has `title: Close (2)`).
- Similar names exist (`Metal.md` next to `Meta (n).md`).

Plan: `auto-fill-applications` (FR7–FR17).

# Decision

- Existing applications for a company are identified **only** by exact filename: `<Company>.md` or `<Company> (n).md`.
- The only data read from them is the `applied` frontmatter date. No `title`, `company`, or content-based matching is used.
- If any match has `applied` on or after today minus six calendar months, the skill aborts without writing and reports the note and its date.
- A missing or blank `applied` never aborts.
- Otherwise, the new note takes `<Company> (max suffix + 1).md`, where a bare name counts as `0`. Existing notes are never renamed.

# Consequences

- The rule is simple, predictable, and immune to `title` drift and inconsistent numbering.
- An earlier application filed under a name variant (e.g. a product brand vs. parent company, or "Inc." suffixes) is not detected. Choosing a consistent company name at the skill's company-name prompt matters.
- A dry run against the vault on 2026-09-14 (`.agents/plans/auto-fill-applications/artifacts/data/dry-run-existing-applications.txt`) gave these results:
  - Lithic aborts as a duplicate.
  - Allstate aborts as a duplicate (`Allstate (0).md`, applied 2026-08-10).
  - Meta → `Meta (3).md`.
  - Walmart → `Walmart (4).md`.
  - Close → `Close (2).md`.
