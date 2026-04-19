from __future__ import annotations

import json
import sys
from .core import load_requirements, build_traceability_rows


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: ai-act-trace <requirements.json>")
        return 1

    payload = load_requirements(sys.argv[1])
    rows = build_traceability_rows(payload)
    print(json.dumps(rows, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
