---
description: Run the traceability checker — cross-reference every AI Act requirement claim to its supporting evidence and surface unevidenced claims.
argument-hint: [system-id or workpaper-path]
---

# /trace

Runs `scripts/traceability_check.py` across the system's classification memo, conformity workpaper, technical file, oversight design, PMM plan, and (if Annex I) safety trace.

## What this does

1. Walks every row of the conformity workpaper and confirms each `evidence` pointer resolves to a versioned, named-signatory artifact.
2. Walks every Annex IV section and confirms every claim links back to at least one Chapter III article and to at least one piece of evidence.
3. Confirms every Art. 14(4) clause (a)–(e) is covered by a pattern in the oversight design.
4. Confirms every PMM row has a threshold, cadence, owner, and Art. 73 trigger mapping.
5. For Annex I systems, confirms the FuSa/SOTIF bridge is bidirectional and retention is ≥ 10 years.
6. Emits an exit code: 0 if clean, non-zero if any unevidenced claim, orphan evidence, or retention mismatch is found.

## When to run

- Before every conformity-workpaper sign-off.
- Before every Annex IV version bump.
- Nightly in CI, against the examples directory, to catch drift.
- Pre-audit, as a rehearsal for the evidence walk.

## Output

Machine-readable JSON report to stdout + human-readable summary to stderr. Report is saved to `reports/trace-<slug>-<date>.json` by convention.

## See also

- Script: `scripts/traceability_check.py`
- Rule: `rules/common/traceability.md`
- Rule: `rules/common/evidence-not-opinion.md`
