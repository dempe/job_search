---
name: djpractice
description: Practice every question in one interview note, in order, the way djq practices a random one. Shows one question at a time, and when the user answers, grades the attempt with djgrade, logs it under the question, and moves on to the next. Takes the application note's name and an interview number (e.g. `micro1 1`). Application notes' own questions are never practiced.
argument-hint: <application-note-name> <interview-number>
---

# Practice an Interview

Go through every question in one note, in order, as a `djq` practice session: show a question, wait for the user's answer, grade and log it, then show the next. The questions come from djq's `pick.sh`, so a question here is exactly what `djq` counts as one.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

## Constraints

- The assistant MUST get the questions by running `pick.sh --all` (Step 2). It MUST NOT find them itself.
- Grading, logging and committing each attempt follow djq's Step 3 exactly, including its constraints: the only file change is one session added to the question's `#### Practice` section, committed with djq's message.
- The Bash tool MUST be used only for `ls`, `test -e`, `pick.sh`, and what djq's Step 3 runs (`date "+%Y-%m-%d %H:%M:%S"`, `git add`, `git commit`). It MUST NOT push.
- This run's earlier answers reach the grader only through `pick.sh --run` (djq's Step 3). The assistant MUST NOT pass them from the conversation, or pick sessions out of the note's `#### Practice` sections by number, since those mix sessions from different runs.

## Step 1: Input

- The arguments are `{Application}`, an application note's name, and `{n}`, an interview number. Resolve `{Application}` to its folder in `Applications/` (`ls`), matching case-insensitively, and use that folder's casing. If either argument is missing, STOP and ask for it. Application notes' own questions are never practiced.
- The note is `Applications/{Application}/Interviews/{n}/{n}.md`. If it doesn't exist (`test -e`), STOP with one line naming it.

## Step 2: List the questions

- Read `.claude/skills/djq/SKILL.md`. Its Steps 2 and 3 are how each question is shown and graded.
- Run, with the note's path:

  ```bash
  bash .claude/skills/djq/pick.sh --all "{note}"
  ```

- The first line of output is the note's name and the second its vault path without `.md`, as in djq. The rest is every question in the note, in order, as `>` lines, with one blank line between questions.
- If the script exits non-zero, STOP with one line saying the note has no questions.
- Number the questions 1 to {total}, in that order.
- Get this run's number `{r}`, and keep it for the rest of the run:

  ```bash
  bash .claude/skills/djq/pick.sh --next-run "{note}"
  ```

  Every session logged in this run gets `- run:: {r}`. If the number is lost (e.g. to compaction), it's the `run::` of the session this run logged last.

## Step 3: Practice each question

Starting with question 1:

1. **Show it** as djq's Step 2 does, with one line before the blockquote: `Question {i} of {total}`. Then wait for the user's reply.
2. **Handle the reply:**
   - An answer: grade, show and log it exactly as djq's Step 3, items 1–4 (djgrade, its full output block, the `#### Practice` session, the commit), with `{r}` as the run. The grader gets the run's earlier answers from `pick.sh --run`; the attempt being graded isn't logged yet, so it sees only earlier questions. Then go on to the next question.
   - A request for the answer: show it as djq's Step 2 says, then wait for their answer to the same question.
   - `skip`: go on to the next question without grading or logging.
   - `stop`: go to Step 4.
3. After the last question, go to Step 4.

## Step 4: Summary and stop

One line: how many questions were answered, the pass/fail tally among them, and how many were skipped. Then STOP.
