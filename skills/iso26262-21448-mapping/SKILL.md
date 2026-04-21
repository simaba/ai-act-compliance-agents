---
name: iso26262-21448-mapping
description: Map AI Act high-risk requirements to ISO 26262 (functional safety) and ISO 21448 (SOTIF — Safety of the Intended Functionality) artifacts for automotive AI systems, so that evidence is produced once and reused across both regimes. Use this when the user says "safety case", "FuSa", "SOTIF", "26262", "21448", "automotive AI Act", "HARA", "safety argument", or has an Annex I in-vehicle AI system and needs to avoid parallel evidence stacks. Not for the conformity workpaper (use `conformity-assessment-checklist`) or for generic risk classification (use `eu-ai-act-risk-classification`).
---

# ISO 26262 / 21448 Mapping

## When to use

Use this skill when:

- An AI system is a safety component of a vehicle regulated under EU 2018/858 → AI Act high-risk via Annex I → and the vehicle program already runs ISO 26262 + ISO 21448. You need one evidence store, not two.
- A functional-safety assessor and an AI Act auditor are both engaging on the same system; you need a single traceability matrix.
- The AI Act technical file (Annex IV §5 risk management) and the functional-safety case are drifting apart; consolidate.
- A new AI feature is being added to an existing ECU; work out what evidence already exists vs. what is AI-specific.

Do NOT use this skill for:

- Non-automotive Annex I systems (medical device → ISO 14971; machinery → ISO 12100) — different standards, same composition principle but separate skill.
- Non-safety automotive AI (e.g., infotainment voice assistant with no safety-component role) — limited-risk; FuSa and SOTIF do not apply.

## Hard rule

**The safety case is a structured argument, not a binder. Each AI Act requirement claim must point to one or more 26262/21448 work products with the version, date, and signatory, and each work product must in turn point back to at least one AI Act article.** Bidirectional traceability or it is not a mapping.

This skill produces the mapping. It does **not** produce the safety case itself; that is owned by the functional-safety lead and closed under the vehicle program.

## What each regime covers

| Regime | Scope | Core artifact |
|---|---|---|
| **ISO 26262** (Functional Safety) | Hazards arising from **failures** of E/E systems (faults, random hardware failure, systematic software faults). | Item definition → HARA → safety goals → functional/technical safety requirements → ASIL decomposition → safety case. |
| **ISO 21448** (SOTIF) | Hazards arising from **correctly functioning** systems in situations not adequately covered (performance limitations, foreseeable misuse, triggering conditions). Essential complement to 26262 for ML-based perception/control. | Scenario analysis → triggering conditions → known-unsafe + known-safe + unknown categories → acceptance criteria → residual risk argument. |
| **EU AI Act Chapter III** | AI-system-specific risk management (Art. 9), data governance (Art. 10), technical documentation (Art. 11), human oversight (Art. 14), accuracy/robustness/cybersecurity (Art. 15), post-market monitoring (Art. 72). | Technical file (Annex IV), conformity workpaper, PMM plan, oversight design. |

26262 addresses "what if this breaks"; 21448 addresses "what if this works as designed but the world is weirder than training assumed"; the AI Act adds data-governance, human-oversight, transparency, and post-market obligations on top. They complement; they do not replace each other.

## The mapping table

Express the mapping as a two-way index. A row per (AI Act requirement) and a row per (safety work product).

### AI Act → safety evidence

| AI Act | FuSa / SOTIF work product | Notes |
|---|---|---|
| Art. 9 risk management | ISO 26262 Part 3 (HARA + safety goals); ISO 21448 §6 (triggering conditions + scenario catalog) | AI-specific additions: data-distribution risks, adversarial-input risks, drift risks. |
| Art. 10 data governance | ISO 21448 §8 (derivation of acceptance criteria); ML data management plan (often separate) | Data-sheets are AI-Act-specific; SOTIF uses them as inputs to scenario catalog. |
| Art. 11 technical documentation | ISO 26262 Part 2 work products index; safety case (GSN or equivalent) | Cross-reference, do not duplicate. Annex IV §2 can point at 26262 work products. |
| Art. 12 record-keeping / logs | ISO 26262 Part 6 §11 (software unit verification logs); field monitoring logs | Ensure retention is 10 years (AI Act Art. 18) — often longer than 26262 defaults. |
| Art. 14 human oversight | Driver-in-the-loop assumptions from 26262 Part 3 §7.4 "controllability"; SOTIF §7 use-case analysis | Controllability C0–C3 maps to oversight pattern strength: C0 needs strongest oversight. |
| Art. 15 accuracy/robustness/cybersecurity | ISO 21448 §9 (verification and validation); ISO/SAE 21434 (cybersecurity) | Accuracy metrics in Annex IV §4 are the ML-specific face of 21448 acceptance criteria. |
| Art. 17 QMS | ISO 26262 Part 2 §5 (safety management); Automotive SPICE | Map procedures once; don't run two quality systems. |
| Art. 43 conformity assessment | Integrated into EU 2018/858 type approval per Art. 43(3) | Notified-body engagement is unified. |
| Art. 72 post-market monitoring | ISO 26262 Part 7 §6 (production, operation, service, decommissioning); SOTIF §12 (continuous improvement) | Field-monitoring data feeds both. |

### Safety work product → AI Act

| Work product | AI Act anchors |
|---|---|
| Item definition | Annex IV §1 (general description); classification memo (intended purpose). |
| HARA (hazard and risk assessment) | Art. 9 (risk management); Annex IV §5 (risk register). |
| Safety goals | Art. 9; Annex IV §3 (foreseeable unintended outcomes). |
| ASIL decomposition | Art. 9 residual-risk acceptance; Annex IV §5. |
| Safety requirements specification | Art. 15 (robustness); Annex IV §2 (design specifications). |
| Software unit verification / integration test reports | Art. 15; Annex IV §2 (test logs with signatory). |
| SOTIF scenario catalog | Art. 9 (foreseeable misuse); Art. 10 (data representativeness); Annex IV §3. |
| SOTIF acceptance criteria | Art. 15; Annex IV §4 (performance metrics). |
| Field monitoring / FSM plan | Art. 72 (post-market monitoring). |

## Row schema

```yaml
- id: TRACE-0014
  ai_act_requirement: Art. 15 robustness
  fusa_work_product: "ISO 21448 §9 V&V report — LKA perception subsystem v2.3"
  version: 2.3
  date: 2026-03-20
  signatory: hiroshi@example.com
  storage_location: vault://safety-case/LKA/v2.3/
  retention_until: 2036-11-03
  reverse_links:
    - schemas: conformity-workpaper CONF-0015
    - technical_file: "Annex IV §4 (accuracy metrics table)"
  notes: >-
    Perception subsystem is shared across LKA and AEB; the same V&V report
    supports two conformity rows. Incremental changes require delta report,
    not full re-run, per SOTIF §9.3.
```

## Worked example — in-vehicle AEB (automatic emergency braking) with ML perception

AEB is a safety component of the vehicle → Annex I → AI Act high-risk → Art. 43(3) route integrated into EU 2018/858 type approval.

Shared evidence:

- HARA (26262 Part 3) covers brake-actuation failure hazards and feeds Art. 9 risk register.
- SOTIF scenario catalog (21448 §6) covers misclassification of pedestrians, occluded cyclists, low-contrast conditions — these ARE the AI-specific foreseeable-unintended-outcomes entries for Annex IV §3.
- Data-sheets for the perception training corpus (AI-Act-specific) feed SOTIF acceptance-criteria derivation (21448 §8) — produce the data-sheet once, reference from both.
- Human-oversight design: controllability is C0 (driver cannot in general react in time); oversight pattern is safe-fallback (#4) and operator-override indirectly (driver can override braking via accelerator) — mapped to Art. 14(4)(e).
- PMM plan (Art. 72) feeds from the same field-monitoring pipeline as the 26262 Part 7 FSM output; one pipeline, two views.

One mapping table, 42 rows, maintained by the safety lead with an AI-Act reviewer on every change.

## Reviewer checklist

- [ ] Every Art. 9, Art. 10, Art. 14, Art. 15, Art. 17, Art. 72 requirement has at least one row pointing to a FuSa or SOTIF work product.
- [ ] Every safety work product that supports an AI Act claim has a reverse-link to the claim.
- [ ] Retention alignment: AI Act 10 years (Art. 18) takes precedence where standards default to shorter.
- [ ] Signatories are named humans on every row.
- [ ] Controllability (26262 Part 3 §7.4) is referenced in the human-oversight design doc.
- [ ] Data-sheets are shared between Art. 10 (AI Act) and §8 (SOTIF); no duplicate data-governance artifact.
- [ ] Conformity workpaper Art. 43 row references Art. 43(3) integration and names the notified body / type-approval authority.
- [ ] Mapping is version-controlled and re-reviewed on every HARA update or SOTIF scenario-catalog update.

## Common failure modes

- **Two parallel evidence stacks.** One for FuSa, one for the AI Act. Auditors will find the drift; teams will burn out maintaining both.
- **Mapping only the "obvious" articles.** Art. 17 (QMS), Art. 72 (PMM), and Art. 12 (logging) are easy to miss — map them explicitly.
- **Treating SOTIF as optional.** For ML-based perception or control, 26262 alone is insufficient; 21448 is the regime that addresses performance-limitation hazards.
- **Claiming "harmonized standard applied" without naming the standard and version.** AI Act Art. 40 + Annex IV §7 require exact references.
- **Forgetting that Art. 43(3) integrates conformity routes.** Running an independent AI Act track parallel to type approval creates process conflict; Art. 43(3) is the escape.

## Composition

- Upstream: `eu-ai-act-risk-classification` (confirms Annex I + safety-component status).
- Central: `conformity-assessment-checklist` (Annex VII via Art. 43(3) — notified-body engagement).
- Lateral: `technical-documentation-template` (Annex IV §2 and §5 reference FuSa work products).
- Lateral: `human-oversight-design-patterns` (controllability → oversight pattern strength).
- Lateral: `post-market-monitoring-plan` (unified field-monitoring pipeline).

## Source

- Regulation (EU) 2024/1689, Art. 6, 9, 10, 14, 15, 17, 43, 72; Annex I, Annex IV.
- Regulation (EU) 2018/858 (approval and market surveillance of motor vehicles).
- ISO 26262:2018 (Road vehicles — Functional safety), all parts.
- ISO 21448:2022 (Road vehicles — Safety of the intended functionality).
- ISO/SAE 21434:2021 (Road vehicles — Cybersecurity engineering).
- ISO/IEC 42001:2023 (AI management system).

*This skill produces the mapping. The safety case and the AI Act technical file remain owned by their respective leads; this is the bridge between them.*
