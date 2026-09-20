---
name: djtrans
description: Turn an interview transcript in a job application note into question/answer blocks. Extracts the substantive questions the interviewer asked and writes the ideal answer to each, in a new `### Questions` section beside the transcript. Takes the application note's name (e.g. `Rivora`).
argument-hint: <application-note-name>
---

# Interview Transcript to Questions

Read the `### Transcript` sections of one application note, pull out the questions the interviewer asked, and write the answer that should have been given to each.

The answers are model answers for study, not a record of what was said and not restricted to what the vault can evidence. Each generated section says so, so a later reader never mistakes them for the user's own words.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

Follow the steps below in order. A step that says STOP ends the run.

## Constraints

- The assistant MUST use only Claude Code's built-in tools (Bash, Read, Edit). It MUST NOT write or run scripts.
- The Bash tool MUST be used only for read-only commands: `ls`, `grep`, `test -e`.
- The only file this skill modifies is `Job Applications/{Application}.md`, and only by adding `### Questions` sections.
- The transcript, its fences, and every other section MUST stay byte-for-byte unchanged.
- The assistant MUST NOT create or modify anything in `Answers/` or `Questions/`.
- The assistant MUST NOT commit or push anything to git.

## Output

- The assistant MUST NOT narrate while working.
- The assistant MUST end with one line per interview section giving the number of questions captured, and one line for any transcript that was skipped and why.
- A run that stops early MUST say why in one line.

## Step 1: Input

- The argument is `{Application}`, an application note's name without `.md`. Resolve it to the real filename in `Job Applications/` (`ls`), matching case-insensitively, and use that file's casing.
- If no argument was provided, the assistant MUST STOP and ask for it.
- If no matching note exists, the assistant MUST STOP with one line naming the missing file.
- Read the whole note.

## Step 2: Find the transcripts

- Find every `### Transcript` section. A note may have several, one per interview.
- A transcript section's content MUST be a single fenced code block with no language. A section that is empty, holds prose, or holds more than one block is skipped and reported.
- Record each transcript's parent `##` section (e.g. `## Interview 1`). The new section goes in that same parent.
- If the note has no `### Transcript` section, the assistant MUST STOP with one line saying so.

## Step 3: Skip work already done

- If a transcript's parent section already contains a `### Questions` section, that transcript is skipped and reported. Re-running the skill is therefore safe.

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

In the transcript's parent section, immediately after the `### Transcript` section, add:

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
- Use Edit, anchoring on the end of the transcript's closing fence and the heading that follows it, so nothing else moves.

## Step 8: Report and stop

Report one line per interview section (for example, `Interview 1: 5 questions`), plus a line for any transcript skipped and why. Then STOP.
