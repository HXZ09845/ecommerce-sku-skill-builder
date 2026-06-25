#!/usr/bin/env python3
"""
{产品名} SKU Skill validator template.

Usage:
  python3 validate_{english_module}.py prompt-plan.md
  python3 validate_{english_module}.py prompt-plan-directory/

Keep common checks here, then add product-specific checks from product-rules.md
and repeated bad cases.

Industry checks (U32 Unit Scope Contract):
  U32a  A-class missing unit goal (本段只做一件事 / Unit goal)
  U32b  A-class missing end condition (结束条件 / End condition)
  U32c  A-class uses segmented second-mark timeline — warn unless SKU documents exception
"""

PY_TRACKED_VERSION = "V2.3"

import re
import sys
from pathlib import Path


class ValidationResult:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, code, message):
        self.errors.append(f"[ERROR {code}] {message}")

    def warn(self, code, message):
        self.warnings.append(f"[WARN  {code}] {message}")

    def ok(self):
        return not self.errors

    def summary(self):
        lines = []
        if self.errors:
            lines.append(f"\n{'=' * 60}")
            lines.append(f"  ERRORS: {len(self.errors)}")
            lines.append(f"{'=' * 60}")
            lines.extend(self.errors)
        if self.warnings:
            lines.append(f"\n{'=' * 60}")
            lines.append(f"  WARNINGS: {len(self.warnings)}")
            lines.append(f"{'=' * 60}")
            lines.extend(self.warnings)
        if not lines:
            lines.append("ALL CHECKS PASSED")
        return "\n".join(lines)


PLACEHOLDER_PATTERNS = [
    r"\{待提供[^}]*\}",
    r"\{[^}]*产品名[^}]*\}",
    r"\bplaceholder\b",
    r"待确认",
]

HIGH_RISK_TEXT_PATTERNS = [
    (r"屏幕显示.{0,8}\d", "screen exact number"),
    (r"(按钮|按键|标签|贴纸).{0,8}(文字|字样|写着)", "readable button/label text"),
    (r"(logo|Logo|LOGO).{0,8}(写着|文字|清晰)", "logo text request"),
]

VAGUE_SCENE_PATTERNS = [
    (r"(咖啡|办公|户外|室内|街道|车厢|厨房|居家)散景", "vague bokeh scene"),
    (r"(summer vibe|coffee vibe|office vibe)", "abstract scene vibe"),
]

B_FORBIDDEN_PATTERNS = [
    (r"\d+\.?\d*-\d+\.?\d*秒", "timeline in B-class prompt"),
    (r"(镜头|相机).{0,10}(推|拉|摇|移|跟|变焦)", "camera movement description"),
    (r"(手指|手).{0,12}(按|拧|拔|拉|倒|打开|合上|旋开)", "manual action description"),
]

# A-class timeline exceptions — SKU may add product-specific markers
TIMELINE_EXEMPT_MARKERS = [
    "通用画面",
    "universal clip",
    "bridge beat",
    "桥段",
    "锚定例外",
]


def has_unit_goal(text):
    return bool(
        re.search(r"本段只做一件事", text)
        or re.search(r"(?i)unit goal\s*[:：]", text)
        or re.search(r"(?i)this unit (only|proves)", text)
    )


def has_end_condition(text):
    return bool(
        re.search(r"结束条件", text)
        or re.search(r"(?i)end condition\s*[:：]", text)
    )


def has_per_second_timeline(text):
    return bool(re.search(r"(?:^|\n)\s*\d+-\d+\s*秒", text))


def is_timeline_exempt(text):
    return any(marker in text for marker in TIMELINE_EXEMPT_MARKERS)


def has_video_ref(text):
    return bool(re.search(r"@视频\d+", text))


def is_a_class_section(text):
    return not has_video_ref(text)


def has_prompt_material_block(text):
    if "【素材说明】" in text or re.search(r"(?m)^\s*素材说明[:：]?\s*$", text):
        return True
    return bool(
        re.search(
            r"(?im)^(?!#{1,6}\s)\s*(Reference Materials|Material Purpose|Material-purpose block)\s*[:：]?\s*$",
            text,
        )
    )


def validate_section(text, label):
    result = ValidationResult()
    prefix = f"[{label}] "

    for pattern in PLACEHOLDER_PATTERNS:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            result.error("C0", f"{prefix}unresolved placeholder: {match.group(0)}")

    img_refs = sorted({int(n) for n in re.findall(r"@图片(\d+)", text)})
    vid_refs = sorted({int(n) for n in re.findall(r"@视频(\d+)", text)})
    if img_refs and img_refs != list(range(1, max(img_refs) + 1)):
        result.error("C1", f"{prefix}@图片 numbering is not continuous: {img_refs}")
    if vid_refs and vid_refs != list(range(1, max(vid_refs) + 1)):
        result.error("C1", f"{prefix}@视频 numbering is not continuous: {vid_refs}")

    if len(text) > 1600:
        result.warn("C2", f"{prefix}section length {len(text)} may dilute instruction priority")

    if re.search(r"@(?:图片|视频)\d+", text) and not has_prompt_material_block(text):
        result.error("C3", f"{prefix}references appear without an in-prompt material-purpose block")

    for pattern, desc in HIGH_RISK_TEXT_PATTERNS:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            result.warn("C4", f"{prefix}high-risk text request ({desc}): {match.group(0)}")

    for pattern, desc in VAGUE_SCENE_PATTERNS:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            result.warn("C5", f"{prefix}vague scene wording ({desc}); replace with concrete visual entities: {match.group(0)}")

    if has_video_ref(text):
        if "严格复刻" not in text and "reference video" not in text.lower() and "参考视频" not in text:
            result.warn("B1", f"{prefix}B-class section lacks reference-video priority statement")
        for pattern, desc in B_FORBIDDEN_PATTERNS:
            match = re.search(pattern, text)
            if match:
                result.warn("B2", f"{prefix}possible B-class over-description ({desc}): {match.group(0)}")

    if re.search(r"A-外|A-out|合盖|闭合", text) and re.search(r"A-内|A-in|开盖|敞口|内部|拆分", text):
        result.warn("S1", f"{prefix}possible mixed product states; verify A-out/A-in compatibility")

    # U32 — Unit Scope Contract (standard A-class)
    if is_a_class_section(text) and re.search(r"@(?:图片|视频)\d+", text):
        if not is_timeline_exempt(text):
            if not has_unit_goal(text):
                result.warn("U32a", f"{prefix}A-class prompt missing unit goal (本段只做一件事 / Unit goal)")
            if not has_end_condition(text):
                result.warn("U32b", f"{prefix}A-class prompt missing end condition (结束条件 / End condition)")
            if has_per_second_timeline(text):
                result.warn(
                    "U32c",
                    f"{prefix}A-class uses segmented second-mark timeline; "
                    f"prefer unit goal + action flow + end condition (U32)",
                )

    # Product-specific checks go here. Examples:
    # - forbidden component count
    # - wrong water direction
    # - wrong wearable/body relation
    # - missing fixed-space anchor
    # - missing required material pack

    return result


def extract_prompt_sections(text, filepath):
    """Extract ### Prompt blocks under ## U* headers from prompt-plan markdown."""
    path = Path(filepath)
    if path.suffix == ".md" and "### Prompt" in text:
        sections = []
        for match in re.finditer(
            r"(?ms)^## (U[^\n]+)\n(?:(?!^## ).)*^### Prompt\s*\n(?P<prompt>.+?)(?=^## |\Z)",
            text,
        ):
            prompt = match.group("prompt").strip()
            unit = match.group(1).strip()
            if len(prompt) >= 20:
                sections.append((prompt, f"{path.name}:{unit}"))
        if sections:
            return sections

    parts = [s.strip() for s in re.split(r"\n(?=##\s|###\s|---\s*$)", text, flags=re.MULTILINE) if s.strip()]
    if len(parts) <= 1:
        return [(text.strip(), path.name)]
    return [(s, f"{path.name}:section{i}") for i, s in enumerate(parts, start=1) if len(s) >= 20]


def validate_document(text, label):
    result = ValidationResult()
    prefix = f"[{label}] "

    if "核心资产" not in text and "Core Asset" not in text:
        result.warn("D1", f"{prefix}missing core asset inventory")
    if "TS 风险" not in text and "TS risk" not in text:
        result.warn("D2", f"{prefix}missing TS risk declaration")
    if (
        "生产原型" not in text
        and "production_archetype" not in text
        and "production archetype" not in text.lower()
    ):
        result.warn("D3", f"{prefix}missing production archetype declaration")
    if (
        "黄金" not in text
        and "golden" not in text.lower()
        and "Case family" not in text
    ):
        result.warn("D4", f"{prefix}missing golden case abstraction record")
    if "文案关键词" in text and "文案到画面" not in text and "copy-to-visual" not in text.lower():
        result.warn("D5", f"{prefix}copy mapping appears without post-prompt visual audit")
    if (
        "脚本文案" in text
        and "脚本-Unit-素材编排" not in text
        and "audio-visual" not in text.lower()
        and "音画同步" not in text
    ):
        result.warn("D9", f"{prefix}script appears without audio-visual sync arrangement")
    if "脚本文案" in text and "文案语义抽取" not in text and "keyword/entity" not in text.lower():
        result.warn("D12", f"{prefix}script appears without keyword/entity extraction")
    if ("Unit 详情" in text or "Unit Info" in text) and "音画同步核对" not in text and "sync audit" not in text.lower():
        result.warn("D10", f"{prefix}unit prompts appear without post-prompt audio-visual sync audit")
    if ("A/B" in text or "A-out" in text or "A-in" in text) and "确认" not in text and "creator" not in text.lower():
        result.warn("D11", f"{prefix}A/B rows appear without creator confirmation marker")
    home_documents = "~/" + "Documents"
    home_new_all = "~/" + "新的all"
    local_path_pattern = r"(" + "/" + r"Users/|" + re.escape(home_documents) + r"|" + re.escape(home_new_all) + r")"
    if re.search(local_path_pattern, text):
        result.warn("D6", f"{prefix}local absolute path appears in runtime-facing text")
    external_skill_terms = r"(creator package|parent package|external package|category meta|meta skill|golden case skill|golden skill)"
    if re.search(r"(read|load|use)\s+.*" + external_skill_terms, text, re.IGNORECASE):
        result.warn("D7", f"{prefix}possible external skill dependency wording")
    if re.search(r"(读取|加载|调用|依赖).*(母\s*Skill|品类\s*Meta|行业通用|黄金\s*Skill|其他\s*Skill)", text):
        result.warn("D8", f"{prefix}possible external skill dependency wording")

    return result


def read_targets(target):
    path = Path(target)
    if path.is_dir():
        return sorted(path.glob("*.md")) + sorted(path.glob("*.txt"))
    if path.is_file():
        return [path]
    raise FileNotFoundError(target)


def main(argv):
    if len(argv) < 2:
        print("Usage: python3 validate_{english_module}.py <prompt-plan-file-or-dir>")
        return 2

    all_ok = True
    for file_path in read_targets(argv[1]):
        text = file_path.read_text(encoding="utf-8")
        document_result = validate_document(text, file_path.name)
        output = document_result.summary()
        if output != "ALL CHECKS PASSED":
            print(f"\n--- {file_path.name}:document ---")
            print(output)
        sections = extract_prompt_sections(text, file_path)
        for section, label in sections:
            if len(section) < 20:
                continue
            result = validate_section(section, label)
            if not result.ok():
                all_ok = False
            output = result.summary()
            if output != "ALL CHECKS PASSED":
                print(f"\n--- {label} ---")
                print(output)

    if all_ok:
        print("\nALL VALIDATION CHECKS PASSED")
        return 0
    print("\nVALIDATION FAILED")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
