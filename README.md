# AI Act Compliance Agents

An agent-harness concept for structured EU AI Act readiness, conformity-assessment support artifacts, and ISO 26262 / ISO 21448 alignment thinking for automotive AI systems.

This repository is designed for product, safety, compliance, and engineering teams exploring repeatable workflows for classification, documentation, oversight, post-market monitoring, and traceability.

## Status

**Early practitioner prototype.**

This repository is a structured drafting and traceability aid. It is not a legal product, compliance certification tool, safety-case generator, or substitute for qualified legal, safety, cybersecurity, privacy, regulatory, or engineering review.

## Scope

- EU AI Act risk-classification support
- conformity-assessment support artifacts
- technical-documentation templates
- human-oversight design patterns
- post-market monitoring plan drafts
- traceability between regulatory and safety expectations

## Core components

- `agents/` specialized compliance roles
- `skills/` repeatable regulatory and safety workflows
- `commands/` entry points for common tasks
- `templates/` draft documentation artifacts
- `rules/` always-on compliance writing standards
- `src/` light Python utilities for requirement traceability
- `tests/` unit tests for mapping helpers

## Included agents

- `risk-classifier`
- `conformity-checker`
- `safety-mapper`
- `oversight-designer`
- `post-market-monitor`

## Included skills

- `eu-ai-act-risk-classification`
- `technical-documentation-template`
- `conformity-assessment-checklist`
- `post-market-monitoring-plan`
- `human-oversight-design-patterns`
- `iso26262-21448-mapping`

## Quick start

1. Install in editable mode:
   `pip install -e .`
2. Run the example traceability check:
   `ai-act-trace examples/sample-requirements.json`
3. Open `AGENTS.md` in your harness for guided workflows.

## Public-safe use rule

Only publish fictional, synthetic, or fully sanitized examples in this repository.

Do not publish:

- real company compliance positions
- confidential legal interpretations
- real vehicle-system safety analyses
- proprietary feature behavior or release gates
- supplier, vendor, or customer details
- internal risk classifications or conformity conclusions
- unreleased product names, roadmaps, or architecture
- real safety requirements, hazards, incidents, or test results

## What this repo does not claim

This repo does **not** claim to provide:

- legal advice
- compliance certification
- EU AI Act conformity assessment
- ISO 26262 or ISO 21448 certification
- safety-case approval
- regulatory approval
- production-release readiness
- official guidance from any standards body, regulator, employer, or automaker

## Next maturity step

Before public promotion, this repo should add:

1. a public-safe sample traceability file using only fictional requirements
2. a clearer schema for regulatory and safety mappings
3. a methodology note explaining how mappings should be reviewed
4. tests for edge cases in requirement traceability
5. a final source-verification checklist for any regulatory references

## Scope and disclaimer

This repository is shared in a personal capacity. It is not affiliated with or endorsed by any automaker, supplier, regulator, standards body, or employer.

References to the EU AI Act, ISO 26262, ISO 21448, conformity assessment, human oversight, post-market monitoring, or safety alignment are practitioner examples for structured thinking. Always verify against official texts, qualified legal counsel, safety engineers, cybersecurity reviewers, privacy reviewers, and internal release processes before using any artifact for real compliance, safety, or release decisions.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
