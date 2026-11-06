---
name: djq
description: Pick one question at random from all the job application and interview notes in `Applications/`, for interview practice. When the user answers it, grade the attempt with djgrade and log it under the question. Takes no arguments.
---

# Random Application Question

Show the user one question chosen at random from every application note and interview note in `Applications/`. When they answer it, grade the attempt and log it.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

## Constraints

- The assistant MUST pick the question by running `pick.sh`. It MUST NOT choose one itself, because a model's "random" choice isn't random.
- The only file change this skill makes is appending one `- practice::` line under the question (Step 3). Everything else in the note MUST stay byte-for-byte unchanged.
- The assistant MUST NOT commit or push anything to git.

## Step 1: Pick

Run the bundled script with Bash:

```bash
bash .claude/skills/djq/pick.sh
```

- The first line of output is the note's name: `{title}` for an application note, `{title} - Interview {n}` for an interview note. The second line is the note's vault path without `.md`. The rest is the question, verbatim, as `>` lines.
- A question is a blockquote followed by one blank line and then an answer (a ```` ``` ```` fence or a `[[link]]` line), or, in an interview note's `## Questions` section, a `### {question}` heading followed by its answer. Quoted emails and notes are not questions.
- If the script exits non-zero, STOP with one line saying no questions were found.

## Step 2: Show it

Write exactly this, and nothing else:

```markdown
{question, verbatim, as a blockquote}

From [[{note path}|{note name}]]
```

- MUST NOT show the answer, comment on the question, or add anything else. The user is practicing.
- If the user then asks for the answer, read it from the note: the code block after the question, or the `Answers/` section its link points to.

## Step 3: Grade an attempt

If the user replies with an answer to the question (typed, or pasted from speech) rather than asking for the model answer:

1. Invoke the `djgrade` skill with the Skill tool, passing the question, the user's reply as the candidate's answer, and the note path, so it finds the reference answer.
2. Show the user `djgrade`'s grade block and its one or two sentences of coaching.
3. Run `date +%F` and log the attempt as one line under the question:

   ```markdown
   - practice:: {YYYY-MM-DD} {grade} -- {the checks labelled under `missing::`, comma-separated, e.g. "specifics, substance:validate, lead", or "nothing missing" for pass}
   ```

   - **Interview note** (`### {question}` heading): append the line after the last `- field::` bullet under the heading, or, if the question has no bullets, directly under the heading, separated from it by one blank line.
   - **Application note** (`> ` blockquote): add one blank line and the line immediately after the question's answer fence or link line, or after the last `- practice::` line already there. It MUST NOT go between the question and its answer, which would break the Q/A format the other skills rely on.
   - Use Edit, anchoring on the question's heading or blockquote and its answer, so nothing else moves.

4. STOP. If the user wants another question, they run `/djq` again.
