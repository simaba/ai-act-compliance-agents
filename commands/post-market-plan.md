---
description: Draft the Art. 72 post-market monitoring plan for a high-risk AI system, with thresholds, escalation, and Art. 73 incident-trigger mapping.
argument-hint: [system-id or conformity-workpaper-path]
---

# /post-market-plan

Run the `post-market-monitor` agent on the supplied system.

## What this does

1. Loads the classification memo, conformity workpaper, and oversight design.
2. Drafts rows for every PMM category — accuracy drift (incl. subgroup), robustness/OOD, safety/harm, human-oversight usage, cybersecurity, data quality, operational, deployer feedback, third-party dependency.
3. For each row: baseline, warn threshold, critical threshold, cadence, owner, escalation text, Art. 73 trigger mapping.
4. Defines collection infrastructure (with retention ≥ 10 years for incident-relevant logs), review cadence (weekly auto / monthly human / quarterly cross-functional), and the deployer feedback channel with SLA.
5. Names PMM owner and incident-reporting owner separately.

## Pre-requisites

- System is classified high-risk.
- Conformity workpaper has an Art. 72 row pointing at this plan.

## Hand-offs

- Annex IV §3 of the technical file references this plan.
- Override-rate / time-to-review / rationale-completion metrics also live in the oversight design — keep both in sync.
- For automotive Annex I systems, the field-monitoring pipeline is unified with FuSa Part 7 — `/safety-map` documents the bridge.

## Output

Saved to `examples/pmm/<slug>-pmm-plan.md`. Validates against the PMM-incident schema.

## See also

- Skill: `skills/post-market-monitoring-plan/SKILL.md`
- Agent: `agents/post-market-monitor.md`
- Schema: `schemas/pmm-incident.json`
