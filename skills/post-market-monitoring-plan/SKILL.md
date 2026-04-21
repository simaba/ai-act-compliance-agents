---
name: post-market-monitoring-plan
description: Draft or update the Art. 72 post-market monitoring (PMM) plan for a high-risk AI system — what you will measure in production, at what cadence, against what thresholds, with what escalation path to Art. 73 serious-incident reporting. Use this when the user says "PMM plan", "post-market monitoring", "Art. 72", "incident reporting procedure", "what do we watch for after launch", or is preparing to place a high-risk system on the market. Not for classification (use `eu-ai-act-risk-classification`) or for the general conformity workpaper (use `conformity-assessment-checklist`).
---

# Post-Market Monitoring Plan

## When to use

Use this skill when:

- A high-risk AI system is approaching market placement — the PMM plan is a required deliverable before shipping (Art. 72(1)).
- An Art. 73 serious incident has occurred and the PMM plan proved insufficient — rebuild from lessons learned.
- A substantial modification (Art. 25) changes the performance or risk profile — existing thresholds may no longer be calibrated.
- A deployer-reported issue reveals a monitoring gap — the plan needs a new metric/threshold row.

Do NOT use this skill for:

- Limited-risk (Art. 50) systems. Transparency obligations are point-in-time, not monitored.
- Routine product-analytics dashboards. PMM is proportionate to **risks**, not feature usage.

## Hard rule

**Every metric has a threshold, a cadence, an owner, and an escalation path. Every threshold has a defined response action, not "investigate".** A PMM row that says "monitor accuracy monthly" without specifying the threshold that triggers action is not a control — it is a data-collection exercise.

The plan must connect to Art. 73: when does an observation become a "serious incident" that requires notification to the market-surveillance authority within 15 days (2 days for a widespread infringement or fundamental-rights breach; immediate for death)?

## Structure

### Frontmatter

```yaml
---
system_id: AI-SYS-0002
system_name: VoxOS Fleet Recruiter Assist
pmm_plan_version: 1.0
pmm_plan_date: 2026-04-19
classification_tier: high-risk
provider: Acme Mobility AB
pmm_owner: chen@example.com
incident_reporting_owner: marcus@example.com
deployer_reporting_channel: compliance@acme-mobility.eu
market_surveillance_authority: SE — IMY (Integritetsskyddsmyndigheten)
next_review: 2026-10-19
retention_until: 2036-04-19
status: in_review
---
```

### Body sections

1. **Purpose and scope** — which system version(s), which deployer populations, which geographies.
2. **Monitored signals** — the table of metric rows (see schema below).
3. **Collection infrastructure** — where logs are stored, how they are pipelined, retention window, access control (ties to Art. 12 logging).
4. **Review cadence** — weekly automated report; monthly human review; quarterly cross-functional review including risk owner and named legal reviewer.
5. **Thresholds and escalation** — threshold table; escalation contact per level; time-to-respond commitments.
6. **Connection to Art. 73 incident reporting** — which thresholds cross into "serious incident"; notification template; 15-day / 2-day / immediate routing.
7. **Deployer feedback channel** — how deployers report issues; SLA on triage; how their reports feed the PMM data.
8. **Change-management hook** — how PMM findings trigger updates to Annex IV §6 and to the risk register.

## Row schema

Each monitored signal (validates against `schemas/pmm-incident.json` for incident rows; monitored-signal rows follow a sibling schema):

```yaml
- id: PMM-0007
  category: accuracy_drift
  metric: top-1 intent accuracy on production JP traffic
  source: production telemetry (anonymized)
  baseline: 0.931 (measured at launch, 2026-11-03)
  threshold_warn: -1.0 absolute pp over 7-day rolling window
  threshold_critical: -2.0 absolute pp over 7-day rolling window OR -1.5 pp over 28-day rolling window
  cadence: weekly automated; daily if in warn
  owner: chen@example.com
  escalation_warn: PMM lead reviews within 5 working days; logs investigation in change register.
  escalation_critical: |
    Within 24h: notify risk owner and sponsor; open incident ticket.
    Within 72h: decide on corrective action (rollback, re-train, deployer notification, market-surveillance pre-notification).
  art_73_trigger: |
    A sustained accuracy drop that results in materially biased outcomes against
    a protected subgroup is a fundamental-rights impairment — reportable as a
    serious incident under Art. 3(49)(c) within 15 days.
  linked_risk: RISK-0002
  last_updated: 2026-04-19
```

## Monitored signal categories

Your plan should cover at minimum these categories; add rows for system-specific risks.

| Category | Typical signals |
|---|---|
| **Accuracy drift** | Top-1 / top-k accuracy on live traffic vs baseline; calibration error; subgroup accuracy (bias watch). |
| **Robustness / OOD** | Out-of-distribution rate; confidence-distribution shift; refusal rate. |
| **Safety / harm** | P0/P1 incident count; near-miss count; user-reported harm reports. |
| **Human-oversight usage** | Override rate; time-to-review; frequency of "acknowledge without reading" patterns (if detectable). |
| **Cybersecurity** | Anomalous input patterns suggestive of adversarial probing; credential/secret leakage attempts; dependency CVE exposure. |
| **Data quality** | Input-distribution drift vs training; missing-feature rate; encoding errors. |
| **Operational** | Latency p50/p95/p99; availability; rate of fallback-path invocation. |
| **Deployer feedback** | Ticket volume by severity; time-to-close; top complaint categories. |
| **Third-party dependency** | GPAI model version changes; vendor incident notifications; license/terms updates. |

## Art. 73 serious-incident mapping

Art. 3(49) defines a "serious incident" as an incident or malfunction of an AI system that directly or indirectly leads to:
(a) the death of a person or serious harm to a person's health;
(b) a serious and irreversible disruption of the management or operation of critical infrastructure;
(c) infringement of obligations under Union law intended to protect fundamental rights;
(d) serious harm to property or the environment.

Map each PMM row's `art_73_trigger` field to one or more of (a)–(d) with reasoning. If no trigger applies, say so explicitly — silence is not a mapping.

Reporting timeline (Art. 73(2)–(4)):
- **Death of a person**: immediate, not later than 10 days after the provider established the causal link.
- **Widespread infringement or critical-infrastructure disruption**: 2 days.
- **All other serious incidents**: 15 days.

## Worked example — VoxOS Fleet Recruiter Assist

11 monitored signals across 6 categories. Accuracy drift has 2 rows (overall + subgroup). Human-oversight usage has 3 rows (override rate, time-to-review, rationale-field completion). Subgroup-accuracy row has the tightest thresholds because Art. 10 + Art. 73 elevate any drift that disproportionately affects a protected subgroup.

Example escalation that exercised the plan: during week 9 post-launch, subgroup accuracy for one regional cohort fell 1.3 pp while overall held. Warn threshold fired. Investigation found a data-labelling shift in one source vendor. Corrective action: retrained on stabilized labels, re-deployed within 14 days, deployer notification issued, filed as a §6 change entry. No Art. 73 notification required because the drift was caught in warn band and corrective action returned the metric within one review cycle — but the investigation memo is retained to show the plan functioned.

## Reviewer checklist

- [ ] Every high-risk category above has at least one row (or an explicit "not applicable" reason).
- [ ] Every row has: baseline, warn threshold, critical threshold, cadence, owner, escalation text.
- [ ] Every row has an `art_73_trigger` field — either mapped to (a)–(d) or explicitly "not a serious-incident trigger" with reason.
- [ ] Collection infrastructure is named (not "our analytics") with retention ≥ 10 years for incident-relevant data.
- [ ] Deployer feedback channel is a real email / ticket system, with an SLA.
- [ ] Named PMM owner and named incident-reporting owner — both present in frontmatter.
- [ ] Next review is scheduled ≤ 6 months out.
- [ ] The plan is referenced from the conformity workpaper Art. 72 row and from Annex IV §3.

## Common failure modes

- **Monitoring is all accuracy, no oversight.** If you don't watch override rate, you don't know whether Art. 14 oversight is real or theater.
- **Warn thresholds with no defined action.** "Investigate" is not an action; specify *who*, *within what*, *producing what artifact*.
- **Missing the deployer channel.** Deployers see issues first. A PMM plan without a named intake channel is incomplete.
- **Conflating PMM with product analytics.** Product metrics are driven by growth; PMM is driven by risk. They can share pipelines; they don't share prioritization.
- **Retention shorter than Art. 18 + Art. 19.** Logs relevant to incidents must be preserved for the 10-year retention window, not the standard telemetry TTL.

## Composition

- Upstream: `eu-ai-act-risk-classification` (defines tier and therefore whether Art. 72 applies); `conformity-assessment-checklist` (the Art. 72 row points here).
- Downstream: `technical-documentation-template` (Annex IV §3 references this plan); `human-oversight-design-patterns` (override-rate metric lives in both).
- Lateral: `iso26262-21448-mapping` (for automotive Annex I systems, PMM ties to FuSa field-monitoring obligations; avoid parallel trackers).

## Source

- Regulation (EU) 2024/1689, Art. 18 (retention), Art. 19 (automatically generated logs), Art. 72 (post-market monitoring), Art. 73 (reporting of serious incidents); Art. 3(49) (serious incident definition).
- Recital 155 (proportionality of PMM).
- ISO/IEC 42001:2023 §9 (performance evaluation), §10 (improvement).

*This skill produces the plan that underlies continuous compliance. Sign-off is by the named incident-reporting owner; the plan is re-reviewed at least every 6 months or on any substantial modification.*
