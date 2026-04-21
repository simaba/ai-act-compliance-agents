---
name: human-oversight-design-patterns
description: Design the human-oversight controls that satisfy Art. 14 for a high-risk AI system — specify the overseer's role, capabilities, training, UX surfaces, and override mechanisms, then express them as testable design patterns rather than slogans. Use this when the user says "design oversight", "Art. 14", "human in the loop", "human on the loop", "oversight UX", "override flow", or has a high-risk system without a documented oversight design. Not for the conformity workpaper row (use `conformity-assessment-checklist`) or for general UX work.
---

# Human Oversight Design Patterns

## When to use

Use this skill when:

- A high-risk AI system needs an Art. 14 oversight design before placing on market.
- An audit or design review surfaces that "human review" is documented but not specified — what does the human see, what can they do, with what training?
- Post-market monitoring shows oversight is degrading (override rate too low, time-to-review too short to be meaningful) and the design needs revision.
- A new use case is added that changes the oversight load (e.g., 10× volume) — existing pattern may not scale.

Do NOT use this skill for:

- Limited-risk transparency obligations (Art. 50) — those are disclosure, not oversight.
- Generic UX copy. Oversight design is binding under the Act; copy review is downstream.

## Hard rule

**Oversight is a designed capability, not a job title.** Saying "a human reviews this" is not Art. 14 compliance. Art. 14(4) requires the natural person to be enabled to:

(a) properly understand the relevant capacities and limitations of the high-risk AI system and duly monitor its operation, including for purposes of detecting and addressing anomalies, dysfunctions and unexpected performance;
(b) remain aware of the possible tendency of automatically relying or over-relying on the output (automation bias), in particular for high-risk systems used to provide information or recommendations for decisions to be taken by natural persons;
(c) correctly interpret the system's output, taking into account, for example, the interpretation tools and methods available;
(d) decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output;
(e) intervene in the operation of the high-risk AI system or interrupt it through a "stop" button or a similar procedure that allows the system to come to a halt in a safe state.

Each of (a)–(e) must map to a specific designed surface or procedure. Vague claims are not compliance.

## The six patterns

### 1. Gated activation

The system does not act until a human has explicitly enabled it for a session, a case, or a transaction. Used when the cost of unintended action is high. Example: AI-drafted communications are queued, never auto-sent.

Design surface: enable button + scope statement + timeout. The overseer must re-confirm after a defined inactivity window.

Maps to Art. 14(4)(d) — explicit decision not to use.

### 2. Confidence threshold escalation

The system acts autonomously below a confidence threshold and escalates to a human above it (or vice versa, depending on the failure mode). Threshold is calibrated against the cost-of-error curve, not picked arbitrarily.

Design surface: telemetry dashboard showing escalation rate; calibration report justifying threshold; review cadence.

Maps to Art. 14(4)(a) — monitor for anomalies; (4)(c) — interpret the output.

### 3. Assisted review

The system produces a recommendation; the human accepts, edits, or rejects with rationale. The rationale field is required (not optional) and is logged for audit.

Design surface: recommendation card + 3 buttons (accept / edit / reject) + free-text rationale + diff view if edited.

Maps to Art. 14(4)(b) — automation-bias mitigation; (4)(d) — decision to override.

### 4. Safe fallback

If the system encounters a state outside its operational design domain, it falls back to a documented safe behavior — handing off to a human, returning a known-safe default, or refusing the task.

Design surface: ODD definition document; fallback decision tree; logged "fallback invoked" telemetry.

Maps to Art. 14(4)(e) — bring system to halt in safe state.

### 5. Operator override

A named operator can stop, pause, or revert the system in real time. The override is one action away (not buried in settings) and the operator is trained.

Design surface: kill switch (literal button or API); revert procedure; on-call rotation; tabletop exercise schedule.

Maps to Art. 14(4)(e) — stop button.

### 6. Audit trail and replay

Every model decision and every oversight action is logged with sufficient detail to replay the decision and reconstruct what the overseer saw. Retention aligns with Art. 18.

Design surface: log schema; replay tool; immutable storage; access control.

Maps to Art. 14(4)(a) — monitor and detect; ties to Art. 12 (logging) and Art. 19 (retention).

## Pattern selection

Choose the smallest set of patterns that covers all five Art. 14(4) clauses for your system. A single pattern rarely covers all five; most high-risk systems combine 3–4 patterns.

Selection guide:

| Risk shape | Primary patterns |
|---|---|
| High-volume, low-per-item stakes (e.g., recruiter shortlist) | Assisted review (#3) + audit trail (#6); calibrate confidence escalation (#2) for edge cases. |
| Low-volume, high-per-item stakes (e.g., critical-infrastructure dispatch) | Gated activation (#1) + assisted review (#3) + operator override (#5) + audit trail (#6). |
| Continuous, real-time (e.g., in-vehicle assistance) | Safe fallback (#4) + operator override (#5) + audit trail (#6); assisted review (#3) only where session boundaries permit. |
| Batch / async (e.g., benefits eligibility scoring) | Assisted review (#3) + confidence escalation (#2) + audit trail (#6); gated activation (#1) on first-use. |

## Oversight design document structure

```yaml
---
system_id: AI-SYS-0002
system_name: VoxOS Fleet Recruiter Assist
oversight_design_version: 1.0
patterns_applied: [assisted_review, confidence_threshold_escalation, audit_trail_replay]
overseer_role_title: Senior Recruiter
overseer_qualification: 2+ years recruiting experience; 4-hour training course on system capacities and limitations.
training_curriculum_ref: docs/training/voxos-fleet-recruiter-overseer-curriculum.md
override_sla: human review of every shortlist before candidate notification; max 24h queue time.
art_14_clause_coverage:
  a: assisted_review (recommendation card surfaces top-3 contributing features); audit_trail
  b: assisted_review (rationale field required); calibration report shown to overseer
  c: assisted_review (interpretation guide linked from card)
  d: assisted_review (reject button) + confidence_escalation (auto-route low-confidence cases)
  e: operator_override (kill switch in admin console; SLA 5 minutes to halt new shortlists)
designer: maya@example.com
reviewed_by: [marcus@example.com, chen@example.com]
last_updated: 2026-04-19
status: in_review
---
```

Body sections: overseer role and qualification; training curriculum and refresher cadence; per-pattern UX spec with screenshots/wireframes; override mechanism spec (technical + procedural); calibration approach for any thresholds; PMM hooks (override-rate metric, time-to-review metric, rationale-completion metric).

## Worked example — VoxOS Fleet Recruiter Assist

Three patterns chosen: assisted review (#3) as the spine; confidence-threshold escalation (#2) for edge-case auto-routing; audit trail (#6) as the substrate.

Operator override (#5) was considered and ruled out — there is no real-time stream to interrupt; the assisted-review queue effectively provides per-item override.

Overseer role: Senior Recruiter, 4-hour training on capacities and limitations + 1-hour quarterly refresher. Training covers: system intended purpose; known failure modes (e.g., name-based bias risk surfaced in pre-launch testing); how to read the top-3 contributing features; how to write a good rationale.

Override mechanism: every shortlist requires accept/edit/reject before candidates are notified. Edit is the most common action (≈ 38% of cases) — design choice was to make Edit one click, not buried, to reduce friction toward the desired oversight behavior.

Art. 14(4) coverage:
- (a) recommendation card includes top-3 contributing features and links to the model card.
- (b) rationale field is required; UI shows a "you accepted 24 of the last 25 — does this case warrant the same?" prompt at high accept-streaks (automation-bias nudge).
- (c) interpretation guide one click away.
- (d) reject button always available; rejected candidates re-enter the manual pipeline.
- (e) admin kill switch halts new shortlist generation within 5 minutes.

PMM hooks: override-rate target is 25–60% (below 25% suggests rubber-stamping; above 60% suggests the model is under-performing); rationale-completion is 100% (enforced by UI); time-to-review p50 ≥ 90 seconds (below this suggests insufficient consideration).

## Reviewer checklist

- [ ] All five Art. 14(4) clauses (a)–(e) are mapped to a specific pattern + design surface in the frontmatter.
- [ ] Overseer role is named with a qualification standard (not "any team member").
- [ ] Training curriculum exists and is referenced; refresher cadence is set.
- [ ] Override mechanism is one action away from the overseer's main UI.
- [ ] Automation-bias mitigation (Art. 14(4)(b)) is a designed surface, not a slogan.
- [ ] PMM hooks are defined: override rate, time-to-review, rationale-completion (or equivalent for the chosen patterns).
- [ ] Calibration of any thresholds is documented (how you chose them, with what data).
- [ ] The oversight design is referenced from the conformity workpaper Art. 14 row and from Annex IV §2 and §3.

## Common failure modes

- **"Human in the loop" without a designed surface.** Not a control; not auditable.
- **Override that takes more than one click.** Friction in the wrong direction biases toward acceptance.
- **No automation-bias mitigation.** Art. 14(4)(b) is explicit; ignoring it is a finding.
- **Training curriculum that is a slide deck with no assessment.** Art. 14(5) requires the overseer to be in a position to understand — measure that.
- **Override rate of 0% or 100%.** Either the model is so good no one disagrees (suspicious) or so bad the overseer overrides everything (the model shouldn't be live). Calibrate via PMM.

## Composition

- Upstream: `eu-ai-act-risk-classification` (high-risk → Art. 14 applies); `conformity-assessment-checklist` (Art. 14 row points here).
- Downstream: `technical-documentation-template` (Annex IV §2 and §3 reference this design); `post-market-monitoring-plan` (override-rate, time-to-review, rationale-completion metrics live in both).

## Source

- Regulation (EU) 2024/1689, Art. 14 (human oversight), Art. 12 (record-keeping), Art. 13 (transparency), Art. 19 (automatically generated logs).
- Recitals 73, 76 (oversight design intent).
- ISO/IEC 42001:2023 §6.1 (actions to address risks); ISO/IEC 23894:2023 §8.5 (human oversight).

*This skill produces the design that operationalizes Art. 14. Sign-off is by the named designer plus a reviewer who is independent of the design team.*
