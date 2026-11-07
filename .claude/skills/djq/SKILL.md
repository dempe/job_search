---
name: djq
description: Pick one question at random from all the job application and interview notes in `Applications/`, for interview practice. When the user answers it, grade the attempt with djgrade and log it under the question. Takes no arguments.
---

# Random Application Question

Show the user one question chosen at random from every application note and interview note in `Applications/`. When they answer it, grade the attempt and log it.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

## Constraints

- The assistant MUST pick the question by running `pick.sh`. It MUST NOT choose one itself, because a model's "random" choice isn't random.
- The only file change this skill makes is adding one practice session to the question's `#### Practice` section (Step 3). Everything else in the note MUST stay byte-for-byte unchanged.
- The assistant commits only that note, in Step 3. It MUST NOT push.

## Step 1: Pick

Run the bundled script with Bash:

```bash
bash .claude/skills/djq/pick.sh
```

- The first line of output is the note's name: `{title}` for an application note, `{title} - Interview {n}` for an interview note. The second line is the note's vault path without `.md`. The rest is the question, verbatim, as `>` lines.
- A question is a blockquote followed by one blank line and then an answer (a ```` ``` ```` fence or a `![[…]]` embed line), or, in an interview note's `## Questions` section, a `### {question}` heading followed by its grade bullets and its answer under `#### Canonical Answer`. Quoted emails and notes are not questions.
- If the script exits non-zero, STOP with one line saying no questions were found.

## Step 2: Show it

Write exactly this, and nothing else:

```markdown
{question, verbatim, as a blockquote}

From [[{note path}|{note name}]]
```

- MUST NOT show the answer, comment on the question, or add anything else. The user is practicing.
- If the user then asks for the answer, read it from the note: the code block after the question (under its `#### Canonical Answer` subheading in an interview note), or the `Answers/` section its embed points to.

## Step 3: Grade an attempt

If the user replies with an answer to the question (typed, or pasted from speech) rather than asking for the model answer:

1. Invoke the `djgrade` skill with the Skill tool, passing the question, the user's reply as the candidate's answer, and the note path, so it finds the reference answer.
2. Show the user `djgrade`'s full output block.
3. Run `date "+%Y-%m-%d %H:%M:%S"` and log the attempt as a new numbered session in the question's `#### Practice` section:

   ````markdown
   #### Practice

   ##### {k}

   - date:: {YYYY-MM-DD HH:mm:ss}
   {djgrade's full output block, exactly as shown to the user}
   ````

   - The `#### Practice` section comes after the question's answer, never before it: in an interview note, after the model answer (code block or embed) under the question's `#### Canonical Answer` subheading; in an application note, after the answer fence or embed line that follows the `> ` blockquote. Putting it between the question and its answer would break the Q/A format the other skills rely on.
   - If the question has no `#### Practice` section yet, add it there with session `##### 1`, separated by one blank line from what comes before and after.
   - Otherwise add the new session after the section's last session. `{k}` is one more than the highest `#####` number in the section.
   - One blank line separates the headings, the session's bullets, and the sessions.
   - Use Edit, anchoring on the question's answer (and the section's last session, if it has one), so nothing else moves.

4. Commit the note: `git add -- "{note path}.md" && git commit -m "Log {Application} practice" -- "{note path}.md"` for an application note, or the same with the message `Log {Application} interview {n} practice` for an interview note. `{note path}` is the second line of `pick.sh`'s output. The message MUST be exactly this, with the placeholders filled in: one line, no body, no other wording.
5. STOP. If the user wants another question, they run `/djq` again.
