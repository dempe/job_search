"""Tests for pick.sh --all. Run: python3 -I .claude/skills/djq/test_pick.py"""

import pathlib
import subprocess
import tempfile
import unittest

PICK = pathlib.Path(__file__).parent / "pick.sh"

APPLICATION = """---
type: job
---

## Application

> Why us?

```
Because.
```

#### Practice

##### 1

- date:: 2026-11-07 14:03:22
- grade:: pass
- score:: 9
- answer:: "Because."
- feedback:: Fine.

> Quoted email, not a question.

Some prose.

> Tell us about a project.<br/>
> Keep it short.

![[Answers note#Acme]]
"""

INTERVIEW = """---
type: interview
---

## Transcript

![[Applications/Acme/Interviews/2/transcript-processed]]

## Questions

### What is Kafka?

- grade:: fail
- missing::
  - **lead:** stalled

#### Canonical Answer

```
A log.
```

#### Practice

##### 1

- date:: 2026-11-07 14:03:22
- grade:: fail
- score:: 6
- answer:: "It's a log."
- missing::
  - **specifics:** no detail
- feedback:: Say more.

##### 2

- date:: 2026-11-08 09:00:00
- grade:: pass
- score:: 10
- answer:: "A distributed, partitioned log."
- feedback:: Good.

### Why leave?

#### Canonical Answer

![[Returning#Acme]]

## Retrospective

### What Went Well

- Calm
"""


class PickAllTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def run_all(self, rel, text):
        note = self.root / rel
        note.parent.mkdir(parents=True)
        note.write_text(text, encoding="utf-8")
        result = subprocess.run(["bash", str(PICK), "--all", str(note)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_lists_every_application_question_in_order(self):
        out = self.run_all("Applications/Acme/Acme.md", APPLICATION)
        self.assertEqual(out, (
            "Acme\nApplications/Acme/Acme\n"
            "> Why us?\n\n"
            "> Tell us about a project.<br/>\n> Keep it short.\n"
        ))

    def test_lists_every_interview_question_in_order(self):
        out = self.run_all("Applications/Acme/Interviews/2/2.md", INTERVIEW)
        self.assertEqual(out, (
            "Acme - Interview 2\nApplications/Acme/Interviews/2/2\n"
            "> What is Kafka?\n\n"
            "> Why leave?\n"
        ))

    def test_lists_more_questions_than_the_interview_number(self):
        out = self.run_all("Applications/Acme/Interviews/1/1.md", INTERVIEW.replace("Interviews/2", "Interviews/1"))
        self.assertEqual(out, (
            "Acme - Interview 1\nApplications/Acme/Interviews/1/1\n"
            "> What is Kafka?\n\n"
            "> Why leave?\n"
        ))

    def test_note_without_questions_exits_non_zero(self):
        note = self.root / "Applications/Acme/Acme.md"
        note.parent.mkdir(parents=True)
        note.write_text("---\ntype: job\n---\n\n## Application\n", encoding="utf-8")
        result = subprocess.run(["bash", str(PICK), "--all", str(note)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)


class PickAnswersTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)
        for rel, text in [
            ("Applications/Acme/Acme.md", APPLICATION + "\n> Unanswered?\n\n```\n  \n```\n"),
            ("Applications/Acme/Interviews/2/2.md", INTERVIEW),
        ]:
            note = self.root / rel
            note.parent.mkdir(parents=True, exist_ok=True)
            note.write_text(text, encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_lists_every_answered_question_with_its_answer(self):
        result = subprocess.run(["bash", str(PICK), "--answers", str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, (
            "Applications/Acme/Acme\n> Why us?\n```\nBecause.\n```\n\n"
            "Applications/Acme/Interviews/2/2\n> What is Kafka?\n```\nA log.\n```\n"
        ))


if __name__ == "__main__":
    unittest.main()
