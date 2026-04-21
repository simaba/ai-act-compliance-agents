#!/usr/bin/env python3
"""
traceability_check.py — Cross-reference auditor for an AI Act technical file.

What this enforces (matches commands/trace.md):

  1. Every conformity-workpaper row marked applicable/partial has at least
     one evidence pointer that resolves to a real file path inside the
     repo (or is a tracked external_certificate / sign_off_memo).
  2. Every Annex IV section in technical-documentation.md has bidirectional
     links: each section either cites a downstream artifact or is itself
     cited by one.
  3. The oversight design covers all five Art. 14(4)(a)-(e) clauses.
  4. Every PMM row has threshold_warn, threshold_critical, cadence, owner,
     and an explicit art_73_trigger (matches schemas/pmm-incident.json).
  5. For Annex I systems, the safety-mapping artifact has bidirectional
     trace tables (AI Act -> FuSa work product AND FuSa -> AI Act) and
     declares 10-year retention precedence.

Outputs:
  - stdout: machine-readable JSON report
  - stderr: human-readable summary
  - exit code: 0 = clean, 1 = warnings only, 2 = at least one failure,
               3 = repo layout could not be parsed at all

Usage:
  python3 scripts/traceability_check.py <repo-root>
  python3 scripts/traceability_check.py <repo-root> --json-only
  python3 scripts/traceability_check.py <repo-root> --strict
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    sys.stderr.write(
        "ERROR: PyYAML is required. Install with: pip install pyyaml\n"
    )
    sys.exit(3)


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
ART_14_CLAUSES = ["a", "b", "c", "d", "e"]
ANNEX_IV_SECTIONS = [
    "general_description",
    "detailed_description",
    "monitoring_validation_control",
    "performance_metrics",
    "risk_management",
    "lifecycle_changes",
    "harmonised_standards",
    "doc_and_pmm",
]


# ---------------------------------------------------------------------------
# Result containers
# ---------------------------------------------------------------------------

@dataclass
class Finding:
    severity: str          # "fail" | "warn" | "info"
    check: str
    artifact: str
    detail: str

    def to_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "check": self.check,
            "artifact": self.artifact,
            "detail": self.detail,
        }


@dataclass
class Report:
    findings: list[Finding] = field(default_factory=list)
    artifacts_seen: dict[str, list[str]] = field(default_factory=dict)

    def add(self, severity: str, check: str, artifact: str, detail: str) -> None:
        self.findings.append(Finding(severity, check, artifact, detail))

    @property
    def fails(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "fail"]

    @property
    def warns(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "warn"]

    def to_dict(self) -> dict[str, Any]:
        return {
            "summary": {
                "total_findings": len(self.findings),
                "fails": len(self.fails),
                "warns": len(self.warns),
            },
            "artifacts_seen": self.artifacts_seen,
            "findings": [f.to_dict() for f in self.findings],
        }


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def split_frontmatter(text: str) -> tuple[dict[str, Any], str] | None:
    """Return (frontmatter_dict, body) or None if no YAML frontmatter."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        data = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None
    if not isinstance(data, dict):
        return None
    return data, m.group(2)


def load_yaml_or_md(path: Path) -> dict[str, Any] | None:
    """Load YAML directly, or YAML frontmatter from a markdown file."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if path.suffix.lower() in (".yaml", ".yml"):
        try:
            data = yaml.safe_load(text)
        except yaml.YAMLError:
            return None
        return data if isinstance(data, dict) else None
    fm = split_frontmatter(text)
    return fm[0] if fm else None


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def find_artifacts(root: Path) -> dict[str, list[Path]]:
    """Locate all artifacts the trace check cares about."""
    examples = root / "examples"
    if not examples.exists():
        # Also accept artifacts in repo root if no examples dir.
        examples = root

    out = {
        "classifications": [],
        "workpapers": [],
        "tech_files": [],
        "pmm_plans": [],
        "oversight_designs": [],
        "safety_traces": [],
    }

    for p in examples.rglob("*.md"):
        fm = load_yaml_or_md(p)
        if not fm:
            continue
        if "classification" in fm and "intended_purpose" in fm:
            out["classifications"].append(p)
        if "annex_iv_section" in fm or "technical_file" in str(p):
            out["tech_files"].append(p)
        if "oversight_design" in fm or "art_14_coverage" in fm:
            out["oversight_designs"].append(p)
        if "safety_trace" in fm or fm.get("kind") == "safety-trace":
            out["safety_traces"].append(p)

    for p in examples.rglob("*.yaml"):
        fm = load_yaml_or_md(p)
        if not fm:
            continue
        if "rows" in fm and any("article" in r for r in (fm.get("rows") or []) if isinstance(r, dict)):
            out["workpapers"].append(p)
        if "rows" in fm and any("art_73_trigger" in r for r in (fm.get("rows") or []) if isinstance(r, dict)):
            out["pmm_plans"].append(p)

    return out


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_workpaper_evidence(path: Path, root: Path, report: Report) -> None:
    fm = load_yaml_or_md(path) or {}
    rows = fm.get("rows", [])
    if not rows:
        report.add("warn", "workpaper.empty", str(path),
                   "Workpaper has no rows. A live conformity assessment must enumerate Chapter III.")
        return

    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            continue
        rid = row.get("id", f"row[{i}]")
        applicability = row.get("applicability")
        if applicability in ("applicable", "partial"):
            ev = row.get("evidence") or []
            if not ev:
                report.add("fail", "workpaper.evidence_missing", str(path),
                           f"{rid} ({row.get('article')}) is {applicability} but has no evidence.")
                continue
            for j, e in enumerate(ev):
                if not isinstance(e, dict):
                    continue
                ref = e.get("ref", "")
                etype = e.get("type", "")
                if etype in ("external_certificate", "sign_off_memo"):
                    continue
                if not ref:
                    report.add("fail", "workpaper.evidence_unref", str(path),
                               f"{rid} evidence[{j}] has empty ref.")
                    continue
                if ref.startswith(("http://", "https://", "s3://")):
                    continue
                # Resolve relative refs against repo root.
                candidate = (root / ref).resolve() if not ref.startswith("/") else Path(ref)
                if not candidate.exists():
                    report.add("warn", "workpaper.evidence_unresolved", str(path),
                               f"{rid} evidence ref '{ref}' does not resolve to a file under repo root.")
        if row.get("status") == "open" and not row.get("gap"):
            report.add("fail", "workpaper.open_no_gap", str(path),
                       f"{rid} status=open but no gap field. Schema forbids this.")
        if row.get("status") == "open" and not row.get("due"):
            report.add("fail", "workpaper.open_no_due", str(path),
                       f"{rid} status=open but no due date.")


def check_annex_iv_bidirectional(path: Path, report: Report) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        report.add("fail", "tech_file.unreadable", str(path), "Cannot read file.")
        return
    sections_present = [s for s in ANNEX_IV_SECTIONS if re.search(rf"\b{s}\b", text, re.I)]
    sections_missing = [s for s in ANNEX_IV_SECTIONS if s not in sections_present]
    if sections_missing:
        report.add("warn", "tech_file.annex_iv_incomplete", str(path),
                   f"Annex IV sections not detected: {', '.join(sections_missing)}.")
    # Each section should reference at least one downstream artifact path
    # or be referenced by another section. We approximate by requiring at
    # least one ./<path> or repo-relative pointer per section header.
    section_blocks = re.split(r"\n#+\s+", text)
    weak = 0
    for block in section_blocks[1:]:
        if not re.search(r"\(\./|\(\.\./|\b(rules/|skills/|examples/|schemas/|scripts/)", block):
            weak += 1
    if weak > 2:
        report.add("warn", "tech_file.weak_links", str(path),
                   f"{weak} sections contain no repo-relative pointers. Bidirectional traceability is fragile.")


def check_oversight_design(path: Path, report: Report) -> None:
    fm = load_yaml_or_md(path) or {}
    coverage = fm.get("art_14_coverage") or {}
    if not isinstance(coverage, dict):
        report.add("fail", "oversight.no_coverage", str(path),
                   "art_14_coverage missing or not a mapping.")
        return
    for clause in ART_14_CLAUSES:
        v = coverage.get(clause)
        if not v or not isinstance(v, str) or len(v) < 10:
            report.add("fail", "oversight.art_14_clause_missing", str(path),
                       f"Art. 14(4)({clause}) coverage is missing or under-specified (<10 chars).")
    overseer = fm.get("named_overseer") or fm.get("overseer")
    if not overseer or "@" not in str(overseer):
        report.add("fail", "oversight.no_named_human", str(path),
                   "Named overseer (email) is required by rules/common/name-the-human-overseer.md.")


def check_pmm(path: Path, report: Report) -> None:
    fm = load_yaml_or_md(path) or {}
    rows = fm.get("rows", [])
    if not rows:
        report.add("warn", "pmm.empty", str(path), "PMM plan has no rows.")
        return
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            continue
        rid = row.get("id", f"row[{i}]")
        for required in ("threshold_warn", "threshold_critical", "cadence",
                         "owner", "art_73_trigger", "escalation_warn",
                         "escalation_critical"):
            if not row.get(required):
                report.add("fail", "pmm.field_missing", str(path),
                           f"{rid} missing required field '{required}'.")
        owner = row.get("owner", "")
        if owner and "@" not in owner:
            report.add("fail", "pmm.owner_not_email", str(path),
                       f"{rid} owner '{owner}' is not an email. Schema requires format=email.")
        for field_name in ("escalation_warn", "escalation_critical"):
            v = row.get(field_name, "")
            if v and v.strip().lower() in ("investigate", "investigate.", "look into it", "review"):
                report.add("fail", "pmm.escalation_not_action", str(path),
                           f"{rid} {field_name}='{v}' is not a defined response. "
                           "See rules/common/evidence-not-opinion.md.")


def check_safety_trace(path: Path, classifications: list[Path],
                       report: Report) -> None:
    fm = load_yaml_or_md(path) or {}
    annex_i_present = False
    for c in classifications:
        cfm = load_yaml_or_md(c) or {}
        if "I" in (cfm.get("annex_i_check") or "").upper():
            annex_i_present = True
            break
    if not annex_i_present:
        report.add("info", "safety_trace.optional", str(path),
                   "No Annex I system detected; FuSa/SOTIF mapping is optional.")
        return
    fwd = fm.get("ai_act_to_fusa") or fm.get("forward_trace")
    rev = fm.get("fusa_to_ai_act") or fm.get("reverse_trace")
    if not fwd:
        report.add("fail", "safety_trace.no_forward", str(path),
                   "Annex I system requires AI Act -> FuSa/SOTIF forward trace.")
    if not rev:
        report.add("fail", "safety_trace.no_reverse", str(path),
                   "Annex I system requires FuSa/SOTIF -> AI Act reverse trace.")
    retention = fm.get("retention_precedence") or fm.get("retention_until")
    if not retention or "10" not in str(retention):
        report.add("fail", "safety_trace.retention_precedence",
                   str(path),
                   "Annex I + AI Act retention precedence (10y under Art. 18) not declared.")


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def run(root: Path, strict: bool, json_only: bool) -> int:
    if not root.is_dir():
        sys.stderr.write(f"ERROR: {root} is not a directory.\n")
        return 3

    artifacts = find_artifacts(root)
    report = Report()
    report.artifacts_seen = {k: [str(p) for p in v] for k, v in artifacts.items()}

    if not any(artifacts.values()):
        report.add("warn", "discovery.empty", str(root),
                   "No AI Act artifacts found. Nothing to trace.")

    for wp in artifacts["workpapers"]:
        check_workpaper_evidence(wp, root, report)
    for tf in artifacts["tech_files"]:
        check_annex_iv_bidirectional(tf, report)
    for od in artifacts["oversight_designs"]:
        check_oversight_design(od, report)
    for pmm in artifacts["pmm_plans"]:
        check_pmm(pmm, report)
    for st in artifacts["safety_traces"]:
        check_safety_trace(st, artifacts["classifications"], report)

    # Output
    payload = report.to_dict()
    sys.stdout.write(json.dumps(payload, indent=2) + "\n")
    if not json_only:
        s = payload["summary"]
        sys.stderr.write(
            f"\nTraceability check: {s['total_findings']} finding(s) "
            f"({s['fails']} fail, {s['warns']} warn).\n"
        )
        for f in report.findings:
            sys.stderr.write(
                f"  [{f.severity.upper()}] {f.check} :: {f.artifact}\n"
                f"      {f.detail}\n"
            )

    if report.fails:
        return 2
    if strict and report.warns:
        return 2
    if report.warns:
        return 1
    return 0


def main() -> None:
    p = argparse.ArgumentParser(
        description="Cross-reference auditor for an AI Act technical file."
    )
    p.add_argument("root", type=Path, help="Repo root containing examples/.")
    p.add_argument("--strict", action="store_true",
                   help="Treat warnings as failures (exit 2 on any warn).")
    p.add_argument("--json-only", action="store_true",
                   help="Suppress human-readable stderr summary.")
    args = p.parse_args()
    sys.exit(run(args.root, args.strict, args.json_only))


if __name__ == "__main__":
    main()
