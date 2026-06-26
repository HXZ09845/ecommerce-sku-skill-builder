#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PRIVATE_PATTERNS = [
    r"/Users/",
    r"asset://",
    r"api[_-]?key\s*[:=]",
    r"secret\s*[:=]",
    r"token\s*[:=]",
]

ASSET_PRIORITIES = {"P0", "P1", "P2", "P3"}
ASSET_STATUS = {"approved", "pending", "deprecated"}
TAKE_VERDICTS = {"keep", "post_fix", "retake", "rewrite", "reject"}


def load_json(path: Path) -> tuple[dict | None, list[str]]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except Exception as exc:
        return None, [f"{path}: could not parse JSON: {exc}"]


def scan_private_patterns(path: Path, data: object) -> list[str]:
    text = json.dumps(data, ensure_ascii=False)
    errors = []
    for pattern in PRIVATE_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            errors.append(f"{path}: private or secret-looking pattern found: {pattern}")
    return errors


def require_string(entry: dict, key: str, prefix: str, errors: list[str]) -> None:
    value = entry.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{prefix}: `{key}` must be a non-empty string")


def validate_asset_manifest(path: Path) -> list[str]:
    data, errors = load_json(path)
    if data is None:
        return errors
    errors.extend(scan_private_patterns(path, data))

    assets = data.get("assets")
    if not isinstance(assets, list) or not assets:
        errors.append(f"{path}: `assets` must be a non-empty list")
        return errors

    seen: set[str] = set()
    for index, asset in enumerate(assets):
        prefix = f"{path}: assets[{index}]"
        if not isinstance(asset, dict):
            errors.append(f"{prefix}: must be an object")
            continue
        for key in ["id", "role", "controls", "does_not_control"]:
            require_string(asset, key, prefix, errors)
        asset_id = asset.get("id")
        if isinstance(asset_id, str):
            if asset_id in seen:
                errors.append(f"{prefix}: duplicate id {asset_id}")
            seen.add(asset_id)
        if asset.get("priority") not in ASSET_PRIORITIES:
            errors.append(f"{prefix}: priority must be one of {sorted(ASSET_PRIORITIES)}")
        if asset.get("status") not in ASSET_STATUS:
            errors.append(f"{prefix}: status must be one of {sorted(ASSET_STATUS)}")

        role = str(asset.get("role", "")).lower()
        does_not_control = str(asset.get("does_not_control", "")).lower()
        if "motion" in role and "identity" not in does_not_control:
            errors.append(f"{prefix}: motion references should say they do not control product identity")
        if "scene" in role and "product identity" not in does_not_control:
            errors.append(f"{prefix}: scene references should say they do not control product identity")

    return errors


def validate_take_review(path: Path) -> list[str]:
    data, errors = load_json(path)
    if data is None:
        return errors
    errors.extend(scan_private_patterns(path, data))

    reviews = data.get("reviews")
    if not isinstance(reviews, list) or not reviews:
        errors.append(f"{path}: `reviews` must be a non-empty list")
        return errors

    for index, review in enumerate(reviews):
        prefix = f"{path}: reviews[{index}]"
        if not isinstance(review, dict):
            errors.append(f"{prefix}: must be an object")
            continue
        for key in ["unit", "observed_end_state", "root_cause", "first_repair_variable"]:
            require_string(review, key, prefix, errors)
        if review.get("verdict") not in TAKE_VERDICTS:
            errors.append(f"{prefix}: verdict must be one of {sorted(TAKE_VERDICTS)}")
        if review.get("verdict") in {"retake", "rewrite", "post_fix"}:
            if not str(review.get("first_repair_variable", "")).strip():
                errors.append(f"{prefix}: repair verdicts require a first_repair_variable")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate structured ecommerce SKU JSON examples.")
    parser.add_argument("--asset-manifest", action="append", type=Path, default=[])
    parser.add_argument("--take-review", action="append", type=Path, default=[])
    args = parser.parse_args(argv)

    errors: list[str] = []
    for raw_path in args.asset_manifest:
        path = raw_path if raw_path.is_absolute() else ROOT / raw_path
        errors.extend(validate_asset_manifest(path))
    for raw_path in args.take_review:
        path = raw_path if raw_path.is_absolute() else ROOT / raw_path
        errors.extend(validate_take_review(path))

    if errors:
        print("Structured data validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Structured data validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
