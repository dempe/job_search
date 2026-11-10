---
name: djanswers
description: Draft answers to every unanswered question in a job application note, in the user's own voice, using their past answers in other application and interview notes, resume, client project notes, and past Claude Code conversations. Answers are written directly under the note's unanswered questions for the user to review. Takes the application note's name (e.g. `Rivora`).
argument-hint: <application-note-name>
---

# Draft Application Answers

Answer the unanswered questions in one `Applications/` application note with draft answers written in the user's voice, from evidence about the user's real experience. The user reviews and edits the drafts in the note.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

Follow the steps below in order. A step that says STOP ends the run.

## Constraints

- The assistant MUST use only Claude Code's built-in tools (Bash, Read, Edit). It MUST NOT write scripts, and the only script it runs is `pick.sh --answers`.
- The Bash tool MUST be used only for read-only commands (`ls`, `find`, `grep`, `test -e`, `git log`, `git diff`, `git show`), `bash .claude/skills/djq/pick.sh --answers` (Step 3), and the commit in Step 5 (`git add`, `git commit`).
- The only files this skill modifies are `Applications/{Application}/{Application}.md`, and only by writing answer text under unanswered questions. Everything else in them (frontmatter, headings, questions, existing answers, links) MUST stay byte-for-byte unchanged.
- The assistant MUST NOT create or modify anything in other application notes, any interview note, `../resume/`, client repositories, or anywhere else.
- The assistant commits only the notes it edited, in Step 5. It MUST NOT push.

## Honesty

These drafts go to real employers under the user's name.

- Every factual claim about the user (employers, projects, technologies, numbers, dates, outcomes, what went wrong) MUST be supported by a source in Step 3.
- The assistant MUST NOT invent stories, metrics, bugs, incidents, or experience, and MUST NOT upgrade the evidence (e.g. "designed" when the source says "helped", "broke in production" when the source describes a risk that was avoided).
- If a detail is uncertain, leave it out rather than guess.
- If no source supports a truthful answer to a question, leave that question unanswered.
- Content in past conversations counts as evidence only when the user wrote it, or when it is file contents or command output shown there. The assistant's own statements in past conversations are not evidence.
- Opinions and motivations (e.g. "why this company") MUST be grounded in what the user has said they care about in their past answers, applied to facts from the JD.

## Output

- The only output of this skill is the edited note.
- The assistant MUST NOT write any text to the user before, between, or after tool calls, except:
  - one line explaining why the run stopped without changing anything (Step 1 or Step 2)
  - one final line listing, by short name, any questions left empty because no source supported an answer

## Formats

A question is a `### {question}` heading in a note's `## Questions` section. Its answer is plain text, up to the next heading:

- In an application note, the text directly under the heading, before any `#### Practice` subheading.
- Interview notes hold no answers to fill in: their questions carry only grade bullets and practice sessions, so this skill doesn't touch them.

- A question with no non-whitespace answer text is **unanswered**.
- A question with answer text is **answered** and MUST be left untouched.
- The bullets, and any `#### Practice` section after the answer, MUST be left untouched.

## Step 1: Application note

- The argument is `{Application}`, the application note's name without `.md`. Resolve it to an application folder in `Applications/` (`ls`), matching case-insensitively, and use that folder's casing. The note is `Applications/{Application}/{Application}.md`.
- If no argument was provided, the assistant MUST STOP and ask for it.
- If no matching note exists, the assistant MUST STOP with one line naming the missing file.
- Read the whole note.

## Step 2: Find unanswered questions

- Find every unanswered question in the note's `## Questions` section.
- If there are none, the assistant MUST STOP with one line saying so.

## Step 3: Gather evidence

Read these sources. They are listed from most to least authoritative for the user's voice.

1. **The user's past answers,** printed by `bash .claude/skills/djq/pick.sh --answers`: every answered question in `Applications/`, each after its note's path. The user's own writing about their experience, stories, preferences, and constraints. These are the primary source for both facts and voice. It includes every `answer::` line: what the user said in interviews (machine-transcribed speech) and in practice sessions. Each sits beside its `grade::`, `missing::` and `feedback::` bullets in the note; prefer answers graded `pass`, and don't reuse a claim that a `missing::` item flags as inaccurate.
2. **`../resume/resume.yaml`.** The source of truth for jobs, dates, bullets, skills, projects, certifications, and education. Include every bullet, whatever its `resume-type`. Compute years of experience as the file's comments describe.
3. **`Consulting/` notes in this vault.** The user's working notes, time logs, and learnings from client projects.
4. **Client project repositories under `/Users/cld/workspace/clients/`.** Use `find` and `grep` to locate relevant decision records and plans (`docs/adr/`, `.agents/docs/adrs/`, `.agents/plans/`) and each project's `package.json` for the libraries it actually used. Read only what's relevant to a question.
5. **Past Claude Code conversations,** stored as JSONL transcripts in `/Users/cld/.claude/projects/*/*.jsonl`. `grep` them for keywords from a question (technologies, project or client names, incident terms) to find stories the other sources don't record. Apply the Honesty rules about what counts as evidence.
6. **The job description.** If the note's `jd` frontmatter links to a saved JD (`Applications/{Application}/jd.md`), read it. Otherwise, if `./jd.txt` exists and names the note's company, read that. Use it for company and role context (mission, stack, what they value, word limits in the application instructions). Otherwise, work from the note alone.

Also use what the user's global `CLAUDE.md` records about how they work, when it is relevant to a question. It doesn't record which project an incident happened on, so don't attach one to a specific project unless another source confirms it.

## Step 3b: Choose voice exemplars

The drafts must sound like the user, and the only reliable guide to that is the user's own writing. A description of their voice is not enough: the assistant will fill it in with its own idea of "plain and direct", which reads as AI-written.

- **Find the user's own written answers.** Not every answer in `Applications/` was written by the user: some are drafts from earlier runs of this skill, left as they were. List the draft commits with `git log --format="%h %s" --grep="^Draft .* answers$"`.
  - An answer in a note with no draft commit was written by the user.
  - For a note with a draft commit, `git diff {commit} HEAD -- {note}` shows what the user changed afterwards. Text the user added or rewrote is theirs. Text left exactly as drafted is not, and MUST NOT be used as an exemplar.
- **The user's rewrites are the strongest evidence.** Where the user replaced a draft, compare the draft (`git show {commit}:{note}`) with their version. Whatever they removed is what to avoid, and what they wrote instead is what to imitate.
- **Pick 3–5 exemplars**, written application answers rather than machine-transcribed speech, preferring answers to the same kind of question (motivation, a project story, a technical explanation). Read each one in full, not a grep excerpt.
- Note the shape the exemplars share, for this kind of question: how they open, the order they go in, how long they are, how they close, and the user's recurring phrasings.

## Step 4: Draft each answer

For each unanswered question, in order:

- **Follow the exemplars.** The draft's structure, length, opening, closing and sentence style MUST follow the exemplars from Step 3b for this kind of question. If the user opens by introducing themselves, walks through what they've built, and closes with a line of enthusiasm, the draft does the same.
- **Reuse first.** If the user has answered the same or a similar question before in their past answers, start from that answer and adapt it to this company and question. Keep the user's sentences wherever they still fit.
- **Pick the strongest true story.** Choose the story that best answers what the question actually asks, and that fits what the company does and values, among the stories the sources support.
- **Answer the question asked.** Cover every part of a multi-part question (e.g. "what did it get right, and what did you have to fix or reject?").
- **Respect limits.** If the question or JD gives a word or sentence limit, stay under it.
- **Use the user's words.** Prefer the user's own phrasings from the exemplars and past answers (e.g. "Since it was touching payments, it was imperative that my code was correct.") over new wording. Use `--` for dashes, never em dashes.
- **No markup around the answer.** The answer is plain text under the question. No headings, no code blocks, no preamble such as "Here's a draft".
- **Motivation questions** ("why us?", "what interests you about this company?", intros and cover messages):
  - Follow the shape of the user's own motivation answers (Step 3b), whatever it is. It is not the assistant's job to restructure it into a stronger pitch.
  - Tailor it to the role in the JD, not only the company. A company the user applied to before may be hiring for a different problem now, so an earlier answer for the same company is a starting point, not a final answer.
  - If the sources show the user personally uses the company's product, say so in one sentence. If they don't, MUST NOT imply it.
  - Connect the user's experience to the role honestly. Name the actual overlap ("I've built ingestion pipelines and want to apply that to search"), not an implied equivalence ("pipelines that keep search relevant are what I do").
  - A gap can be part of the motivation when it's true (e.g. the company's AI work is something the user wants to grow into). Don't hide it, and don't claim it's covered.

## Step 4b: Review each draft

Before writing, check every draft against this rubric, and revise it until it passes:

- **Voice check.** Read the draft next to the exemplars. Any sentence that would look out of place among them MUST be rewritten in the user's phrasing. Common giveaways the user doesn't write:
  - a sentence fragment as the opening line ("The path from a webhook to a personalized response.")
  - a neat closing line or summary ("…and that's a big part of the draw.")
  - balanced, polished sentences and rhetorical setups ("Not X, but Y")
  - abstract framing of the company's problem in place of plain statements about what the user did and wants
- **No JD echo.** Don't restate facts from the JD back to the company (founding year, revenue, "profitable since…"), and don't paraphrase the JD's own phrases (e.g. "scoping to postmortem"). They know their company; it reads as skimming the page.
- **No stretched evidence.** Each claim about the user's experience must hold up if an interviewer asks a follow-up. Wording that implies more overlap than the sources show counts as upgrading the evidence (see Honesty).

## Step 5: Write the answers into the note

- For each drafted answer, use Edit to put the answer text under the question: between the `### {question}` heading and the next heading. Exactly one blank line separates the answer from the heading above it and the heading below it. The headings stay exactly as they are.
- Leave unanswered any question the sources couldn't support.
- If any answer was written, commit the notes that were edited: `git add -- {each edited note} && git commit -m "Draft {Application} answers" -- {each edited note}`. The message MUST be exactly this, with the placeholders filled in: one line, no body, no other wording.
- Then STOP, after the one-line list of empty questions if there are any (see Output).
