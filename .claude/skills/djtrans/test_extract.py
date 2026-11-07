"""Tests for extract.py. Run: python3 -I .claude/skills/djtrans/test_extract.py"""

import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from extract import attach  # noqa: E402

FRONT = "---\ntype: interview\nround: 1\n---\n"
EMBED = "## Transcript\n\n![[Applications/Acme/Interviews/1/transcript]]\n"
RAW = "Hi, Chris.  Hi.\nSo tell me about Kafka.\n"


class AttachTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(self.tmp.name)
        self.folder = root / "Applications" / "Acme" / "Interviews" / "1"
        self.folder.mkdir(parents=True)
        self.note = self.folder / "1.md"
        self.source = root / "transcript.txt"
        self.source.write_text(RAW, encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def attach_to(self, body):
        self.note.write_text(FRONT + body, encoding="utf-8")
        attach(self.note, self.source)
        return self.note.read_text(encoding="utf-8")

    def test_moves_the_source_unchanged(self):
        self.attach_to("")
        self.assertEqual((self.folder / "transcript.md").read_bytes(), RAW.encode())

    def test_leaves_no_source_behind(self):
        self.attach_to("")
        self.assertFalse(self.source.exists())

    def test_adds_the_transcript_embed_to_an_empty_note(self):
        self.assertEqual(self.attach_to(""), FRONT + "\n" + EMBED)

    def test_puts_the_transcript_before_the_existing_sections(self):
        body = "\n## Preparation\n\nRead up on Kafka.\n"
        self.assertEqual(self.attach_to(body), FRONT + "\n" + EMBED + body)

    def test_fills_an_empty_transcript_section(self):
        body = "\n## Transcript\n\n## Preparation\n\nRead up.\n"
        self.assertEqual(self.attach_to(body), FRONT + "\n" + EMBED + "\n## Preparation\n\nRead up.\n")

    def test_existing_transcript_is_not_overwritten(self):
        (self.folder / "transcript.md").write_text("old\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.attach_to("")
        self.assertEqual((self.folder / "transcript.md").read_text(encoding="utf-8"), "old\n")
        self.assertTrue(self.source.exists())
        self.assertEqual(self.note.read_text(encoding="utf-8"), FRONT)

    def test_transcript_section_with_content_is_left_alone(self):
        body = "\n## Transcript\n\nsomething\n"
        with self.assertRaisesRegex(ValueError, "already has"):
            self.attach_to(body)
        self.assertTrue(self.source.exists())
        self.assertFalse((self.folder / "transcript.md").exists())

    def test_missing_source_is_an_error(self):
        self.source.unlink()
        with self.assertRaisesRegex(ValueError, "not found"):
            self.attach_to("")


if __name__ == "__main__":
    unittest.main()
