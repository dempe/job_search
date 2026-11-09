"""Tests for pick.sh (interview questions only), --all, and --answers (answer text, then every answer:: line). Run: python3 -I .claude/skills/djq/test_pick.py"""

import pathlib
import subprocess
import tempfile
import unittest

PICK = pathlib.Path(__file__).parent / "pick.sh"

APPLICATION = """---
type: job
---

## Questions

### Why us?

Because.

It's a good fit.

#### Practice

##### 1

- date:: 2026-11-07 14:03:22
- grade:: pass
- score:: 9
- answer:: "Because."
- feedback:: Fine.

### Tell us about a project. Keep it short.

- Built a crawler
- Built a pipeline

### Unanswered?

## Notes

> Quoted email, not a question.

### Cover letter draft

Some prose.

## Rejection

No thanks.
"""

INTERVIEW = """---
type: interview
---

## Transcript

![[Applications/Acme/Interviews/2/transcript-processed]]

## Questions

### What is Kafka?

- grade:: fail
- answer:: "Uh, a queue."
- missing::
  - **lead:** stalled

#### Practice

##### 1

- date:: 2026-11-07 14:03:22
- grade:: fail
- score:: 6
- answer:: "It's a log."
- missing::
  - **specifics:** no detail
- feedback:: Say more.

### Why leave?

## Retrospective

### What Went Well

- Calm
"""


class PickTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        note = self.root / rel
        note.parent.mkdir(parents=True, exist_ok=True)
        note.write_text(text, encoding="utf-8")
        return note

    def run_pick(self, *args):
        result = subprocess.run(["bash", str(PICK), *map(str, args)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_all_rejects_an_application_note(self):
        note = self.write("Applications/Acme/Acme.md", APPLICATION)
        result = subprocess.run(["bash", str(PICK), "--all", str(note)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

    def test_random_pick_skips_application_notes(self):
        self.write("Applications/Acme/Acme.md", APPLICATION)
        self.write("Applications/Acme/Interviews/2/2.md", INTERVIEW.replace("### Why leave?\n\n", ""))
        for _ in range(10):
            self.assertEqual(self.run_pick(self.root), (
                "Acme - Interview 2\nApplications/Acme/Interviews/2/2\n> What is Kafka?\n"
            ))

    def test_random_pick_without_interviews_exits_non_zero(self):
        self.write("Applications/Acme/Acme.md", APPLICATION)
        result = subprocess.run(["bash", str(PICK), str(self.root)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)

    def test_lists_every_interview_question_in_order(self):
        note = self.write("Applications/Acme/Interviews/2/2.md", INTERVIEW)
        self.assertEqual(self.run_pick("--all", note), (
            "Acme - Interview 2\nApplications/Acme/Interviews/2/2\n"
            "> What is Kafka?\n\n"
            "> Why leave?\n"
        ))

    def test_lists_more_questions_than_the_interview_number(self):
        note = self.write("Applications/Acme/Interviews/1/1.md", INTERVIEW.replace("Interviews/2", "Interviews/1"))
        self.assertEqual(self.run_pick("--all", note), (
            "Acme - Interview 1\nApplications/Acme/Interviews/1/1\n"
            "> What is Kafka?\n\n"
            "> Why leave?\n"
        ))

    def test_note_without_questions_exits_non_zero(self):
        note = self.write("Applications/Acme/Interviews/1/1.md", "---\ntype: interview\n---\n\n## Notes\n\n### Not a question\n")
        result = subprocess.run(["bash", str(PICK), "--all", str(note)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)

    def test_lists_every_answered_question_with_its_answer(self):
        self.write("Applications/Acme/Acme.md", APPLICATION)
        self.write("Applications/Acme/Interviews/2/2.md", INTERVIEW)
        self.assertEqual(self.run_pick("--answers", self.root), (
            "## Applications/Acme/Acme\n### Why us?\n\nBecause.\n\nIt's a good fit.\n\n"
            "## Applications/Acme/Acme\n### Why us?\n\n\"Because.\"\n\n"
            "## Applications/Acme/Acme\n### Tell us about a project. Keep it short.\n\n- Built a crawler\n- Built a pipeline\n\n"
            "## Applications/Acme/Interviews/2/2\n### What is Kafka?\n\n\"Uh, a queue.\"\n\n"
            "## Applications/Acme/Interviews/2/2\n### What is Kafka?\n\n\"It's a log.\"\n"
        ))


if __name__ == "__main__":
    unittest.main()
