from ai_act_compliance_agents.core import build_traceability_rows


def test_build_traceability_rows():
    payload = {
        "feature": "assistant",
        "intended_purpose": "help users",
        "controls": ["refuse unsafe requests", "mask PII"],
    }
    rows = build_traceability_rows(payload)
    assert len(rows) == 2
    assert rows[0]["id"] == "CTRL-001"
    assert rows[1]["control"] == "mask PII"
