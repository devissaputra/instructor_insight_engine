# Analytic system card

## System

Instructor Insight Engine

## Purpose

Teacher facing aggregation baseline that turns course events into learner summaries, review flags, and class level signals.

## Current maturity

Working research prototype. The bundled example checks the software path with synthetic inputs. It does not establish validity for real learners, instructors, courses, or workplaces.

## Inputs

See `../data/README.md` for the current synthetic schema and the documentation expected before real data are connected.

## Outputs

The current code produces learner summaries, a transparent review flag, and class level aggregate signals. These outputs are research signals and should be interpreted with the educational context that produced them.

## Evidence needed before real use

Evaluate flag precision and coverage against instructor review, then study whether the summaries lead to useful actions. Report cases where missing or sparse event data create misleading signals.

## Main limitation

The current flag rule is intentionally simple and should not be interpreted as a diagnosis. Low accuracy can reflect task difficulty, sparse evidence, access barriers, or data quality problems.

## Human oversight

A person must review any output before it can affect a learner, instructor, applicant, or employee.
