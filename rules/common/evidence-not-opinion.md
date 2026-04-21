# Rule: evidence-not-opinion

**Applies**: always, across every skill, agent, command, and artifact.

## The rule

Every metric, threshold, performance claim, and effectiveness assertion is evidenced by a named artifact (test report, log, dataset, sign-off memo). No unsourced numbers. No "we believe" or "it is likely". Replace with "measured on dataset X v1.2 on 2026-03-14, see report Z, signatory Chen Wei."

## Why

Annex IV §2 requires test logs dated and signed. Art. 13(3) requires accuracy/robustness/cybersecurity disclosures grounded in real measurements. Market-surveillance authorities under Art. 74 can request supporting evidence at any time. A number without a provenance chain fails both obligations.

## Required patterns

- Every metric states: value, unit, dataset identifier with version, measurement date, signatory.
- Every effectiveness claim links to a test report or audit memo.
- Subjective language ("we believe", "it should", "we are confident") is replaced with the evidentiary basis or explicitly flagged as an open question for legal.

## Forbidden patterns

- Performance numbers in a summary without a link to the source report.
- "State of the art" or "industry leading" without a benchmark reference.
- Aggregating numbers from multiple dataset versions without stating which.
- Copying prior-period numbers without re-measurement when the system has changed.

## Enforcement

QA agent flags any numeric claim within an AI Act artifact that is not followed within the same paragraph (or via a footnote) by a dataset + version + date + signatory reference.
