# Context mode: regulator-mode

**Activate with**: `/context regulator-mode` or by prefixing a prompt with `[regulator]`.

## When to use

- Preparing artifacts for a notified body (Annex VII route).
- Responding to a market-surveillance authority request (Art. 74).
- Drafting the package that accompanies the EU AI-system registration under Art. 49.
- Briefing external legal counsel.

## What this mode changes

- **Tone**: precise, article-anchored, formal register. Drop internal shorthand.
- **Citation**: every regulatory claim cites article + paragraph + literal, plus annex section where relevant. Recitals referenced only to clarify interpretation, never as normative basis.
- **Evidence**: every claim points to a specific versioned artifact with named signatory and retention_until.
- **Traceability**: outputs must pass `/trace` before presentation.
- **Scope**: no speculation about unreleased guidance or draft standards; if something depends on guidance not yet issued, say so explicitly.
- **Disclaimers**: the not-legal-advice footer stays, but the artifact is expected to be reviewed by named counsel before submission to the authority.

## Output preferences

- Structured memos over prose.
- YAML frontmatter on every artifact, validating against the corresponding schema.
- Executive summary on page 1 naming the article coverage and the open questions.
- Appendix with full Chapter III walk for any high-risk system.

## What this mode forbids

- Marketing language ("cutting-edge", "state of the art", "trusted by…").
- Forward-looking commitments not supported by a dated owner.
- Redacting inconvenient findings; surface P0/P1 gaps prominently.

## Companion rules

- `rules/common/cite-the-article.md`
- `rules/common/evidence-not-opinion.md`
- `rules/common/traceability.md`
- `rules/common/review-boundary.md`
