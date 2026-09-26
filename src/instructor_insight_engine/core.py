# Calculation reading guide: ../CALCULATIONS.md (repository root).
# Learner accuracy = total correct / total attempts; flag if accuracy < .5 and attempts ≥ 3.
# Class mean accuracy is an unweighted average across learners. No-attempt records currently use a zero sentinel, so sparse evidence must be inspected rather than interpreted as demonstrated failure.

from collections import defaultdict


def cohort_summary(events):
    """Aggregate event level evidence into learner summaries and review flags."""
    by_learner = defaultdict(lambda: {"minutes": 0, "attempts": 0, "correct": 0})
    for event in events:
        if "learner" not in event:
            raise ValueError("each event must include a learner")
        learner = event["learner"]
        attempts = event.get("attempts", 0)
        correct = event.get("correct", 0)
        minutes = event.get("minutes", 0)
        if min(attempts, correct, minutes) < 0 or correct > attempts:
            raise ValueError("event counts must be non-negative and correct cannot exceed attempts")
        summary = by_learner[learner]
        summary["minutes"] += minutes
        summary["attempts"] += attempts
        summary["correct"] += correct

    output = {}
    for learner, summary in by_learner.items():
        accuracy = summary["correct"] / summary["attempts"] if summary["attempts"] else 0.0
        output[learner] = {
            **summary,
            "accuracy": accuracy,
            "flag": accuracy < 0.5 and summary["attempts"] >= 3,
        }
    return output


def class_signals(summary):
    """Return a small class level summary from learner aggregates."""
    values = list(summary.values())
    return {
        "learners": len(values),
        "flagged": sum(bool(value["flag"]) for value in values),
        "mean_accuracy": (
            sum(value["accuracy"] for value in values) / len(values) if values else 0.0
        ),
    }
