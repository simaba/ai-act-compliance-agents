---
name: eu-ai-act-risk-classification
description: Classify an AI system into one of the four EU AI Act risk tiers — prohibited, high-risk, limited-risk, or minimal-risk — with article-level justification. Use this when the user says "classify this", "what tier is this", "is this high-risk", "AI Act category", "Annex III check", or has a system description and needs to know which obligations apply. Not for drafting technical documentation (use `technical-documentation-template`) or planning conformity routes (use `conformity-assessment-checklist`).
---

# EU AI Act Risk Classification

## When to use

Use this skill when:

- A team has a feature or product idea and needs to know whether the AI Act applies and at what tier.
- An external counsel, auditor, or sponsor asks "what's our risk class for X?".
- An existing system changes intended purpose, deployment context, or user population in a way that could move it across tiers (Art. 25 substantial-modification trigger).
- You are preparing a conformity-assessment plan and the route choice depends on the tier (`conformity-assessment-checklist` calls this skill first).

Do NOT use this skill to:

- Provide legal advice. Output is a structured technical opinion that cites articles. Sign-off requires a named legal reviewer.
- Classify general-purpose AI models (Art. 51–55) — those follow a separate route based on FLOPs threshold and systemic-risk designation.

## Hard rule

**Classify by intended purpose, not by capability.** The same model (e.g., a fine-tuned LLM) can be minimal-risk in one deployment and high-risk in another. The classification is bound to:

1. The intended purpose stated by the provider (Art. 3(12)).
2. The deployment context (sector, user population, output use).
3. Reasonably foreseeable misuse (Art. 9(2)(b)).

If intended purpose is vague, the classification is invalid. Refuse to classify until the team can answer: *"What decision does this system make or support, for whom, with what consequence if wrong?"*

## The four tiers

| Tier | Source | Examples | Consequence |
|---|---|---|---|
| **Prohibited** | Art. 5 | Social scoring by public authorities; subliminal manipulation causing harm; real-time remote biometric ID in public spaces (with narrow law-enforcement carveouts); emotion recognition in workplace/education; untargeted facial scraping. | Cannot be placed on the EU market or put into service. Period. |
| **High-risk** | Art. 6 + Annex I (safety components of regulated products) and Annex III (eight standalone use-case areas) | In-vehicle systems used as safety components of a regulated product; CV systems for critical infrastructure; AI in education for assessing students; AI in employment for screening candidates; AI in essential private/public services (credit scoring, benefit eligibility); biometric categorization; law enforcement; migration; administration of justice. | Full Chapter III obligations: risk management (Art. 9), data governance (Art. 10), technical documentation (Art. 11 + Annex IV), record-keeping (Art. 12), transparency (Art. 13), human oversight (Art. 14), accuracy/robustness/cybersecurity (Art. 15), QMS (Art. 17), conformity assessment (Art. 43), CE marking (Art. 48), registration (Art. 49), post-market monitoring (Art. 72). |
| **Limited-risk** | Art. 50 | Chatbots interacting with humans; emotion-recognition systems (outside prohibited contexts); biometric-categorization systems; deepfake / synthetic content generators. | Transparency obligations only: disclose to the human that they are interacting with AI, label synthetic content, label biometric/emotion inference. |
| **Minimal-risk** | Default residual | Spam filters; AI-enabled video games; inventory ML. | No mandatory obligations under the Act. Voluntary codes of conduct (Art. 95) encouraged. |

## Decision walk

Run these gates in order. Stop at the first that fires.

### Gate 1 — Prohibited (Art. 5)

Read each Art. 5 prohibition (a–h, as adopted) against the intended purpose AND foreseeable misuse. If any matches, the system is **prohibited**. Stop. Document which prohibition and the matching system facts.

### Gate 2 — High-risk via Annex I

Is the AI system itself a product, or a safety component of a product, that is covered by the Union harmonization legislation listed in Annex I (toys, machinery, lifts, medical devices, in-vitro diagnostics, civil aviation, marine equipment, agricultural and forestry vehicles, two/three-wheel and quadricycle vehicles, motor vehicles and trailers, etc.) AND is required to undergo a third-party conformity assessment under that legislation? If yes → **high-risk**. The conformity route follows the sector legislation (Art. 43(3)).

### Gate 3 — High-risk via Annex III

Does the intended purpose fall within one of the eight Annex III areas?

1. Biometrics (remote ID, categorization, emotion recognition — outside Art. 5).
2. Critical infrastructure (safety components of road traffic, water, gas, heating, electricity).
3. Education and vocational training (admission, assessment, monitoring).
4. Employment, workers' management and access to self-employment (recruitment, task allocation, performance evaluation).
5. Access to and enjoyment of essential private and public services (credit scoring; eligibility for public benefits; emergency services dispatch; risk assessment in life and health insurance).
6. Law enforcement.
7. Migration, asylum and border control.
8. Administration of justice and democratic processes.

If yes → **high-risk** UNLESS the provider can document the **Art. 6(3) carve-out**: the system performs a narrow procedural task; improves the result of a previously completed human activity; detects decision-making patterns without replacing or influencing the human assessment; or performs a preparatory task. The carve-out is narrow; default is to classify as high-risk and let legal review demote.

### Gate 4 — Limited-risk (Art. 50)

Does the system interact directly with natural persons, generate synthetic audio/image/video/text, infer emotions, or perform biometric categorization? If yes and not already prohibited or high-risk → **limited-risk**. Only Art. 50 transparency obligations apply.

### Gate 5 — Minimal-risk

Otherwise → **minimal-risk**. Document the reasoning anyway; intended-purpose drift can move a system into a higher tier later.

## Structure of the classification memo

Output a memo with this YAML frontmatter (validates against `schemas/ai-system-classification.json`):

```yaml
---
id: AI-SYS-0001
system_name: VoxOS Japan In-Vehicle Assistant
provider: Acme Mobility AB
intended_purpose: >-
  Hands-free voice control of in-vehicle media, navigation queries,
  and vehicle settings while driving on public roads in Japan.
deployment_context: passenger vehicles, MY27, JP market only
user_population: licensed drivers, primary user is the vehicle operator
foreseeable_misuse:
  - using voice commands to override safety-critical vehicle settings while in motion
  - hands-free messaging used as substitute for visual attention to road
classification: limited-risk
articles_cited: [Art. 3(1), Art. 3(12), Art. 50, Art. 6(1), Annex I]
annex_iii_check: not applicable — passenger media/nav is not within the eight Annex III areas
annex_i_check: vehicle is regulated under EU 2018/858; voice assistant is NOT a safety component (does not control braking/steering/acceleration); not subject to third-party conformity assessment under that legislation
art_5_check: no prohibited use case matched
classified_by: sima@example.com
reviewed_by: marcus@example.com
classification_date: 2026-04-19
review_due: 2026-10-19
status: in_review
substantial_modification_triggers:
  - addition of biometric driver-monitoring capability
  - integration into ADAS pipeline (would invoke Annex I)
  - expansion to commercial fleet management with worker-evaluation features (would invoke Annex III #4)
---
```

The memo body should contain: short narrative justification, the gate-by-gate walk, an "Open Questions" block for items requiring legal review, and a "Re-classification Triggers" block listing the specific changes that would invalidate this classification.

## Worked example — VoxOS Japan in-vehicle voice assistant

**Intended purpose**: hands-free voice control of media, nav queries, vehicle settings.

- Gate 1 (Art. 5): No prohibition matches. Not subliminal, not manipulative beyond ordinary product UX, not biometric ID, not workplace emotion recognition.
- Gate 2 (Annex I): The vehicle itself is regulated under EU 2018/858. The voice assistant is NOT a safety component — it does not actuate braking, steering, or throttle, and a failure does not directly create a safety hazard within the meaning of EU 2018/858 Art. 13. Not high-risk via Annex I.
- Gate 3 (Annex III): Not within any of the eight areas. Closest candidates considered and ruled out: critical infrastructure (the system is not a safety component of road traffic infrastructure; it is in a single private vehicle); employment (no worker assessment).
- Gate 4 (Art. 50): The system interacts directly with a natural person via voice. Transparency obligation applies — driver must be informed they are interacting with an AI system on first use and on material changes.
- Result: **Limited-risk**. Art. 50 disclosure UX required. No Chapter III obligations.

**Re-classification triggers** (must re-run on any of these): adding driver-state monitoring (biometric inference → Art. 50 + possibly Annex III #1); integration into ADAS lane-keeping (Annex I); fleet-manager edition that uses voice telemetry to evaluate driver performance (Annex III #4).

## Reviewer checklist

Before sending the memo for sign-off:

- [ ] Intended purpose is one sentence and is testable (you can write a unit test for what the system is *for*).
- [ ] Foreseeable misuse listed with at least 3 entries (Art. 9(2)(b) anchor).
- [ ] All five gates walked in order; each non-firing gate has a one-line reason.
- [ ] Articles and annexes cited by number, not by paraphrase.
- [ ] If high-risk: Art. 6(3) carve-out either applied with documented evidence or explicitly ruled out.
- [ ] Re-classification triggers list includes the specific changes that would move tier.
- [ ] A named legal reviewer is in `reviewed_by` (not "team", not "legal").
- [ ] `review_due` is set ≤ 6 months from classification date OR tied to next material release, whichever is sooner.

## Common failure modes

- **Classifying by capability** — "it uses an LLM, so it must be high-risk." Wrong. LLM-based help text in a documentation site is minimal-risk.
- **Missing the foreseeable-misuse leg** — Art. 9 explicitly covers misuse; if you only consider intended use, you under-classify.
- **Skipping Annex I when the host product is regulated** — vehicles, medical devices, machinery have their own conformity routes that pull AI components into high-risk via the safety-component test.
- **Treating Art. 6(3) carve-out as default** — it is narrow and you bear the documentation burden. When in doubt, classify as high-risk and let legal review demote with documented reasoning.
- **One classification for the whole product** — a vehicle may carry a limited-risk voice assistant AND a high-risk driver-monitoring system AND a minimal-risk recommender. Classify per intended purpose, not per product.

## Composition

- Pairs with `conformity-assessment-checklist` — high-risk classifications drive the Art. 43 route choice and the requirements list.
- Pairs with `technical-documentation-template` — for any classification at limited-risk or above, the memo becomes Section 1 of the Annex IV technical documentation.
- Pairs with `human-oversight-design-patterns` — high-risk classifications trigger Art. 14 oversight-design work.

## Source

- Regulation (EU) 2024/1689 of 13 June 2024 (EU AI Act), in particular Art. 3, 5, 6, 9, 50, 51–55; Annex I, Annex III.
- Recital 27 (intended-purpose anchoring), Recital 53 (Art. 6(3) carve-out scope).
- ISO/IEC 42001:2023 §6.1.2 (risk-based AI management).

*This skill produces a structured technical opinion, not legal advice. The Reviewer Checklist requires a named legal reviewer before any classification is treated as decisional.*
