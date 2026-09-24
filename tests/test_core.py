import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from instructor_insight_engine import core


class CoreTests(unittest.TestCase):
    def test_low_accuracy_is_flagged_after_enough_attempts(self):
        summary = core.cohort_summary([{"learner": "A", "attempts": 4, "correct": 1}])
        self.assertTrue(summary["A"]["flag"])
        self.assertEqual(core.class_signals(summary)["flagged"], 1)

    def test_low_accuracy_is_not_flagged_with_sparse_evidence(self):
        summary = core.cohort_summary([{"learner": "A", "attempts": 2, "correct": 0}])
        self.assertFalse(summary["A"]["flag"])

    def test_multiple_events_are_aggregated_per_learner(self):
        summary = core.cohort_summary([
            {"learner": "A", "attempts": 2, "correct": 1, "minutes": 5},
            {"learner": "A", "attempts": 2, "correct": 2, "minutes": 7},
        ])
        self.assertEqual(summary["A"]["attempts"], 4)
        self.assertEqual(summary["A"]["correct"], 3)
        self.assertEqual(summary["A"]["minutes"], 12)
        self.assertAlmostEqual(summary["A"]["accuracy"], 0.75)

    def test_class_signals_match_demo_logic(self):
        summary = core.cohort_summary([
            {"learner": "A", "attempts": 3, "correct": 1, "minutes": 15},
            {"learner": "B", "attempts": 3, "correct": 3, "minutes": 12},
        ])
        signals = core.class_signals(summary)
        self.assertEqual(signals["learners"], 2)
        self.assertEqual(signals["flagged"], 1)
        self.assertAlmostEqual(signals["mean_accuracy"], 2 / 3)

    def test_invalid_event_is_rejected(self):
        with self.assertRaises(ValueError):
            core.cohort_summary([{"learner": "A", "attempts": 1, "correct": 2}])
        with self.assertRaises(ValueError):
            core.cohort_summary([{"attempts": 1, "correct": 1}])

    def test_empty_cohort_has_zero_signals(self):
        self.assertEqual(
            core.class_signals({}),
            {"learners": 0, "flagged": 0, "mean_accuracy": 0.0},
        )


if __name__ == "__main__":
    unittest.main()
