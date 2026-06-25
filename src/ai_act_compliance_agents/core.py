from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REVIEW_STATUSES = {"planned", "evidence_pending", "in_review", "verified", "blocked"}


class RequirementsValidationError(ValueError):
    """Raised when a traceability input cannot support accountable review."""


def _non_empty_string(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise RequirementsValidationError(f"{field} must be a non-empty string")
    return value.strip()


def _validate_evidence(control_id: str, evidence: Any, status: str) -> list[dict[str, str]]:
    if not isinstance(evidence, list):
        raise RequirementsValidationError(f"controls[{control_id}].evidence must be a list")
    if status == "verified" and not evidence:
        raise RequirementsValidationError(f"controls[{control_id}].evidence is required when review_status is verified")

    normalized: list[dict[str, str]] = []
    for index, item in enumerate(evidence, start=1):
        if not isinstance(item, dict):
            raise RequirementsValidationError(f"controls[{control_id}].evidence[{index}] must be an object")
        normalized.append(
            {
                "artifact": _non_empty_string(item.get("artifact"), f"controls[{control_id}].evidence[{index}].artifact"),
                "location": _non_empty_string(item.get("location"), f"controls[{control_id}].evidence[{index}].location"),
            }
        )
    return normalized


def validate_requirements(payload: dict[str, Any]) -> dict[str, Any]:
    """Validate a compact, reviewable traceability control register."""
    if not isinstance(payload, dict):
        raise RequirementsValidationError("requirements payload must be a JSON object")

    feature = _non_empty_string(payload.get("feature"), "feature")
    intended_purpose = _non_empty_string(payload.get("intended_purpose"), "intended_purpose")
    controls = payload.get("controls")
    if not isinstance(controls, list) or not controls:
        raise RequirementsValidationError("controls must be a non-empty list")

    normalized_controls: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for index, raw_control in enumerate(controls, start=1):
        prefix = f"controls[{index}]"
        if not isinstance(raw_control, dict):
            raise RequirementsValidationError(f"{prefix} must be an object with traceability fields")

        control_id = _non_empty_string(raw_control.get("id"), f"{prefix}.id")
        if control_id in seen_ids:
            raise RequirementsValidationError(f"duplicate control id: {control_id}")
        seen_ids.add(control_id)

        source = raw_control.get("source")
        if not isinstance(source, dict):
            raise RequirementsValidationError(f"{prefix}.source must be an object")
        normalized_source = {
            "framework": _non_empty_string(source.get("framework"), f"{prefix}.source.framework"),
            "reference": _non_empty_string(source.get("reference"), f"{prefix}.source.reference"),
            "version": _non_empty_string(source.get("version"), f"{prefix}.source.version"),
        }

        status = _non_empty_string(raw_control.get("review_status"), f"{prefix}.review_status").lower()
        if status not in REVIEW_STATUSES:
            allowed = ", ".join(sorted(REVIEW_STATUSES))
            raise RequirementsValidationError(f"{prefix}.review_status must be one of: {allowed}")

        normalized_controls.append(
            {
                "id": control_id,
                "control": _non_empty_string(raw_control.get("control"), f"{prefix}.control"),
                "source": normalized_source,
                "owner": _non_empty_string(raw_control.get("owner"), f"{prefix}.owner"),
                "review_status": status,
                "evidence": _validate_evidence(control_id, raw_control.get("evidence"), status),
            }
        )

    return {
        "feature": feature,
        "intended_purpose": intended_purpose,
        "controls": normalized_controls,
    }


def load_requirements(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RequirementsValidationError(f"invalid JSON in {path}: {exc.msg}") from exc
    return validate_requirements(payload)


def build_traceability_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    """Create stable, source-versioned rows for human review and export."""
    normalized = validate_requirements(payload)
    rows: list[dict[str, Any]] = []
    for control in normalized["controls"]:
        rows.append(
            {
                "id": control["id"],
                "feature": normalized["feature"],
                "intended_purpose": normalized["intended_purpose"],
                "control": control["control"],
                "source_framework": control["source"]["framework"],
                "source_reference": control["source"]["reference"],
                "source_version": control["source"]["version"],
                "evidence": control["evidence"],
                "evidence_status": control["review_status"],
                "owner": control["owner"],
            }
        )
    return rows
