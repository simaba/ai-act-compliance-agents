# Traceability Methodology

## Purpose

This repository provides a compact structure for drafting and reviewing fictional AI traceability records. It helps preserve the link between a feature, intended purpose, a stated control, its cited source, accountable owner, review state, and evidence location.

It is not a legal interpretation engine, safety case, regulatory mapping authority, conformity-assessment process, or release approval mechanism.

## Working model

A traceability register contains:

1. **System context** — a fictional feature and intended purpose.
2. **Control statement** — a concise expected behavior, process, or review requirement.
3. **Source provenance** — framework, reference, and source version or checked date.
4. **Accountability** — the role accountable for progressing or reviewing the control.
5. **Review state** — planned, evidence pending, in review, verified, or blocked.
6. **Evidence pointer** — a fictional or sanitized artifact and its location.

The utility validates structure and completeness. It does not validate whether a source is authoritative, whether a control is sufficient, whether evidence is valid, or whether a system is compliant.

## Review workflow

1. Create a fictional or sanitized feature context.
2. Add controls with unique IDs.
3. Cite the authoritative source in the `source` object and record the version/check date.
4. Assign an accountable owner role.
5. Start controls as `planned`, `evidence_pending`, or `in_review` unless evidence has actually been reviewed.
6. Mark a control `verified` only when the required evidence pointer exists and qualified reviewers have completed the relevant review outside this tool.
7. Treat `blocked` as an explicit decision state that requires follow-up, not as a pass.

## Source discipline

Prefer official primary sources: legislation, regulator guidance, standards-body publications, and formally controlled internal policies where appropriate. The public repository should link only to public sources and must not include employer or confidential source material.

A source version is mandatory because regulatory, standards, and guidance material can change. `SOURCES.md` records the initial public-source baseline; verify it before any real use.

## Public-safety boundary

Only fictional, synthetic, or fully sanitized controls, evidence names, and context may be committed. Do not use this repository to publish real system classification, hazards, test results, supplier details, legal analysis, security posture, or conformity conclusions.

## Known limitations

The prototype does not yet model lifecycle history, reviewer identity/approval signatures, evidence hashes, jurisdiction-specific applicability, legal interpretation, safety assurance arguments, or complete standards mappings. Any real compliance or safety decision requires appropriate qualified review.