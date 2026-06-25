# Traceability Register Input

`ai-act-trace` accepts a JSON control register for creating review-ready traceability rows.

This is a drafting and evidence-organization format. It is not a legal, safety, cybersecurity, privacy, or compliance determination.

## Required top-level fields

```json
{
  "feature": "Fictional feature name",
  "intended_purpose": "What the fictional system is intended to do",
  "controls": []
}
```

## Required control fields

Each control must be an object with a stable ID, a source record, an accountable owner, a review status, and evidence records.

```json
{
  "id": "CTRL-SAF-001",
  "control": "Describe the fictional control and expected behavior.",
  "source": {
    "framework": "Named framework or practitioner mapping",
    "reference": "Section, article, or source reference",
    "version": "Version or checked date"
  },
  "owner": "Fictional accountable role",
  "review_status": "evidence_pending",
  "evidence": []
}
```

Allowed review statuses are:

- `planned`
- `evidence_pending`
- `in_review`
- `verified`
- `blocked`

A control marked `verified` must include at least one evidence object with `artifact` and `location` fields. The utility rejects duplicate control IDs and missing source, owner, or review metadata.

## Migration from the earlier example shape

Earlier prototypes accepted a list of strings such as:

```json
{
  "controls": ["refuse unsafe requests", "mask direct identifiers"]
}
```

That shape cannot support source provenance, ownership, evidence, or review state. Convert every string into a control object before using the current CLI.

## Public-safety guidance

Use fictional or fully sanitized feature names, controls, evidence locations, and source notes in this repository. Do not commit real safety analyses, conformity conclusions, confidential requirements, supplier information, or internal release evidence.
