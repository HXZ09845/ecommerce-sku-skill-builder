#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PRIVATE_PATTERNS = [
    r"/Users/",
    r"asset://",
    r"api[_-]?key\s*[:=]",
    r"secret\s*[:=]",
    r"token\s*[:=]",
]

UNIT_ROW_RE = re.compile(r"^\|\s*(U[-A-Za-z0-9_]*)\s*\|", re.MULTILINE)
REF_ROW_RE = re.compile(r"^\|\s*`?@(?:Image|Video|Audio|图片|视频|音频)[^|`]*`?\s*\|", re.MULTILINE)


@dataclass(frozen=True)
class Expectations:
    min_units: int = 1
    min_reference_rows: int = 1
    min_clip_scopes: int = 1
    min_stop_when: int = 1
    requires_take_review: bool = True


def count_unit_rows(text: str) -> int:
    units = {match.group(1) for match in UNIT_ROW_RE.finditer(text)}
    return len(units)


def count_reference_rows(text: str) -> int:
    return len(REF_ROW_RE.findall(text))


def has_reference_role_contract(text: str) -> bool:
    lowered = text.lower()
    return (
        "controls" in lowered
        and ("does_not_control" in lowered or "does not control" in lowered or "must not transfer" in lowered)
    )


def has_ab_decision(text: str) -> bool:
    return bool(re.search(r"\|\s*(A|A-in|A-out|A\+B|B)\s*\|", text))


def validate_prompt_plan(path: Path, expectations: Expectations) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"missing prompt plan: {path}"]

    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else str(path)

    for pattern in PRIVATE_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            errors.append(f"{rel}: private or secret-looking pattern found: {pattern}")

    unit_count = count_unit_rows(text)
    if unit_count < expectations.min_units:
        errors.append(f"{rel}: expected at least {expectations.min_units} Unit rows, found {unit_count}")

    ref_count = count_reference_rows(text)
    if ref_count < expectations.min_reference_rows:
        errors.append(
            f"{rel}: expected at least {expectations.min_reference_rows} reference rows, found {ref_count}"
        )

    clip_scopes = text.count("This clip only")
    if clip_scopes < expectations.min_clip_scopes:
        errors.append(
            f"{rel}: expected at least {expectations.min_clip_scopes} `This clip only` scopes, found {clip_scopes}"
        )

    stop_when = text.count("Stop when")
    if stop_when < expectations.min_stop_when:
        errors.append(
            f"{rel}: expected at least {expectations.min_stop_when} `Stop when` endpoints, found {stop_when}"
        )

    if not has_reference_role_contract(text):
        errors.append(f"{rel}: missing reference role contract with controls and does_not_control")

    if not has_ab_decision(text):
        errors.append(f"{rel}: missing A/B type decision in a Unit table")

    if expectations.requires_take_review and "Take Review" not in text:
        errors.append(f"{rel}: missing Take Review section")

    return errors


def load_eval_cases(path: Path) -> list[tuple[str, Path, Expectations]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    cases = []
    for item in data.get("cases", []):
        case_id = item["id"]
        prompt_path = ROOT / item["path"]
        expectations = Expectations(
            min_units=int(item.get("min_units", 1)),
            min_reference_rows=int(item.get("min_reference_rows", 1)),
            min_clip_scopes=int(item.get("min_clip_scopes", 1)),
            min_stop_when=int(item.get("min_stop_when", 1)),
            requires_take_review=bool(item.get("requires_take_review", True)),
        )
        cases.append((case_id, prompt_path, expectations))
    return cases


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate ecommerce SKU prompt-plan markdown files.")
    parser.add_argument("paths", nargs="*", type=Path, help="Prompt-plan markdown files to validate.")
    parser.add_argument("--evals", type=Path, help="Eval JSON file with prompt-plan cases.")
    parser.add_argument("--min-units", type=int, default=1)
    parser.add_argument("--min-reference-rows", type=int, default=1)
    parser.add_argument("--min-clip-scopes", type=int, default=1)
    parser.add_argument("--min-stop-when", type=int, default=1)
    parser.add_argument("--no-take-review", action="store_true")
    args = parser.parse_args(argv)

    errors: list[str] = []

    if args.evals:
        for case_id, path, expectations in load_eval_cases(args.evals):
            case_errors = validate_prompt_plan(path, expectations)
            errors.extend(f"{case_id}: {error}" for error in case_errors)

    expectations = Expectations(
        min_units=args.min_units,
        min_reference_rows=args.min_reference_rows,
        min_clip_scopes=args.min_clip_scopes,
        min_stop_when=args.min_stop_when,
        requires_take_review=not args.no_take_review,
    )
    for raw_path in args.paths:
        path = raw_path if raw_path.is_absolute() else ROOT / raw_path
        errors.extend(validate_prompt_plan(path, expectations))

    if errors:
        print("Prompt-plan validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Prompt-plan validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
