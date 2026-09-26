# Calculation guide

## Question and evidence

Which learner summaries deserve a closer look?

Synthetic events containing learner IDs, minutes, attempts and correct counts.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Aggregate within learners; calculate accuracy; flag low accuracy only when at least three attempts exist.

## Calculation and interpretation

`Learner accuracy = total correct / total attempts; flag if accuracy < .5 and attempts ≥ 3.`

Class mean accuracy is an unweighted average across learners. No-attempt records currently use a zero sentinel, so sparse evidence must be inspected rather than interpreted as demonstrated failure.

## Evidence table

Worked example — illustrative, not a measured research result. Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| accuracy A (1 correct / 3) | 0.3333333333333333 | unitless | `outputs.accuracy A (1 correct / 3)` |
| flag A | True | unitless | `outputs.flag A` |

Source: [results/review_examples.json](results/review_examples.json). Values resolve directly from this file when figures are regenerated.

This prototype converts synthetic activity events into learner-level summaries and simple instructor review flags. Accuracy is calculated from aggregated correct and attempted responses, and a low-accuracy flag requires at least three attempts. It also exposes class-level summaries, with clear limits: the thresholds are unvalidated, time spent is not learning, and sparse records need human interpretation.

## Verification performed in this review

6 existing unittest checks passed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

For the explicitly illustrative example:

```bash
python scripts/review_examples.py
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`cohort_summary`](src/instructor_insight_engine/core.py#L8) | Aggregate event level evidence into learner summaries and review flags. |
| [`class_signals`](src/instructor_insight_engine/core.py#L36) | Return a small class level summary from learner aggregates. |

## What remains before a stronger research claim

Class mean accuracy is an unweighted average across learners. No-attempt records currently use a zero sentinel, so sparse evidence must be inspected rather than interpreted as demonstrated failure. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
