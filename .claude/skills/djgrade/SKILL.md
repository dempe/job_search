---
name: djgrade
description: Grade an answer to an interview or application question as right, partial, or missed, with what was said and what was missing. Use ad hoc to grade a practice answer, or from another skill (djtrans, djq). Takes a question and an answer, and optionally a reference answer or the note the question lives in.
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

Grade the substance of the answer against the question and the reference answer.

**Grades**

- `right`: meets every rule below.
- `partial`: correct, but breaks any rule below. For example:
  - thin, or vague when asked for specifics
  - missing a part the question asked for
  - claiming more than the candidate's experience supports (e.g. rating themselves 9–10 at something they use routinely but not deeply)
- `missed`:
  - wrong
  - a non-answer ("I forget", "I don't know", trailing off)
  - an answer to a different question

**Rules for `right`**

- **Every part answered.** Each part of the question gets an actual answer.
  - Mentioning every topic the reference answer covers isn't enough.
  - When unsure between `right` and `partial`, re-read the question and check each part it asked for.
- **Concrete specifics.** Names, numbers, technologies, and actions, not generalities.
- **Lead with the answer.** The first sentence or two directly answers the question asked, then details follow.
  - An answer that opens with background, context, or details and only reaches the point later (or never states it) is `partial`, even if everything it says is correct.
  - Examples of a direct lead: "Yes, twice -- the worst was…", "Kafka, because…", "About an 8.", "Mostly TypeScript and Node, with…"
- **Stories are real stories.** For story questions ("tell me about a time…", "have you ever…", "walk me through a project…"), the answer tells one specific situation with:
  - a **beginning**: the problem, and who or what it affected
  - a **middle**: what the candidate personally did to fix it
  - an **end**: the outcome
- **What doesn't count as a story** (each is `partial`):
  - describing an approach ("I stay calm and isolate the issue")
  - "I had to deal with it"
  - listing topics without the actions and the outcome
  - a story missing its beginning, middle, or end
- **The example matches the question.** A smaller or different kind of situation (a slow or failing job when asked about an outage) is at best `partial`, unless the candidate says plainly that it's the closest they've had and why it still counts.
  - Hedges that shrink the example ("I think it happened twice") count against it.

**What to ignore**

- Filler, stutters, and transcription errors. Judge delivery only when rambling buried the answer, or when the answer didn't lead with the point.
- The reference answer's extra polish. A short answer that leads with the point and hits every part the question asked for is `right`.

### Reference example

> Have you ever had to manage an emergency or a big outage or anything like that? Something high stress.

Answer: on-call at a previous job as a junior and "had to ask for some help"; at Octimine "there were 2 times where it would just like keep failing", "I had to babysit it", "It wasn't a complete outage"; staying calm and separating what's known from what isn't; a root cause analysis and incident documentation afterwards.

Grade: `partial`, for four reasons:

- **The example doesn't fit the question.** A batch job that kept failing and running late isn't an emergency or an outage: nothing was down, and the candidate said so ("It wasn't a complete outage"). The answer swapped in a smaller problem instead of telling a real high-stress incident, or saying plainly that the closest thing they'd handled was a recurring failure and explaining why it was still high stakes.
- **The story has no middle or end.** It never says what was failing, what the candidate did to fix it, or how it ended. The hedges ("I think there were 2 times") shrink it further.
- **It doesn't lead with the answer.** It opens with on-call as a junior at a previous job before reaching any incident, and never states up front whether there was an emergency.
- **Approach replaces action.** Staying calm and separating what's known from what isn't is a reasonable approach, but the answer describes the approach in place of what was actually done.

A `right` answer leads with a direct yes, and the incident it will describe, then tells that one incident end to end:

- **beginning:** what broke and who it hurt
- **middle:** the specific steps the candidate took
- **end:** the outcome, and what changed afterwards

## Output

For each item, exactly this shape, one field per list item:

```markdown
- grade:: {right | partial | missed}
- answer:: {what the candidate said}
- missing:: {what was missing or wrong}
```

- `answer::` is a short verbatim quote from the candidate's answer in double quotes, or a faithful paraphrase without quotes. It MUST NOT attribute anything to the candidate that their answer doesn't show.
- `missing::` names what the answer lacked or got wrong, concretely (e.g. "the re-key to family ID before the join"). Omit it for `right`.

**Ad hoc:** print the block for each item, then one or two sentences of coaching on what to add or change next time. Then STOP.

**Invoked by another skill:** produce the blocks and continue with the caller's steps. The caller's output rules apply.
