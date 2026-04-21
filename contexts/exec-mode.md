# Context mode: exec-mode

**Activate with**: `/context exec-mode` or by prefixing a prompt with `[exec]`.

## When to use

- Briefing a sponsor, executive sponsor, board member, or audit committee.
- Producing a quarterly compliance update.
- Asking for go/no-go on placing a high-risk system on the EU market.
- Surfacing material risk to leadership: P0 gaps, Art. 73 incidents, regulator engagement.

## What this mode changes

- **Tone**: decision-oriented, terse, top-down. Lead with the recommendation; supporting detail follows.
- **Length**: one page maximum unless the executive asks for more. Most outputs are 200–400 words.
- **Citation**: regulatory anchors named once at the bottom, not inline. The lead does not require a non-lawyer to look up Art. 14(4)(b).
- **Numbers**: every claim with a number includes the comparison (vs target, vs prior period, vs peer). Numbers without context are noise.
- **Risk framing**: P0/P1/P2/P3 with EUR exposure where calculable; trend (improving / steady / deteriorating); ask (decision, resource, escalation).

## Output preferences

- Memo structure: Recommendation → Rationale (3 bullets) → Risk → Ask → Appendix.
- One-glance status: GREEN / YELLOW / RED with the single sentence that justifies the color.
- For high-risk system go/no-go: a single decision table (option / conformity status / market exposure / cost / reversibility / recommendation).

## What this mode forbids

- Burying the recommendation under preamble.
- Article numbers in the body (move to appendix or footer).
- Hedging language without a defined trigger; "we should consider…" gets replaced with "decide by <date> whether to <action>".
- More than one ask per memo.

## Companion rules

- `rules/common/conservative-classification.md` — when the exec asks "are we high-risk?", default to the higher tier in the brief.
- `rules/common/review-boundary.md` — the brief is a structured technical opinion, not legal sign-off.
