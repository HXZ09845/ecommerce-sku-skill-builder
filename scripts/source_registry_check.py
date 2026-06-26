#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "data" / "source-registry.json"

REQUIRED_ENTRY_KEYS = {
    "id",
    "title",
    "type",
    "path",
    "privacy_level",
    "status",
    "includes",
    "excludes",
    "verified_on",
}

ALLOWED_PRIVACY_LEVELS = {"public", "anonymized"}
ALLOWED_STATUS = {"included", "pending", "deprecated"}
ANONYMIZED_TYPES = {"anonymized_real_run", "anonymized_output_package"}

PRIVATE_PATTERNS = [
    r"/Users/",
    r"asset://",
    r"api[_-]?key\s*[:=]",
    r"secret\s*[:=]",
    r"token\s*[:=]",
]

SENSITIVE_EXCLUSIONS = {
    "raw product photos",
    "raw action videos",
    "local paths",
    "asset IDs",
}


def should_scan_text(path: Path) -> bool:
    return path.suffix.lower() in {".md", ".py", ".json", ".yaml", ".yml", ".txt"} or path.name in {
        "LICENSE",
        ".gitignore",
    }


def load_registry(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def registry_base(path: Path) -> Path:
    try:
        if path.resolve() == DEFAULT_REGISTRY.resolve():
            return ROOT
    except FileNotFoundError:
        pass
    return path.resolve().parent


def validate_registry(path: Path = DEFAULT_REGISTRY) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"missing source registry: {path}"]

    try:
        data = load_registry(path)
    except Exception as exc:
        return [f"could not parse source registry: {exc}"]

    base = registry_base(path)

    if not data.get("version"):
        errors.append("registry missing version")
    if not data.get("last_updated"):
        errors.append("registry missing last_updated")
    if not data.get("policy"):
        errors.append("registry missing policy")

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("registry sources must be a non-empty list")
        return errors

    seen_ids: set[str] = set()
    for index, entry in enumerate(sources):
        prefix = f"sources[{index}]"
        missing = REQUIRED_ENTRY_KEYS - set(entry)
        for key in sorted(missing):
            errors.append(f"{prefix}: missing key {key}")
        if missing:
            continue

        source_id = str(entry["id"])
        if source_id in seen_ids:
            errors.append(f"{prefix}: duplicate id {source_id}")
        seen_ids.add(source_id)

        privacy = entry["privacy_level"]
        if privacy not in ALLOWED_PRIVACY_LEVELS:
            errors.append(f"{source_id}: invalid privacy_level {privacy}")

        status = entry["status"]
        if status not in ALLOWED_STATUS:
            errors.append(f"{source_id}: invalid status {status}")

        includes = entry["includes"]
        excludes = entry["excludes"]
        if not isinstance(includes, list) or not includes:
            errors.append(f"{source_id}: includes must be a non-empty list")
        if not isinstance(excludes, list) or not excludes:
            errors.append(f"{source_id}: excludes must be a non-empty list")

        entry_type = entry["type"]
        if entry_type in ANONYMIZED_TYPES and privacy != "anonymized":
            errors.append(f"{source_id}: anonymized type must use privacy_level=anonymized")

        if entry_type in ANONYMIZED_TYPES:
            exclusions_text = "\n".join(str(item) for item in excludes)
            for required in SENSITIVE_EXCLUSIONS:
                if required not in exclusions_text:
                    errors.append(f"{source_id}: anonymized entry should exclude `{required}`")

        source_path = base / entry["path"]
        if not source_path.exists():
            errors.append(f"{source_id}: path does not exist: {entry['path']}")
            continue

        if source_path.is_file() and source_path.stat().st_size == 0:
            errors.append(f"{source_id}: registered file is empty: {entry['path']}")

        if source_path.is_file() and should_scan_text(source_path):
            text = source_path.read_text(encoding="utf-8", errors="ignore")
            for pattern in PRIVATE_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    errors.append(f"{source_id}: private or secret-looking pattern in {entry['path']}: {pattern}")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate public source registry entries.")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args(argv)

    errors = validate_registry(args.registry)
    if errors:
        print("Source registry validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Source registry validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
