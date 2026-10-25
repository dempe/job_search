---
name: djq
description: Pick one question at random from all the job application notes in `Job Applications/`, for interview practice. Takes no arguments.
---

# Random Application Question

Show the user one question chosen at random from every note in `Job Applications/`.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

## Constraints

- The assistant MUST pick the question by running `pick.sh`. It MUST NOT choose one itself, because a model's "random" choice isn't random.
- The assistant MUST NOT read or use the legacy `Questions/` directory.
- This skill MUST NOT create or modify any file.

## Step 1: Pick

Run the bundled script with Bash:

```bash
bash .claude/skills/djq/pick.sh
```

- The first line of output is the application note's name. The rest is the question, verbatim, as `>` lines.
- A question is a blockquote followed by one blank line and then an answer (a ```` ``` ```` fence or a `[[link]]` line), the same Q/A format the other skills use. Quoted emails and notes are not questions.
- If the script exits non-zero, STOP with one line saying no questions were found.

## Step 2: Show it

Write exactly this, and nothing else:

```markdown
{question, verbatim, as a blockquote}

From [[{note name}]]
```

- MUST NOT show the answer, comment on the question, or add anything else. The user is practicing.
- If the user then asks for the answer, read it from the note: the code block after the question, or the `Answers/` section its link points to.
