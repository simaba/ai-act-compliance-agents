# Rule: cite-the-article

**Applies**: always, across every skill, agent, command, and artifact.

## The rule

Every regulatory claim is cited by article number and (where relevant) annex and recital. Paraphrases are not citations. "The Act says we must..." is not a citation; "Art. 14(4)(b) requires..." is.

## Why

Auditors and notified bodies will check claims by walking back to the regulatory text. A paraphrase forces the reviewer to guess which article you meant; a precise citation lets them verify in seconds. Imprecise citations also make automated traceability checks (`scripts/traceability_check.py`) impossible.

## Required pattern

`Art. <N>(<para>)(<lit>)` — for example `Art. 6(3)`, `Art. 14(4)(b)`, `Art. 73(2)(a)`. Annex citations use `Annex <Roman>` and section number where relevant: `Annex IV §5`, `Annex III #4`. Recitals: `Recital 73`. Standards: `EN ISO/IEC 42001:2023 §6.1.2`.

## Forbidden patterns

- "The AI Act requires..."
- "Per the regulation..."
- "Article 14" without the paragraph and literal where the text has them.
- Citing recitals as binding obligations (recitals are interpretive, not normative).

## Enforcement

The QA pass on every artifact greps for `Art\.\s+\d+` and verifies that every regulatory claim within 50 characters carries an article-number citation. Failures are surfaced before sign-off.
