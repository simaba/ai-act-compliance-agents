---
kind: oversight-design
system_id: AI-SYS-0002
system_name: VoxOS Fleet Recruiter
classification_memo: examples/classification-voxos-fleet-recruiter.md
named_overseer: hiring-manager-role@deployer.example
escalation_chain:
  - hiring-manager-role@deployer.example
  - compliance-reviewer@deployer.example
  - safety-lead@voxos.example
patterns_used:
  - confidence_threshold_escalation
  - assisted_review
  - audit_trail_replay
  - operator_override
art_14_coverage:
  a: >-
    Overseers can fully understand the capacities and limitations of the system.
    Every deployed hiring manager completes the mandatory 45-minute training
    course covering intended purpose, known failure modes, the four documented
    foreseeable-misuse patterns, and the score interpretation guide. Completion
    is attested in docs/training/hiring-manager-oversight-2026-Q2.md.
  b: >-
    Overseers remain aware of the possible tendency to over-rely on the output
    (automation bias). The UI surfaces every score with the structured rationale,
    confidence band, and a standing "disagree & proceed" button that records the
    reason. The weekly deployer-health dashboard flags any hiring manager with
    a score-only-session rate above 20% for targeted coaching.
  c: >-
    Overseers can correctly interpret the output. The rationale surfaces the
    five top contributing features, a plain-language summary, and the score's
    percentile relative to the current requisition. Score bands are labelled
    "strong fit / fit / borderline / low-fit / insufficient-data" rather than
    raw 0-100 values in the primary UI.
  d: >-
    Overseers can decide not to use the system or otherwise disregard, override
    or reverse the output. Every requisition has an explicit "proceed without
    scoring" option; any shortlist can be assembled without invoking the
    scoring pipeline; every scored applicant can be moved forward or rejected
    independent of the score.
  e: >-
    Overseers can intervene in the operation of the system or interrupt it
    through a "stop button". A deployer-level kill switch is available to the
    deployer's compliance-reviewer; a provider-level kill switch is held by
    VoxOS safety-lead. Both route through the same feature-flag system and
    take effect within 60 seconds of being flipped.
last_updated: '2026-04-19'
documentation_version: '1.0.0'
status: in_review
reverse_links:
  - examples/classification-voxos-fleet-recruiter.md
  - examples/conformity-workpaper-voxos-fleet-recruiter.yaml
---

# Human-oversight design — VoxOS Fleet Recruiter

## 1. Oversight objective

The hiring manager remains the decision-maker. Fleet Recruiter produces
a structured input; the hiring manager's final decision on every
applicant is recorded before the scoring record is considered closed.

## 2. Oversight patterns in use

- **Confidence-threshold escalation** — scores with low-confidence
  rationale or OOD-flagged inputs are surfaced with a yellow "needs
  closer review" badge. A hiring manager cannot advance an applicant
  past screening-stage on a yellow-badged score without explicitly
  confirming "I have reviewed and accept the uncertainty".
- **Assisted review** — the UI never surfaces a raw score alone;
  every score is accompanied by the top five contributing features, a
  plain-language rationale, and the confidence band.
- **Audit trail + replay** — every scoring call is logged with the
  input hash, model version, score, rationale, and the hiring-manager
  action that followed. Logs are WORM-retained for 10 years under
  Art. 18.
- **Operator override** — every score is overridable; every override
  records a free-text reason.

## 3. Trigger matrix

| Signal | Oversight response | Art. 14(4) clause |
| --- | --- | --- |
| OOD-flagged input | Yellow badge; mandatory confirmation before advance | (a), (b), (c) |
| Score band "borderline" or below | Mandatory rationale review; "disagree & proceed" requires a reason | (c), (d) |
| Protected-characteristic disparity alert (PMM-0004 warn) | Deployer-level soft freeze on new scoring until reviewer re-certifies | (e) |
| PMM-0006 cybersecurity warn | Provider-level kill switch available to safety-lead | (e) |
| PMM-0005 score-only-session > 25% | Triggered coaching; targeted training refresh | (a), (b) |

## 4. Training and qualification

- Every hiring manager with Fleet Recruiter access completes the 45-minute
  training before their first scoring session.
- Annual refresher training is mandatory; completion is tracked per
  individual.
- Compliance-reviewers at each deployer complete an additional 60-minute
  "oversight-of-oversight" module covering Art. 26 deployer obligations
  and when to invoke the kill switch.

## 5. Effectiveness evaluation

- PMM-0005 measures score-only-session rate as a proxy for automation-bias
  drift.
- Quarterly oversight-effectiveness review by safety-lead: sample of 25
  override reasons read manually, sampled equally across the four
  protected-characteristic proxies.
- Any quarter with more than one oversight-pattern failure (e.g., kill
  switch lag > 60s, training-record gap, rationale-missing event) is
  reported in the PMM plan and added to the risk register.

## 6. What this design forbids

- It forbids silent automatic rejection based on score.
- It forbids routing scored applicants to any downstream automated
  pipeline that removes the hiring-manager decision.
- It forbids displaying the raw 0-100 score as the primary UI element.
- It forbids suppressing the rationale or the confidence band in any
  customer-requested skin or integration.

## 7. Reviewer boundary

This design is a structured technical opinion. Final sign-off by legal
counsel and DPO before launch. See `rules/common/review-boundary.md`.
