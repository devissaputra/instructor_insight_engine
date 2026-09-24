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

    def test_invalid_event_is_rejected(self):
        with self.assertRaises(ValueError):
            core.cohort_summary([{"learner": "A", "attempts": 1, "correct": 2}])


if __name__ == "__main__":
    unittest.main()
