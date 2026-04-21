# Rule: no-legal-advice-without-human-sign-off

**Applies**: always, across every skill, agent, command, and artifact.

## The rule

Outputs from this repo are structured technical opinions, drafts, and workpapers. They are not legal advice and not certification evidence until a named human with appropriate authority has reviewed and signed them. Every artifact says so, in a place a reader cannot miss.

## Why

The AI Act assigns legal responsibility to providers, deployers, importers, and distributors (Art. 16, 22, 23, 24, 26). LLM-generated drafts cannot bear that responsibility. Treating a draft as a final artifact creates compliance theater and exposes the organization to enforcement risk under Art. 99 (penalties up to EUR 35M or 7% of global turnover for prohibited-system violations).

## Required patterns

- Every classification memo, workpaper, oversight design, PMM plan, and Annex IV section ends with a footer: *"This artifact is a structured technical opinion drafted with assistance from `<agent>`. It is not legal advice. Sign-off requires <named role> review."*
- Frontmatter includes `reviewed_by:` with at least one named human (not "team", not "legal").
- The Declaration of Conformity (Art. 47 + Annex V) is signed only by the authorized representative, never auto-generated.

## Forbidden patterns

- Telling a user "you are now compliant" or "this satisfies Art. X" — only a competent reviewer can certify that.
- Producing artifacts that omit the not-legal-advice footer.
- Closing a workpaper row whose `reviewed_by` is empty.

## Enforcement

Agents refuse to issue a final-status artifact without a named reviewer. The `/audit-prep` command lists any artifact missing the footer or the reviewer field as a P0 finding.
