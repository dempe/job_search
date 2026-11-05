# Rubric v3: handoff

## State

- **Done and committed:** the v3 rubric itself (`.claude/skills/djgrade/SKILL.md`):
  - each question has a `qtype` (design, technical, story, experience, motivation, simple)
  - **content** is scored out of 8, or 4 for `simple`: `answered` (a gate), `complete`, `specifics`, `accurate`, plus 0–4 `substance:{dimension}` points judged on reasoning, not on matching the reference answer
  - **delivery** is scored out of 3: `lead`, `confident`, `focused`
  - the grade is derived from both scores
- **Callers updated:** `djtrans`, `djq` and its `pick.sh` (field regex is `[a-z_]+`), `djmvanswers`, `djanswers`, ADR 0010.
- **`Interviews.md` queries already use the new fields:** `content`, `content_max`, `delivery`, `delivery_max`, `qtype`. These show blank or 0% until the scores are written into the notes.
- **The interview notes still use the old fields:** `points::`, `possible::`, `failed::`, and `missing::` sub-bullets labelled with the old check names.
- The field is `qtype::`, not `type::`. Dataview lifts list-item fields to page level, so `type::` would collide with the frontmatter's `type: interview`.

## Scores

`scores.tsv` holds the full v3 re-score of all 160 graded questions, from three fresh-context agents. It's tab-separated with no header:

`note path, heading, qtype, content, content_max, delivery, failed (comma-separated; substance dims as substance:{dim}), missing items (" || "-joined "check: text"), derived grade, current grade`

- **Totals:** content 73%, delivery 85%. Grades: 34 right, 121 partial, 5 missed.
- **Changes:** 28 right → partial, 3 partial → right.

## Calibration problems to fix before writing

1. **`substance:relevance` fails 76 times.** It fails whenever an answer doesn't tie back to the role, even for plain questions ("Which AWS services have you used?", "Tell me about yourself").
   - **Proposed:** `relevance` (experience) and `specific` (motivation) are scored only when the question asks about fit, the role or the company. Otherwise that dimension passes.
2. **Coding tasks are typed `technical`,** so a correct snippet loses `when`.
   - **Proposed:** a coding task with correct code is typed `simple`.
3. **"I helped build…" fails `confident`** even when the user built the thing.
   - **Proposed:** keep it. It's real delivery feedback.

Some `qtype` calls are borderline, listed in the agents' reports: "Have you used X?" as `experience` vs `simple`, and "Walk me through the lifecycle…" as `story`.

## Next steps

1. **Get the user's approval for fixes 1 and 2,** then edit djgrade's rubric to add them.
2. **Re-score only the affected rows** of `scores.tsv`: rows failing `substance:relevance` or `substance:specific`, and coding tasks typed `technical`. Fresh agents, write to a TSV, and merge into `scores.tsv`.
3. **Validate every row:**
   - 10 fields
   - `content_max` = 8, or 4 for `simple`
   - `content` = `content_max` minus the failed content items, or 0 if `answered` failed
   - `delivery` = 3 minus the failed delivery items
   - one missing item per failed item, or a single `answered` item for missed
   - the grade derived from the scores
4. **Show the user every grade change for approval.**
5. **Write into each note,** under each matching `#### {heading}`:
   - replace `points::` and `possible::` with `qtype::`, `content::`, `content_max::`, `delivery::`, `delivery_max:: 3`
   - replace `failed::`
   - rebuild `missing::` as `  - **{check}:** {text}` sub-bullets
   - set the grade
   - leave `answer::` (a verbatim quote) and any `practice::` lines untouched
   - update each note's tally line
6. **Verify:** no `points::` or `possible::` remain, and `bash .claude/skills/djq/pick.sh` still finds the 172 interview questions. The Reasint #2 study-note headings are expected not to count.
7. **Commit** with a one-line imperative message and no attribution. The user has authorized commits in this repo.
