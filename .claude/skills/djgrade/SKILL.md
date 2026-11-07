---
name: djgrade
description: Grade an answer to an interview or application question: what was said, what was missing (from content and delivery checks), pass if nothing was missing else fail, plus the grader's own 1–12 score and feedback. Use ad hoc to grade a practice answer, from another skill (djtrans, djq), or on a whole interview to re-grade every question in its note. Takes a question and an answer (optionally a reference answer or the note the question lives in), or an application note's name and an interview number (e.g. `Rivora 1`).
argument-hint: <question> <answer> | <application> <interview-number>
---

# Grade an Answer

Grade a candidate's answer to a question against a reference answer, and return the result in a fixed shape that other skills write into notes as is.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

## Modes

- **Item mode:** grade the question/answer items given, and print or return the blocks (see Output). This is the mode when invoked by another skill, and ad hoc when given a question and an answer.
- **Interview mode:** `/djgrade {Application} {n}`. Re-grade every question in one interview note from its transcript, and write the results into the note (see Interview mode).

Use interview mode when the arguments are an application name followed by a number, and `Applications/{Application}/Interviews/{n}/{n}.md` exists (resolve `{Application}` to its folder in `Applications/` with `ls`, matching case-insensitively). Otherwise use item mode.

## Constraints

- In item mode, the assistant MUST NOT create or modify any file. Callers decide where results go.
- In interview mode, the assistant modifies only the target interview note, and only its `## Questions` section: the field bullets under each `###` question, and removing an old tally line (step 6). Question headings, model answers and their `![[…]]` embeds, `- practice::` lines, and everything outside the section MUST stay byte-for-byte unchanged. It MUST NOT modify any transcript.
- In item mode, the assistant MUST NOT commit anything. In interview mode, it commits only the interview note, in step 7. It MUST NOT push.

## Input (item mode)

One or more items. Each item is:

- **the question**
- **the candidate's answer**: text the user typed or said, or the relevant excerpt of an interview transcript, including any follow-up exchange on the same point
- **a reference answer** (optional)

When invoked ad hoc (`/djgrade`), take these from the arguments or the user's message. If the question or the answer is missing, ask for it and STOP until the user replies.

## Finding the reference answer

If the caller names the note a question lives in, the reference answer is:

- In an interview note's `## Questions` section, the fenced code block under the question's `### {question}` heading, after any `- field::` bullets.
- In an application note, the fenced code block after the question's `> ` blockquote.
- If the question is followed by a `![[Note#Heading]]` embed instead of a code block (the answer was filed with `djmvanswers`), the code block in that `Answers/` section.

If there's no reference answer, grade against the question alone, using correct technical knowledge.

## Rubric

Classify the question, then go through its **content** and **delivery** checks. Each failed check becomes one `missing::` item. The rubric decides what goes in `missing::`; it doesn't set the grade directly (see Grade).

### Question type

Pick exactly one type. It decides which substance dimensions are checked.

| type | asked like | substance dimensions |
|---|---|---|
| `design` | "how would you build / scale / handle X" | `diagnose`: clarifies the workload and finds the limits or bottleneck · `mechanism`: how the proposal works, including constraints like shared state · `reliability`: containing failures, changing safely, tradeoffs · `validate`: how testing and metrics guide the next step |
| `technical` | "what is / explain / what's the difference" | `concept`: the correct core idea · `how`: the mechanism or internals · `when`: when it applies, and the tradeoffs · `example`: a concrete use or case |
| `story` | "tell me about a time / have you ever / walk me through a project / most difficult…" | `beginning`: one specific problem, and who or what it affected · `middle`: what the candidate personally did (an approach like "I stay calm" or "I had to deal with it" doesn't count) · `end`: the outcome · `fits`: the example matches what was asked, not a smaller or different kind of situation, unless the candidate says plainly it's the closest they've had and why it still counts |
| `experience` | "what have you used / are you comfortable with / rate yourself / your background" | `claim`: a direct statement of level or extent · `evidence`: where and what they did with it · `depth`: how recently and how deeply · `relevance`: a tie to this role or stack |
| `motivation` | "why us / why leave / what are you looking for / how do you feel about" | `reason`: a clear reason · `specific`: specific to this company and role · `grounded`: tied to the candidate's real experience · `forward`: what they'd bring or want next |
| `simple` | yes/no or one-fact questions ("Did you only build the mobile app?"), and coding tasks answered with correct code | none |

- **Fit dimensions apply only to fit questions.** `relevance` (`experience`) and `specific` (`motivation`) are checked only when the question asks about fit, the role or the company ("why this role", "how would your experience help here"). For any other question ("Which AWS services have you used?", "Tell me about yourself") that dimension passes automatically.
- **Coding tasks with correct code are `simple`.** A request to write or fix code that the answer gets right is typed `simple`, so it isn't marked down for `when` or `example`. Incorrect or incomplete code stays `technical`.

**Substance is judged on reasoning, not on matching the reference answer.** The reference answer is one good example. Any sound approach that covers a dimension passes it, even if it uses a different design or technology.

### Content

| Check | Passes if… |
|---|---|
| `answered` | it answers this question: not wrong, not a non-answer ("I forget", "I don't know", trailing off), not an answer to a different question. A real but weak answer passes; its weakness shows elsewhere. **Gate:** if it fails, `missing::` holds only the `answered` item (see Output). |
| `complete` | every named part of the question is addressed. Leaving out a part ("…without sacrificing reliability?") fails it. |
| `specifics` | it gives concrete names, numbers, technologies and actions, not generalities. A `simple` question passes with a direct answer. Ratings and "are you comfortable with X" are `experience`, not `simple`, and need backing. |
| `accurate` | nothing in it is technically wrong and it claims no more than the candidate's experience supports (e.g. not rating themselves 9–10 at something they use routinely but not deeply). |
| `substance:{dimension}` | the answer covers that dimension of the question's type. One check per dimension; none for `simple`. |

### Delivery

| Check | Passes if… |
|---|---|
| `lead` | The first words directly answer the question. Anything before the point fails it: stalling ("Um… let's see… that's a huge increase"), a run of filler and hedging ("Um, so, I think, in this case, we'd want to make sure to have, uh, …"), background, or context. Direct leads look like "Yes, twice -- the worst was…", "Kafka, because…", "About an 8." |
| `confident` | No hedges that shrink the candidate's own claims ("I think it was twice", "maybe I would have…", "it wasn't really…"). Honest uncertainty about a fact ("I don't remember the exact number") is fine. |
| `focused` | It stays on the question, with no long backstory or tangent that buries the answer. |

Transcription errors don't fail a delivery check. A stray filler word mid-answer doesn't either, but filler before the point fails `lead`.

### Grade

- `pass` if `missing::` is empty.
- `fail` otherwise.

The grade comes only from the `missing::` list, so it can never disagree with it.

### Reference examples

**1. Story question**

> Have you ever had to manage an emergency or a big outage or anything like that? Something high stress.

Answer: on-call at a previous job as a junior and "had to ask for some help"; at Octimine "there were 2 times where it would just like keep failing", "I had to babysit it", "It wasn't a complete outage"; staying calm and separating what's known from what isn't; a root cause analysis and incident documentation afterwards.

- **Content:**
  - pass: `answered`, `accurate`
  - fail: `complete` (no actual emergency handled), `specifics` (never says what failed or what was done)
  - substance: no story dimension passes. There's no specific problem or impact (`beginning`), the approach stands in for actions (`middle`), there's no outcome (`end`), and a failing, late batch job isn't an outage (`fits`).
- **Delivery:** all three fail. It doesn't lead (it opens with on-call as a junior), it hedges ("I think there were 2 times"), and the backstory buries the point.
- **Grade:** `fail`.

**2. Design question**

> If Wonderland suddenly grows from 1,000 to a million users, how would you approach scaling the infrastructure without sacrificing reliability?

Answer: "Um... Let's see. That's a huge increase. 1000 to a million." Then: deploy to a small number of servers with a standard configuration, and add more servers seamlessly as users grow.

- **Content:**
  - pass: `answered`, `accurate`
  - fail: `complete` (the reliability half is unaddressed), `specifics` (no mechanisms named)
  - substance: only `mechanism` passes (standardized configuration, horizontal scaling). There's no `diagnose`, `reliability` or `validate`. A threshold on user count is a weak capacity signal.
- **Delivery:** `lead` fails (it stalls before the point). `confident` and `focused` pass.
- **Grade:** `fail`.

## Interview mode

1. **Read the note.** Read `Applications/{Application}/Interviews/{n}/{n}.md`. If it has no `## Questions` section with at least one `### {question}` heading, STOP with one line saying so.
2. **Get the transcript.** If `transcript-processed.md` doesn't exist beside the note, invoke the `djspeakers` skill with the Skill tool for `{Application} {n}` first; if it can't label the transcript, STOP with one line saying why. Read `transcript-processed.md` in full. `**Me:**` turns are the candidate's; every other label is an interviewer's.
3. **Gather the items.** For each `###` question in `## Questions`, in order:
   - the question: the heading text
   - the reference answer: the fenced block after the question's bullets, or, if the question is followed by a `![[Note#Heading]]` embed, the code block in that `Answers/` section (see Finding the reference answer)
   - the candidate's answer: the text of their `**Me:**` turns from where the interviewer asks that question until the interviewer moves on, including follow-up exchanges on the same point, copied exactly and joined with ` … `. If the question can't be found in the transcript, grade it as unanswered (`answered` fails, with the `answered` item explaining that the transcript has no answer to it).
4. **Grade** each item by the Rubric, into the block shape in Output.
5. **Write the results.** For each question, replace its existing field bullets (`grade`, `score`, `answer`, `missing` with its sub-bullets, `feedback`, and any other `- field::` bullets except `- practice::`) with the new block, using Edit anchored on the question's heading. The new block sits between the heading's blank line and the model answer; keep any `- practice::` lines right after it. A question with no bullets gets the block inserted under its heading, separated by one blank line on each side.
6. **Remove any tally line.** Older notes open the section with a `Graded against the transcript: …` line. If there is one, delete it, along with the blank line after it. Don't add one.
7. **Commit, report and stop.** Commit the note: `git add -- "Applications/{Application}/Interviews/{n}/{n}.md" && git commit -m "Grade {Application} interview {n}" -- "Applications/{Application}/Interviews/{n}/{n}.md"`. The message MUST be exactly this, with the placeholders filled in: one line, no body, no other wording. Then report one line: the note, the number of questions, the pass/fail tally, and the average score. Then STOP.

## Output

For each item, exactly this shape, one field per list item:

```markdown
- grade:: {pass | fail}
- score:: {1–12}
- answer:: {what the candidate said}
- missing::
  - **{check}:** {what was missing or wrong, for that check}
- feedback:: {the grader's own thoughts on the answer}
```

The question type is worked out to choose the substance checks, but it isn't part of the output.

- `answer::` is the candidate's whole answer, verbatim, in double quotes, on one line. It MUST NOT be a paraphrase, a summary or an excerpt: every point the candidate made is in it, so the `missing::` list can be checked against it.
  - It runs from the candidate's first word on the question to their last, including any follow-up exchange on the same point.
  - Leave out the interviewer's words (questions, interjections like "Okay." or "Yeah, that's great."). Where the interviewer's words split the answer, join the candidate's parts with ` … `.
  - Quote filler and transcription errors as they appear; don't correct them.
- `missing::` has no value on its own line. Under it, indented two spaces, is one sub-bullet per failed check, content checks first, then delivery, labelled with the check name in bold: `  - **lead:** …`. A substance dimension is labelled `substance:{dimension}` (e.g. `  - **substance:validate:** …`).
  - Each sub-bullet names, concretely, what that check needed. For a substance dimension, describe the gap and give one possible example ("e.g. …"), never a required solution. For `lead`, give the direct first sentence the answer could have opened with.
  - If `answered` fails, give a single `**answered:**` sub-bullet with the correct answer in brief, instead of one per check.
  - Omit `missing::` entirely for `pass`.
- `score::` is a whole number from 1 to 12: the grader's own overall judgment of how well the candidate did on this question. It's entirely subjective. It isn't computed from the checks, the `missing::` list or the grade, and two answers with the same grade can score very differently.
- `feedback::` is the grader's own thoughts on the answer, in a few sentences of plain prose on one line. It's entirely subjective and can cover anything: what worked, what didn't, how it would land with an interviewer, what to change. It isn't limited to the rubric, and it's written for `pass` as well as `fail`.

**Item mode, ad hoc:** print the block for each item. Then STOP.

**Item mode, invoked by another skill:** produce the blocks and continue with the caller's steps. The caller's output rules apply.

**Interview mode:** write the blocks into the note (see Interview mode); don't print them.
