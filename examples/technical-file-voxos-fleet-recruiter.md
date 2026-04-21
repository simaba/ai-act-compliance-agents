---
kind: technical-file
annex_iv_section: all
system_id: AI-SYS-0002
system_name: VoxOS Fleet Recruiter
provider: VoxOS GmbH
classification_memo: examples/classification-voxos-fleet-recruiter.md
conformity_workpaper: examples/conformity-workpaper-voxos-fleet-recruiter.yaml
pmm_plan: examples/pmm-plan-voxos-fleet-recruiter.yaml
oversight_design: examples/oversight-voxos-fleet-recruiter.md
technical_file: true
retention_until: '2036-04-19'
documentation_version: '1.0.0'
status: in_review
prepared_by: bagherisima@gmail.com
last_updated: '2026-04-19'
reverse_links:
  - examples/classification-voxos-fleet-recruiter.md
  - examples/conformity-workpaper-voxos-fleet-recruiter.yaml
---

# VoxOS Fleet Recruiter — AI Act Annex IV technical documentation

Retention: **until 2036-04-19** (10-year floor under Art. 18). This file
supersedes any internal retention schedule with a shorter window.

---

## Section 1 — General description of the AI system

**Provider**: VoxOS GmbH (`provider-id: VXS-DE-0001`).
**System name**: Fleet Recruiter.
**Intended purpose**: ranks commercial-vehicle driver applicants and
produces a structured rationale. The score is one input among many to a
human hiring-manager decision. Full intended-purpose statement in
[classification memo](./classification-voxos-fleet-recruiter.md).
**Deployment**: SaaS, EU-resident data plane, customers in DE/NL/PL/ES/FR.
**User population**: ~2,100 hiring managers across ~35 fleet operators;
applicants ~42,000/year.
**Interface**: REST API + embedded UI component within customers' ATS.
**Downstream artifacts**: intended-purpose owns every other section in
this file.

---

## Section 2 — Detailed description of the elements and the development process

### 2.1 Architecture

Ingress → validation layer (schema + OOD sidecar) → feature extractor →
scoring service (foundation model + structured rationale head) →
post-processor → WORM logger → UI/API response.

Architecture diagram and component contracts live in
`docs/architecture/fleet-recruiter-arch.md@v1.3`.

### 2.2 Model

Fine-tuned open-weight foundation model (details in
`docs/model/model-card.md@v2.0`). The scoring head is a linear
calibration layer; the rationale head is prompt-driven with constrained
output grammar.

### 2.3 Data

Data sheet: `docs/data/training-dataset.md@v2.1`.
Includes provenance, consent basis, representativeness analysis per
Member State, bias-examination methodology, and data-minimisation
controls. Open representativeness gap for ES/FR tracked as CONF-0002.

### 2.4 Development process

ISO/IEC 42001-aligned AIMS under `docs/qms/`. Every model change runs
through a four-stage gate: offline eval, shadow deployment,
1% canary, full rollout. Each gate has a named approver
(`ml-lead@voxos.example`, `safety-lead@voxos.example`).

---

## Section 3 — Monitoring, functioning, and control

Pointer: [oversight design](./oversight-voxos-fleet-recruiter.md)
and [PMM plan](./pmm-plan-voxos-fleet-recruiter.yaml).

Every scoring request is logged under the WORM pipeline described in
CONF-0004. Confidence-threshold escalation, assisted review, audit trail
+ replay, and operator override are the four oversight patterns in use.

Kill switches: deployer-level (compliance-reviewer) and provider-level
(safety-lead), both 60-second SLA.

---

## Section 4 — Performance metrics

Baseline performance declared in
`docs/testing/accuracy-report-2026-Q1.md@v1.0`.

Headline metrics:
- Spearman correlation between score percentile and hiring-manager
  final-stage-advance rate: 0.62 at 2026-03-31 (primary accuracy
  metric, tracked in PMM-0001).
- Demographic-parity disparity across four protected-characteristic
  proxies: within 0.05 (tracked in PMM-0004).
- OOD detector true-positive rate on held-out OOD battery: 0.91; false
  positive rate: 0.04.
- End-to-end latency P95: 420ms (tracked in PMM-0010).

Performance is re-measured monthly; methodology is published so deployers
can reproduce.

---

## Section 5 — Risk management system

Pointer: `docs/risk/AI-SYS-0002-risk-register.yaml@v1.3`.

17 residual risks, each mapped to Art. 9(2)(a)-(d), each with a named
mitigation owner and cadence. Quarterly review signed off by head-of-risk
under CONF-0001.

Top three residual risks:
1. R-01 — automation bias leading to score-only decisions (mitigated by
   oversight design §2).
2. R-07 — accuracy drift on telematics feature distribution (mitigated
   by PMM-0001 and PMM-0002).
3. R-12 — foundation-model vendor outage (mitigated by PMM-0009
   safe-fallback).

---

## Section 6 — Lifecycle changes

Substantial-modification triggers enumerated in the classification memo
frontmatter (`substantial_modification_triggers`). Every candidate
trigger is logged in `docs/changes/AI-SYS-0002-change-log.md`.

Change-management workflow: proposed-change → Art. 25 evaluation →
either (a) no substantial modification → update this file → CI validates
schemas; or (b) substantial modification → new classification memo → new
conformity workpaper → new DoC.

---

## Section 7 — Harmonised standards applied

- ISO/IEC 42001:2023 — applied, AIMS documented in `docs/qms/`.
- ISO/IEC 23894:2023 — applied to risk-management structure in
  `docs/risk/`.
- ISO/IEC 27001:2022 — applied to the broader information-security
  management system; certificate in `docs/security/iso27001-2025.pdf`.
- No CEN-CENELEC AI Act harmonised standards formally cited for
  presumption of conformity at time of writing (monitoring for
  publication under Art. 40).

---

## Section 8 — Declaration of Conformity + PMM plan

- DoC template: `docs/conformity/doc-template.md@v1.0`. Final DoC signed
  under CONF-0010 prior to placing on market.
- PMM plan: [pmm-plan-voxos-fleet-recruiter.yaml](./pmm-plan-voxos-fleet-recruiter.yaml),
  11 monitored signals, named owners, Art. 73 mapping.
- Art. 73 incident-response runbook: `docs/incident-response/art-73-runbook.md`.

---

## Reviewer boundary

Technical file is a structured technical artifact prepared under provider
obligations. Legal review signs off the DoC, not this file. This file
requires sign-off from `coo@voxos.example` and `safety-lead@voxos.example`
before it can accompany a DoC placing the system on the market. See
`rules/common/review-boundary.md`.
