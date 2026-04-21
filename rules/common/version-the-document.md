# Rule: version-the-document

**Applies**: always, to every artifact produced by this repo.

## The rule

Every artifact has a version number, a documentation date, and a change-log entry capturing what changed, why, and who signed off. Editing in place without a version bump is forbidden. Annex IV §6 requires a lifecycle change log for high-risk systems; this rule extends that discipline to the rest of the repo.

## Why

Art. 11(2) requires the technical documentation to be kept up to date. Art. 25 triggers a conformity-assessment re-run on substantial modification; without a version history, you cannot tell which version is on the market, which was assessed, and which triggered the modification. Notified bodies and market-surveillance authorities both rely on versioned trails.

## Required patterns

- Frontmatter includes `documentation_version`, `documentation_date`, and (where relevant) `supersedes:` pointing to the prior version.
- A §6 or equivalent change-log section captures: date, version, summary of change, impact on intended purpose, impact on Chapter III conformity, re-test or re-review outcome, signatory.
- Storage location supports immutable retention of prior versions (not overwrite-in-place).
- Retention is ≥ 10 years from market placement (Art. 18).

## Forbidden patterns

- `documentation_version: latest` or other mutable strings.
- Deleting or rewriting a prior version instead of issuing a new one.
- Change-log entries that say "minor updates" without enumerating the changes.

## Enforcement

The `/trace` script confirms that `documentation_version` is a semantic-version string and that `supersedes` (if set) resolves to an existing version. The `/audit-prep` command includes a version-history page for every artifact.
