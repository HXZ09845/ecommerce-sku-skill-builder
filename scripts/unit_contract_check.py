#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LOCAL_ROOT = Path(__file__).resolve().parents[1]
if str(LOCAL_ROOT) not in sys.path:
    sys.path.insert(0, str(LOCAL_ROOT))

from scripts.selling_point_check import ROOT, parse_markdown_tables


VALID_UNIT_TYPES = {"A", "A-in", "A-out", "A+B", "B"}


def normalize_unit_type(value: str) -> str:
    compact = value.strip()
    aliases = {
        "a": "A",
        "a_in": "A-in",
        "a-in": "A-in",
        "ain": "A-in",
        "a_out": "A-out",
        "a-out": "A-out",
        "aout": "A-out",
        "a+b": "A+B",
        "b": "B",
    }
    return aliases.get(compact.lower().replace(" ", ""), compact)


def section_for_unit(text: str, unit: str) -> str:
    pattern = re.compile(rf"^#+\s+.*{re.escape(unit)}.*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return text
    next_heading = re.search(r"^##\s+", text[match.end() :], re.MULTILINE)
    if not next_heading:
        return text[match.start() :]
    return text[match.start() : match.end() + next_heading.start()]


def validate_unit_contract_file(path: Path) -> list[str]:
    if not path.is_file():
        return [f"missing file: {path}"]

    text = path.read_text(encoding="utf-8")
    tables = parse_markdown_tables(text)
    errors: list[str] = []
    seen_units: set[str] = set()
    unit_rows = []

    for table in tables:
        if "unit" not in table.headers:
            continue
        type_key = "a_b_type" if "a_b_type" in table.headers else "type" if "type" in table.headers else ""
        if not type_key:
            continue
        for row in table.rows:
            unit = row.get("unit", "").strip()
            unit_type = normalize_unit_type(row.get(type_key, ""))
            if not unit:
                errors.append(f"{path}: unit table row has empty Unit")
                continue
            if unit in seen_units:
                errors.append(f"{path}: duplicate Unit `{unit}`")
            seen_units.add(unit)
            if unit_type not in VALID_UNIT_TYPES:
                errors.append(f"{path}: Unit `{unit}` has invalid A/B type `{row.get(type_key, '')}`")
            if "product_state" in row and not row.get("product_state", "").strip():
                errors.append(f"{path}: Unit `{unit}` must declare product state")
            if "stop_when" in row and not row.get("stop_when", "").strip():
                errors.append(f"{path}: Unit `{unit}` must declare Stop when")
            unit_rows.append((unit, unit_type))

    if not unit_rows:
        errors.append(f"{path}: no Unit table with A/B type found")

    for unit, unit_type in unit_rows:
        if unit_type != "B":
            continue
        unit_section = section_for_unit(text, unit)
        if not re.search(r"@Video\d*", unit_section, re.IGNORECASE):
            errors.append(f"{path}: B-class Unit `{unit}` must reference an action video such as @Video1")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Unit A/B contracts in prompt-plan markdown.")
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args(argv)

    errors: list[str] = []
    for raw_path in args.paths:
        path = raw_path if raw_path.is_absolute() else ROOT / raw_path
        errors.extend(validate_unit_contract_file(path))

    if errors:
        print("Unit contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Unit contract validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
