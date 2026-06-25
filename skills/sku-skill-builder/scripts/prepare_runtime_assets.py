#!/usr/bin/env python3
"""Create semantic runtime assets from a category skill asset manifest."""

from __future__ import annotations

import argparse
import csv
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    from PIL import Image, ImageOps
except Exception:  # pragma: no cover - optional dependency
    Image = None
    ImageOps = None


IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}
VIDEO_EXTS = {".mp4", ".mov", ".m4v"}


@dataclass
class AssetRow:
    runtime_path: str
    original_path: str
    asset_type: str
    required: str


def parse_markdown_table(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    lines = [line.strip() for line in text.splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        return rows
    header = [cell.strip().strip("`") for cell in lines[0].strip("|").split("|")]
    for line in lines[2:]:
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        if len(cells) != len(header):
            continue
        rows.append(dict(zip(header, cells)))
    return rows


def load_manifest(path: Path) -> list[AssetRow]:
    text = path.read_text(encoding="utf-8")
    rows = []
    for item in parse_markdown_table(text):
        runtime = item.get("runtime_path", "")
        original = item.get("original_path", "")
        if not runtime.startswith("assets/") or not original or "Replace this row" in item.get("notes", ""):
            continue
        rows.append(
            AssetRow(
                runtime_path=runtime,
                original_path=original,
                asset_type=item.get("type", "").lower(),
                required=item.get("required", "").lower(),
            )
        )
    return rows


def run_checked(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def prepare_image(src: Path, dst: Path, long_edge: int, max_kb: int, copy_only: bool) -> str:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not copy_only and is_cmyk_image(src) and shutil.which("sips"):
        return prepare_image_sips_srgb(src, dst, long_edge, max_kb)
    if not copy_only and Image is not None:
        return prepare_image_pillow(src, dst, long_edge, max_kb)
    if copy_only or not shutil.which("sips"):
        shutil.copy2(src, dst)
        return "copied"
    run_checked(["sips", "-Z", str(long_edge), str(src), "--out", str(dst)])
    if dst.stat().st_size <= max_kb * 1024:
        return "resized"
    if dst.suffix.lower() in {".jpg", ".jpeg"}:
        for quality in ["80", "70", "60", "50"]:
            run_checked(["sips", "-s", "formatOptions", quality, str(dst), "--out", str(dst)])
            if dst.stat().st_size <= max_kb * 1024:
                return f"resized+jpeg-q{quality}"
    return "resized-large"


def is_cmyk_image(src: Path) -> bool:
    if Image is None:
        return False
    try:
        with Image.open(src) as image:
            return image.mode == "CMYK"
    except Exception:
        return False


def prepare_image_sips_srgb(src: Path, dst: Path, long_edge: int, max_kb: int) -> str:
    max_bytes = max_kb * 1024
    srgb = "/System/Library/ColorSync/Profiles/sRGB Profile.icc"
    qualities = [85, 80, 75, 70, 65, 60, 55, 50]
    edges = [long_edge, 1600, 1400, 1200, 1000, 850, 720]
    for edge in edges:
        for quality in qualities:
            run_checked([
                "sips",
                "-Z",
                str(edge),
                "-s",
                "format",
                "jpeg",
                "-s",
                "formatOptions",
                str(quality),
                "--matchTo",
                srgb,
                str(src),
                "--out",
                str(dst),
            ])
            if dst.stat().st_size <= max_bytes:
                return f"sips-srgb-{edge}-q{quality}"
    return "sips-srgb-large"


def save_pillow_image(image, dst: Path, quality: int) -> None:
    suffix = dst.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        if image.mode in {"RGBA", "LA", "P"}:
            background = Image.new("RGB", image.size, "white")
            background.paste(image.convert("RGBA"), mask=image.convert("RGBA").split()[-1])
            image = background
        else:
            image = image.convert("RGB")
        image.save(dst, format="JPEG", quality=quality, optimize=True, progressive=True)
        return

    if suffix == ".png":
        png_image = image
        if png_image.mode in {"RGBA", "LA"}:
            png_image = png_image.convert("RGBA").quantize(colors=256, method=Image.Quantize.FASTOCTREE)
        elif png_image.mode != "P":
            png_image = png_image.convert("RGB").quantize(colors=256)
        png_image.save(dst, format="PNG", optimize=True)
        return

    image.save(dst, optimize=True)


def prepare_image_pillow(src: Path, dst: Path, long_edge: int, max_kb: int) -> str:
    max_bytes = max_kb * 1024
    with Image.open(src) as raw:
        image = ImageOps.exif_transpose(raw)
        image.thumbnail((long_edge, long_edge), Image.Resampling.LANCZOS)
        working = image.copy()

    if dst.suffix.lower() in {".jpg", ".jpeg"}:
        for quality in [85, 78, 70, 62, 55, 48, 42]:
            save_pillow_image(working, dst, quality)
            if dst.stat().st_size <= max_bytes:
                return f"pillow-q{quality}"

    scale = 1.0
    for attempt in range(10):
        candidate = working
        if scale < 1.0:
            width = max(320, int(working.width * scale))
            height = max(320, int(working.height * scale))
            candidate = working.resize((width, height), Image.Resampling.LANCZOS)
        save_pillow_image(candidate, dst, 80)
        if dst.stat().st_size <= max_bytes:
            return f"pillow-resize-{candidate.width}x{candidate.height}"
        scale *= 0.82

    return "pillow-large"


def prepare_video(src: Path, dst: Path, transcode: bool) -> str:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not transcode:
        shutil.copy2(src, dst)
        return "copied"
    if not shutil.which("ffmpeg"):
        shutil.copy2(src, dst)
        return "copied-no-ffmpeg"
    vf = "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280"
    run_checked([
        "ffmpeg",
        "-y",
        "-i",
        str(src),
        "-vf",
        vf,
        "-c:v",
        "libx264",
        "-crf",
        "23",
        "-pix_fmt",
        "yuv420p",
        "-an",
        str(dst),
    ])
    return "transcoded"


def prepare_assets(args: argparse.Namespace) -> int:
    skill_dir = args.skill_dir.resolve()
    raw_root = args.raw_root.resolve()
    manifest = (skill_dir / args.manifest).resolve()
    rows = load_manifest(manifest)
    if not rows:
        print(f"No usable asset rows found in {manifest}", file=sys.stderr)
        return 1

    missing = []
    prepared = []
    for row in rows:
        src = raw_root / row.original_path
        dst = skill_dir / row.runtime_path
        if not src.exists():
            if row.required == "yes":
                missing.append(row.original_path)
            continue
        suffix = dst.suffix.lower()
        try:
            if suffix in IMAGE_EXTS:
                action = prepare_image(src, dst, args.image_long_edge, args.image_max_kb, args.copy_only)
            elif suffix in VIDEO_EXTS:
                action = prepare_video(src, dst, args.transcode_videos)
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                action = "copied"
        except subprocess.CalledProcessError as exc:
            print(f"FAILED {row.original_path} -> {row.runtime_path}: {exc}", file=sys.stderr)
            return 1
        prepared.append((row.runtime_path, action, dst.stat().st_size if dst.exists() else 0))

    for runtime, action, size in prepared:
        print(f"{action}: {runtime} ({size} bytes)")
    if missing:
        print("Missing required originals:", file=sys.stderr)
        for item in missing:
            print(f"- {item}", file=sys.stderr)
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-dir", required=True, type=Path)
    parser.add_argument("--raw-root", required=True, type=Path)
    parser.add_argument("--manifest", default="references/asset-manifest.md")
    parser.add_argument("--image-long-edge", type=int, default=1920)
    parser.add_argument("--image-max-kb", type=int, default=500)
    parser.add_argument("--copy-only", action="store_true", help="Copy images without resizing/compression.")
    parser.add_argument("--transcode-videos", action="store_true", help="Transcode videos to 720x1280 H.264.")
    return prepare_assets(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
