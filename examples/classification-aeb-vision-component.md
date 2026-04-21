---
id: AI-SYS-0003
system_name: VoxOS AEB Vision Component
provider: VoxOS GmbH
intended_purpose: >-
  Detect and classify forward obstacles (vehicles, pedestrians, cyclists,
  large debris) from a forward-facing camera stream, and emit a
  brake-request signal when collision probability exceeds a calibrated
  threshold; the signal is consumed by the OEM's autonomous-emergency-braking
  ECU which makes the final actuation decision.
deployment_context: >-
  Embedded in commercial-vehicle platforms type-approved under EU 2018/858
  by three OEM partners; field operation across the EU.
user_population: >-
  Drivers of commercial vehicles equipped with the AEB system; indirectly
  every road user in proximity.
foreseeable_misuse:
  - Driver disables AEB via cabin switch and continues to operate in
    conditions outside the system's operational design domain.
  - OEM integrates the brake-request signal without the documented torque-arbitration
    safety layer, causing unintended deceleration under benign conditions.
  - Aftermarket camera replacement with a sensor outside the qualified
    optical-path envelope, breaking calibration assumptions.
  - Operation outside daylight + clear-weather ODD without driver awareness
    that performance degrades and false-negative rate rises.
classification: high-risk
articles_cited:
  - Art. 6
  - Annex I Section A
  - Art. 9
  - Art. 10
  - Art. 14
  - Art. 15
  - Art. 43
  - Art. 72
  - Art. 73
  - Recital 49
annex_iii_check: Not the operative gate; system is high-risk via Annex I.
annex_i_check: >-
  Annex I Section A — Regulation (EU) 2018/858 (motor-vehicle type
  approval). The AEB Vision Component is a safety component of a
  vehicle type-approved under this regulation.
art_5_check: >-
  No prohibited practice. No subliminal manipulation, exploitation,
  social scoring, biometric identification, or predictive offending.
classified_by: safety-lead@voxos.example
reviewed_by:
  - legal-counsel@voxos.example
  - functional-safety-lead@voxos.example
  - external-type-approval-counsel@voxos.example
classification_date: '2026-04-19'
review_due: '2027-04-19'
status: in_review
substantial_modification_triggers:
  - Replacement of the perception backbone with a different model family.
  - ODD expansion (e.g., night operation, adverse weather).
  - Change in brake-request signal envelope or threshold calibration that
    affects controllability.
  - Integration with a new OEM platform requiring re-validation.
documentation_version: '1.0.0'
---

# VoxOS AEB Vision Component — AI Act risk classification memo

## 1. Intended purpose

Forward-perception component for an automatic emergency braking system.
Outputs a brake-request signal consumed by the OEM ECU, which performs
arbitration with other safety functions before commanding actuation.
Driver retains override authority via brake, steering, or accelerator.

## 2. Five-gate walk

### Gate 1 — Art. 5

No prohibited practice. See `art_5_check` in the frontmatter.

### Gate 2 — Annex I

**Match**: the AEB Vision Component is a safety component of a vehicle
type-approved under Regulation (EU) 2018/858 (motor-vehicle type
approval), which appears in Annex I Section A. The system is therefore
high-risk under Art. 6(1).

### Gate 3 — Annex III

Not the operative gate; analysis stops at Gate 2 once Annex I is
satisfied.

### Gate 4 — Art. 50

Not applicable.

### Gate 5 — default

Not applicable.

## 3. Classification

**High-risk** under Art. 6(1) via Annex I Section A.

Conformity-assessment route is determined by the underlying type-approval
regime and Art. 43(3) integration: when third-party assessment is
already required by Annex I sectoral legislation, the AI Act's
conformity-assessment is integrated into that existing assessment.
For EU 2018/858, this means coordinating with the type-approval authority
and the technical service. Confirmation is captured in CONF-0009 of the
conformity workpaper.

Obligations triggered:
- Full Chapter III (Art. 8-17).
- Art. 25 substantial modifications.
- Art. 43(3) integrated conformity assessment with type-approval regime.
- Art. 47 + Annex V Declaration of Conformity (in addition to type
  approval).
- Art. 72 post-market monitoring + Art. 73 serious-incident reporting.
- Parallel obligations under ISO 26262 (FuSa), ISO 21448 (SOTIF), and
  ISO/SAE 21434 (cybersecurity), bridged in
  [examples/safety-trace-aeb-annex-i.md](./safety-trace-aeb-annex-i.md).

## 4. Reviewer boundary

This memo is a structured technical opinion. Final sign-off requires
legal counsel, functional-safety lead, and external type-approval counsel.
See `rules/common/review-boundary.md`.
