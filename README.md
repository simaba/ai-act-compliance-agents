# AI Act Compliance Agents

An agent-harness concept for structured, **fictional or fully sanitized** AI traceability drafts and review artifacts.

## Maturity

**Early practitioner prototype.**

This repository is a structured drafting and traceability aid. It is not a legal product, compliance certification tool, safety-case generator, or substitute for qualified legal, safety, cybersecurity, privacy, regulatory, or engineering review.

## Start here

- [Traceability input contract](docs/traceability-input.md): required input shape, statuses, and migration guidance.
- [Traceability methodology](METHODOLOGY.md): what the utility validates and where accountable human review begins.
- [Public source provenance baseline](SOURCES.md): reference discipline and update cadence.
- [Public Release Checklist](docs/PUBLIC_RELEASE_CHECKLIST.md): repository-wide pre-publication review.
- [Draft v0.1.0 notes](docs/releases/v0.1.0.md): intended public-release scope.

## Purpose

The repository helps product, safety, compliance, and engineering teams explore repeatable structures for:

- EU AI Act risk-classification support artifacts
- technical-documentation drafts
- human-oversight design patterns
- post-market-monitoring plan drafts
- traceability between stated controls, source references, ownership, review state, and evidence pointers

## Current capabilities

- specialized agent, skill, command, template, and rule materials for practitioner workflows
- lightweight Python utility for structured traceability rows
- `schemas/traceability.schema.json` machine-readable input schema
- validation for stable control IDs, source framework/reference/version, owner, review status, and evidence records
- fictional sample input and unit tests
- an explicit input contract, methodology, source baseline, and release-preflight checklist

## Quick start

1. Install in editable mode: `python -m pip install -e .`
2. Review the [traceability input contract](docs/traceability-input.md).
3. Run the fictional example: `ai-act-trace examples/sample-requirements.json`
4. Read [METHODOLOGY.md](METHODOLOGY.md) and [SOURCES.md](SOURCES.md) before adapting any structure.

## Traceability input migration

The utility expects structured control objects, not a list of plain strings. Each control contains a stable ID, source framework/reference/version, accountable owner, review status, and evidence list.

This supports traceability and review preparation; it does not make a control legally sufficient or technically verified.

## Publication safety

Only fictional, synthetic, or fully sanitized material belongs here.

Do not publish:

- real company compliance positions or internal risk classifications
- confidential legal interpretations, safety analyses, or security/privacy assessments
- proprietary feature behavior, release gates, architecture, roadmaps, supplier details, or test results
- real safety requirements, hazards, incidents, evidence, or conformity conclusions
- licensed standards text, employer policies, credentials, endpoints, or personal data

## Out of scope

This prototype does not provide:

- legal advice, compliance certification, or EU AI Act conformity assessment
- ISO 26262, ISO 21448, or safety-case certification
- regulatory or production-release approval
- evidence-quality validation, legal applicability determination, or authoritative standards interpretation
- official guidance from any standards body, regulator, employer, or automaker

## Next quality steps

1. broader edge-case coverage for nested evidence, lifecycle updates, and reviewer handover
2. export formats that preserve source provenance and review history
3. a controlled example of lifecycle status changes using only fictional information
4. a documented source-refresh process for maintained public examples

## Scope and disclaimer

This repository is shared in a personal capacity. It is not affiliated with or endorsed by any automaker, supplier, regulator, standards body, or employer.

References to laws, standards, conformity assessment, human oversight, post-market monitoring, or safety alignment are practitioner examples for structured thinking. Verify against official texts and use qualified review before applying any artifact to a real system, compliance process, safety process, or release decision.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*