---
id: AI-SYS-0002
system_name: VoxOS Fleet Recruiter
provider: VoxOS GmbH
intended_purpose: >-
  Rank applicants for commercial-vehicle driver openings at fleet operators
  by producing a 0-100 fit score and structured rationale from the
  applicant's resume, telematics history (if present with consent), and the
  hiring-manager's job card; the hiring manager uses the score as an input
  to their own sourcing decision.
deployment_context: >-
  SaaS deployed to EU-headquartered fleet operators (DE, NL, PL, ES, FR)
  running commercial road-freight operations regulated under EU 561/2006
  (driver hours) and EU 2018/858 (vehicle approval).
user_population: >-
  Primary: talent-acquisition specialists and fleet HR managers. Indirectly
  affected: ~42,000 EU-resident commercial-driver applicants per year.
foreseeable_misuse:
  - Operator overrides the structured rationale and uses the score as the
    sole decision input, inverting Art. 14(4)(d) intended use.
  - Operator feeds legacy CV data with tenure-based proxy features that
    correlate with age, violating Art. 10 data-governance obligations.
  - Operator pipes scores into a separate downstream automated-rejection
    tool, creating an unreviewed pipeline that is effectively an automated
    decision under GDPR Art. 22.
  - Operator deploys the scoring in jurisdictions where Annex III #4(a)
    employment-decision characterisation is contested without updating the
    applicability memo.
classification: high-risk
articles_cited:
  - Art. 6
  - Annex III #4
  - Art. 9
  - Art. 10
  - Art. 14
  - Art. 43
  - Art. 72
  - Recital 57
annex_iii_check: >-
  #4(a) — systems intended to be used for the recruitment or selection of
  natural persons, in particular for placing targeted job advertisements, to
  analyse and filter job applications, and to evaluate candidates. Direct
  match.
annex_i_check: >-
  Not applicable. System is not a safety component of a regulated product
  under Annex I Section A or B.
art_5_check: >-
  No prohibited practice implicated. Specifically: no subliminal
  manipulation (5(1)(a)); no exploitation of vulnerability (5(1)(b)); no
  social scoring by public authorities (5(1)(c)); no real-time remote
  biometric identification (5(1)(h)); no predictive individual offending
  (5(1)(d)); no emotion recognition in workplace (5(1)(f)) — scores are
  derived from resume text and consented telematics only, and the system
  does not infer affective state.
classified_by: bagherisima@gmail.com
reviewed_by:
  - legal-counsel@voxos.example
  - dpo@voxos.example
classification_date: '2026-04-19'
review_due: '2027-04-19'
status: in_review
substantial_modification_triggers:
  - Replacement of the fit-scoring foundation model with a different model
    family (change of training data distribution or architecture).
  - Addition of telematics feature classes not declared in the current
    intended-purpose statement.
  - Expansion to a new Member State with different labour-law classifications.
  - Change from advisory scoring to any form of automated decision-making
    under GDPR Art. 22.
documentation_version: '1.0.0'
---

# VoxOS Fleet Recruiter — AI Act risk classification memo

## 1. Intended purpose

VoxOS Fleet Recruiter produces a 0-100 fit score and a structured rationale
for commercial-vehicle driver applicants. The score is one input among many
to a human hiring-manager decision. The system does not send any message to
the applicant, does not auto-reject, and does not operate in a mode where
its output is the sole decision.

## 2. Five-gate walk

### Gate 1 — Art. 5 (prohibited practices)

None triggered. See `art_5_check` in the frontmatter for clause-level
reasoning. Recorded here because the memo is not considered complete
without an explicit refutation.

### Gate 2 — Annex I (safety component of a regulated product)

Not applicable. The system is not a safety component of a product covered
by Annex I Section A (new approach harmonisation legislation) or Section B
(other Union harmonisation legislation). A commercial fleet operator's
HR system is outside EU 2018/858's scope of vehicle type approval even
though its users operate in an EU 2018/858-regulated environment.

### Gate 3 — Annex III (stand-alone high-risk use cases)

**Match**: Annex III #4(a) — systems used to filter job applications and
evaluate candidates.

Art. 6(3) derogation examined: does the system perform a "narrow
procedural task", "improve the result of a previously completed human
activity", "detect decision-making patterns without replacing human
assessment", or "perform a preparatory task to an assessment"?

Rejected. The system materially influences the hiring manager's attention
allocation across applicants and directly assigns a numeric score to each
applicant. This is not a "narrow procedural task". Recital 57 explicitly
notes that "the profiling of natural persons" in employment contexts
remains high-risk. The derogation is therefore not invoked.

### Gate 4 — Art. 50 (transparency)

Not the operative gate — Art. 50 applies to systems interacting with
natural persons, generating synthetic content, or performing emotion
recognition / biometric categorisation. Fleet Recruiter does none of
these. Transparency to the applicant is nonetheless required via GDPR
Art. 13-14 and is separately documented in the DPIA (not this memo).

### Gate 5 — default

Skipped (system already classified high-risk under Gate 3).

## 3. Classification

**High-risk** under Art. 6(2) via Annex III #4(a).

Conformity assessment route under Art. 43(2): internal control (Annex VI)
is available because the system does not fall under any of the Art. 43(1)
exceptions that require third-party assessment (no remote biometric
identification; no critical-infrastructure integration). This will be
confirmed by the conformity-checker in a separate workpaper.

Obligations triggered:
- Art. 8-17 provider obligations (full Chapter III).
- Art. 14 human oversight.
- Art. 17 quality management.
- Art. 18 10-year retention of technical documentation.
- Art. 26 deployer obligations (flowed to fleet-operator customers via
  contract).
- Art. 47 + Annex V Declaration of Conformity.
- Art. 48 CE marking.
- Art. 49 EU database registration.
- Art. 72 post-market monitoring.
- Art. 73 serious-incident reporting.

## 4. What would change this classification

See `substantial_modification_triggers` in the frontmatter. Any of those
triggers a re-classification and a new memo version. This memo is
superseded on the first such trigger; it is otherwise valid for 12 months
under the `review_due` policy.

## 5. Reviewer boundary

This memo is a structured technical opinion. It is not legal advice. It
must be signed off by a named human legal reviewer (`reviewed_by`) before
it can leave draft status. See `rules/common/review-boundary.md`.
