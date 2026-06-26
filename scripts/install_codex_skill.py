#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "sku-skill-builder"
DEFAULT_DEST = Path.home() / ".codex" / "skills" / "sku-skill-builder"


def copy_skill(source: Path, dest: Path, *, force: bool, dry_run: bool) -> None:
    if not source.is_dir():
        raise FileNotFoundError(f"skill source not found: {source}")

    skill_md = source / "SKILL.md"
    if not skill_md.is_file():
        raise FileNotFoundError(f"skill source missing SKILL.md: {skill_md}")

    if dest.exists() and not force:
        raise FileExistsError(
            f"destination already exists: {dest}\n"
            "Re-run with --force to replace it, or pass --dest for another location."
        )

    print(f"Source: {source}")
    print(f"Destination: {dest}")

    if dry_run:
        action = "replace" if dest.exists() else "install"
        print(f"Dry run: would {action} the skill.")
        return

    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(source, dest)
    print("Installed sku-skill-builder.")
    print("Restart Codex, then invoke: $sku-skill-builder")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Install the sku-skill-builder Codex Skill into a local skills directory."
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=DEFAULT_DEST,
        help=f"Destination skill directory. Default: {DEFAULT_DEST}",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace the destination if it already exists.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would happen without writing files.",
    )
    args = parser.parse_args(argv)

    try:
        copy_skill(SOURCE, args.dest.expanduser(), force=args.force, dry_run=args.dry_run)
    except Exception as exc:
        print(f"Install failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
