# Rule: traceability-required

**Applies**: always, across every skill, agent, command, and artifact in this repo.

## The rule

Every compliance claim points to (a) the specific article/annex it satisfies, and (b) the versioned evidence that supports it. A claim without both is a finding, not a control.

## Why

AI Act Art. 11 (technical documentation), Art. 12 (record-keeping), Art. 17 (QMS), Art. 47 + Annex V (declaration of conformity), and Art. 18 (10-year retention) all presuppose that a third party can walk from claim → article → evidence → signatory in bounded time. Undocumented claims do not compose into a defensible audit.

## Forbidden patterns

- "We comply with Art. 14" as a standalone row.
- Evidence pointers that resolve to a directory ("see the compliance folder") rather than a specific versioned artifact.
- "TBD" as a signatory.
- Claims whose evidence has a retention window shorter than 10 years from market placement.

## Required patterns

- Every workpaper row carries: article citation, current control description, evidence pointer (path + version + date), named owner, named reviewer, retention_until.
- Every Annex IV section paragraph that makes a substantive claim carries a footnote or inline link to the supporting artifact.
- `scripts/traceability_check.py` passes before any sign-off action.

## Enforcement

Agents refuse to mark rows "closed" without passing the traceability check. The `/trace` command runs the check and blocks sign-off on failure.
