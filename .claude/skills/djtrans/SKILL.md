---
name: djtrans
description: Turn the interview transcripts in an application's interview notes into question/answer blocks. Extracts the substantive questions the interviewer asked and writes the ideal answer to each, in a new `### Questions` section beside the transcript. Takes the application note's name (e.g. `Rivora`).
argument-hint: <application-note-name>
---

# Interview Transcript to Questions

Each interview is its own note in `Interviews/`, embedded in its application note (see ADR 0010). Read the transcripts in one application's interview notes, pull out the questions the interviewer asked, and write the answer that should have been given to each.

The answers are model answers for study, not a record of what was said and not restricted to what the vault can evidence. Each generated section says so, so a later reader never mistakes them for the user's own words.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

Follow the steps below in order. A step that says STOP ends the run.

## Constraints

- The assistant MUST use only Claude Code's built-in tools (Bash, Read, Edit). It MUST NOT write scripts, and the only script it runs is the bundled `extract.py` (Step 2).
- Other than `extract.py`, the Bash tool MUST be used only for read-only commands: `ls`, `grep`, `test -e`.
- `extract.py` is the only thing that moves transcripts, so they are copied byte for byte and never retyped.
- The assistant modifies the application's interview notes in `Interviews/` only by adding `### Questions` sections. Every other part of them MUST stay byte-for-byte unchanged. The application note itself MUST NOT be modified.
- The assistant MUST NOT modify any existing file in `Transcripts/`.
- The assistant MUST NOT create or modify anything in `Answers/` or `Questions/`.
- The assistant MUST NOT commit or push anything to git.

## Output

- The assistant MUST NOT narrate while working.
- The assistant MUST end with one line per interview note giving the number of questions captured, and one line for any transcript that was skipped and why.
- A run that stops early MUST say why in one line.

## Step 1: Input

- The argument is `{Application}`, an application note's name without `.md`. Resolve it to the real filename in `Applications/` (`ls`), matching case-insensitively, and use that file's casing.
- If no argument was provided, the assistant MUST STOP and ask for it.
- If no matching note exists, the assistant MUST STOP with one line naming the missing file.
- Read the whole note. Its interview notes are the `![[Interviews/...]]` embeds under its `## Interview…` headings. Read each one.
- If the note embeds no interview notes, the assistant MUST STOP with one line saying so.

## Step 2: Find the transcripts

Transcripts live in their own files in `Transcripts/`, named after their interview note (e.g. `Interviews/People Data Labs - Interview 2.md` has `Transcripts/People Data Labs - Interview 2.md`), and the interview note embeds it. The user pastes a new transcript into the interview note as a fenced block under `### Transcript`, so move those out first:

- For each interview note, run `python3 -I .claude/skills/djtrans/extract.py "Interviews/{interview note}.md"`. For each `### Transcript` section holding a fenced block, it writes the block's text to its file in `Transcripts/` and replaces the block with an embed, e.g. `![[Transcripts/People Data Labs - Interview 2]]`. Sections that already embed a file are left alone.
- Each `skipped:` line it prints is reported in Step 8. If it printed any `moved:` line, Read that interview note again.

Then, in each interview note:

- Find its `### Transcript` section. An interview note without one is passed over silently: not every interview has a transcript.
- A transcript section's content MUST be a single embed of a file in `Transcripts/`. Read the embedded file; its whole content is the transcript.
- A section that is empty, holds anything other than one embed, or embeds a file that doesn't exist (`test -e`) is skipped and reported.
- If none of the interview notes has a `### Transcript` section, the assistant MUST STOP with one line saying so.

## Step 3: Skip work already done

- If an interview note already contains a `### Questions` section, its transcript is skipped and reported. Re-running the skill is therefore safe.

## Step 4: Extract the interviewer's questions

From each transcript, take the questions the **interviewer** asked the candidate.

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

## Step 7: Write the section

In the interview note, immediately after the `### Transcript` section, add:

````markdown
### Questions

Model answers, not a record of what was said.

> {question}

```
{ideal answer}
```
````

- Question/answer pairs are separated by exactly one blank line.
- A multi-line question follows the vault's convention: every line starts with `> `, and every line but the last ends with `<br/>`.
- The answer goes in a fenced code block with no language, matching the rest of the vault.
- Use Edit, anchoring on the transcript's embed line and whatever follows it, so nothing else moves.

## Step 8: Report and stop

Report one line per interview note (for example, `Interview 1: 5 questions`), plus a line for any transcript skipped and why. Then STOP.
