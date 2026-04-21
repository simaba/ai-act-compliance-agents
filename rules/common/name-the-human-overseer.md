# Rule: name-the-human-overseer

**Applies**: always, across every artifact that touches Art. 14.

## The rule

The human overseer is a named role with a named qualification standard. "The team", "operations", "legal", "trained personnel" are not overseers. Art. 14(5) presupposes a specific natural person who can be trained, assessed, and held accountable.

## Why

Art. 14(1) requires human oversight designed into the system such that it can be "effectively overseen by natural persons." Art. 14(5) further requires that the oversight person be "in a position to understand" the system's capacities and limitations — which implies identity, training, and assessment. Undesignated oversight is non-compliant oversight.

## Required patterns

- Oversight design frontmatter includes `overseer_role_title` (e.g., "Senior Recruiter") and `overseer_qualification` (e.g., "2+ years experience; 4-hour training course with assessment").
- Training curriculum is referenced by path and has a refresher cadence.
- The PMM plan monitors oversight behavior (override rate, time-to-review, rationale-completion) and escalates if the signals degrade.

## Forbidden patterns

- "A human reviews this" without role, qualification, or training curriculum.
- Rotating oversight duty across a large unnamed pool without a qualification standard applying to each member.
- Assuming that "anyone who uses the product" constitutes oversight — Art. 14 requires *designed* oversight, not incidental exposure.

## Enforcement

The `oversight-designer` agent refuses to issue a design with an empty `overseer_role_title` or `overseer_qualification` field. The `/audit-prep` command surfaces oversight rows with vague role definitions as P1 findings.
