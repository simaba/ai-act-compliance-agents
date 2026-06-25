# AI Act Compliance Agents

An agent-harness concept for EU AI Act readiness, conformity-assessment support artifacts, and ISO 26262 / ISO 21448 traceability for automotive AI systems.

## Maturity

**Early practitioner prototype.**

This repository is a structured drafting and traceability aid. It is not a legal product, compliance certification tool, safety-case generator, or substitute for qualified legal, safety, cybersecurity, privacy, regulatory, or engineering review.

## Purpose

This repository is designed for product, safety, compliance, and engineering teams exploring repeatable workflows for classification, documentation, oversight, post-market monitoring, and traceability.

Core focus areas:

- EU AI Act risk-classification support
- conformity-assessment support artifacts
- technical-documentation templates
- human-oversight design patterns
- post-market monitoring plan drafts
- traceability between regulatory and safety expectations

## Current capabilities

- `agents/` specialized compliance roles
- `skills/` repeatable regulatory and safety workflows
- `commands/` entry points for common tasks
- `templates/` draft documentation artifacts
- `rules/` always-on compliance writing standards
- `src/` lightweight Python utilities for requirement traceability
- `schemas/traceability.schema.json` machine-readable input schema
- `docs/traceability-input.md` input contract, status definitions, and migration notes
- `tests/` unit tests for traceability validation and mapping helpers

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
2. Review the [traceability input contract](docs/traceability-input.md).
3. Run the fictional example traceability check:
   `ai-act-trace examples/sample-requirements.json`
4. Open `AGENTS.md` in your harness for guided workflows.

### Traceability input migration

The traceability utility now expects structured control objects, not a list of plain strings. Each control has a stable ID, source framework/reference/version, accountable owner, review status, and evidence list. This allows the output to support review and provenance rather than only generate a display row.

See [docs/traceability-input.md](docs/traceability-input.md) for the required shape, supported statuses, and migration guidance.

## Publication safety

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

## Out of scope

This prototype does not provide:

- legal advice
- compliance certification
- EU AI Act conformity assessment
- ISO 26262 or ISO 21448 certification
- safety-case approval
- regulatory approval
- production-release readiness
- official guidance from any standards body, regulator, employer, or automaker

## Roadmap

Before public promotion, this repository should add:

1. a methodology note explaining how mappings and source versions should be reviewed
2. a final source-verification checklist for any regulatory references
3. broader edge-case coverage for nested evidence, lifecycle updates, and reviewer handover
4. export formats that preserve source provenance and review history

## Scope and disclaimer

This repository is shared in a personal capacity. It is not affiliated with or endorsed by any automaker, supplier, regulator, standards body, or employer.

References to the EU AI Act, ISO 26262, ISO 21448, conformity assessment, human oversight, post-market monitoring, or safety alignment are practitioner examples for structured thinking. Always verify against official texts, qualified legal counsel, safety engineers, cybersecurity reviewers, privacy reviewers, and internal release processes before using any artifact for real compliance, safety, or release decisions.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*