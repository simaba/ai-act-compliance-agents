# Methodology

*How this plugin turns Regulation (EU) 2024/1689 into a reviewable technical
file — and what it deliberately does not do.*

---

## 1. Operating premise

The EU AI Act does not grade effort. It grades **artifacts**: the
classification memo (Art. 6), the conformity-assessment workpaper (Art. 43),
the technical file (Annex IV), the post-market monitoring plan (Art. 72), the
serious-incident report (Art. 73), and the Declaration of Conformity
(Art. 47 + Annex V). If these are vague, inconsistent, or missing named
human owners, no amount of internal diligence will substitute.

This plugin is an **opinion-first, schema-backed drafting harness**. Every
artifact it produces is:

1. **Opinionated**. The risk-classifier defaults to the higher tier under
   ambiguity. The conformity-checker refuses to mark a requirement
   `applicable` without evidence. The post-market-monitor refuses to accept
   "investigate" as an escalation response. See `rules/common/` for the
   full list.
2. **Schema-validated**. Frontmatter on every memo, every row in every
   workpaper, every PMM line, must validate against a JSON Schema Draft
   2020-12 document under `schemas/`. The helpers in `scripts/` enforce this
   in CI.
3. **Traceable in both directions**. Every claim points to evidence.
   Every piece of evidence points back to the claim it supports. The
   `trace` command and `scripts/traceability_check.py` audit this.
4. **Bounded by review**. Nothing here is legal advice. Classifications
   are structured technical opinions that require sign-off from a named
   human legal reviewer before they leave the repo. See
   `rules/common/review-boundary.md`.

## 2. The five artifacts that matter

```
+---------------------------+      +------------------------------+
|  Classification memo      | -->  |  Conformity workpaper         |
|  (Art. 6 + Annex III)     |      |  (Art. 43 + Chapter III)      |
+---------------------------+      +------------------------------+
             |                                    |
             v                                    v
+---------------------------+      +------------------------------+
|  Oversight design         |      |  Technical file (Annex IV)   |
|  (Art. 14(4)(a)-(e))      |      |  8 sections, 10-year        |
+---------------------------+      |  retention                   |
             |                      +------------------------------+
             v                                    |
+---------------------------+                     v
|  PMM plan (Art. 72)       | -->  +------------------------------+
|  + Art. 73 incident       |      |  Declaration of Conformity   |
|  response                 |      |  (Art. 47 + Annex V)         |
+---------------------------+      +------------------------------+
```

Each arrow corresponds to a traceability obligation that the plugin
enforces mechanically. A gap in one box becomes a concrete finding in the
next. That is intentional — the Act does not let you reason about any of
these in isolation.

## 3. Five-gate risk classification

The `risk-classifier` agent walks five gates in order. The first gate that
matches determines the tier.

| Gate | Article | Decision |
| --- | --- | --- |
| 1 | Art. 5(1) | If any practice in (a)-(h) is implicated, classify **prohibited**. Stop. |
| 2 | Annex I (safety component) | If the system is a safety component of a product listed in Annex I Section A or B, classify **high-risk**. |
| 3 | Annex III | If the system falls into one of the eight Annex III categories, classify **high-risk** — unless the Art. 6(3) derogation applies and the rationale is written. |
| 4 | Art. 50 | If the system interacts with natural persons, generates synthetic content, or performs emotion recognition / biometric categorisation, classify **limited-risk** with transparency obligations. |
| 5 | Default | Otherwise, **minimal-risk**. Document the reasoning anyway. |

A classification that skips gates is not a classification. The memo
frontmatter (`schemas/ai-system-classification.json`) enforces that all
five gate checks are recorded even when the answer is "no".

## 4. Conformity workpaper discipline

For every high-risk system, the `conformity-checker` produces a row per
Chapter III article (Art. 8-17), Art. 25 (substantial modifications),
Art. 43 route, Art. 47 + Annex V (DoC), Art. 48 (CE), Art. 49
(registration), and Art. 72 (PMM plan). Each row carries:

- `applicability`: `applicable` | `partial` | `not_applicable`.
- `applicability_reason`: why — in one sentence anchored to the
  intended-purpose statement, not to generic language.
- `current_control`: what the team actually does. Absent = fail.
- `evidence`: at least one pointer with `type` and `ref`.
  "We have a document" is not evidence. "design_doc:/docs/arch.md@v1.3"
  is evidence.
- `gap` + `due` + `owner`: mandatory when status is `open`.
- `priority`: P0/P1/P2/P3 with explicit placing-on-market exposure.

The row schema uses conditional `allOf`: an `applicable` row without
evidence fails validation. A `partial` row without a gap fails. An `open`
status without a due date fails. CI will not let a thin row through.

## 5. Annex IV as a contract

Annex IV mandates eight sections. The plugin's technical-documentation
skill treats them as a contract — not a suggestion:

1. General description of the AI system.
2. Detailed description of the elements of the AI system and the
   process for its development.
3. Information about the monitoring, functioning, and control of the AI
   system.
4. Performance metrics appropriate to the specific AI system.
5. Risk-management system under Art. 9.
6. Description of relevant changes made through the lifecycle of the AI
   system.
7. List of harmonised standards applied (or rationale if none).
8. Copy of the EU Declaration of Conformity and the Art. 72 post-market
   monitoring plan.

Every section in the technical file must either cite a downstream artifact
(data sheet, test report, oversight design) or be cited by one. The
`traceability_check.py` script flags sections that are internally
consistent but disconnected from the rest of the file.

## 6. Human oversight as design, not wish

`rules/common/name-the-human-overseer.md` forbids phrases like "human in
the loop" or "manual review" unless accompanied by:

- A named individual or role with an email address.
- A measurable decision the overseer can make (intervene, override,
  escalate, halt).
- The exact signal that triggers their involvement.
- The oversight pattern used, from the six catalogued in
  `skills/human-oversight-design-patterns/SKILL.md`:
  gated activation, confidence-threshold escalation, assisted review,
  safe fallback, operator override, audit trail + replay.
- The training or qualification the overseer holds, per Art. 14(4)(d).

The oversight design artifact frontmatter enforces coverage of all five
Art. 14(4) clauses (a)-(e). Missing any clause is a hard fail.

## 7. Post-market monitoring and Art. 73

A PMM row without an `art_73_trigger` field is a failed PMM row. The
trigger is either:

- An explicit mapping to one of Art. 73(1)(a)-(d) — death or serious
  harm; critical infrastructure disruption; infringement of fundamental
  rights; property or environmental damage — **plus** the reporting SLA
  (`immediate_10_days` for death; `two_days` for widespread harm or
  critical infrastructure disruption; `fifteen_days` default per
  Art. 73(3)); or
- An explicit "not a serious-incident trigger" with reason.

`scripts/traceability_check.py` enforces this. "Escalate to the team" is
not an escalation. "Page safety-eng@example.com, halt inference within 10
minutes, draft Art. 73(3) report for the Market Surveillance Authority
within two days" is an escalation.

## 8. Functional-safety bridge for Annex I systems

Annex I systems (safety components of regulated products) carry parallel
obligations under ISO 26262 (FuSa), ISO 21448 (SOTIF), ISO/SAE 21434
(cybersecurity), and instrument-specific type-approval frameworks like
EU 2018/858. The `safety-mapper` agent produces a bidirectional trace:

- **Forward**: for each AI Act Chapter III article, point to the FuSa /
  SOTIF work product that satisfies the intent (HARA, FTTI, safety case,
  SOTIF triggering-conditions analysis).
- **Reverse**: for each safety work product, point to the AI Act article
  it discharges.
- **Retention precedence**: whichever regime demands a longer retention
  period wins. For AI Act + FuSa, the AI Act's ten-year floor under
  Art. 18 dominates a typical FuSa project archive.

`scripts/traceability_check.py` enforces the bidirectional obligation and
the retention declaration.

## 9. Context modes

Three context modes adjust voice without changing the underlying
artifacts:

- `regulator-mode` — for engagement with Notified Bodies or the Market
  Surveillance Authority. Article numbers inline. Hedging flagged.
- `engineer-mode` — for internal safety, ML, or platform teams.
  Assumes fluency in ML and systems vocabulary. Regulation is
  translated into concrete control language.
- `exec-mode` — for sponsors and audit committees. One page max,
  recommendation first, articles moved to the appendix.

## 10. What this plugin will not do

- It will not classify a system without foreseeable-misuse enumeration
  (Art. 9(2)(b) — minimum three).
- It will not produce a Declaration of Conformity without a signed
  conformity assessment workpaper backing it.
- It will not accept "the team" as an owner.
- It will not treat "under review by legal" as evidence.
- It will not be a substitute for engaging a Notified Body where
  Annex VII or Art. 43(3) integration demands one.

## 11. Repo map

```
ai-act-compliance-agents/
├── .claude-plugin/plugin.json      # Entry point for Claude Code / Cowork
├── agents/                          # 5 specialised roles
├── skills/                          # 6 gold-depth SKILL.md files
├── commands/                        # 8 slash commands
├── rules/common/                    # 8 always-on rules (constitutional)
├── contexts/                        # 3 context modes
├── schemas/                         # 3 JSON Schema Draft 2020-12 files
├── scripts/
│   ├── classify_cli.py              # interview / validate / validate-workpaper
│   └── traceability_check.py       # bidirectional audit
├── templates/                       # Stubs the agents populate
├── examples/                        # Worked, schema-valid artifacts
├── docs/METHODOLOGY.md              # This file
└── install.sh                       # Plugin installer
```

## 12. Source anchors

- Regulation (EU) 2024/1689 (AI Act).
- ISO/IEC 42001:2023 (AI management system).
- ISO/IEC 23894:2023 (AI risk management).
- ISO 26262:2018 (road vehicles — functional safety).
- ISO 21448:2022 (SOTIF — safety of the intended functionality).
- ISO/SAE 21434:2021 (road vehicles — cybersecurity).
- Regulation (EU) 2018/858 (type approval of motor vehicles).
- Relevant Recitals of the AI Act are cited inline in individual SKILL.md
  files.
