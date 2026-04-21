---
description: Draft or update the Annex IV technical documentation file (eight mandated sections, 10-year retention).
argument-hint: [system-id or conformity-workpaper-path]
---

# /tech-doc

Drafts the Annex IV file using `skills/technical-documentation-template/SKILL.md`.

## What this does

1. Loads the classification memo, conformity workpaper, oversight design, PMM plan, and — for Annex I — the safety trace.
2. Produces the eight mandated Annex IV sections:
   - §1 General description of the AI system
   - §2 Detailed description of elements and development process
   - §3 Monitoring, functioning and control information
   - §4 Appropriateness of performance metrics
   - §5 Risk management system (Art. 9)
   - §6 Relevant changes made through the lifecycle
   - §7 List of harmonized standards applied
   - §8 Copy of the EU declaration of conformity
3. Sets `retention_until` to 10 years from planned market placement and names the storage location with immutable-retention support.
4. Validates that every claim has a versioned evidence pointer or a named owner + due date.

## Pre-requisites

- Classification memo exists.
- Conformity workpaper in place (evidence pointers across §2, §5, §7 draw from it).

## Hand-offs

- §6 change-log entries update on every substantial modification (Art. 25).
- §8 holds the signed DoC — do not file the draft; the draft lives in the conformity workpaper.
- The file is the artifact most likely to be requested by a notified body or market-surveillance authority.

## Output

Saved to `examples/tech-file/<slug>-annex-iv.md`. Treat as immutable once executed; updates are new versions captured in §6.

## See also

- Skill: `skills/technical-documentation-template/SKILL.md`
