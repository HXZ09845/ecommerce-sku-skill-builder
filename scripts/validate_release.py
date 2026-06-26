#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "sku-skill-builder"

REQUIRED_ROOT_FILES = [
    "README.md",
    "README.zh.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".gitignore",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    "assets/workflow-hero.png",
    "case-studies/real-run-a6-office-tea-bar/README.md",
    "case-studies/real-run-a6-office-tea-bar/prompt-before-after.md",
    "case-studies/real-run-a6-office-tea-bar/office-tea-bar-overtime-sku/SKILL.md",
    "case-studies/real-run-a6-office-tea-bar/office-tea-bar-overtime-sku/agents/openai.yaml",
    "case-studies/real-run-a6-office-tea-bar/office-tea-bar-overtime-sku/references/gotchas.md",
    "case-studies/real-run-a6-office-tea-bar/office-tea-bar-overtime-sku/references/product-rules.md",
    "case-studies/real-run-a6-office-tea-bar/office-tea-bar-overtime-sku/references/prompt-plan.md",
    "case-studies/real-run-a6-office-tea-bar/office-tea-bar-overtime-sku/references/trigger-tests.md",
    "case-studies/real-run-a6-office-tea-bar/office-tea-bar-overtime-sku/scripts/validate_case.py",
    "data/source-registry.json",
    "docs/architecture.md",
    "docs/launch-playbook.md",
    "docs/project-status.md",
    "docs/roadmap.md",
    "docs/source-registry.md",
    "docs/why-sku-skills.md",
    "evals/prompt-plan-evals.json",
    "examples/before-after.md",
    "examples/complete-chinese-case.md",
    "examples/demo-asset-manifest.json",
    "examples/demo-product-brief.md",
    "examples/demo-selling-point-map.md",
    "examples/demo-take-review.json",
    "examples/demo-prompt-plan.md",
    "scripts/install_codex_skill.py",
    "scripts/prompt_plan_check.py",
    "scripts/selling_point_check.py",
    "scripts/source_registry_check.py",
    "scripts/structured_data_check.py",
    "schemas/asset-manifest.schema.json",
    "schemas/prompt-plan.schema.json",
    "schemas/source-registry.schema.json",
    "schemas/take-review.schema.json",
    "templates/README.md",
    "templates/asset-manifest-template.json",
    "templates/product-brief-template.md",
    "templates/prompt-plan-template.md",
    "templates/selling-point-map-template.md",
    "templates/take-review-template.json",
    "skills/sku-skill-builder/SKILL.md",
    "skills/sku-skill-builder/agents/openai.yaml",
    "tests/test_prompt_plan_check.py",
    "tests/test_selling_point_check.py",
    "tests/test_structured_data_check.py",
    "tests/test_source_registry_check.py",
]

REQUIRED_REFERENCES = [
    "asset-manifest.md",
    "audio-visual-sync.md",
    "category-questionnaire.md",
    "core-asset-layer.md",
    "creator-onboarding.md",
    "golden-case-abstractions.md",
    "gotchas.md",
    "method-decision-tree.md",
    "migration-map.md",
    "product-rules.md",
    "prompt-plan-format.md",
    "quickstart-template.md",
    "skill-template.md",
    "sku-creator-workflow.md",
    "trigger-tests.md",
    "validate-template.py",
]

PRIVATE_PATTERNS = [
    r"/Users/jerry",
    r"新的all in one",
    r"真行业Meta",
    r"api[_-]?key\s*[:=]",
    r"secret\s*[:=]",
    r"token\s*[:=]",
]

README_REQUIRED_SNIPPETS = [
    "Why Star This",
    "The Problem",
    "Before / After",
    "Complete Chinese Walkthrough",
    "Real Run Case Study",
    "Source Registry",
    "Project Status",
    "templates/",
    "assets/workflow-hero.png",
    "Schemas And Evals",
    "README.zh.md",
    "```mermaid",
    "skills/sku-skill-builder/SKILL.md",
]

README_ZH_REQUIRED_SNIPPETS = [
    "解决什么问题",
    "快速安装",
    "项目成熟度",
    "templates/",
    "真实案例",
    "最终输出 SKU Skill 包样例",
    "Schema / Eval / Test",
    "来源登记",
]


def split_frontmatter(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("frontmatter must start with ---")
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[1:index]), "\n".join(lines[index + 1 :])
    raise ValueError("frontmatter must end with ---")


def value_for(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.*)$", frontmatter, re.MULTILINE)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] in {"'", '"'} and value[-1] == value[0]:
        value = value[1:-1]
    return value


def scan_text_files(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path == Path(__file__).resolve():
            continue
        if path.suffix not in {".md", ".py", ".yaml", ".yml", ".txt"} and path.name not in {
            "LICENSE",
            ".gitignore",
        }:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(ROOT).as_posix()
        for pattern in PRIVATE_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE):
                errors.append(f"{rel}: private or secret-looking pattern `{pattern}`")


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED_ROOT_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")

    for ref in REQUIRED_REFERENCES:
        if not (SKILL / "references" / ref).is_file():
            errors.append(f"missing reference: references/{ref}")

    skill_md = SKILL / "SKILL.md"
    if skill_md.exists():
        try:
            frontmatter, body = split_frontmatter(skill_md.read_text(encoding="utf-8"))
            name = value_for(frontmatter, "name")
            description = value_for(frontmatter, "description")
            if name != "sku-skill-builder":
                errors.append("SKILL.md frontmatter name must be sku-skill-builder")
            if not description or "SKU" not in description:
                errors.append("SKILL.md description should mention SKU trigger scope")
            if len(body) > 14000:
                errors.append("SKILL.md body is large; consider moving more detail to references")
        except Exception as exc:
            errors.append(f"SKILL.md frontmatter error: {exc}")

    readme = ROOT / "README.md"
    if readme.exists():
        readme_text = readme.read_text(encoding="utf-8")
        for snippet in README_REQUIRED_SNIPPETS:
            if snippet not in readme_text:
                errors.append(f"README.md missing public positioning snippet: {snippet}")

    readme_zh = ROOT / "README.zh.md"
    if readme_zh.exists():
        readme_zh_text = readme_zh.read_text(encoding="utf-8")
        for snippet in README_ZH_REQUIRED_SNIPPETS:
            if snippet not in readme_zh_text:
                errors.append(f"README.zh.md missing Chinese positioning snippet: {snippet}")

    scan_text_files(errors)

    if errors:
        print("Release validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Release validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
