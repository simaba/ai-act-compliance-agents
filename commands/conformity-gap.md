---
description: Build the Art. 43 conformity-assessment workpaper for a high-risk AI system, with route selection and gap analysis.
argument-hint: [classification-memo-path]
---

# /conformity-gap

Run the `conformity-checker` agent against the supplied classification memo.

## What this does

1. Selects the conformity route (Annex VI internal control / Annex VII third-party / Art. 43(3) integrated with Annex I sector route) with article citation.
2. Walks Chapter III article by article, producing a row per applicable requirement (and an N/A row with reason for each that does not apply).
3. Each row carries: applicability reason, current control, evidence pointer, gap, named owner, priority (P0/P1/P2/P3), due date, status.
4. Surfaces a gap summary: count by priority, blocking-vs-parallelizable split.
5. Validates the workpaper against `schemas/conformity-assessment-row.json`.

## Pre-requisites

- Classification memo exists and is high-risk. If not high-risk, the command will hand back with the appropriate next step.

## Hand-offs

- Art. 14 row → `/oversight-plan`.
- Art. 72 row → `/pmm-plan`.
- Annex I automotive → `/safety-map` to consolidate FuSa evidence.
- Final declaration of conformity (Art. 47 + Annex V) → only after every P0 and P1 row is closed; signed by the named authorized representative.

## Output

Saved to `examples/conformity/<slug>-workpaper.md`. The gap summary should drive the engineering and legal sequencing.

## See also

- Skill: `skills/conformity-assessment-checklist/SKILL.md`
- Agent: `agents/conformity-checker.md`
- Schema: `schemas/conformity-assessment-row.json`
