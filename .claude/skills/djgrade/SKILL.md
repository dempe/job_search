---
name: djgrade
description: Grade an answer to an interview or application question against content and delivery checks: pass / fail, what was said, and what was missing for each failed check. Use ad hoc to grade a practice answer, or from another skill (djtrans, djq). Takes a question and an answer, and optionally a reference answer or the note the question lives in.
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

- In an interview note's `## Questions` section, the fenced code block under the question's `### {question}` heading, after any `- field::` bullets.
- In an application note, the fenced code block after the question's `> ` blockquote.
- If the question is followed by a `[[Note#Heading|Note]]` link instead of a code block (the answer was filed with `djmvanswers`), the code block in that `Answers/` section.

If there's no reference answer, grade against the question alone, using correct technical knowledge.

## Rubric

Classify the question, score its **content** and its **delivery** check by check, then derive the grade from the scores.

### Question type

Pick exactly one type. It decides which substance dimensions are scored.

| type | asked like | substance dimensions (1 point each) |
|---|---|---|
| `design` | "how would you build / scale / handle X" | `diagnose`: clarifies the workload and finds the limits or bottleneck · `mechanism`: how the proposal works, including constraints like shared state · `reliability`: containing failures, changing safely, tradeoffs · `validate`: how testing and metrics guide the next step |
| `technical` | "what is / explain / what's the difference" | `concept`: the correct core idea · `how`: the mechanism or internals · `when`: when it applies, and the tradeoffs · `example`: a concrete use or case |
| `story` | "tell me about a time / have you ever / walk me through a project / most difficult…" | `beginning`: one specific problem, and who or what it affected · `middle`: what the candidate personally did (an approach like "I stay calm" or "I had to deal with it" doesn't count) · `end`: the outcome · `fits`: the example matches what was asked, not a smaller or different kind of situation, unless the candidate says plainly it's the closest they've had and why it still counts |
| `experience` | "what have you used / are you comfortable with / rate yourself / your background" | `claim`: a direct statement of level or extent · `evidence`: where and what they did with it · `depth`: how recently and how deeply · `relevance`: a tie to this role or stack |
| `motivation` | "why us / why leave / what are you looking for / how do you feel about" | `reason`: a clear reason · `specific`: specific to this company and role · `grounded`: tied to the candidate's real experience · `forward`: what they'd bring or want next |
| `simple` | yes/no or one-fact questions ("Did you only build the mobile app?"), and coding tasks answered with correct code | none |

- **Fit dimensions apply only to fit questions.** `relevance` (`experience`) and `specific` (`motivation`) are scored only when the question asks about fit, the role or the company ("why this role", "how would your experience help here"). For any other question ("Which AWS services have you used?", "Tell me about yourself") that dimension passes automatically.
- **Coding tasks with correct code are `simple`.** A request to write or fix code that the answer gets right is typed `simple`, so it isn't marked down for `when` or `example`. Incorrect or incomplete code stays `technical`.

**Substance is judged on reasoning, not on matching the reference answer.** The reference answer is one good example. Any sound approach that covers a dimension earns its point, even if it uses a different design or technology.

### Content

Every point is all-or-nothing.

| Check | Points |
|---|---|
| `answered` | 1 if it answers this question: not wrong, not a non-answer ("I forget", "I don't know", trailing off), not an answer to a different question. A real but weak answer passes; its weakness shows elsewhere. **Gate:** if it fails, `content` is 0. |
| `complete` | 1 if every named part of the question is addressed. Leaving out a part ("…without sacrificing reliability?") fails it. |
| `specifics` | 1 if it gives concrete names, numbers, technologies and actions, not generalities. A `simple` question passes with a direct answer. Ratings and "are you comfortable with X" are `experience`, not `simple`, and need backing. |
| `accurate` | 1 if nothing in it is technically wrong and it claims no more than the candidate's experience supports (e.g. not rating themselves 9–10 at something they use routinely but not deeply). |
| `substance:{dimension}` | 1 per dimension of the type that the answer actually covers: 0–4 points. Not scored for `simple`. |

Content is out of 8, or 4 for `simple`.

### Delivery (out of 3)

| Check | 1 point if… |
|---|---|
| `lead` | The first words directly answer the question. Anything before the point fails it: stalling ("Um… let's see… that's a huge increase"), a run of filler and hedging ("Um, so, I think, in this case, we'd want to make sure to have, uh, …"), background, or context. Direct leads look like "Yes, twice -- the worst was…", "Kafka, because…", "About an 8." |
| `confident` | No hedges that shrink the candidate's own claims ("I think it was twice", "maybe I would have…", "it wasn't really…"). Honest uncertainty about a fact ("I don't remember the exact number") is fine. |
| `focused` | It stays on the question, with no long backstory or tangent that buries the answer. |

Transcription errors don't fail a delivery check. A stray filler word mid-answer doesn't either, but filler before the point fails `lead`.

### Grade

- `pass` only if every content and delivery point is earned.
- `fail` otherwise.

The grade is always derived this way, so it can never disagree with the scores.

### Reference examples

**1. Story question**

> Have you ever had to manage an emergency or a big outage or anything like that? Something high stress.

Answer: on-call at a previous job as a junior and "had to ask for some help"; at Octimine "there were 2 times where it would just like keep failing", "I had to babysit it", "It wasn't a complete outage"; staying calm and separating what's known from what isn't; a root cause analysis and incident documentation afterwards.

- **Content: 2/8.**
  - pass: `answered`, `accurate`
  - fail: `complete` (no actual emergency handled), `specifics` (never says what failed or what was done)
  - substance: no story dimension passes. There's no specific problem or impact (`beginning`), the approach stands in for actions (`middle`), there's no outcome (`end`), and a failing, late batch job isn't an outage (`fits`).
- **Delivery: 0/3.** It doesn't lead (it opens with on-call as a junior), it hedges ("I think there were 2 times"), and the backstory buries the point.
- **Grade:** `fail`.

**2. Design question**

> If Wonderland suddenly grows from 1,000 to a million users, how would you approach scaling the infrastructure without sacrificing reliability?

Answer: "Um... Let's see. That's a huge increase. 1000 to a million." Then: deploy to a small number of servers with a standard configuration, and add more servers seamlessly as users grow.

- **Content: 3/8.**
  - pass: `answered`, `accurate`
  - fail: `complete` (the reliability half is unaddressed), `specifics` (no mechanisms named)
  - substance: only `mechanism` passes (standardized configuration, horizontal scaling). There's no `diagnose`, `reliability` or `validate`. A threshold on user count is a weak capacity signal.
- **Delivery: 2/3.** `lead` fails (it stalls before the point). `confident` and `focused` pass.
- **Grade:** `fail`.

## Output

For each item, exactly this shape, one field per list item:

```markdown
- grade:: {pass | fail}
- answer:: {what the candidate said}
- missing::
  - **{check}:** {what was missing or wrong, for that check}
```

The type and the scores are worked out to derive the grade, but they aren't part of the output.

- `answer::` is the candidate's whole answer, verbatim, in double quotes, on one line. It MUST NOT be a paraphrase, a summary or an excerpt: every point the candidate made is in it, so the `missing::` list can be checked against it.
  - It runs from the candidate's first word on the question to their last, including any follow-up exchange on the same point.
  - Leave out the interviewer's words (questions, interjections like "Okay." or "Yeah, that's great."). Where the interviewer's words split the answer, join the candidate's parts with ` … `.
  - Quote filler and transcription errors as they appear; don't correct them.
- `missing::` has no value on its own line. Under it, indented two spaces, is one sub-bullet per failed check, content checks first, then delivery, labelled with the check name in bold: `  - **lead:** …`. A substance dimension is labelled `substance:{dimension}` (e.g. `  - **substance:validate:** …`).
  - Each sub-bullet names, concretely, what that check needed. For a substance dimension, describe the gap and give one possible example ("e.g. …"), never a required solution. For `lead`, give the direct first sentence the answer could have opened with.
  - If `answered` fails, give a single `**answered:**` sub-bullet with the correct answer in brief, instead of one per check.
  - Omit `missing::` entirely for `pass`.

**Ad hoc:** print the block for each item, with both scores as percentages after it (content and delivery), then one or two sentences of coaching on what to add or change next time. Then STOP.

**Invoked by another skill:** produce the blocks and continue with the caller's steps. The caller's output rules apply.
