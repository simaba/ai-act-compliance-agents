# Rule: label-uncertainty-explicitly

**Applies**: always, across every skill, agent, command, and artifact.

## The rule

When an interpretation is contested, novel, or awaiting legal review, it is labeled as such — inline — with the reason and a named reviewer. Silence is not acceptable; confident-sounding language where confidence does not exist is worse.

## Why

AI Act enforcement will rest in part on guidance from the AI Office, harmonized standards still under development, and national competent authorities. Some questions genuinely do not have a stable answer yet. Recording which is which — known-settled vs awaiting-interpretation — is itself evidence of good-faith compliance and lets reviewers focus.

## Required patterns

- "Open Questions for Legal" block at the end of every classification memo, conformity workpaper, and oversight design.
- Each entry has: the question, why it is uncertain, the specific article that would settle it, a named reviewer, and an expected-resolution date.
- Where a classification depends on an unsettled interpretation, the memo records the fallback classification (usually the more conservative one) that applies until the question is resolved.

## Forbidden patterns

- Writing "clearly applicable" or "obviously out of scope" where ambiguity exists.
- Burying uncertainty in a footnote on page 11 instead of the open-questions block.
- Attaching a non-binding reviewer ("legal") rather than a named person.

## Enforcement

Quality assurance agents flag any claim that uses "clear", "obvious", "settled", "guaranteed" without an accompanying citation. The `/audit-prep` dossier lists all open questions and their owners on the first page.
