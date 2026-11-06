"""Tests for label.py. Run: python3 -I .claude/skills/djspeakers/test_label.py"""

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from label import label, render, switch_embed  # noqa: E402

NOTE = "---\ntype: interview\n---\n\n## Transcript\n\n![[Applications/Acme/Interviews/2/transcript]]\n\n## Questions\n"

RAW = "Hi, Chris. Hi.  Can you hear me?  Yeah, I can hear you.\nSo tell me about Kafka. Kafka is a log. Okay.  Yeah."


class LabelTest(unittest.TestCase):
    def test_splits_raw_text_at_anchors(self):
        anchors = "Interviewer: Hi, Chris.\nMe: Hi.\nInterviewer: Can you hear\nMe: Yeah, I can hear\nInterviewer: So tell me\nMe: Kafka is a log.\nInterviewer: Okay.\nMe: Yeah."
        self.assertEqual(label(RAW, anchors), [
            ("Interviewer", "Hi, Chris."),
            ("Me", "Hi."),
            ("Interviewer", "Can you hear me?"),
            ("Me", "Yeah, I can hear you."),
            ("Interviewer", "So tell me about Kafka."),
            ("Me", "Kafka is a log."),
            ("Interviewer", "Okay."),
            ("Me", "Yeah."),
        ])

    def test_turns_rejoin_to_the_raw_text(self):
        turns = label(RAW, "Interviewer: Hi, Chris.\nMe: Hi.\nInterviewer: Can you hear\nMe: Yeah, I can hear")
        self.assertEqual(" ".join(t for _, t in turns), " ".join(RAW.split()))

    def test_merges_consecutive_turns_by_the_same_speaker(self):
        turns = label(RAW, "Interviewer: Hi, Chris.\nInterviewer: Hi.\nMe: Can you hear")
        self.assertEqual(turns[0], ("Interviewer", "Hi, Chris. Hi."))
        self.assertEqual(len(turns), 2)

    def test_render_writes_one_bold_labelled_paragraph_per_turn(self):
        self.assertEqual(render([("Me", "Hi."), ("Interviewer", "Okay.")]), "**Me:** Hi.\n\n**Interviewer:** Okay.\n")

    def test_first_anchor_must_start_the_transcript(self):
        with self.assertRaisesRegex(ValueError, "line 1"):
            label(RAW, "Me: Hi.\nInterviewer: Can you hear")

    def test_anchor_not_found_names_its_line(self):
        with self.assertRaisesRegex(ValueError, "line 2.*not found"):
            label(RAW, "Interviewer: Hi, Chris.\nMe: Something never said")

    def test_anchor_that_recurs_before_the_next_anchor_is_ambiguous(self):
        # "Yeah." appears twice before "Done.", so it's unclear which one starts the turn.
        raw = "Right. Yeah. Right. Yeah. Done."
        with self.assertRaisesRegex(ValueError, "line 2.*ambiguous"):
            label(raw, "Interviewer: Right.\nMe: Yeah.\nInterviewer: Done.")

    def test_malformed_line_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "line 2.*Label: words"):
            label(RAW, "Interviewer: Hi, Chris.\nno label here")

    def test_blank_lines_in_anchors_are_ignored(self):
        turns = label(RAW, "Interviewer: Hi, Chris.\n\nMe: Hi.\n")
        self.assertEqual([s for s, _ in turns], ["Interviewer", "Me"])


class SwitchEmbedTest(unittest.TestCase):
    def test_points_the_raw_transcript_embed_at_the_processed_file(self):
        self.assertEqual(
            switch_embed(NOTE, "Applications/Acme/Interviews/2"),
            NOTE.replace("/transcript]]", "/transcript-processed]]"),
        )

    def test_already_switched_note_is_unchanged(self):
        switched = NOTE.replace("/transcript]]", "/transcript-processed]]")
        self.assertEqual(switch_embed(switched, "Applications/Acme/Interviews/2"), switched)

    def test_embed_of_another_interview_is_left_alone(self):
        self.assertEqual(switch_embed(NOTE, "Applications/Acme/Interviews/1"), NOTE)


if __name__ == "__main__":
    unittest.main()
