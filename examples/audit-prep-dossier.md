# Audit-prep dossier — VoxOS Fleet Recruiter

*Prepared in anticipation of a Notified Body review or Market Surveillance
Authority inquiry under Regulation (EU) 2024/1689. This is the one-file
index an auditor would want on day one.*

**Prepared by**: bagherisima@gmail.com
**Prepared on**: 2026-04-19
**System under assessment**: VoxOS Fleet Recruiter (AI-SYS-0002)
**Classification**: high-risk under Annex III #4(a)
**Conformity route**: Annex VI internal control under Art. 43(2)
**Documentation version**: 1.0.0
**Retention window**: through 2036-04-19 (Art. 18)

---

## 1. The five artifacts an auditor must see

| Artifact | Path | Signed by | Last updated |
| --- | --- | --- | --- |
| Classification memo | [classification-voxos-fleet-recruiter.md](./classification-voxos-fleet-recruiter.md) | legal-counsel@voxos.example + dpo@voxos.example | 2026-04-19 |
| Conformity workpaper | [conformity-workpaper-voxos-fleet-recruiter.yaml](./conformity-workpaper-voxos-fleet-recruiter.yaml) | coo@voxos.example (pending full sign-off) | 2026-04-19 |
| Technical file (Annex IV) | [technical-file-voxos-fleet-recruiter.md](./technical-file-voxos-fleet-recruiter.md) | coo@voxos.example + safety-lead@voxos.example (pending) | 2026-04-19 |
| Oversight design | [oversight-voxos-fleet-recruiter.md](./oversight-voxos-fleet-recruiter.md) | product-manager@voxos.example (pending legal + DPO) | 2026-04-19 |
| PMM plan | [pmm-plan-voxos-fleet-recruiter.yaml](./pmm-plan-voxos-fleet-recruiter.yaml) | safety-lead@voxos.example | 2026-04-19 |

## 2. Open obligations and gap register

Extracted from the conformity workpaper. Each gap is owned by a named
human with a due date.

| ID | Article | Gap | Owner | Due | Priority |
| --- | --- | --- | --- | --- | --- |
| CONF-0002 | Art. 10 | Representativeness analysis for ES and FR pending | data-governance@voxos.example | 2026-06-30 | P1 |
| CONF-0007 | Art. 15 | OOD robustness battery incomplete for non-primary vehicle categories | ml-lead@voxos.example | 2026-07-15 | P1 |
| CONF-0010 | Art. 47 | DoC unsigned — blocked on CONF-0002 + CONF-0007 | coo@voxos.example | 2026-07-31 | P0 |
| CONF-0011 | Art. 49 | EU database registration unsubmitted — blocked on CONF-0010 | coo@voxos.example | 2026-08-15 | P0 |

## 3. Evidence index (by article)

The conformity workpaper is the authoritative source. Abbreviated index
here for auditor navigation.

- **Art. 9 risk management** — `docs/risk/AI-SYS-0002-risk-register.yaml@v1.3`; quarterly review memo `docs/risk/Q1-2026-review.md`.
- **Art. 10 data governance** — `docs/data/training-dataset.md@v2.1`.
- **Art. 11 technical documentation** — this Annex IV file.
- **Art. 12 logging** — `docs/logs/sample-inference-log-2026-04-10.jsonl`; retention spec `docs/platform/log-retention.md@v1.0`.
- **Art. 13 transparency** — `docs/customer/instructions-for-use-v1.0.pdf`.
- **Art. 14 human oversight** — oversight design doc; training record `docs/training/hiring-manager-oversight-2026-Q2.md`.
- **Art. 15 accuracy + robustness + cyber** — `docs/testing/accuracy-report-2026-Q1.md@v1.0`; SOC 2 Type II `docs/security/soc2-type2-2025.pdf`.
- **Art. 17 QMS** — `docs/qms/aims-overview.md@v1.0`.
- **Art. 43 conformity route** — `docs/conformity/annex-vi-sign-off.md@v1.0`.
- **Art. 47 DoC** — `docs/conformity/doc-template.md@v1.0` (unsigned).
- **Art. 72 PMM plan** — PMM plan in this examples directory.

## 4. PMM hot signals at time of audit

Extracted from PMM plan. All signals currently within warn-threshold.

| ID | Signal | Status | Owner |
| --- | --- | --- | --- |
| PMM-0001 | Score-advance correlation | green | ml-lead@voxos.example |
| PMM-0003 | Confirmed decision reversals | green (0 confirmed) | safety-lead@voxos.example |
| PMM-0004 | Demographic-parity disparity | green (< 0.05) | data-governance@voxos.example |
| PMM-0005 | Score-only-session rate | green (11% vs 15% target) | product-manager@voxos.example |
| PMM-0006 | Cybersecurity events | green (0 successful) | security-lead@voxos.example |

## 5. Incident history

No Art. 73 reportable events in the rolling 12-month window at the date
of preparation. Incident-response runbook: `docs/incident-response/art-73-runbook.md`.

## 6. Change log summary

- 2025-11-15: v0.1 classification memo draft.
- 2026-01-30: v0.5 classification memo + v0.5 conformity workpaper skeleton.
- 2026-03-15: v0.9 technical file; log-retention pipeline cut over to WORM.
- 2026-04-10: oversight-design training-cohort #1 completed.
- 2026-04-19: v1.0.0 dossier frozen for audit prep.

## 7. Outstanding reviews and the path to DoC

| Review | Owner | Status | Blocks |
| --- | --- | --- | --- |
| Classification memo sign-off | legal-counsel@voxos.example, dpo@voxos.example | in progress | DoC |
| Technical file sign-off | coo@voxos.example, safety-lead@voxos.example | pending | DoC |
| Oversight design sign-off | legal-counsel@voxos.example, dpo@voxos.example | pending | deployer rollout |
| Conformity workpaper CONF-0002 | data-governance@voxos.example | open, due 2026-06-30 | DoC |
| Conformity workpaper CONF-0007 | ml-lead@voxos.example | open, due 2026-07-15 | DoC |
| DoC signature | coo@voxos.example | blocked | EU registration |
| EU database registration (Art. 49) | coo@voxos.example | blocked | placing on market |

## 8. Reviewer boundary

This dossier is a structured index of technical artifacts. It is not a
conformity-assessment sign-off. Final sign-off is by `coo@voxos.example`
and backed by the signed artifacts listed above. See
`rules/common/review-boundary.md`.
