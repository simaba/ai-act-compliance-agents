#!/usr/bin/env python3
"""
classify_cli.py — interactive AI Act risk-classification questionnaire and validator.

Walks the user through the five-gate decision (Art. 5 → Annex I → Annex III →
Art. 50 → minimal-risk default), produces a draft classification memo with
YAML frontmatter that validates against schemas/ai-system-classification.json,
and surfaces open questions for legal review.

Usage:
  python scripts/classify_cli.py interview --out examples/classification/<slug>.md
  python scripts/classify_cli.py validate examples/classification/<slug>.md
  python scripts/classify_cli.py validate-workpaper examples/conformity/<slug>-workpaper.md

Exit codes:
  0 — success / valid
  1 — usage error
  2 — validation failure (file is non-conforming)
  3 — schema or runtime error
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # PyYAML
except ImportError:
    sys.stderr.write("Missing dependency 'PyYAML'. Install with: pip install pyyaml jsonschema\n")
    sys.exit(3)

try:
    import jsonschema
    from jsonschema import Draft202012Validator
except ImportError:
    sys.stderr.write("Missing dependency 'jsonschema'. Install with: pip install jsonschema\n")
    sys.exit(3)


REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = REPO_ROOT / "schemas"
CLASSIFICATION_SCHEMA = SCHEMAS_DIR / "ai-system-classification.json"
CONFORMITY_SCHEMA = SCHEMAS_DIR / "conformity-assessment-row.json"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_schema(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fp:
        return json.load(fp)


def _coerce_dates(obj: Any) -> Any:
    """PyYAML auto-parses ISO date literals into datetime.date.
    The JSON-Schema 'format: date' validator wants strings — coerce back."""
    if isinstance(obj, dict):
        return {k: _coerce_dates(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_coerce_dates(v) for v in obj]
    if isinstance(obj, _dt.datetime):
        return obj.isoformat()
    if isinstance(obj, _dt.date):
        return obj.isoformat()
    return obj


def _split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---"):
        raise ValueError("File does not start with YAML frontmatter (---).")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Could not locate closing '---' for YAML frontmatter.")
    fm = yaml.safe_load(parts[1]) or {}
    body = parts[2].lstrip("\n")
    return _coerce_dates(fm), body


def _ask(prompt: str, *, multiline: bool = False, required: bool = True) -> str:
    sys.stderr.write(f"\n{prompt}\n")
    if multiline:
        sys.stderr.write("(end with a single '.' on a line)\n> ")
        lines: list[str] = []
        for raw in sys.stdin:
            if raw.rstrip() == ".":
                break
            lines.append(raw.rstrip("\n"))
        value = "\n".join(lines).strip()
    else:
        sys.stderr.write("> ")
        value = sys.stdin.readline().strip()
    if required and not value:
        sys.stderr.write("Required. Try again.\n")
        return _ask(prompt, multiline=multiline, required=required)
    return value


def _ask_list(prompt: str, *, min_items: int) -> list[str]:
    sys.stderr.write(f"\n{prompt}\n(one per line; end with a single '.' on a line)\n")
    items: list[str] = []
    for raw in sys.stdin:
        if raw.rstrip() == ".":
            break
        v = raw.strip()
        if v:
            items.append(v)
    if len(items) < min_items:
        sys.stderr.write(f"Need at least {min_items} entries. Try again.\n")
        return _ask_list(prompt, min_items=min_items)
    return items


def _today() -> str:
    return _dt.date.today().isoformat()


def _months_from_today(months: int) -> str:
    today = _dt.date.today()
    year = today.year + (today.month - 1 + months) // 12
    month = (today.month - 1 + months) % 12 + 1
    day = min(today.day, 28)
    return _dt.date(year, month, day).isoformat()


# ---------------------------------------------------------------------------
# Interview
# ---------------------------------------------------------------------------

def _walk_gates(intended_purpose: str, foreseeable_misuse: list[str]) -> dict[str, Any]:
    sys.stderr.write("\nGate 1 — Art. 5 (prohibited)\n")
    art5 = _ask("Does any Art. 5 prohibition match the intended purpose or foreseeable misuse? (yes/no + reason)")
    if art5.lower().startswith("y"):
        return {"classification": "prohibited", "art_5_check": art5,
                "annex_i_check": "n/a — system is prohibited", "annex_iii_check": "n/a — system is prohibited"}

    sys.stderr.write("\nGate 2 — Annex I (regulated product safety component)\n")
    annex_i = _ask("Is the AI a safety component of a product regulated under Annex I AND subject to third-party conformity assessment? (yes/no + reason)")
    if annex_i.lower().startswith("y"):
        return {"classification": "high-risk", "art_5_check": art5,
                "annex_i_check": annex_i, "annex_iii_check": "n/a — already high-risk via Annex I"}

    sys.stderr.write("\nGate 3 — Annex III (eight standalone areas)\n")
    annex_iii = _ask("Does the intended purpose fall in one of the 8 Annex III areas? (yes/no + which area + reason)")
    if annex_iii.lower().startswith("y"):
        carveout = _ask("Does the Art. 6(3) carve-out apply (narrow procedural / improving prior human work / pattern detection / preparatory)? (yes + evidence | no)")
        if carveout.lower().startswith("y"):
            sys.stderr.write("Art. 6(3) carve-out invoked — flag for legal review. Defaulting to high-risk in draft.\n")
        return {"classification": "high-risk", "art_5_check": art5,
                "annex_i_check": annex_i, "annex_iii_check": f"{annex_iii} | carveout: {carveout}"}

    sys.stderr.write("\nGate 4 — Art. 50 (limited-risk transparency)\n")
    art50 = _ask("Does the system interact with humans, generate synthetic content, infer emotion, or do biometric categorization? (yes/no + reason)")
    if art50.lower().startswith("y"):
        return {"classification": "limited-risk", "art_5_check": art5,
                "annex_i_check": annex_i, "annex_iii_check": annex_iii}

    return {"classification": "minimal-risk", "art_5_check": art5,
            "annex_i_check": annex_i, "annex_iii_check": annex_iii}


def _interview(out_path: Path) -> int:
    sys.stderr.write("AI Act Risk Classification — interview mode\n")
    sys.stderr.write("Press Ctrl+C at any time to abort.\n")

    system_id = _ask("System ID (e.g., AI-SYS-0001)")
    if not re.match(r"^AI-SYS-\d{4,}$", system_id):
        sys.stderr.write("Invalid ID format; expected AI-SYS-NNNN.\n")
        return 1

    system_name = _ask("System name")
    provider = _ask("Provider organization")
    intended_purpose = _ask("Intended purpose (one testable sentence: what decision, for whom, with what consequence if wrong?)", multiline=True)
    deployment_context = _ask("Deployment context (sector, geography, product line)")
    user_population = _ask("User population")
    foreseeable_misuse = _ask_list("Foreseeable misuse — at least 3 entries", min_items=3)
    classified_by = _ask("Your email (classified_by)")
    reviewed_by = _ask("Named legal reviewer email (reviewed_by)")

    gate_result = _walk_gates(intended_purpose, foreseeable_misuse)

    triggers = _ask_list("Substantial-modification triggers that would invalidate this classification (≥1)", min_items=1)

    fm = {
        "id": system_id,
        "system_name": system_name,
        "provider": provider,
        "intended_purpose": intended_purpose,
        "deployment_context": deployment_context,
        "user_population": user_population,
        "foreseeable_misuse": foreseeable_misuse,
        "classification": gate_result["classification"],
        "articles_cited": ["Art. 3(1)", "Art. 3(12)", "Art. 5", "Art. 6", "Annex I", "Annex III", "Art. 50"],
        "annex_iii_check": gate_result["annex_iii_check"],
        "annex_i_check": gate_result["annex_i_check"],
        "art_5_check": gate_result["art_5_check"],
        "classified_by": classified_by,
        "reviewed_by": reviewed_by,
        "classification_date": _today(),
        "review_due": _months_from_today(6),
        "status": "draft",
        "substantial_modification_triggers": triggers,
        "documentation_version": "0.1",
    }

    body = (
        "## Intended Purpose\n\n"
        f"{intended_purpose}\n\n"
        "## Gate Walk\n\n"
        f"- **Art. 5 (prohibited)**: {gate_result['art_5_check']}\n"
        f"- **Annex I (safety component)**: {gate_result['annex_i_check']}\n"
        f"- **Annex III (eight areas)**: {gate_result['annex_iii_check']}\n"
        f"- **Result**: **{gate_result['classification']}**\n\n"
        "## Re-classification Triggers\n\n"
        + "\n".join(f"- {t}" for t in triggers) + "\n\n"
        "## Open Questions for Legal\n\n"
        "- TBD — populate during legal review.\n\n"
        "---\n\n"
        "*This memo is a structured technical opinion drafted with assistance from "
        "the `risk-classifier` agent. It is not legal advice. Sign-off requires the "
        "named legal reviewer.*\n"
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + "---\n\n" + body,
        encoding="utf-8",
    )

    schema = _load_schema(CLASSIFICATION_SCHEMA)
    Draft202012Validator.check_schema(schema)
    errors = sorted(Draft202012Validator(schema).iter_errors(_coerce_dates(fm)), key=lambda e: e.path)
    if errors:
        sys.stderr.write(f"\nDraft saved to {out_path} but does NOT validate:\n")
        for e in errors:
            sys.stderr.write(f"  - {'/'.join(map(str, e.path)) or '<root>'}: {e.message}\n")
        return 2

    sys.stderr.write(f"\nDraft saved and validated: {out_path}\n")
    return 0


# ---------------------------------------------------------------------------
# Validate
# ---------------------------------------------------------------------------

def _validate_classification(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    fm, _ = _split_frontmatter(text)
    schema = _load_schema(CLASSIFICATION_SCHEMA)
    Draft202012Validator.check_schema(schema)
    errors = sorted(Draft202012Validator(schema).iter_errors(fm), key=lambda e: e.path)
    if errors:
        sys.stderr.write(f"FAIL: {path}\n")
        for e in errors:
            sys.stderr.write(f"  - {'/'.join(map(str, e.path)) or '<root>'}: {e.message}\n")
        return 2
    sys.stderr.write(f"OK: {path}\n")
    return 0


def _validate_workpaper(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    fm, body = _split_frontmatter(text)
    rows = fm.get("rows") or []
    if not rows:
        sys.stderr.write(f"FAIL: {path} — no 'rows' in frontmatter (workpaper must use rows: list).\n")
        return 2

    schema = _load_schema(CONFORMITY_SCHEMA)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    failed = 0
    for idx, row in enumerate(rows):
        errors = sorted(validator.iter_errors(_coerce_dates(row)), key=lambda e: e.path)
        if errors:
            failed += 1
            sys.stderr.write(f"FAIL row[{idx}] (id={row.get('id', '?')}):\n")
            for e in errors:
                sys.stderr.write(f"  - {'/'.join(map(str, e.path)) or '<root>'}: {e.message}\n")

    if failed:
        sys.stderr.write(f"{failed} of {len(rows)} rows failed validation.\n")
        return 2

    sys.stderr.write(f"OK: {path} ({len(rows)} rows valid)\n")
    return 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_interview = sub.add_parser("interview", help="Run the classification interview and produce a draft memo.")
    p_interview.add_argument("--out", required=True, type=Path)

    p_v = sub.add_parser("validate", help="Validate a classification memo against the schema.")
    p_v.add_argument("path", type=Path)

    p_w = sub.add_parser("validate-workpaper", help="Validate a conformity workpaper's rows against the row schema.")
    p_w.add_argument("path", type=Path)

    args = parser.parse_args(argv)

    try:
        if args.cmd == "interview":
            return _interview(args.out)
        if args.cmd == "validate":
            return _validate_classification(args.path)
        if args.cmd == "validate-workpaper":
            return _validate_workpaper(args.path)
    except (FileNotFoundError, ValueError, yaml.YAMLError, json.JSONDecodeError) as exc:
        sys.stderr.write(f"ERROR: {exc}\n")
        return 3

    return 1


if __name__ == "__main__":
    sys.exit(main())
