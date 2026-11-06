---
name: djtrans
description: Turn the interview transcripts in an application's interview notes into question/answer blocks, then grade how the user actually answered. Extracts the substantive questions the interviewer asked, and writes a `### Questions` section beside the transcript with, for each question, a pass / fail grade of the real answer and the ideal answer. Takes the application note's name (e.g. `Rivora`).
argument-hint: <application-note-name>
---

# Interview Transcript to Questions

Each interview is its own note, `Applications/{Application}/Interviews/{n}/{n}.md`, embedded in its application note (see ADRs 0010 and 0011). Read the transcripts in one application's interview notes, pull out the questions the interviewer asked, write the answer that should have been given to each, and grade the answer the user actually gave.

The answers are model answers for study, not a record of what was said and not restricted to what the vault can evidence. Each generated section says so, so a later reader never mistakes them for the user's own words.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

Follow the steps below in order. A step that says STOP ends the run.

## Constraints

- The assistant MUST use only Claude Code's built-in tools (Bash, Read, Edit, Skill for `djspeakers` in Step 2, and Agent for grading in Step 7). It MUST NOT write scripts, and the only script it runs itself is the bundled `extract.py` (Step 2).
- Other than `extract.py`, the Bash tool MUST be used only for read-only commands: `ls`, `grep`, `test -e`.
- `extract.py` is the only thing that moves transcripts, so they are copied byte for byte and never retyped.
- The assistant modifies the application's interview notes only by adding a `### Questions` section, or by adding the tally and grade bullets to an existing ungraded one (Step 3). Every other part of them, including existing model answers and links, MUST stay byte-for-byte unchanged. The application note itself MUST NOT be modified.
- The assistant MUST NOT modify any existing `transcript.md` or `transcript-speakers.md`.
- The assistant MUST NOT create or modify anything in `Answers/`. It MAY read `Answers/` notes (Step 7).
- The assistant MUST NOT commit or push anything to git.

## Output

- The assistant MUST NOT narrate while working.
- The assistant MUST end with one line per interview note giving the number of questions and the grade tally, and one line for any transcript that was skipped and why.
- A run that stops early MUST say why in one line.

## Step 1: Input

- The argument is `{Application}`, an application note's name without `.md`. Resolve it to an application folder in `Applications/` (`ls`), matching case-insensitively, and use that folder's casing. The note is `Applications/{Application}/{Application}.md`.
- If no argument was provided, the assistant MUST STOP and ask for it.
- If no matching note exists, the assistant MUST STOP with one line naming the missing file.
- Read the whole note. Its interview notes are the `![[Applications/{Application}/Interviews/{n}/{n}]]` embeds under its `## Interview…` headings. Read each one.
- If the note embeds no interview notes, the assistant MUST STOP with one line saying so.

## Step 2: Find the transcripts

Each transcript is a `transcript.md` beside its interview note (e.g. `Applications/People Data Labs/Interviews/2/2.md` has `Applications/People Data Labs/Interviews/2/transcript.md`), and the interview note embeds it. The user pastes a new transcript into the interview note as a fenced block under `### Transcript`, so move those out first:

- For each interview note, run `python3 -I .claude/skills/djtrans/extract.py "Applications/{Application}/Interviews/{n}/{n}.md"`. For each `### Transcript` section holding a fenced block, it writes the block's text to `transcript.md` beside the note and replaces the block with an embed, e.g. `![[Applications/People Data Labs/Interviews/2/transcript]]`. Sections that already embed a file are left alone.
- Each `skipped:` line it prints is reported in Step 9. If it printed any `moved:` line, Read that interview note again.

Then, in each interview note:

- Find its `### Transcript` section. An interview note without one is passed over silently: not every interview has a transcript.
- A transcript section's content MUST be a single embed of the `transcript.md` beside the interview note. Read the embedded file; its whole content is the transcript.
- A section that is empty, holds anything other than one embed, or embeds a file that doesn't exist (`test -e`) is skipped and reported.
- If none of the interview notes has a `### Transcript` section, the assistant MUST STOP with one line saying so.

Then make sure each transcript to process has a speaker-labelled copy, `transcript-speakers.md`, beside it (ADR 0012):

- If any is missing, invoke the `djspeakers` skill with the Skill tool for this application, and report its uncertain speaker calls in Step 9.
- If `djspeakers` couldn't label a transcript, skip that transcript and report it.
- Read each `transcript-speakers.md`. From here on, it's the transcript: `**Me:**` turns are the user's and every other label is an interviewer's.

## Step 3: Skip work already done

- If an interview note's `### Questions` section already contains `grade::` items, it is skipped and reported.
- If it has a `### Questions` section without grades (written before its transcript existed), skip Steps 4–6 for it: grade its existing questions in Step 7, then in Step 8 add only the tally line and each question's grade bullets.
- Re-running the skill is therefore safe.

## Step 4: Extract the interviewer's questions

From each speaker-labelled transcript, take the questions the **interviewer** asked the candidate, from the interviewer's turns.

**Include** anything substantive:

- technical questions ("what's the difference between a GET and a POST?")
- behavioral and situational questions ("tell me about a time something good enough for now turned out to be the wrong call")
- motivation and preference questions ("do you want to work with these languages?")
- requests to walk through experience ("walk me through the languages and frameworks you feel most comfortable with")
- follow-up questions that ask for something new, as their own entry

**Exclude:**

- small talk and rapport ("How's it going?", "Where are you based?", weather, travel)
- administrative and logistics questions: scheduling, ID verification, "can you hear me", next steps, references, notice periods
- compensation, location, and work-authorization questions
- rhetorical questions inside the interviewer's own narration ("you know what I mean?")
- every question the candidate asked the interviewer

A question interrupted and resumed later in the transcript is one question, not two.

## Step 5: Write the question text

Transcripts are machine-transcribed and rough. For each question:

- Write it as the interviewer plainly meant it: drop filler, stutters, false starts, and repeated words.
- Keep their wording otherwise, including their framing and any example they gave.
- The assistant MUST NOT invent a question that was not asked, and MUST NOT sharpen a vague question into a more specific one.
- If a question genuinely has two parts, keep both parts.

## Step 6: Write the ideal answer

For each question, write the answer that should have been given:

- **Technical questions** get the correct technical answer, accurate and specific.
- **Experience and behavioral questions** get a strong, concrete, well-structured answer in first person.
- Aim for what a person would actually say out loud: roughly 30–90 seconds, longer only when the question demands it.
- Match the user's plain, direct voice (see `Answers/` for tone). Use `--` for dashes, never em dashes.
- No filler openers ("Great question"), no corporate register, no bullet-point speech.
- The answer MUST answer every part of the question.

These answers are not constrained by what the user actually said in the interview, nor by what the vault can evidence. That is deliberate: they are the target to study toward. The user decides what to adapt.

## Step 7: Grade each answer

Grading runs in a fresh context, so it isn't biased by having just written the model answers.

- For each interview note to grade, launch one `general-purpose` agent with the Agent tool. Its prompt MUST include:
  - the path of `.claude/skills/djgrade/SKILL.md`, to read and follow as its grading rules
  - the path of the interview's `transcript-speakers.md`, to read in full, and that `**Me:**` turns are the user's
  - every question, in order, with its reference answer: the model answer from Step 6, or, for an existing section, the fenced block under the question's heading (or, if the heading is followed by an `Answers/` link, that section's code block, read by the assistant first)
  - the instruction to take the user's answer to each question from the transcript: the text of their `**Me:**` turns from that question until the interviewer moves on (including follow-up exchanges on the same point), copied exactly and joined with ` … `; then grade it, and return only `djgrade`'s output block for each question, in order, labeled by question number
  - the instruction not to create or modify any file
- Launch the agents for different notes in parallel.
- Use each agent's blocks as is in Step 8. If an agent returns the wrong number of blocks or a block that doesn't match `djgrade`'s output shape, re-run that agent once. If it fails again, STOP that note and report it.

## Step 8: Write the section

In the interview note, immediately after the `### Transcript` section, add:

````markdown
### Questions

Graded against the transcript: {p} pass, {f} fail. Each question shows how you answered, then a model answer to study.

#### {question}

- grade:: {grade}
- answer:: {what the user said}
- missing::
  - **{check}:** {what was missing or wrong, for that check}

```
{ideal answer}
```
````

- One `####` heading per question, in the order asked. `{question}` is the complete question on one line, with any `#`, `|`, or `^` removed and `[`/`]` replaced with `(`/`)` (a Markdown link becomes `text (url)`), so the heading still works as a link. `Interviews.md` links to it.
- The bullets are `djgrade`'s output for that question, written as is. Each field is its own list item, so Dataview reads it per section.
- The ideal answer goes in a fenced code block with no language, matching the rest of the vault. Blocks are separated by exactly one blank line.
- For an existing ungraded section (Step 3), replace its intro line with the tally line and insert each question's bullets between its heading and its model answer. Nothing else in it changes.
- Use Edit, anchoring on the transcript's embed line (or on each heading) and whatever follows it, so nothing else moves.

## Step 9: Report and stop

Report one line per interview note (for example, `Interview 1: 5 questions (3 pass, 2 fail)`), plus a line for any transcript skipped and why. Then STOP.
