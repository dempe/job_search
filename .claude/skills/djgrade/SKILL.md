---
name: djgrade
description: Score and grade an answer to an interview or application question: points per rubric check, right / partial / missed, what was said, and what was missing. Use ad hoc to grade a practice answer, or from another skill (djtrans, djq). Takes a question and an answer, and optionally a reference answer or the note the question lives in.
argument-hint: <question> <answer>
---

# Grade an Answer

Grade a candidate's answer to a question against a reference answer, and return the result in a fixed shape that other skills write into notes as is.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

## Constraints

- This skill only grades. It MUST NOT create or modify any file. Callers decide where results go.
- The assistant MUST NOT commit or push anything to git.

## Input

One or more items. Each item is:

- **the question**
- **the candidate's answer**: text the user typed or said, or the relevant excerpt of an interview transcript, including any follow-up exchange on the same point
- **a reference answer** (optional)

When invoked ad hoc (`/djgrade`), take these from the arguments or the user's message. If the question or the answer is missing, ask for it and STOP until the user replies.

## Finding the reference answer

If the caller names the note a question lives in, the reference answer is:

- In an interview note's `### Questions` section, the fenced code block under the question's `#### {question}` heading, after any `- field::` bullets.
- In an application note, the fenced code block after the question's `> ` blockquote.
- If the question is followed by a `[[Note#Heading|Note]]` link instead of a code block (the answer was filed with `djmvanswers`), the code block in that `Answers/` section.

If there's no reference answer, grade against the question alone, using correct technical knowledge.

## Rubric

Score the answer against the question and the reference answer, check by check, then derive the grade from the score.

### Checks and points

Each check is worth exactly **1 point**. A check either passes (1) or fails (0); there is no partial credit within a check.

**Every question: 5 checks, 5 points possible**

| Check | Passes (1 point) if… |
|---|---|
| `answered` | It answers this question. It is not wrong, not a non-answer ("I forget", "I don't know", trailing off), and not an answer to a different question. |
| `complete` | Every part of the question gets an actual answer. Mentioning every topic the reference answer covers isn't enough. |
| `specifics` | It gives concrete names, numbers, technologies, and actions, not generalities. |
| `lead` | The first sentence or two directly answers the question, before any background, context, or detail. Direct leads look like "Yes, twice -- the worst was…", "Kafka, because…", "About an 8.", "Mostly TypeScript and Node, with…" |
| `accurate` | It claims no more than the candidate's experience supports (e.g. not rating themselves 9–10 at something they use routinely but not deeply), and nothing in it is technically wrong. |

**Story questions: 4 more checks, 9 points possible**

A story question asks for an experience: "tell me about a time…", "have you ever…", "walk me through a project…", "what was the most difficult…". For these, also score:

| Check | Passes (1 point) if… |
|---|---|
| `beginning` | It states one specific problem, and who or what it affected. |
| `middle` | It says what the candidate personally did to fix it. Describing an approach ("I stay calm and isolate the issue") or "I had to deal with it" does not pass. |
| `end` | It gives the outcome. |
| `fits` | The example matches what was asked, not a smaller or different kind of situation (a slow or failing job when asked about an outage), unless the candidate says plainly it's the closest they've had and why it still counts. Hedges that shrink the example ("I think it happened twice") fail it. |

### From score to grade

- `points` is the number of checks passed. `possible` is 5, or 9 for a story question.
- **`answered` is a gate:** if it fails, every check fails, `points` is 0, and the grade is `missed`.
- If every check passes, the grade is `right`.
- Otherwise the grade is `partial`.

The grade is always derived this way, so it can never disagree with the score.

### What to ignore

- Filler, stutters, and transcription errors. Delivery only matters through `lead`, or when rambling buried the answer so a check fails.
- The reference answer's extra polish. A short answer that passes every check is `right`.

### Reference example

> Have you ever had to manage an emergency or a big outage or anything like that? Something high stress.

Answer: on-call at a previous job as a junior and "had to ask for some help"; at Octimine "there were 2 times where it would just like keep failing", "I had to babysit it", "It wasn't a complete outage"; staying calm and separating what's known from what isn't; a root cause analysis and incident documentation afterwards.

This is a story question, so `possible` is 9.

| Check | Result | Why |
|---|---|---|
| `answered` | pass | It addresses the question. |
| `complete` | pass | The question has one part, and it gets a response. |
| `specifics` | fail | It never says what was failing or what was done. |
| `lead` | fail | It opens with on-call as a junior at a previous job, and never states up front whether there was an emergency. |
| `accurate` | pass | Nothing is overclaimed or wrong. |
| `beginning` | fail | No specific problem or impact is stated. |
| `middle` | fail | "I had to babysit it" and the approach stand in for actions. |
| `end` | fail | No outcome. |
| `fits` | fail | A failing, late batch job isn't an outage ("It wasn't a complete outage"), and "I think there were 2 times" shrinks it. |

Score: 3/9. Grade: `partial`. A full-score answer leads with a direct yes and the incident it will describe, then tells that one incident: what broke and who it hurt, the specific steps taken, and the outcome.

## Output

For each item, exactly this shape, one field per list item:

```markdown
- grade:: {right | partial | missed}
- points:: {checks passed}
- possible:: {5, or 9 for a story question}
- failed:: {comma-separated names of the failed checks}
- answer:: {what the candidate said}
- missing:: {what was missing or wrong}
```

- `failed::` lists check names exactly as in the tables (e.g. `lead, specifics`). Omit it when every check passes.

- `answer::` is a short verbatim quote from the candidate's answer in double quotes, or a faithful paraphrase without quotes. It MUST NOT attribute anything to the candidate that their answer doesn't show.
- `missing::` names what the answer lacked or got wrong, concretely (e.g. "the re-key to family ID before the join"). Omit it for `right`.

**Ad hoc:** print the block for each item, with the score as a percentage after it (`points / possible`), then one or two sentences of coaching on what to add or change next time. Then STOP.

**Invoked by another skill:** produce the blocks and continue with the caller's steps. The caller's output rules apply.
