# Standard SKU Skill Package Template V2

Use this template when drafting the target product/SKU skill. Replace placeholders, then refine with real product rules and creator-confirmed material mapping.

## Directory

```text
{skill_name}/
  SKILL.md
  agents/openai.yaml
  references/
    product-rules.md
    core-asset-layer.md
    audio-visual-sync.md
    asset-manifest.md
    prompt-plan-format.md
    gotchas.md
    trigger-tests.md
    quickstart.md
  scripts/
    validate_{english_module}.py
  assets/
```

## SKILL.md

```markdown
---
name: {skill_name}
description: "{产品名} SKU short-video generation skill for ecommerce AIGC workflows. Use when creating prompt-plans, selecting materials, validating A/B Units, or generating videos for {产品名}, {品类名}, {核心卖点}. Triggers: {触发词1}, {触发词2}, {触发词3}."
---

# {产品名} SKU Skill

Use this skill to create and review prompt-plans for {产品名}. The skill is self-contained for this SKU; read only the required references inside this package before writing or validating prompts.

## Required Reading

1. `references/product-rules.md` — product structure, state matrix, selling-point proof, A/B rules, product-specific gotchas.
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
8.5. **Scene narrative derivation**: If the script scene is NOT the product's default/primary scene, complete the four-step derivation before writing any A-class prompt: Step 1 scene micro-actions → Step 2 scene-specific props → Step 3 emotional arcs → Step 4 narrative quality self-check (Q1-Q6). Output a "Scene Narrative Adaptation Table" at the top of the prompt plan.
9. Write every referenced Unit prompt with an in-prompt `【素材说明】` / `Reference Materials` block before the visual instruction.
10. Write the prompt-plan using the required format.
11. Run `scripts/validate_{english_module}.py` on the finished plan.
12. Record warnings, accepted downgrades, sync issues, and bad cases.
13. Confirm the plan uses only this package's rules, manifest, assets, and validator.

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
- **Scene-adaptive narrative quality gate (U31)**: every A-class Unit passes Q1-Q6 — Q1: ≥2 scene-specific micro-actions; Q2: ≥3 scene-specific props; Q3: emotional arc (from→to); Q4: person is protagonist; Q5: no long continuous pure-product segment that breaks lifestyle rhythm; Q6: closing satisfaction moment. Non-default scenes require four-step derivation first.
- **Unit Scope Contract (U32)**: every standard A-class submit prompt declares unit goal (`本段只做一件事`) + action flow (one paragraph, no segmented second-by-second timeline) + end condition (`结束条件`). Document SKU-specific exceptions without concrete second marks in prompt prose.
- No runtime instruction points outside this package.
- Validator has 0 errors before handoff.
```

## references/product-rules.md

```markdown
# Product Rules - {产品名}

## 1. Product Understanding

- Product:
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

| 组件 | 默认状态 | 结果状态 | 过程动作 | 高危原因 | A/B |
|---|---|---|---|---|---|

## 3. Selling Point To Visual Proof

Run this dialogue test before marking a selling point row as `OK`:

| 卖点 | 候选实拍引用 | 证明目标 | 素材会控制什么 | 素材不能控制什么 | A/B/状态判断 | creator 经验判断 | 结论 |
|---|---|---|---|---|---|---|---|

| 卖点 | 证明目标 | 视觉证明 | A/B | 必选素材 | 禁用素材 | 降级策略 |
|---|---|---|:---:|---|---|---|

## 3.5 Audio-Visual Sync

Script mode: test stage / production stage / pending

| 文案原句 | 显性词 | 隐性场景/情绪 | 实际物理环境 | 必须出现的具象画面 | 可选素材类型 | 禁用空泛表达 | 备注 |
|---|---|---|---|---|---|---|---|

| Script | Unit | 文案范围 | 显性/隐性关键词 | 实际环境 | 具象画面实体 | 证明目标 | 画面动作/关键帧 | 产品状态 | A/B | 素材组合 | 时长/节奏 | 禁用素材/状态 | TS风险 | 降级方案 | 确认 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

| Script | 文案原句 | Unit | 显性/隐性关键词 | 实际环境 | 应出现的画面/动作/实体 | 实际 prompt 是否覆盖 | 使用素材 | A/B | 风险 | 修复 |
|---|---|---|---|---|---|---|---|---|---|---|

## 4. Core Asset And TS Risk

| Case family | Archetype fit | Abstracted rule | Applies to this SKU? | Keep / rewrite / reject | Destination |
|---|---|---|:---:|---|---|

| Product part / action | Likely hallucination | Abstracted evidence family | A/B decision | Material strategy | Prompt safeguard | Validator / gotchas hook |
|---|---|---|---|---|---|---|

| Product signal | Production archetype | A/B shape | Prompt learning focus | Hallucination guard | Bad-case prevention |
|---|---|---|---|---|---|

| Asset layer | What to extract | Source | Controls | Must not control | TS risk | Rule destination |
|---|---|---|---|---|---|---|

| Unit | copy range | proof target | state | A/B | duration/rhythm | TS risk | downgrade |
|---|---|---|---|---|---|---|---|

## 5. A/B/A-Out/A-In Rules

| Unit type | Use when | Material recipe | Forbidden |
|---|---|---|---|

## 6. Material Role Rules

| Role | Meaning | This SKU examples |
|---|---|---|
| P0 | identity/space anchor | |
| P1 | selling-point proof | |
| P2 | narrative support | |

## 6.5 Scene-Adaptive Narrative Engine

Default/primary scenes for this product: {列出默认场景, e.g., 客厅、家庭固定角落}

For scripts set in a non-default scene, the executor must complete the four-step derivation BEFORE writing any A-class prompt:

1. **Scene micro-actions**: list 8-10 actions unique to this scene (no generic actions).
2. **Scene-specific props**: list 5-8 props with visible identity unique to this scene.
3. **Emotional arcs**: for each A-class Unit, define "from X emotion → to Y emotion."
4. **Narrative quality self-check (R-NQ)**: every A-class Unit must pass Q1-Q6:

| Check | Requirement |
|---|---|
| Q1 | ≥2 scene-specific micro-actions (no generic) |
| Q2 | ≥3 scene-specific props with visual identity |
| Q3 | Clear emotional arc (from X → to Y) |
| Q4 | Person is protagonist; product serves the story |
| Q5 | No long continuous pure-product segment that breaks lifestyle rhythm (except universal clips) |
| Q6 | Closing has "enjoying the result" moment |

Output a **Scene Narrative Adaptation Table** at the top of the prompt plan for non-default scenes. Default-scene scripts may skip Steps 1-3 but must still pass Q1-Q6.

## 7. Product-Specific Hard Rules

| ID | Rule | Why |
|---|---|---|

## 8. Prompt Rules

- Style:
- Space anchoring:
- Reference material-purpose block policy:
- **Unit Scope Contract (U32):** every standard A-class prompt includes unit goal + action flow + end condition; no segmented second-by-second prompt prose unless a documented exception still avoids concrete second marks.
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
```

## references/asset-manifest.md

```markdown
# Asset Manifest - {产品名}

Approved material version:

| runtime_path | original_path | type | required | semantic_role | product_state | status | notes |
|---|---|---|:---:|---|---|---|---|
```

## references/audio-visual-sync.md

```markdown
# Audio-Visual Sync - {产品名}

Use this before prompt writing. The script, selling-point proof, Unit split, material roles, and prompt must be arranged together.

Priority: creator A/B judgment > script copy / voiceover > selling-point proof target > approved material reality > prompt wording

## Script Mode

| Mode | Input | Rule |
|---|---|---|
| Test stage | usually 1-2 test scripts | create first SKU Skill draft, test visual output, collect feedback, and update rules |
| Production stage | batch scripts after the SKU Skill passes | batch-generate prompt-plans, material arrangements, validation records, and video task inputs |

## Pre-Prompt Arrangement

| 文案原句 | 显性词 | 隐性场景/情绪 | 实际物理环境 | 必须出现的具象画面 | 可选素材类型 | 禁用空泛表达 | 备注 |
|---|---|---|---|---|---|---|---|

| Script | Unit | 文案范围 | 显性/隐性关键词 | 实际环境 | 具象画面实体 | 证明目标 | 画面动作/关键帧 | 产品状态 | A/B | 素材组合 | 时长/节奏 | 禁用素材/状态 | TS风险 | 降级方案 | 确认 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Prompt Material-Purpose Block

Every Unit prompt that uses `@图片` or `@视频` must copy a short material-purpose block into the prompt before the visual instruction. Explain each reference separately: what it is, P0/P1/P2 or B role, what it controls, what it must not control, and which selling point or copy beat it supports.

```text
【素材说明】
@图片1：P0，{是什么素材}，控制{产品身份/版本/空间/身体关系}，不控制{不应继承的内容}，对应{卖点/文案beat}
@图片2：P1，{是什么素材}，证明{卖点/部件/状态}，不控制{不应继承的内容}，对应{卖点/文案beat}
@图片3：P2，{是什么素材}，控制{场景/人物/道具/情绪}，不控制{产品状态/动作}，对应{文案实体}
@视频1：B，{是什么动作视频}，控制{动作/节奏/视角/状态变化}，不控制{背景/人物/其他}，对应{动作beat}

本段只做一件事：[本 Unit 唯一证明目标，一句话]。
动作流：[一段动作/运镜/情绪描述，标准 A 类不写具体秒段或逐秒分段]。
结束条件：[clip 停在哪一帧]。

【画面要求】（legacy — prefer the three lines above for A-class）
...
```

## Post-Prompt Audit

| Script | 文案原句 | Unit | 显性/隐性关键词 | 实际环境 | 应出现的画面/动作/实体 | 实际 prompt 是否覆盖 | 使用素材 | A/B | 风险 | 修复 |
|---|---|---|---|---|---|---|---|---|---|---|

## Batch Production

| Script | status | prompt_plan_path | material_arrangement_path | scripts/Units | A/B counts | missing materials | validation | video_task_status |
|---|---|---|---|---|---|---|---|---|
```

## references/gotchas.md

```markdown
# Gotchas - {产品名}

| Failure | Why it happens | Prevention | Validator |
|---|---|---|---|

## Scene-Adaptive Narrative Gotchas

| Do not | Why | Correct approach |
|---|---|---|
| Use generic micro-actions (rubs temples, picks up phone, yawns) for non-default scenes | They apply to any scene and destroy scene identity | Derive 8-10 unique micro-actions from the specific scene's physical environment |
| Use generic props (cup, book, plant) as scene markers | They lack visual identity for any particular scene | List 5-8 props with visible markers that only belong in this scene |
| Write A-class prompts with product as subject, person as background | Product-centric framing kills narrative and seed-video authenticity | Person is always protagonist; product is the tool that enables the emotional arc |
| Have long continuous pure-product segments in A-class Units | Breaks lifestyle rhythm, feels like an ad insert | Intercut product closeups with person actions and return to the person before the shot feels product-only |
| Skip emotional arc definition for A-class Units | Prompts become flat scene descriptions without narrative tension | Every A-class Unit needs a "from X → to Y" emotional change |
| End a Unit without a "satisfaction moment" | Missing payoff makes the clip feel unfinished | Close with person visibly enjoying the product's result (drinking, relaxing, smiling at the output) |
```

## references/trigger-tests.md

```markdown
# Trigger Tests - {产品名}

## Should Trigger

- "帮我做{产品名} prompt-plan"
- "{产品名}素材怎么选"
- "检查{产品名} A/B Unit"

## Should Not Trigger

- "做另一个没有{产品名}素材的新产品"
- "只写普通文案，不做视频生成"
```

## scripts/validate_{english_module}.py

Start from `references/validate-template.py`, then add product-specific checks from confirmed hard rules and bad cases.
