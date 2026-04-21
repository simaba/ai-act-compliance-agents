---
description: Classify a system into one of the four EU AI Act risk tiers with article-level rationale.
argument-hint: [system-description-path | system name to brief]
---

# /classify-risk

Run the `risk-classifier` agent on the system you describe (or attach).

## What this does

1. Restates the intended purpose in one testable sentence and confirms with you.
2. Walks the five-gate decision (Art. 5 → Annex I → Annex III → Art. 50 → minimal-risk default).
3. Lists foreseeable misuse (≥ 3 entries).
4. Produces a classification memo with YAML frontmatter that validates against `schemas/ai-system-classification.json`.
5. Names a legal reviewer for sign-off and lists re-classification triggers.

## When NOT to use

- For GPAI model documentation (Art. 53–55) — different template.
- For final legal sign-off — this produces a structured technical opinion, not legal advice.

## Hand-offs

- High-risk → run `/conformity-gap` next.
- Limited-risk (Art. 50) → embed the disclosure spec in the deployer instructions; no full conformity workpaper needed.
- Minimal-risk → record the memo for re-classification on substantial modification.

## Output

Saved to `examples/classification/<slug>.md`. Open the memo and confirm the gate walk before acting on the result.

## See also

- Skill: `skills/eu-ai-act-risk-classification/SKILL.md`
- Agent: `agents/risk-classifier.md`
- Schema: `schemas/ai-system-classification.json`
