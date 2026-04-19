# ai-act-compliance-agents

An agent harness for EU AI Act conformity assessment and ISO 26262 / ISO 21448 alignment in automotive AI systems.

This repo is designed for product, safety, compliance, and engineering teams working on AI-enabled automotive features who need structured, repeatable workflows for classification, documentation, oversight, and post-market monitoring.

## Scope

- EU AI Act risk classification
- conformity assessment support artifacts
- technical documentation templates
- human oversight design patterns
- post-market monitoring plans
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

## Important note

This repo does not provide legal advice or a substitute for formal functional-safety processes. It is a structured drafting and traceability aid.
