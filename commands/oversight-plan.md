---
description: Design the Art. 14 human-oversight controls for a high-risk AI system using the six-pattern catalog.
argument-hint: [system-id or conformity-workpaper-path]
---

# /oversight-plan

Run the `oversight-designer` agent on the supplied system.

## What this does

1. Identifies the risk shape (high-volume low-stakes / low-volume high-stakes / continuous real-time / batch async).
2. Selects the smallest set of patterns from the six (gated activation, confidence-threshold escalation, assisted review, safe fallback, operator override, audit trail and replay) that covers all five Art. 14(4) clauses (a)–(e).
3. Specifies the overseer role, qualification, training curriculum, and refresher cadence.
4. Names the override mechanism — one action away from the overseer's main UI.
5. Defines automation-bias mitigation as a designed surface (not a slogan).
6. Sets PMM hooks (override rate, time-to-review, rationale-completion).
7. Maps each Art. 14(4) clause to a specific pattern + surface in the frontmatter.

## Pre-requisites

- System is classified high-risk.

## Hand-offs

- The Art. 14 row in the conformity workpaper points at the resulting design.
- PMM hooks are added to the PMM plan (override rate, time-to-review, rationale-completion).
- For automotive Annex I systems, controllability C0–C3 from `/safety-map` informs the pattern strength.

## Output

Saved to `examples/oversight/<slug>-oversight-design.md`.

## See also

- Skill: `skills/human-oversight-design-patterns/SKILL.md`
- Agent: `agents/oversight-designer.md`
