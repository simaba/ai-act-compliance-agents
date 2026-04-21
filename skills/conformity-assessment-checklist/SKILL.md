---
name: conformity-assessment-checklist
description: Plan the Art. 43 conformity assessment for a high-risk AI system — select the route (Annex VI internal control vs Annex VII third-party), enumerate the Chapter III requirements, and produce a requirement-by-requirement workpaper showing current controls, evidence, gaps, and owners. Use this when the user says "conformity check", "gap analysis", "Art. 43 route", "CE marking readiness", "can we self-assess", or "what do we need to ship this under the AI Act". Not for classification (use `eu-ai-act-risk-classification` first) or for drafting the technical file itself (use `technical-documentation-template`).
---

# Conformity Assessment Checklist

## When to use

Use this skill when:

- A system has been classified high-risk (via `eu-ai-act-risk-classification`) and you need a plan to close the gap between current state and Art. 43 + Art. 48 (CE marking) readiness.
- An auditor or notified body is about to engage and you need a workpaper that shows every applicable requirement with evidence pointers.
- A substantial modification (Art. 25) has occurred and you need to re-verify that existing conformity still holds.
- A sponsor asks "what does it cost to ship this compliantly?" and needs a gap-to-owner-to-cost line item view.

Do NOT use this skill for:

- Limited-risk systems (Art. 50 transparency is a much narrower checklist — handle inline in the classification memo).
- General-purpose AI models (Art. 53–55 documentation obligations are a separate template).
- Legal sign-off on the final Declaration of Conformity (Art. 47 + Annex V). This skill prepares the workpaper that underlies the declaration; the declaration itself requires a named authorized signatory.

## Hard rule

**Every Chapter III article that applies gets a row. Every row has: applicability reason, current control, evidence location, gap, owner, due date.** A row with "N/A" is acceptable only if the memo records *why* the article does not apply (e.g., "Art. 10(5) does not apply — no special-category personal data is processed in training"). Unevidenced claims are not controls.

## Route selection (Art. 43)

Decide the conformity assessment route before enumerating requirements; the route determines whether a notified body is in scope.

| Route | When it applies | Who certifies |
|---|---|---|
| **Annex VI — internal control** | Default for Annex III high-risk systems where the provider has applied harmonized standards covering all relevant requirements (Art. 43(1)(a)). | Provider self-attests. Notified body not required unless the system is in Annex III #1 biometrics and no harmonized standards cover all requirements — then Annex VII is mandatory. |
| **Annex VII — third-party assessment** | (i) Annex III #1 biometrics without full harmonized-standards coverage; (ii) all Annex I safety-component systems (route follows the sector conformity legislation, e.g., medical device notified-body route under EU 2017/745). | Notified body assesses QMS and technical documentation; issues EU technical documentation assessment certificate. |

For Annex I systems, the AI Act conformity assessment is integrated into the sector product conformity assessment (Art. 43(3)) — do not run a parallel AI Act track; feed the AI-specific requirements into the sector notified-body engagement.

## Requirement enumeration

For every high-risk system, walk the following Chapter III articles. Mark each applicable/not-applicable with a one-line reason.

| Article | Requirement | Typical evidence |
|---|---|---|
| **Art. 9** | Risk management system across the lifecycle (identification, estimation, evaluation, mitigation of known/foreseeable risks; residual risk acceptability). | Linked `raid-log` with AI-specific risks; mitigation testing records; residual-risk sign-off memo. |
| **Art. 10** | Data governance for training/validation/test sets: relevance, representativeness, examination for biases, appropriate data practices. Art. 10(5) allows processing of special-category personal data strictly to detect and correct bias, with additional safeguards. | Data-sheet per dataset; bias audit report; DPIA if personal data. |
| **Art. 11 + Annex IV** | Technical documentation drawn up before placing on the market, kept up to date. Eight sections specified. | The technical file itself (see `technical-documentation-template`). |
| **Art. 12** | Automatic logging of events over the lifetime, traceability of system behavior. | Telemetry design doc; log schema; retention policy aligned with Art. 19. |
| **Art. 13** | Transparency and provision of information to deployers (user-facing). | Deployer instructions for use; model card; accuracy/robustness/cybersecurity disclosures. |
| **Art. 14** | Human oversight measures designed and built in. Enables the overseer to understand, monitor, intervene, override. | Oversight design doc (see `human-oversight-design-patterns`); training material; override UX spec. |
| **Art. 15** | Accuracy, robustness, cybersecurity — appropriate level, consistent performance throughout lifecycle, resilience to errors/faults/inconsistencies, resilience to adversarial attacks. | Accuracy test report; robustness corpus; red-team/security assessment. |
| **Art. 17** | Quality management system — documented procedures for design, development, quality control, change mgmt, data mgmt, post-market monitoring, incident reporting, communication with authorities. | QMS manual; linked SOPs; ISO/IEC 42001 mapping if pursued. |
| **Art. 43** | Conformity assessment carried out before placing on the market. | This workpaper + sign-off; notified-body certificate if Annex VII. |
| **Art. 47 + Annex V** | EU declaration of conformity drawn up and signed. | Signed DoC on file; 10-year retention (Art. 18). |
| **Art. 48** | CE marking affixed, visibly, legibly, indelibly. | Product-marking artwork; digital equivalent for non-physical products. |
| **Art. 49** | Registration in the EU database before placing on the market. | Database entry ID; provider registration confirmation. |
| **Art. 72** | Post-market monitoring system proportionate to risks. | PMM plan (see `post-market-monitoring-plan`); incident-reporting procedure (Art. 73). |

## Row schema

Each requirement row (validates against `schemas/conformity-assessment-row.json`):

```yaml
- id: CONF-0009
  article: Art. 14
  requirement: Human oversight measures enabling understand-monitor-intervene-override.
  applicability: applicable
  applicability_reason: System is high-risk under Annex III #4 (employment — candidate screening).
  current_control: >-
    Recruiters must confirm each AI-shortlisted candidate before the candidate
    enters the interview pipeline. Confirmation UI shows top-3 contributing
    features and a free-text rationale field.
  evidence:
    - type: design_doc
      ref: docs/oversight/voxos-fleet-recruiter-v1.md
    - type: screen_recording
      ref: evidence/voxos-fleet-recruiter-oversight-2026-03-14.mp4
  gap: >-
    Operator training curriculum not yet signed off; Art. 14(5) requires the
    overseer to be in a position to understand the system's capacities and
    limitations, which implies documented training.
  owner: maya@example.com
  priority: P1
  due: 2026-07-15
  status: open
```

## Workpaper structure

One Markdown file per system, with YAML frontmatter and a table of rows:

```yaml
---
system_id: AI-SYS-0002
system_name: VoxOS Fleet Recruiter Assist
classification_memo: examples/classification/voxos-fleet-recruiter.md
classification_tier: high-risk
route: annex_vi
route_rationale: >-
  Harmonized standards (EN ISO/IEC 42001, EN AI Act harmonized standards
  once published) cover all Chapter III requirements for this system.
  No biometric component triggers Annex VII.
provider: Acme Mobility AB
deployer_instructions_version: 1.2
prepared_by: sima@example.com
reviewed_by: marcus@example.com
status: in_review
last_updated: 2026-04-19
---
```

Followed by the requirement rows, then an open-questions block, then a sign-off block.

## Worked example — VoxOS Fleet Recruiter Assist

High-risk under Annex III #4 (employment — candidate screening). Annex VI route selected because no biometric input and harmonized-standards coverage is available.

Walked 13 Chapter III articles. Outcome: 9 applicable, 3 N/A with documented reason (Art. 10(5) — no special-category data; Art. 43(3) — not an Annex I safety component; Art. 50 — supersede by Chapter III obligations), 1 partial (Art. 15 robustness testing covers nominal drift but not adversarial prompt injection — filed as gap CONF-0011, owner Chen Wei, due 2026-06-01).

Result: 4 P1 gaps, 6 P2 gaps, estimated 11 engineering-weeks to close. Two gaps (CONF-0007 data governance documentation, CONF-0014 post-market monitoring plan) block placing on market; the remaining 8 can be closed in parallel with the early deployer pilot.

## Reviewer checklist

- [ ] Route is justified in one paragraph with citation to Art. 43(1)(a) or 43(1)(b) (and Art. 43(3) for Annex I).
- [ ] Every Chapter III article listed above has a row — either applicable (with evidence or a gap) or N/A with reason.
- [ ] Every row has a named human owner (not "team", not "legal").
- [ ] Every gap has a priority (P0/P1/P2/P3) and a due date.
- [ ] Evidence pointers resolve to actual artifacts — not "forthcoming" without a due date.
- [ ] Open questions for legal are in their own block with a named reviewer assigned.
- [ ] Workpaper is in version control; `last_updated` within the last 30 days.
- [ ] Declaration-of-conformity draft is NOT signed until every P0 and P1 row is closed.

## Common failure modes

- **Copying the article text into `current_control`.** The control is what you *do* in response to the article. "We comply with Art. 14" is not a control; "Recruiter confirms each shortlist with rationale; monthly audit of 10% sample by people-ops lead" is a control.
- **One evidence item per row.** Most rows need at least two: design/spec and operational evidence (log, sample, sign-off).
- **Skipping Art. 10 because you use a vendor model.** Deployer of a GPAI-based high-risk system still owes Art. 10 for fine-tuning data and validation sets; provider up the chain owes the rest.
- **Treating CE marking as the finish line.** Art. 72 post-market monitoring and Art. 73 incident reporting are continuous obligations; the workpaper needs living rows for them, not one-time entries.
- **Running the AI Act route in parallel with an Annex I sector route.** Art. 43(3) integrates them; duplicate tracks waste effort and confuse the notified body.

## Composition

- Upstream: `eu-ai-act-risk-classification` — provides the tier and Annex III area that drive this workpaper.
- Downstream: `technical-documentation-template` — the evidence pointers in this workpaper seed the Annex IV file.
- Downstream: `post-market-monitoring-plan` — Art. 72 row points at the PMM plan.
- Downstream: `human-oversight-design-patterns` — Art. 14 row points at the oversight design doc.
- Lateral: `iso26262-21448-mapping` — for Annex I automotive systems, the AI Act evidence feeds into the functional-safety case; avoid duplicate evidence stores.

## Source

- Regulation (EU) 2024/1689, Art. 9–17, 25, 43, 47–49, 72–73; Annex IV, V, VI, VII.
- Recital 73 (route choice), Recital 153 (post-market monitoring proportionality).
- ISO/IEC 42001:2023 §7 (support) and §8 (operation) — evidence mapping.

*This skill produces a compliance workpaper, not legal advice. A named legal reviewer must sign off on route selection and on the final declaration of conformity.*
