---
name: technical-documentation-template
description: Draft or update the Annex IV technical documentation for a high-risk AI system — the eight-section file that the AI Act requires before placing on the market and that must be retained for 10 years (Art. 18). Use this when the user says "tech file", "Annex IV", "technical documentation", "draft the AI Act file", "model card for AI Act", or has a system that needs to ship and the documentation does not yet exist. Not for classification (use `eu-ai-act-risk-classification`) or conformity-route selection (use `conformity-assessment-checklist`).
---

# Technical Documentation Template

## When to use

Use this skill when:

- A high-risk AI system is approaching market placement and the Annex IV file does not yet exist or is incomplete.
- A substantial modification (Art. 25) has occurred — Art. 11(2) requires the file to be kept up to date.
- A notified body (Annex VII route) or market-surveillance authority requests the technical documentation.
- A new GPAI model has been integrated as a sub-component and the system file needs an addendum.

Do NOT use this skill for:

- Limited-risk systems (Art. 50) — disclosures live in the deployer instructions and product UX, not a technical file.
- Provider-only model documentation for a GPAI model (Art. 53 + Annex XI/XII is a separate template).

## Hard rule

**Annex IV is a regulatory artifact, not marketing copy. Every claim is either evidenced (with a versioned reference) or flagged "not-yet-evidenced" with an owner and due date.** No present-tense aspirational language. No unsourced metrics. No "we believe" — replace with "measured on dataset X version Y, see report Z".

The file must be retained for **10 years from market placement** (Art. 18). Plan the storage and provenance accordingly; this is a durable artifact.

## The eight Annex IV sections

These are mandated by Annex IV and must each be present.

### Section 1 — General description of the AI system

- Intended purpose (verbatim from the classification memo).
- Provider name and contact details.
- Version and date of the documentation.
- Hardware on which the AI system is intended to run.
- Description of how the AI system is integrated with other systems / hardware where applicable.
- Photographs/illustrations showing external features, marking, internal layout (where relevant).
- Basic description of the user interface provided to the deployer.
- Instructions for use for the deployer and basic description of any user interface for the affected person.

### Section 2 — Detailed description of elements of the AI system and the process for its development

- Methods and steps performed for the development, including resort to pre-trained systems / tools provided by third parties.
- Design specifications: general logic of the AI system and of the algorithms; key design choices including rationale and assumptions made (including with regard to persons or groups on which the system is intended to be used); main classification choices; what the system is designed to optimize for; relevance of the different parameters.
- Description of the system architecture: how software components build on / feed into each other and integrate into the overall processing; computational resources used to develop, train, test and validate.
- Where applicable, data requirements in terms of datasheets describing training methodologies and techniques and the training datasets used (origin, scope, characteristics, how data was obtained and selected, labelling procedures, data cleaning).
- Assessment of the human oversight measures (Art. 14) including technical measures put in place to facilitate interpretation of outputs by deployers.
- Where applicable, predetermined changes to the system and its performance, with all the relevant information related to the technical solutions adopted to ensure continuous compliance.
- Validation and testing procedures used, including information about the validation/testing data and their main characteristics; metrics used to measure accuracy, robustness and compliance with other relevant requirements; potentially discriminatory impacts; test logs and reports dated and signed by the responsible persons.
- Cybersecurity measures put in place.

### Section 3 — Detailed information about the monitoring, functioning and control of the AI system

- Capabilities and limitations in performance, including degrees of accuracy for specific persons or groups and overall expected level of accuracy in relation to intended purpose.
- Foreseeable unintended outcomes and sources of risks to health and safety, fundamental rights and discrimination in view of the intended purpose.
- The human oversight measures (Art. 14) and technical measures to facilitate interpretation by deployers.
- Specifications on input data, as appropriate.

### Section 4 — Description of the appropriateness of the performance metrics for the specific AI system

- Why the chosen metrics (accuracy, F1, calibration, latency, robustness scores) are appropriate for the intended purpose and the affected population.
- Method for computing each metric, including dataset definitions and statistical confidence.

### Section 5 — Detailed description of the risk management system in accordance with Art. 9

- The risk-management procedures, the risks identified, the risks accepted, the residual-risk justification, and the testing of mitigations.
- Cross-reference the linked RAID log or risk register.

### Section 6 — Description of relevant changes made by the provider to the system through its lifecycle

- Change log entries: date, change description, impact on intended purpose, impact on Chapter III conformity, re-test results, sign-off.

### Section 7 — List of harmonized standards applied (in full or in part)

- Reference to each standard by number and version (e.g., EN ISO/IEC 42001:2023). Where harmonized standards have not been applied, a description of the solutions adopted to meet the requirements.

### Section 8 — Copy of the EU declaration of conformity (Art. 47, Annex V)

- Full text of the signed declaration. Updates require re-issuance.

## File frontmatter

```yaml
---
system_id: AI-SYS-0002
system_name: VoxOS Fleet Recruiter Assist
provider: Acme Mobility AB
provider_address: Vasagatan 1, 111 20 Stockholm, Sweden
documentation_version: 1.0
documentation_date: 2026-04-19
classification_tier: high-risk
classification_memo: examples/classification/voxos-fleet-recruiter.md
conformity_workpaper: examples/conformity/voxos-fleet-recruiter-workpaper.md
authorized_representative: marcus@example.com
retention_until: 2036-04-19
storage_location: vault://compliance/ai-act/voxos-fleet-recruiter/
prepared_by: sima@example.com
reviewed_by:
  - chen@example.com
  - marcus@example.com
status: in_review
---
```

`retention_until` must be ≥ 10 years from market placement. `storage_location` must reference a system that supports immutable retention and access logging.

## Reviewer checklist

Walk this section by section. A reviewer should be able to find each item without searching.

- [ ] **§1**: Intended purpose is verbatim from the classification memo. Provider contact, version, date, hardware all present.
- [ ] **§1**: Deployer instructions for use are referenced (not embedded; they are a separate versioned artifact).
- [ ] **§2**: Every pre-trained component (foundation model, third-party library) named with version. Vendor model cards linked.
- [ ] **§2**: Datasheet exists per training/validation/test dataset, with origin, scope, labelling procedure, cleaning steps. Special-category data (Art. 10(5)) has separate justification.
- [ ] **§2**: Test logs are dated and have a named signatory.
- [ ] **§2**: Cybersecurity measures cover at minimum: access control, dependency provenance, model-tampering protection, input-validation against adversarial inputs.
- [ ] **§3**: Performance metrics are broken down by relevant subgroups (Art. 10(2)(g)/(h) — bias surfacing).
- [ ] **§3**: Foreseeable unintended outcomes list has ≥ 5 entries with severity tagging.
- [ ] **§4**: Each metric has a defensible "why this metric" paragraph, not just a number.
- [ ] **§5**: Linked risk register has ≥ one row per identified risk; residual-risk acceptance is signed by a named risk owner.
- [ ] **§6**: Change log opens at version 0.1 with the initial design choice, not at version 1.0.
- [ ] **§7**: Standards list includes version. Where a harmonized standard is not applied, alternative solution paragraph is present.
- [ ] **§8**: Declaration of conformity is the signed version, not the draft. Re-issued on every substantial modification.
- [ ] Frontmatter `retention_until` is ≥ 10 years out and storage location supports immutable retention.

## Common failure modes

- **Treating §1 as a marketing summary.** It is the binding statement of intended purpose and integration boundary. Drift here invalidates the entire file.
- **Pointing §2 at "the codebase".** Auditors need a description of the design choices, not a repo URL. Architecture diagrams, training-pipeline diagrams, data-flow diagrams should be embedded or linked at a stable path.
- **Skipping subgroup metrics in §3.** Aggregate accuracy can hide a 15-point gap on a protected subgroup. Art. 10 + Art. 13 require subgroup-level disclosure where relevant.
- **Letting §6 lag.** Every release that touches model weights, training data, or intended-purpose phrasing needs a §6 entry within 30 days. A six-month gap in §6 is a material finding in any audit.
- **Filing the unsigned DoC in §8.** §8 is the executed declaration. The draft lives in the conformity workpaper.

## Composition

- Inputs: `eu-ai-act-risk-classification` memo (→ §1, §3), `conformity-assessment-checklist` workpaper (→ evidence pointers across §2, §5), `human-oversight-design-patterns` (→ §2 and §3 oversight description), `post-market-monitoring-plan` (→ §3 monitoring section), `iso26262-21448-mapping` (→ §5 risk register, where applicable).
- Output: the Annex IV file itself, retained 10 years, regenerated on substantial modification.

## Source

- Regulation (EU) 2024/1689, Art. 11 (technical documentation), Art. 18 (retention), Art. 25 (substantial modification), Art. 47 + Annex V (declaration of conformity); Annex IV (full structure).
- Recital 71 (technical documentation purpose).
- ISO/IEC 42001:2023 §7.5 (documented information), §8.3 (operational planning and control).

*This skill produces a regulatory artifact. Treat the file as immutable once executed; updates are new versions, not in-place edits, and §6 captures the change.*
