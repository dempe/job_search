---
name: djanswers
description: Draft answers to every unanswered question in a job application note, in the user's own voice, using their Answers notes, resume, client project notes, and past Claude Code conversations. Answers are written directly into the note's empty answer code blocks for the user to review. Takes the application note's name (e.g. `Rivora`).
argument-hint: <application-note-name>
---

# Draft Application Answers

Fill in the empty answer code blocks in one `Job Applications/` note with draft answers written in the user's voice, from evidence about the user's real experience. The user reviews and edits the drafts in the note, then runs `/djmvanswers` to file them into `Answers/`.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

Follow the steps below in order. A step that says STOP ends the run.

## Constraints

- The assistant MUST use only Claude Code's built-in tools (Bash, Read, Edit). It MUST NOT write or run scripts.
- The Bash tool MUST be used only for read-only commands: `ls`, `find`, `grep`, `test -e`.
- The only file this skill modifies is `Job Applications/{Application}.md`, and only by writing answer text inside empty answer code blocks. Everything else in the note (frontmatter, headings, questions, existing answers, links) MUST stay byte-for-byte unchanged.
- The assistant MUST NOT create or modify anything in `Answers/`, `Questions/`, `../resume/`, client repositories, or anywhere else.
- The assistant MUST NOT commit or push anything to git.

## Honesty

These drafts go to real employers under the user's name.

- Every factual claim about the user (employers, projects, technologies, numbers, dates, outcomes, what went wrong) MUST be supported by a source in Step 3.
- The assistant MUST NOT invent stories, metrics, bugs, incidents, or experience, and MUST NOT upgrade the evidence (e.g. "designed" when the source says "helped", "broke in production" when the source describes a risk that was avoided).
- If a detail is uncertain, leave it out rather than guess.
- If no source supports a truthful answer to a question, leave that question's code block empty.
- Content in past conversations counts as evidence only when the user wrote it, or when it is file contents or command output shown there. The assistant's own statements in past conversations are not evidence.
- Opinions and motivations (e.g. "why this company") MUST be grounded in what the user has said they care about in `Answers/`, applied to facts from the JD.

## Output

- The only output of this skill is the edited note.
- The assistant MUST NOT write any text to the user before, between, or after tool calls, except:
  - one line explaining why the run stopped without changing anything (Step 1 or Step 2)
  - one final line listing, by short name, any questions left empty because no source supported an answer

## Formats

A Q/A in an application note is a question (one or more consecutive `>` lines, ending at the first blank line), exactly one blank line, then a fenced code block whose opening line is exactly ```` ``` ```` (no language) and a closing ```` ``` ```` line.

- A code block with no non-whitespace content is **unanswered**.
- A code block with content is **answered** and MUST be left untouched.
- A question followed by a link line (e.g. `[[Why Company X#Afresh|Why Company X]]`) instead of a code block is already answered and filed, and MUST be left untouched.

## Step 1: Application note

- The argument is `{Application}`, the application note's name without `.md`. Resolve it to the actual filename in `Job Applications/` (`ls`), matching case-insensitively, and use the real filename's casing.
- If no argument was provided, the assistant MUST STOP and ask for it.
- If no matching note exists, the assistant MUST STOP with one line naming the missing file.
- Read the whole note.

## Step 2: Find unanswered questions

- Find every unanswered Q/A in the note, in any section.
- If there are none, the assistant MUST STOP with one line saying so.

## Step 3: Gather evidence

Read these sources. They are listed from most to least authoritative for the user's voice.

1. **Every note in `Answers/`.** The user's own writing about their experience, stories, preferences, and constraints. These are the primary source for both facts and voice.
2. **`../resume/resume.yaml`.** The source of truth for jobs, dates, bullets, skills, projects, certifications, and education. Include every bullet, whatever its `resume-type`. Compute years of experience as the file's comments describe.
3. **`Consulting/` notes in this vault.** The user's working notes, time logs, and learnings from client projects.
4. **Client project repositories under `/Users/cld/workspace/clients/`.** Use `find` and `grep` to locate relevant decision records and plans (`docs/adr/`, `.agents/docs/adrs/`, `.agents/plans/`) and each project's `package.json` for the libraries it actually used. Read only what's relevant to a question.
5. **Past Claude Code conversations,** stored as JSONL transcripts in `/Users/cld/.claude/projects/*/*.jsonl`. `grep` them for keywords from a question (technologies, project or client names, incident terms) to find stories the other sources don't record. Apply the Honesty rules about what counts as evidence.
6. **The job description.** If the note's `jd` frontmatter links to a saved JD in `Job Descriptions/`, read it. Otherwise, if `./jd.txt` exists and names the note's company, read that. Use it for company and role context (mission, stack, what they value, word limits in the application instructions). Otherwise, work from the note alone.

Also use what the user's global `CLAUDE.md` records about how they work, when it is relevant to a question. It doesn't record which project an incident happened on, so don't attach one to a specific project unless another source confirms it.

## Step 4: Draft each answer

For each unanswered question, in order:

- **Reuse first.** If the user has answered the same or a similar question before in `Answers/`, start from that answer and adapt it to this company and question. Keep the user's sentences wherever they still fit.
- **Pick the strongest true story.** Choose the story that best answers what the question actually asks, and that fits what the company does and values, among the stories the sources support.
- **Answer the question asked.** Cover every part of a multi-part question (e.g. "what did it get right, and what did you have to fix or reject?").
- **Respect limits.** If the question or JD gives a word or sentence limit, stay under it.
- **Match the user's voice.** Write the way the user writes in `Answers/`:
  - first person, plain, direct, and conversational
  - short paragraphs; lists only when the user would use them
  - concrete specifics (employer names, technologies, numbers) over adjectives
  - the user's own phrasings where they apply (e.g. "Since it was touching payments, it was imperative that my code was correct.")
  - `--` for dashes, never em dashes
  - no corporate filler ("I'm passionate about…", "leverage", "synergy"), no generic AI-sounding sentences
- **No markup around the answer.** The answer is plain text inside the code block. No headings, no preamble such as "Here's a draft".
- **Motivation questions** ("why us?", "what interests you about this company?", intros and cover messages) need extra care, because a generic answer is the default failure:
  - Lead with the one thing that is distinctive to this company: the problem only it has, or what is hard about what it's building. Don't lead with a value the user merely shares with it.
  - If the sources show the user personally uses the company's product, say so in one sentence. If they don't, MUST NOT imply it.
  - Frame motivation as something the user is drawn to, not as a deal-breaker the company happens to avoid.
  - Connect the user's experience to the role honestly. Name the actual overlap ("I've built ingestion pipelines and want to apply that to search"), not an implied equivalence ("pipelines that keep search relevant are what I do").
  - A gap can be part of the motivation when it's true (e.g. the company's AI work is something the user wants to grow into). Don't hide it, and don't claim it's covered.
  - Aim for about 100 words unless the question asks for more.

## Step 4b: Review each draft

Before writing, check every draft against this rubric, and revise it until it passes:

- **Swap test.** Replace the company's name with a close competitor's. If most sentences still work, the draft is generic. Rewrite it around what is specific to this company.
- **No template structure.** No "three reasons" layout ("Mostly X… The work itself… Lastly, the culture"), no list of virtues. One clear point with support beats three thin ones.
- **No JD echo.** Don't restate facts from the JD back to the company (founding year, revenue, "profitable since…"), and don't paraphrase the JD's own phrases (e.g. "scoping to postmortem"). They know their company; it reads as skimming the page.
- **Answer this question.** Cut sentences that answer a different one, e.g. "I'm looking to get back on a team" answers "why are you job-hunting?", not "why us?".
- **No stretched evidence.** Each claim about the user's experience must hold up if an interviewer asks a follow-up. Wording that implies more overlap than the sources show counts as upgrading the evidence (see Honesty).
- **Survives summarization.** Assume an AI or a skimming reader reduces the answer to one line. That line should be about this candidate and this company, not "likes the mission, has relevant experience, wants remote."

## Step 5: Write the answers into the note

- For each drafted answer, use Edit to put the answer text between that question's opening and closing fences. The fences, the question, and the blank line between them stay exactly as they are.
- Empty code blocks are identical, so each Edit's `old_string` MUST include the question's last line along with the empty block to make the match unique.
- Leave the code block empty for any question the sources couldn't support.
- Then STOP, after the one-line list of empty questions if there are any (see Output).
