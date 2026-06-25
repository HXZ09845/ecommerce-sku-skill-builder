#!/usr/bin/env python3
"""
Scaffold a standard Codex SKU skill package.

Usage:
  python3 scaffold_category_skill.py --number 27 --name "净水器" --english "water-purifier" --method "直出"

The CLI keeps the historical arguments, but the output is no longer an old
three-file package. It creates SKILL.md, references/, scripts/, assets/, and
agents/openai.yaml.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

METHODS = {
    "直出": "direct-generation",
    "实拍换景": "direct-generation",
    "参考视频": "direct-generation",
    "口播直出": "direct-generation",
    "宫格": "grid-tvc",
    "TVC": "grid-tvc",
}


def slugify(value: str) -> str:
    value = value.strip().lower().replace("_", "-")
    value = re.sub(r"[^a-z0-9-]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "sku-skill"


def read_template(name: str) -> str:
    return (ROOT / "references" / name).read_text(encoding="utf-8")


def write(path: Path, content: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    if executable:
        os.chmod(path, 0o755)


def render(content: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        content = content.replace("{" + key + "}", value)
    return content


def build_skill_md(values: dict[str, str]) -> str:
    return f"""---
name: {values["skill_name"]}
description: "{values["product_name"]} SKU short-video generation skill for ecommerce AIGC workflows. Use when creating prompt-plans, selecting materials, validating A/B Units, or generating videos for {values["product_name"]}, {values["category_name"]}, {values["trigger_terms"]}."
---

# {values["product_name"]} SKU Skill

Use this skill to create and review prompt-plans for {values["product_name"]}. This skill is self-contained for this SKU; read only the required references inside this package before writing or validating prompts.

## Required Reading

1. `references/product-rules.md` — product structure, state matrix, selling-point proof, A/B rules, and SKU-specific hard rules.
2. `references/core-asset-layer.md` — production archetype routing plus core identity/logo, environment, rhythm, prompt, submission, and TS-risk extraction.
3. `references/audio-visual-sync.md` — script-to-Unit arrangement, copy/proof/material binding, A/B confirmation, and sync audit.
4. `references/asset-manifest.md` — approved and pending runtime assets with semantic roles.
5. `references/prompt-plan-format.md` — required prompt-plan output.
6. `references/gotchas.md` — common failures and forbidden outputs.
7. `references/trigger-tests.md` — routing examples.

## Workflow

1. Confirm script mode, target ratio, platform, and material version: test stage uses 1-2 scripts for initial visual validation; production stage batch-processes scripts after the Skill has passed.
2. Extract script keywords/entities and map copy lines to concrete visuals, selling points, and visual proof.
3. Choose the production archetype before prompt writing: large fixed A+B, small movable A+B, or pure A non-deforming/wearable.
4. Record which built-in golden case abstraction family informed hallucination and A/B rules.
5. Build the core asset and TS risk table.
6. Build the script-Unit-material arrangement before prompt writing.
7. Select references from the manifest by semantic role and product state.
8. Classify each unit as A, A-out, A-in, or B; follow creator-confirmed A/B decisions when provided.
8.5. If the script scene is not the product's default/primary scene, complete scene narrative derivation before writing any A-class prompt: scene micro-actions, scene-specific props, emotional arc, and Q1-Q6 self-check.
9. Write every referenced Unit prompt with an in-prompt `【素材说明】` / `Reference Materials` block before the visual instruction.
10. For every standard A-class prompt, write a Unit Scope Contract: unit goal, one action-flow paragraph, and end condition. Do not use segmented second-by-second prompt prose.
11. Write the prompt-plan using the required format.
12. Run `scripts/validate_{values["english_module"]}.py` on the finished plan.
13. Record warnings, accepted downgrades, sync issues, and bad cases.
14. Confirm the plan uses only this package's rules, manifest, assets, and validator.

## Quality Gates

- Every core selling point maps to a visual proof route.
- Production archetype is recorded with a reason.
- Golden case abstraction family for hallucination and A/B rules is recorded.
- Core asset inventory and TS risk table are present before prompts.
- Script keyword/entity extraction, script-Unit-material arrangement, and audio-visual sync audit are present.
- A/B key rows are creator-confirmed or marked pending.
- Every core selling point has a creator-confirmed visual proof route and one-by-one material dialogue test record.
- Every reference has a role, state, and `does_not_control` note.
- Every Unit prompt using `@图片` or `@视频` includes a concise in-prompt material-purpose block for each reference.
- A-out/A-in/B states do not conflict.
- B Units use action videos according to product rules.
- High-risk text/logo/UI regions are not rewritten as exact prompt text.
- Scene-adaptive narrative quality gate: all A-class Units pass Q1-Q6; non-default scenes have Scene Narrative Adaptation Table.
- Unit Scope Contract: all standard A-class prompts have unit goal, action flow, and end condition; no segmented second-by-second prompt prose.
- No runtime instruction points outside this package.
- Validator has 0 errors before handoff.
"""


def build_product_rules(values: dict[str, str]) -> str:
    return f"""# Product Rules - {values["product_name"]}

> Scaffolded {values["date"]}. Fill this file from confirmed product understanding, old-case mining, selling-point proof mapping, approved materials, and bad-case regression.

## 1. Product Understanding

- Product: {values["product_name"]}
- Category: {values["category_name"]}
- Method: {values["method_label"]}
- Target user:
- Main scenes:
- Core video identity:
- Ratio/model defaults:

## 1.5 Self-Contained Runtime

- Required reading must be files in this package.
- Applied industry/category/case-family rules have been rewritten into this package.
- Runtime assets must live in `assets/` or be marked `pending` in `asset-manifest.md`.
- No required local absolute paths.

## 2. Component And State Matrix

| Component | Default state | Result state | Process action | Risk | A/B |
|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending |

## 3. Selling Point To Visual Proof

Run this dialogue test before marking a selling point row as OK:

| selling_point | candidate_real_shot_reference | proof_target | material_controls | material_must_not_control | A/B_or_state_judgment | creator_experience_judgment | conclusion |
|---|---|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending | pending | pending |

| Selling point | Proof target | Visual proof | A/B | Required materials | Forbidden materials | Downgrade |
|---|---|---|:---:|---|---|---|
| pending | pending | pending | pending | pending | pending | pending |

## 3.5 Audio-Visual Sync

Script mode: test stage / production stage / pending

| copy line | explicit words | implied scene/emotion | actual physical environment | required concrete visuals | optional material type | forbidden vague wording | notes |
|---|---|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending | pending | pending |

| Script | Unit | copy range | explicit/implied keywords | actual environment | concrete visual entities | proof target | visual action/keyframe | product state | A/B | material mix | duration/rhythm | forbidden material/state | TS risk | downgrade | confirmation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |

| Script | copy line | Unit | explicit/implied keywords | actual environment | required visual/action/entity | prompt coverage | materials used | A/B | risk | fix |
|---|---|---|---|---|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |

| Script | status | prompt_plan_path | material_arrangement_path | scripts/Units | A/B counts | missing materials | validation | video_task_status |
|---|---|---|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending | pending | pending | pending |

## 4. Core Asset And TS Risk

| Case family | Archetype fit | Abstracted rule | Applies to this SKU? | Keep / rewrite / reject | Destination |
|---|---|---|:---:|---|---|
| pending | pending | pending | pending | pending | pending |

| Product part / action | Likely hallucination | Abstracted evidence family | A/B decision | Material strategy | Prompt safeguard | Validator / gotchas hook |
|---|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending | pending |

| Product signal | Production archetype | A/B shape | Prompt learning focus | Hallucination guard | Bad-case prevention |
|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending |

| Asset layer | What to extract | Source | Controls | Must not control | TS risk | Rule destination |
|---|---|---|---|---|---|---|
| identity/logo/text | pending | pending | pending | pending | pending | pending |
| structure/state | pending | pending | pending | pending | pending | pending |
| environment | pending | pending | pending | pending | pending | pending |
| rhythm | pending | pending | pending | pending | pending | pending |
| action | pending | pending | pending | pending | pending | pending |
| copy/audio | pending | pending | pending | pending | pending | pending |
| prompt form | pending | pending | pending | pending | pending | pending |
| submission/API | pending | pending | pending | pending | pending | pending |
| bad cases | pending | pending | pending | pending | pending | pending |

| Unit | copy range | proof target | state | A/B | duration/rhythm | TS risk | downgrade |
|---|---|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending | pending | pending |

## 5. A/B/A-Out/A-In Rules

| Unit type | Use when | Material recipe | Forbidden |
|---|---|---|---|
| A | Product state does not change | P0 identity/space + P1 proof + P2 narrative as needed | state conflicts |
| A-out | Product remains external/default/closed | external/default-state refs only | internal/open-state refs |
| A-in | Product is already open/unfolded/internal/result state | matching result-state refs only | closed/default refs unless explicitly narrowed |
| B | Product state changes and a reference video controls the process | exactly one action video by default + compatible anchors | prompt-written action timeline |

## 6. Material Role Rules

| Role | Meaning | This SKU examples |
|---|---|---|
| P0 | identity/space anchor | pending |
| P1 | selling-point proof | pending |
| P2 | narrative support | pending |

## 7. Product-Specific Hard Rules

| ID | Rule | Why |
|---|---|---|
| P1 | pending | pending |

## 8. Prompt Rules

- Style:
- Space anchoring:
- Audio-visual sync policy:
- Reference material-purpose block policy:
- Unit Scope Contract: every standard A-class prompt includes unit goal + action flow + end condition; no segmented second-by-second prompt prose.
- Text/logo/UI policy:
- Action difficulty policy:
- State consistency policy:

## 9. Review Checklist

- [ ] Script keyword/entity extraction complete.
- [ ] Copy-to-visual mapping complete.
- [ ] Production archetype selected and justified.
- [ ] Golden case abstraction applied or current-run gap documented.
- [ ] Core asset inventory and TS risk table complete.
- [ ] Script-Unit-material arrangement complete.
- [ ] Audio-visual sync audit complete.
- [ ] A/B key rows confirmed by creator or marked pending.
- [ ] Component states are compatible per unit.
- [ ] Material roles declared.
- [ ] Every referenced Unit prompt contains `【素材说明】` / `Reference Materials` before the visual instruction.
- [ ] High-risk text handled.
- [ ] Scene-adaptive narrative quality gate: all A-class Units pass Q1-Q6; non-default scenes have Scene Narrative Adaptation Table.
- [ ] Unit Scope Contract: all standard A-class prompts have unit goal, action flow, and end condition; no segmented second-by-second prompt prose.
- [ ] Self-contained handoff check passed: no runtime instruction points outside this package.
- [ ] Validator run recorded.

## 10. Version History

| Version | Date | Change | Impacted prompt-plans | Refresh status |
|---|---|---|---|---|
| V1.0 | {values["date"]} | Initial scaffold | none | n/a |
"""


def build_asset_manifest(values: dict[str, str]) -> str:
    return f"""# Asset Manifest - {values["product_name"]}

Approved material version: pending

| runtime_path | original_path | type | required | semantic_role | product_state | status | notes |
|---|---|---|:---:|---|---|---|---|
| pending | pending | image | yes | product_full / P0 | pending | pending | Locks product identity after creator approval |
"""


def build_audio_visual_sync(values: dict[str, str]) -> str:
    return f"""# Audio-Visual Sync - {values["product_name"]}

Use this before prompt writing. The script, selling-point proof, Unit split, material roles, A/B decision, and prompt must be arranged together.

Priority:

```text
creator A/B judgment > script copy / voiceover > concrete visual entity > selling-point proof target > approved material reality > prompt wording
```

## Script Mode

| Mode | Input | Rule |
|---|---|---|
| Test stage | usually 1-2 test scripts | Create first SKU Skill draft, test visual output, collect feedback, and update rules |
| Production stage | batch scripts after the SKU Skill passes | Batch-generate prompt-plans, material arrangements, validation records, and video task inputs |

## Pre-Prompt Arrangement

| copy line | explicit words | implied scene/emotion | actual physical environment | required concrete visuals | optional material type | forbidden vague wording | notes |
|---|---|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending | pending | pending |

| Script | Unit | copy range | explicit/implied keywords | actual environment | concrete visual entities | proof target | visual action/keyframe | product state | A/B | material mix | duration/rhythm | forbidden material/state | TS risk | downgrade | confirmation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |

Rules:

- Every meaningful copy beat maps to one Unit, an intentional omission, or an approved downgrade.
- Every visible keyword maps to a concrete visual entity, environment, prop, user role, or approved omission.
- Every Unit has one dominant proof target.
- A/B key rows are creator-confirmed or marked pending.
- Materials are selected by semantic role and product state; A, B, and A+B mixed material use is allowed when roles do not conflict.
- If exact sync creates fragile action, text, state, or swap-back risk, split the Unit or downgrade with creator approval.

## Prompt Material-Purpose Block

Every Unit prompt that uses `@图片` or `@视频` must copy a short material-purpose block into the prompt before the visual instruction. Explain each reference separately: what it is, P0/P1/P2 or B role, what it controls, what it must not control, and which selling point or copy beat it supports.

```text
【素材说明】
@图片1：P0，what material this is，controls product identity/version/space/body relation，does not control unsupported scene/action，supports selling point or copy beat
@图片2：P1，what material this is，proves selling point/component/state，does not control unrelated scene/action，supports selling point or copy beat
@图片3：P2，what material this is，controls scene/person/prop/mood，does not control product state/action，supports visual keyword/entity
@视频1：B，what action video this is，controls action/rhythm/viewpoint/state change，does not control background/person/other details，supports action beat

本段只做一件事：[standard A-class unit's single proof target; for B-class, state reference-video priority instead].
动作流：[standard A-class one-paragraph motion/camera/emotion flow, no concrete second marks or segmented second-by-second timeline; for B-class, do not rewrite the reference video's action timeline].
结束条件：[standard A-class stop frame; for B-class, end on the reference video's action result].

【画面要求】（legacy — prefer the three lines above for standard A-class）
...
```

## Post-Prompt Audit

| Script | copy line | Unit | explicit/implied keywords | actual environment | required visual/action/entity | prompt coverage | materials used | A/B | risk | fix |
|---|---|---|---|---|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |

## Batch Production

| Script | status | prompt_plan_path | material_arrangement_path | scripts/Units | A/B counts | missing materials | validation | video_task_status |
|---|---|---|---|---|---|---|---|---|
| pending | pending | pending | pending | pending | pending | pending | pending | pending |
"""


def build_gotchas(values: dict[str, str]) -> str:
    return f"""# Gotchas - {values["product_name"]}

| Failure | Why it happens | Prevention | Validator |
|---|---|---|---|
| Product state conflict | References mix incompatible product states | Separate A-out/A-in/B states in product-rules and manifest | pending |
| A/B row not creator-confirmed | The default classifier may not match current production judgment | Mark key rows for creator confirmation and follow the creator's decision | pending |
| Reference explanation missing in prompt | The material table is correct, but the video model treats every reference as a full-scene instruction | Put a concise `【素材说明】` / `Reference Materials` block inside each Unit prompt | pending |
| A prompt uses segmented second-by-second timeline | Timing prose dilutes attention and hides the Unit's proof target | Use unit goal + one action-flow paragraph + end condition; document exceptions without concrete second marks | pending |
| A prompt lacks unit goal or end condition | The model drifts across multiple proof targets in one clip | Declare `本段只做一件事` and `结束条件` in every standard A-class prompt | pending |
| Script keyword has no concrete visual | Copy says summer/coffee/office/car but prompt only uses vague mood words | Extract concrete visible entities before Unit prompts | pending |
| Audio-visual mismatch | Copy, material, Unit, and prompt prove different things | Complete the script-Unit-material arrangement and post-prompt sync audit | pending |
| Production batch lacks per-script plans | Batch scripts are treated as one generic prompt-plan | Create one prompt-plan and material arrangement per script | pending |
| Text/logo hallucination | Prompt asks model to recreate readable text | Treat text as visual texture; exact claims go to VO/post | pending |
"""


def build_trigger_tests(values: dict[str, str]) -> str:
    return f"""# Trigger Tests - {values["product_name"]}

## Should Trigger

- "帮我做{values["product_name"]} prompt-plan"
- "{values["product_name"]}素材怎么选"
- "检查{values["product_name"]} A/B Unit"
- "用 ${values["skill_name"]} 生成脚本素材编排"

## Should Not Trigger

- "做另一个没有{values["product_name"]}素材的新产品"
- "只写普通文案，不做视频生成"
- "总结卖点，不生成 prompt-plan"
"""


def build_openai_yaml(values: dict[str, str]) -> str:
    return f"""interface:
  display_name: "{values["product_name"]}"
  short_description: "{values["product_name"]} SKU 视频生成 Skill"
  default_prompt: "Use ${values["skill_name"]} to create a prompt-plan: read product rules and asset manifest, choose the production archetype, map copy to visual proof, classify A/B Units, then validate with scripts/validate_{values["english_module"]}.py."
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a standard Codex SKU skill package")
    parser.add_argument("--number", type=int, required=True, help="Business/source number, e.g. 27")
    parser.add_argument("--name", required=True, help="Chinese product/category/source name")
    parser.add_argument("--english", required=True, help="English slug/module name")
    parser.add_argument("--method", required=True, choices=sorted(METHODS), help="Generation method label")
    parser.add_argument("--output", default=None, help="Output directory")
    args = parser.parse_args()

    method_kind = METHODS[args.method]
    if method_kind == "grid-tvc":
        method_label = "grid-tvc (user explicitly requested TVC/grid)"
    else:
        method_label = "direct-generation"

    english_slug = slugify(args.english)
    english_module = english_slug.replace("-", "_")
    output_dir = Path(args.output) if args.output else ROOT.parent
    folder = output_dir / english_slug

    if folder.exists():
        print(f"Folder already exists: {folder}")
        print("Remove it manually or choose a different --output.")
        return 1

    values = {
        "number": str(args.number),
        "product_name": args.name,
        "category_name": args.name,
        "english_name": english_slug,
        "english_module": english_module,
        "skill_name": english_slug,
        "method_label": method_label,
        "trigger_terms": f"{args.name}, {english_slug}",
        "date": date.today().isoformat(),
    }

    (folder / "references").mkdir(parents=True)
    (folder / "scripts").mkdir()
    (folder / "assets").mkdir()
    (folder / "agents").mkdir()

    write(folder / "SKILL.md", build_skill_md(values))
    write(folder / "agents" / "openai.yaml", build_openai_yaml(values))
    write(folder / "references" / "product-rules.md", build_product_rules(values))
    core_asset_layer = read_template("core-asset-layer.md")
    write(folder / "references" / "core-asset-layer.md", core_asset_layer)
    write(folder / "references" / "audio-visual-sync.md", build_audio_visual_sync(values))
    write(folder / "references" / "asset-manifest.md", build_asset_manifest(values))
    write(folder / "references" / "gotchas.md", build_gotchas(values))
    write(folder / "references" / "trigger-tests.md", build_trigger_tests(values))

    prompt_plan = read_template("prompt-plan-format.md")
    write(folder / "references" / "prompt-plan-format.md", prompt_plan)
    quickstart = render(read_template("quickstart-template.md"), values)
    write(folder / "references" / "quickstart.md", quickstart)
    validator = render(read_template("validate-template.py"), values)
    write(folder / "scripts" / f"validate_{english_module}.py", validator, executable=True)

    prepare_assets = ROOT / "scripts" / "prepare_runtime_assets.py"
    if prepare_assets.exists():
        shutil.copy2(prepare_assets, folder / "scripts" / "prepare_runtime_assets.py")

    print(f"Created standard Codex SKU skill package: {folder}")
    print(f"- method: {method_label}")
    print(f"- skill name: {english_slug}")
    print("Next: fill product understanding, state matrix, material mapping, and product-specific validator checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
