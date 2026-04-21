---
description: For automotive Annex I safety-component AI systems, map AI Act requirements to ISO 26262 / ISO 21448 work products bidirectionally.
argument-hint: [system-id or fusa-work-product-index-path]
---

# /safety-map

Run the `safety-mapper` agent on the supplied automotive AI system.

## What this does

1. Confirms the system is Annex I + safety-component; otherwise hands back (wrong skill).
2. Loads the FuSa work-product index (HARA, safety goals, safety requirements, V&V reports) and the SOTIF scenario catalog.
3. Produces a bidirectional trace table:
   - AI Act requirement → FuSa/SOTIF work product (with version, date, signatory, storage location, retention_until).
   - Safety work product → AI Act anchors.
4. Flags gaps (AI Act requirement without supporting work product, or vice versa).
5. Surfaces retention / signatory / version-drift mismatches.
6. Recommends a re-review cadence (typically on every HARA or SOTIF scenario-catalog update).

## Pre-requisites

- System is high-risk via Annex I (vehicle + safety component).
- Vehicle program already runs ISO 26262 and ISO 21448.

## Hand-offs

- Conformity workpaper rows (Art. 9, 10, 11, 14, 15, 17, 72) reference the trace rather than creating parallel evidence.
- Art. 43(3) integrates the AI Act conformity into EU 2018/858 type approval — trace proves unified evidence.
- Retention mismatches flagged here must be resolved before declaration of conformity.

## Output

Saved to `examples/trace/<slug>-trace.md`.

## See also

- Skill: `skills/iso26262-21448-mapping/SKILL.md`
- Agent: `agents/safety-mapper.md`
