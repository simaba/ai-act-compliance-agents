from __future__ import annotations

import json
from pathlib import Path


def load_requirements(path: str | Path) -> dict:
    path = Path(path)
    return json.loads(path.read_text(encoding="utf-8"))


def build_traceability_rows(payload: dict) -> list[dict]:
    feature = payload.get("feature", "unknown feature")
    intended = payload.get("intended_purpose", "")
    controls = payload.get("controls", [])
    rows = []
    for idx, control in enumerate(controls, start=1):
        rows.append(
            {
                "id": f"CTRL-{idx:03d}",
                "feature": feature,
                "intended_purpose": intended,
                "control": control,
                "evidence_status": "TBD",
                "owner": "TBD",
            }
        )
    return rows
