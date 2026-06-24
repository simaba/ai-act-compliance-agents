import pytest

from ai_act_compliance_agents.core import RequirementsValidationError, build_traceability_rows


def valid_payload():
    return {
        "feature": "fictional assistant",
        "intended_purpose": "help users with synthetic requests",
        "controls": [
            {
                "id": "CTRL-001",
                "control": "refuse unsafe requests",
                "source": {
                    "framework": "Synthetic safety framework",
                    "reference": "Section 1",
                    "version": "v1",
                },
                "owner": "Fictional Safety Owner",
                "review_status": "verified",
                "evidence": [
                    {"artifact": "Synthetic test report", "location": "tests/synthetic-report.md"}
                ],
            },
            {
                "id": "CTRL-002",
                "control": "mask PII",
                "source": {
                    "framework": "Synthetic privacy framework",
                    "reference": "Section 2",
                    "version": "v1",
                },
                "owner": "Fictional Privacy Owner",
                "review_status": "evidence_pending",
                "evidence": [],
            },
        ],
    }


def test_build_traceability_rows_has_stable_source_versioned_fields():
    rows = build_traceability_rows(valid_payload())

    assert len(rows) == 2
    assert rows[0]["id"] == "CTRL-001"
    assert rows[0]["source_framework"] == "Synthetic safety framework"
    assert rows[0]["source_version"] == "v1"
    assert rows[1]["evidence_status"] == "evidence_pending"


def test_control_without_required_source_owner_or_evidence_is_rejected():
    payload = valid_payload()
    del payload["controls"][0]["owner"]

    with pytest.raises(RequirementsValidationError, match="controls\[1\].owner"):
        build_traceability_rows(payload)


def test_verified_control_requires_evidence():
    payload = valid_payload()
    payload["controls"][0]["evidence"] = []

    with pytest.raises(RequirementsValidationError, match="evidence is required when review_status is verified"):
        build_traceability_rows(payload)


def test_duplicate_control_ids_are_rejected():
    payload = valid_payload()
    payload["controls"][1]["id"] = "CTRL-001"

    with pytest.raises(RequirementsValidationError, match="duplicate control id"):
        build_traceability_rows(payload)
