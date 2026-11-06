# Rubric v3: handoff

## State

Complete. The v3 rubric (`.claude/skills/djgrade/SKILL.md`) is in place and every graded interview question uses it.

- Each question has a `qtype` (design, technical, story, experience, motivation, simple).
- **Content** is scored out of 8, or 4 for `simple`: `answered` (a gate), `complete`, `specifics`, `accurate`, plus 0–4 `substance:{dimension}` points judged on reasoning, not on matching the reference answer.
  - `relevance` (experience) and `specific` (motivation) are scored only when the question asks about fit, the role or the company. Otherwise they pass.
  - A coding task answered with correct code is `simple`.
- **Delivery** is scored out of 3: `lead`, `confident`, `focused`.
- The grade is derived from both scores.
- The field is `qtype::`, not `type::`. Dataview lifts list-item fields to page level, so `type::` would collide with the frontmatter's `type: interview`.

## Scores

`scores.tsv` holds the v3 score of all 160 graded interview questions, and matches what's written in the notes. It's tab-separated with no header:

`note path, heading, qtype, content, content_max, delivery, failed (comma-separated; substance dims as substance:{dim}), missing items (" || "-joined "check: text"), grade, v2 grade`

- **Totals:** content 77%, delivery 86%. Grades: 51 right, 104 partial, 5 missed.
- No interview note has `points::` or `possible::` left. `pick.sh` finds 172 interview questions (the Reasint #2 study-note headings don't count).
