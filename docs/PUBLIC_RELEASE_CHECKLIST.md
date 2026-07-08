# Public Release Checklist

Complete this checklist before making the repository public or publishing a release.

## Content safety

- [ ] Confirm all features, intended purposes, controls, owners, evidence names, and examples are fictional or fully sanitized.
- [ ] Confirm no real legal analysis, applicability determination, conformity conclusion, hazard analysis, safety case, security assessment, privacy assessment, test result, supplier detail, or internal policy is present.
- [ ] Confirm no licensed standard text is reproduced.
- [ ] Confirm no employer, customer, vehicle program, project, colleague, product, architecture, roadmap, endpoint, credential, or personal-data reference remains.

## Public provenance

- [ ] Review `SOURCES.md` against official public sources.
- [ ] Confirm every public example names a version or check date rather than implying timeless authority.
- [ ] Confirm documentation states that the repository is a drafting aid, not legal, safety, compliance, or release approval.

## GitHub surface review

- [ ] Review current files, all branches, commit history, issues, pull requests, comments, discussions, releases, tags, and attached files.
- [ ] Review GitHub Actions logs, artifacts, caches, and screenshots.
- [ ] Review repository metadata, topics, homepage, social-preview image, and contributor details.

## Quality baseline

- [ ] CI passes on the intended release commit.
- [ ] The fictional sample validates against the JSON Schema and CLI.
- [ ] README, input contract, methodology, and source baseline agree.
- [ ] Changelog and release notes accurately describe the published scope.

## Release practice

- [ ] Create a draft release and review all notes/assets before publishing.
- [ ] Record commit SHA, reviewer, date, CI URL, and source-check date in the release description.
- [ ] Publish a new release for corrections; do not alter published versioned artifacts.
