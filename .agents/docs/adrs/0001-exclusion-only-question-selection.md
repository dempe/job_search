---
title: Exclusion-only question selection in dapplication
status: accepted
superseded_by:
---

# Context

The `dapplication` skill (`.claude/skills/dapplication/SKILL.md`) records application-form questions from a JD into a new note in `Job Applications/`. Some questions are trivial and shouldn't be recorded, such as contact fields, sponsorship, and salary.

Defining which questions to *include* (e.g. "asks for composed prose about experience") is subjective and tied to answer format. A dropdown-answered puzzle like "What did you get when you cracked the code?" is substantive, but an inclusion rule based on prose or free text would drop it.

Plan: `auto-fill-applications` (FR36–FR43).

# Decision

The skill has no inclusion criteria. Every form question is included unless it clearly falls into one of seven closed exclusion categories:

1. identity and contact
2. work authorization, visa, and sponsorship
3. compensation
4. location, travel, and availability logistics
5. yes/no confirmations of interview or employment conditions
6. demographics and EEO
7. follow-ups to excluded questions

Answer format (free text, dropdown, selection) is never grounds for exclusion. Each run reports the excluded questions with their category.

# Consequences

- Substantive questions answered by dropdown or selection are kept.
- Question types not covered by a category (e.g. "Where did you hear about this role?") are included, which may add some noise. Fix this by adding a category to the skill, not by adding inclusion logic.
- The excluded-question report makes wrong exclusions easy to spot after each run.
