#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_SNIPPETS = [
    "PROJECT ID:",
    "Continuity Locks",
    "Unit Schedule",
    "Reference Materials",
    "This clip only",
    "Stop when",
    "Take Review",
]

PRIVATE_PATTERNS = [
    r"/Users/",
    r"asset://",
    r"api[_-]?key\s*[:=]",
    r"secret\s*[:=]",
    r"token\s*[:=]",
]


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"missing prompt plan: {path}"]

    text = path.read_text(encoding="utf-8")
    for snippet in REQUIRED_SNIPPETS:
        if snippet not in text:
            errors.append(f"missing required snippet: {snippet}")

    for pattern in PRIVATE_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            errors.append(f"private or secret-looking pattern found: {pattern}")

    if text.count("Stop when") < 3:
        errors.append("expected at least three explicit Stop when endpoints")

    if text.count("This clip only") < 3:
        errors.append("expected at least three explicit This clip only scopes")

    return errors


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if args:
        path = Path(args[0])
    else:
        path = Path(__file__).resolve().parents[1] / "references" / "prompt-plan.md"

    errors = validate(path)
    if errors:
        print("Case validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Case validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
