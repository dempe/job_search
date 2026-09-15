---
title: Empty fenced code block as the answer placeholder in new application notes
status: accepted
superseded_by:
---

# Context

The vault has two question/answer conventions in `Job Applications/`:

- Older notes put the answer in a fenced code block under the `> question`.
- Recently reorganized notes (e.g. `Lithic.md`, `Resend.md`) put `Answer: [[<Answer note>#<Application>|<Answer note>]]` under the question, and the answer text lives in `Answers/`.

The `dapplication` skill needs a placeholder under each recorded question.

Plan: `auto-fill-applications` (FR49, FR55–FR57).

# Decision

New notes use the original convention: `> question`, one blank line, then an empty fenced code block (an opening and a closing fence with nothing between them). Pairs are separated by one blank line. This matches the pre-reorganization notes in git history.

The skill writes no answers and doesn't touch `Answers/` or `Questions/`.

# Consequences

- The user drafts each answer directly in the note.
- Moving a finished answer into an `Answers/` note and replacing the code block with an `Answer: [[...]]` link is a manual follow-up. Until then, newly created notes look like older notes rather than recently reorganized ones.
