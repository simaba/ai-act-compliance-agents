---
kind: safety-trace
system_id: AI-SYS-0003
system_name: VoxOS AEB Vision Component
provider: VoxOS GmbH
classification_memo: examples/classification-aeb-vision-component.md
retention_precedence: '10 years (AI Act Art. 18 dominates ISO 26262 default project archive)'
retention_until: '2036-04-19'
documentation_version: '1.0.0'
status: in_review
prepared_by: safety-lead@voxos.example
last_updated: '2026-04-19'
ai_act_to_fusa:
  - ai_act_article: Art. 9 (risk management)
    fusa_work_product: HARA + ASIL decomposition
    work_product_ref: docs/safety/hara-aeb.md@v3.2
    sotif_work_product: SOTIF triggering-conditions analysis
    sotif_ref: docs/safety/sotif-tca-aeb.md@v2.0
  - ai_act_article: Art. 10 (data governance)
    fusa_work_product: Data validation plan + camera-image dataset bias review
    work_product_ref: docs/safety/data-validation-plan.md@v1.4
    sotif_ref: docs/safety/sotif-tca-aeb.md@v2.0#dataset-coverage
  - ai_act_article: Art. 13 (transparency to deployers)
    fusa_work_product: Item definition + safety manual to OEM
    work_product_ref: docs/safety/item-definition.md@v2.1
  - ai_act_article: Art. 14 (human oversight)
    fusa_work_product: Driver-state monitoring + override behaviour spec
    work_product_ref: docs/safety/driver-override-spec.md@v1.0
  - ai_act_article: Art. 15 (accuracy, robustness, cybersecurity)
    fusa_work_product: Safety case + ISO/SAE 21434 TARA
    work_product_ref: docs/safety/safety-case.md@v4.0
    cyber_ref: docs/security/tara-aeb.md@v1.2
  - ai_act_article: Art. 17 (quality management)
    fusa_work_product: ASPICE + ISO 26262 process audit
    work_product_ref: docs/qms/aspice-audit-2026-Q1.md
  - ai_act_article: Art. 72 (post-market monitoring)
    fusa_work_product: Field-monitoring plan + safety-anomaly review board
    work_product_ref: docs/pmm/field-monitoring-aeb.md@v1.0
fusa_to_ai_act:
  - fusa_work_product: HARA + ASIL decomposition
    ai_act_article: Art. 9
    notes: Hazard analysis discharges Art. 9(2)(a)-(d) for foreseeable misuse and reasonably foreseeable harm.
  - fusa_work_product: SOTIF triggering-conditions analysis
    ai_act_article: Art. 9 + Art. 15
    notes: TCA covers performance limitations under reasonably foreseeable conditions; satisfies robustness obligation when paired with the validation report.
  - fusa_work_product: Item definition + safety manual to OEM
    ai_act_article: Art. 13
    notes: OEM safety manual is the deployer "instructions for use" envelope; cross-referenced in Art. 13 row of conformity workpaper.
  - fusa_work_product: Driver-state monitoring + override behaviour spec
    ai_act_article: Art. 14
    notes: Driver retains override authority and is the named human overseer in the loop.
  - fusa_work_product: Safety case
    ai_act_article: Art. 15 + Art. 11 (technical documentation)
    notes: Safety case is cited in Annex IV §4 (performance metrics) and §5 (risk management).
  - fusa_work_product: ISO/SAE 21434 TARA
    ai_act_article: Art. 15(4) cybersecurity obligation
    notes: TARA discharges the cybersecurity portion of Art. 15(4); separate WP-15-04 entry in conformity workpaper.
  - fusa_work_product: Field-monitoring plan + safety-anomaly review board
    ai_act_article: Art. 72 + Art. 73
    notes: Safety-anomaly review board is the Art. 73 incident-decision authority; SLA 10 days for fatal events under Art. 73(3).
forward_trace: see ai_act_to_fusa
reverse_trace: see fusa_to_ai_act
safety_trace: true
art_14_coverage:
  a: Driver receives in-cabin instructions on system limitations during onboarding.
  b: Driver-state monitoring detects automation bias signs and warns.
  c: HMI annunciates intervention with explicit reason text.
  d: Driver can disable AEB via cabin-control switch with confirmation.
  e: System is overridable by braking, steering, or accelerator override.
named_overseer: driver-of-record (vehicle operator)
reverse_links:
  - examples/classification-aeb-vision-component.md
---

# Safety mapping — VoxOS AEB Vision Component

This artifact bridges AI Act Chapter III obligations with ISO 26262
(FuSa), ISO 21448 (SOTIF), ISO/SAE 21434 (cybersecurity), and the
type-approval framework (EU 2018/858). Required because the system is a
safety component of a regulated product under Annex I (vehicle type
approval), making it both Annex I high-risk under the AI Act and
ASIL-D under ISO 26262.

## 1. Bidirectional trace tables

See `ai_act_to_fusa` and `fusa_to_ai_act` in the frontmatter.
`scripts/traceability_check.py` enforces that every Chapter III article
cited in the classification memo has at least one outgoing FuSa pointer
**and** at least one incoming reverse pointer.

## 2. Retention precedence

ISO 26262 typically calls for project-archive retention until end of
production + 10 years; ISO/SAE 21434 calls for "the lifetime of the
item". The AI Act's Art. 18 fixes a 10-year minimum from placing on
market. **Whichever regime demands the longer retention wins.** For
this system, the AI Act's 10-year floor from placing-on-market is the
operative deadline (`retention_until: 2036-04-19`).

## 3. Hazardous overlaps

Two areas where AI Act and FuSa requirements look similar but are not
substitutes:

- **Art. 14 human oversight** vs. **driver controllability under FuSa**.
  Driver-controllability is a precondition for ASIL allocation; it is
  not, by itself, sufficient for Art. 14(4)(a)-(e). The driver-override
  spec must additionally cover automation-bias mitigation (Art. 14(4)(b))
  and "stop button" semantics (Art. 14(4)(e)) explicitly.
- **Art. 9 risk management** vs. **HARA + SOTIF TCA**. HARA addresses
  systematic-fault hazards; SOTIF addresses performance limitations under
  reasonably foreseeable conditions. Neither covers Art. 9(2)(b)
  *foreseeable misuse* — that requires a separate misuse analysis. This
  is enumerated in `docs/safety/foreseeable-misuse-aeb.md@v1.0`.

## 4. Cross-regulatory incident reporting

A single field event may need to be reported under multiple regimes:

- AI Act Art. 73 to the Market Surveillance Authority.
- EU 2018/858 to the type-approval authority.
- Vehicle-defect reporting under Member-State product-safety law.

The incident runbook in `docs/incident-response/aeb-runbook.md@v1.5`
sequences these in parallel; the Art. 73 SLA (10 days for death,
2 days for widespread harm or critical-infrastructure impact, 15 days
default) governs the AI Act timeline and is typically the tightest.

## 5. Reviewer boundary

This mapping is a structured technical opinion. It is reviewed by the
functional-safety lead, the AI Act conformity owner, and external
type-approval counsel before it can be relied on for product release.
See `rules/common/review-boundary.md`.
