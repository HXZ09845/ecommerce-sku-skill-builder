#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

GENERIC_PROOF_PATTERNS = [
    r"^show\s+selling\s+point$",
    r"^display\s+feature$",
    r"^展示卖点$",
    r"^体现卖点$",
    r"^突出卖点$",
]


@dataclass(frozen=True)
class MarkdownTable:
    heading: str
    headers: list[str]
    rows: list[dict[str, str]]


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def parse_markdown_tables(text: str) -> list[MarkdownTable]:
    lines = text.splitlines()
    tables: list[MarkdownTable] = []
    heading = ""
    index = 0

    while index < len(lines):
        line = lines[index].strip()
        if line.startswith("#"):
            heading = line.lstrip("#").strip()
            index += 1
            continue
        if not line.startswith("|") or index + 1 >= len(lines):
            index += 1
            continue
        separator = lines[index + 1].strip()
        if not separator.startswith("|") or "---" not in separator:
            index += 1
            continue

        headers = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        normalized_headers = [normalize(header) for header in headers]
        rows: list[dict[str, str]] = []
        index += 2
        while index < len(lines) and lines[index].strip().startswith("|"):
            cells = [cell.strip().strip("`") for cell in lines[index].strip().strip("|").split("|")]
            row = {
                normalized_headers[column_index]: cells[column_index] if column_index < len(cells) else ""
                for column_index in range(len(normalized_headers))
            }
            rows.append(row)
            index += 1
        tables.append(MarkdownTable(heading=heading, headers=normalized_headers, rows=rows))

    return tables


def first_existing(row: dict[str, str], keys: list[str]) -> str:
    for key in keys:
        value = row.get(key, "").strip()
        if value:
            return value
    return ""


def is_generic_proof(value: str) -> bool:
    lowered = value.strip().lower()
    return any(re.search(pattern, lowered) for pattern in GENERIC_PROOF_PATTERNS)


def collect_unit_ids(tables: list[MarkdownTable]) -> set[str]:
    unit_ids: set[str] = set()
    for table in tables:
        if "unit" not in table.headers:
            continue
        if not any(header in table.headers for header in ["proof_target", "purpose", "goal", "stop_when"]):
            continue
        for row in table.rows:
            unit = row.get("unit", "").strip()
            if unit:
                unit_ids.add(unit)
    return unit_ids


def validate_unit_proof_targets(path: Path, tables: list[MarkdownTable], min_proof_units: int) -> list[str]:
    errors: list[str] = []
    proof_rows: list[tuple[str, str]] = []
    seen_units: set[str] = set()

    for table in tables:
        if "unit" not in table.headers:
            continue
        if not any(header in table.headers for header in ["proof_target", "purpose", "goal"]):
            continue
        for row in table.rows:
            unit = row.get("unit", "").strip()
            proof = first_existing(row, ["proof_target", "purpose", "goal"])
            if not unit:
                errors.append(f"{path}: unit proof table has a row with empty Unit")
                continue
            if unit in seen_units:
                errors.append(f"{path}: duplicate Unit `{unit}` in proof table")
            seen_units.add(unit)
            if not proof:
                errors.append(f"{path}: Unit `{unit}` must have a non-empty proof target")
            elif is_generic_proof(proof):
                errors.append(f"{path}: Unit `{unit}` proof target is too generic: {proof}")
            proof_rows.append((unit, proof))

    if len(proof_rows) < min_proof_units:
        errors.append(f"{path}: expected at least {min_proof_units} Unit proof rows, found {len(proof_rows)}")

    return errors


def validate_selling_point_maps(path: Path, tables: list[MarkdownTable], unit_ids: set[str]) -> list[str]:
    errors: list[str] = []
    found_map = False

    for table in tables:
        if "selling_point" not in table.headers and "卖点" not in table.headers:
            continue
        if not any(header in table.headers for header in ["visual_proof", "proof", "视觉证明"]):
            continue
        found_map = True
        for row_index, row in enumerate(table.rows, start=1):
            selling_point = first_existing(row, ["selling_point", "卖点"])
            proof = first_existing(row, ["visual_proof", "proof", "视觉证明"])
            unit = row.get("unit", "").strip()
            fallback = first_existing(row, ["fallback", "downgrade_route", "降级方案"])
            prefix = f"{path}: selling-point row {row_index}"

            if not selling_point:
                errors.append(f"{prefix} must have a selling point")
            if not proof:
                errors.append(f"{prefix} must have a visual proof")
            elif is_generic_proof(proof):
                errors.append(f"{prefix} visual proof is too generic: {proof}")
            if not unit:
                errors.append(f"{prefix} must bind to a Unit")
            elif unit_ids and unit not in unit_ids:
                errors.append(f"{prefix} references missing Unit `{unit}`")
            if not fallback:
                errors.append(f"{prefix} should include a fallback or downgrade route")

    if not found_map:
        errors.append(f"{path}: missing Selling-Point Proof Map table")

    return errors


def validate_selling_point_file(path: Path, *, require_map: bool, min_proof_units: int) -> list[str]:
    if not path.is_file():
        return [f"missing file: {path}"]
    text = path.read_text(encoding="utf-8")
    tables = parse_markdown_tables(text)
    if not tables:
        return [f"{path}: no markdown tables found"]

    unit_ids = collect_unit_ids(tables)
    errors = validate_unit_proof_targets(path, tables, min_proof_units)
    if require_map:
        errors.extend(validate_selling_point_maps(path, tables, unit_ids))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate selling-point proof coverage in prompt-plan markdown.")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--require-map", action="store_true")
    parser.add_argument("--min-proof-units", type=int, default=1)
    args = parser.parse_args(argv)

    errors: list[str] = []
    for raw_path in args.paths:
        path = raw_path if raw_path.is_absolute() else ROOT / raw_path
        errors.extend(
            validate_selling_point_file(
                path,
                require_map=args.require_map,
                min_proof_units=args.min_proof_units,
            )
        )

    if errors:
        print("Selling-point validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Selling-point validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
