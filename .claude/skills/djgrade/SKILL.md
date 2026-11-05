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

Grade the substance of the answer against the question and the reference answer:

- `right`: answered every part of the question correctly, with concrete specifics.
- `partial`: correct but thin, missing a part the question asked for, vague when asked for specifics, or claiming more than the user's experience supports (e.g. rating themselves 9–10 at something they use routinely but not deeply).
- `missed`: wrong, a non-answer ("I forget", "I don't know", trailing off), or an answer to a different question.

- Ignore filler, stutters, and transcription errors. Judge delivery only when rambling buried the answer.
- The grade is about the answer, not about the reference answer's extra polish: a short answer that hits every point the question asked for is `right`.

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
