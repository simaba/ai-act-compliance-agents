# Rule: conservative-classification

**Applies**: to every classification decision, especially where Annex III scope or the Art. 6(3) carve-out is in play.

## The rule

When the tier is genuinely ambiguous, classify at the higher tier and document why. Demotion happens later with documented reasoning by a named legal reviewer. Promotion after market placement is more costly than a conservative initial classification.

## Why

Art. 6(3) carve-out is narrow and the documentation burden is on the provider. Art. 25 substantial-modification re-classification is operationally painful — pulling a system off market mid-lifecycle to retrofit Chapter III obligations is far more expensive than building them in. The cost of over-classifying is documentation effort; the cost of under-classifying is enforcement exposure (Art. 99 penalties up to EUR 35M / 7% global turnover for prohibited-system violations) plus market withdrawal.

## Required patterns

- Where two tiers are plausible, the higher tier is selected and the memo records the lower-tier alternative as an explicit "consider promotion to lower tier on legal review" entry.
- Art. 6(3) carve-out is invoked only with documented evidence for each of the four sub-conditions; default is high-risk.
- The "Open Questions for Legal" block lists the specific question(s) that, if answered favorably, would support reclassification — and names the reviewer.

## Forbidden patterns

- "We think this is probably limited-risk so we'll go with that" without documenting the high-risk alternative considered.
- Applying Art. 6(3) by default — it is an exception, not a baseline.
- Classifying capability rather than intended purpose to land in a more convenient tier.

## Enforcement

The `risk-classifier` agent flags ambiguous classifications and, where two tiers are plausible, defaults to the higher tier in the draft. The reviewer can demote with rationale; the draft itself does not.
