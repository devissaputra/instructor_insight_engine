# Research protocol

## Project

Instructor Insight Engine

## Questions

1. Which aggregated indicators are actionable for instructors without encouraging surveillance?
2. How should cohort and learner views distinguish signal from noise?
3. Can trend detection surface intervention opportunities early?

## Baseline methods

- event aggregation
- attempt and accuracy summaries
- minimum evidence flag rule
- class level aggregation
- human review output

## Evidence to collect

Start from the current transparent baseline and record every transformation needed to produce learner summaries, a transparent review flag, and class level aggregate signals. Keep a clear boundary between synthetic demonstration data and any future empirical dataset.

## Validation

Evaluate flag precision and coverage against instructor review, then study whether the summaries lead to useful actions. Report cases where missing or sparse event data create misleading signals.

## What counts as a useful result

The next version should test whether these summaries help instructors notice actionable patterns earlier than a raw gradebook. Flag rules should be compared with instructor judgments and tuned around real review capacity.

## Threats to validity

Different courses generate different event patterns, attempts may not be comparable across tasks, and a low activity trace does not necessarily mean low engagement.
