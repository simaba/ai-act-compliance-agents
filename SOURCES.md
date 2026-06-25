# Public Source Provenance Baseline

This file records public reference points used for illustrative practitioner mapping. It does **not** establish legal interpretation, applicability, certification status, or compliance conclusions.

Before using a reference in a real review, confirm the latest official text, jurisdiction, version, applicability, and internal governance requirements.

| Topic | Primary public source | Baseline version / reference | Public-use note |
|---|---|---|---|
| European Union AI governance | Regulation (EU) 2024/1689 (EU AI Act) | Official EUR-Lex text, checked 2026-06 | Use the official consolidated text and confirm dates of application for the specific obligation. |
| EU data protection | Regulation (EU) 2016/679 (GDPR) | Official EUR-Lex text, checked 2026-06 | Privacy analysis requires context-specific legal review. |
| Functional safety context | ISO 26262 | Standard title/reference only; licensed text is not reproduced | Use authorized copies and qualified functional-safety review. |
| Safety of the intended functionality | ISO/PAS 21448 (SOTIF) | Standard title/reference only; licensed text is not reproduced | Use authorized copies and qualified safety review. |
| AI management systems | ISO/IEC 42001:2023 | Standard title/reference only; licensed text is not reproduced | Use authorized copies and determine applicability independently. |
| AI risk management | ISO/IEC 23894:2023 | Standard title/reference only; licensed text is not reproduced | Treat as a framework reference, not a completed risk assessment. |

## How to cite a source in a control

Use a source object that names the framework, an exact public reference or section, and the version or check date.

```json
{
  "framework": "Regulation (EU) 2024/1689",
  "reference": "Official EUR-Lex text; relevant provision recorded by qualified reviewer",
  "version": "Checked YYYY-MM-DD"
}
```

Do not insert confidential legal memos, employer policies, licensed standard text, internal safety requirements, or non-public source locations into this public repository.

## Review cadence

- Check regulatory sources before any real use and at least every six months for maintained examples.
- Check standard title/version references at least annually.
- Update the date and pull-request notes when a public source is materially changed or replaced.