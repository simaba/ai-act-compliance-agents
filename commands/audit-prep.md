---
description: Assemble an audit-ready evidence package — what an auditor will ask for, where each item lives, who signed it, when it was last reviewed.
argument-hint: [system-id]
---

# /audit-prep

Generates the audit-prep dossier for a notified body, market-surveillance authority, or internal-audit engagement.

## What this does

1. Produces an index of the AI Act artifacts for the system: classification memo, conformity workpaper, Annex IV file (all versions), oversight design, PMM plan, declaration of conformity, registration record (Art. 49), incident log, and (for Annex I) the safety trace.
2. For each artifact: version, date, named author, named reviewer, storage location, retention_until.
3. For each Chapter III article: the row in the workpaper, the supporting evidence pointers, the gap status (open/closed), and the named owner.
4. Surfaces any open P0/P1 gaps, any expired reviews, any unsigned drafts where an executed version is required.
5. Emits a "questions an auditor will ask" checklist with the specific artifact that answers each.

## When to run

- 30 days before a notified-body engagement (Annex VII route).
- Annually, as an internal-audit rehearsal.
- After any Art. 73 serious-incident report — to confirm the supporting evidence is in order.
- Before a substantial modification (Art. 25) goes to market — to confirm the new evidence is in place.

## Pre-requisites

- All upstream artifacts exist; if any are missing, this command lists them as the first action.
- Run `/trace` first; resolve any failures before assembling the dossier.

## Output

A Markdown index at `examples/audit/<slug>-audit-prep.md` plus a zipped evidence bundle at `reports/audit-<slug>-<date>.zip` containing every referenced artifact at the version stated in the index.

## See also

- Skill: `skills/conformity-assessment-checklist/SKILL.md`
- Command: `/trace`
- Rule: `rules/common/version-the-document.md`
