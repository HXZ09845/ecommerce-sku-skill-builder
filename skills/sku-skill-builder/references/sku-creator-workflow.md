# creator/operator SKU Skill Creator Workflow V2

Use this workflow when creating, updating, or migrating a product/SKU skill. The goal is not to draft everything in one pass. The goal is to converge on product understanding, selling-point proof strategy, material mapping, skill package behavior, validation, and video bad-case regression.

Current-stage focus is concrete product SKU Skill creation. This workflow may later create abstract category skills, but only after enough qualified concrete SKU Skills exist; those category skills remain auxiliary inputs for future concrete SKU Skill creation. Do not make category abstraction the default output in early runs.

## Phase 0: Source Loading And Confirmation

Before the first creator-facing response, read `references/creator-onboarding.md`. The first response must guide a novice creator through named input slots and must not ask for an arbitrary source or material. Missing slots may be marked `pending`, but the slots remain visible.

Read sources in this order:

1. Current-thread industry-general meta or provided `sku-skill-builder`.
2. Current category meta if available.
3. Bundled baseline references in this package, including `references/golden-case-abstractions.md`.
4. Old SKU references only when the creator explicitly provides them for the current run.
5. Memory only as non-authoritative background.

If category meta is missing, weak, or outdated, continue with industry rules plus the built-in golden case abstractions. Mark that the category layer is `fallback`.

Output:

```text
读取确认卡
- 行业通用：path / read scope / priority
- 品类 Meta：path or fallback / read scope / known weakness
- 旧 SKU / 黄金案例：path / intended use
- 黄金案例抽象：case family / expected rule family / known gap
- 本轮来源优先级
- 不可降级铁律摘要
- 案例继承判断方式
```

## Phase 1: Product Understanding Only

Use the beginner-safe intake wording from `references/creator-onboarding.md` when the creator has not yet provided the first-round essentials.

Use the first round only to understand the product. Require the first-round essentials before moving into product understanding:

- product brief: product name and category required; model/version optional unless it affects color, capacity, bundle, or SKU rules
- text selling points: list, priority, must-say, optional, and claims that cannot be exaggerated
- real-shot/case video: product structure, true actions, use scenes, pacing, and visual quality reference
- other production requirements: platform, ratio, duration, model, style direction, brand/compliance red lines

Target user and core scene should be extracted from brief, script, case video, or material first. Ask only when extraction fails. Do not ask for a full approved material library yet unless the creator already offers it.

Output:

```text
产品理解卡
- 产品一句话定位
- 目标用户 / 场景
- 核心卖点初判
- 组件结构初判
- 活动件 / 高危件初判
- 案例视频意图
- 最接近的黄金案例
- 我不确定的问题
```

Stop for correction when structure, audience, or selling-point priority is uncertain.

## Phase 2: Structure And State Gate

Before detailed rules, produce a draft component/state matrix.

```text
| 组件 | 默认状态 | 结果状态 | 过程动作 | 是否高危 | A/B 倾向 | 备注 |
|---|---|---|---|:---:|---|---|
```

Confirm:

- which components truly exist
- which parts move, open, unfold, light up, fill, pour, stretch, or detach
- which states must appear
- which states must never mix in one unit
- which regions carry text/logo/UI risk

Do not finalize product rules until this gate is accepted.

## Phase 2.5: Core Asset And TS Risk Gate

Before selling-point mapping, choose the production archetype and create the core asset inventory from current inputs and the built-in golden case abstractions.

Use `references/core-asset-layer.md` and `references/golden-case-abstractions.md`.

Output:

```text
生产原型判断
| Product signal | Production archetype | A/B shape | Prompt learning focus | Hallucination guard | Bad-case prevention |
|---|---|---|---|---|---|
```

Allowed current archetypes:

- Large fixed A+B: tea-bar-machine-style large appliances, fixed product position, A lifestyle plus B state/action units.
- Small movable A+B: cups, containers, handheld/tabletop objects, A-out/A-in plus possible B actions.
- Pure A non-deforming/wearable: clothing, shoes, bags, accessories, and other products where no state-changing B action is needed.

After the archetype is chosen, apply the matching built-in golden case abstractions:

```text
黄金案例抽象应用表
| Case family | Archetype fit | Abstracted rule | Applies to this SKU? | Keep / rewrite / reject | Destination |
|---|---|---|:---:|---|---|

幻觉点与 A/B 方案抽象
| Product part / action | Likely hallucination | Abstracted evidence family | A/B decision | Material strategy | Prompt safeguard | Validator / gotchas hook |
|---|---|---|---|---|---|---|
```

```text
核心资产盘点
| Asset layer | What to extract | Source | Controls | Must not control | TS risk | Rule destination |
|---|---|---|---|---|---|---|
```

Also output a Unit/rhythm risk draft:

```text
| Unit candidate | copy range | proof target | state | A/B | duration/rhythm | TS risk | downgrade |
|---|---|---|---|---|---|---|---|
```

Rules:

- Do not write the core asset table until the archetype is chosen or the uncertainty is explicitly recorded.
- Do not finalize hallucination rules or A/B handling until the built-in golden case abstraction table is applied or a current-run gap is documented.
- Do not write prompts before this gate.
- Treat logo, screen, label, product color/version, environment, rhythm, action video, material count, and API count as assets.
- Let the archetype decide which prompt examples to learn, which hallucination guards to enforce first, and which bad cases to pre-block.
- If audio-visual sync would create a fragile generation point, propose a safer Unit split or downgrade and ask the creator.
- A/B judgment is the most important decision gate. The agent may propose based on state behavior, but the creator's current-run standard and explicit judgment override default heuristics.
- Bad-case risks identified here must be routed to product rules, manifest, gotchas, or validator before handoff.

## Phase 3: Old Case Mining

When the creator provides old SKU cases, mine them before writing new rules.

Use this table:

```text
| 来源案例 | 规则/经验 | 可继承 | 需改写 | 禁止继承 | 处理方式 |
|---|---|:---:|:---:|:---:|---|
```

Defaults from current golden cases:

- Tea bar machine: inherit fixed-space anchoring, G0 dual-role pattern as a large-appliance strategy, universal clips for text risk, direct-action exceptions only when action is simple.
- Jingci Fanhua cup: inherit component/state matrix, state consistency, color/version control, validator-backed maturity.
- Insulated food carrier: inherit A-out/A-in separation, angle completion, state-conflict checks.
- Crewneck T-shirt: inherit wear-state priority and person-product inseparability for wearable goods.

Never copy old filenames, old colors, old selling-point order, or deprecated failed strategies into a new SKU.

## Phase 4: Selling-Point Material Mapping, One By One

This phase is a dialogue test loop, not a batch filling task. The creator's historical material-selection experience is the source of truth for which real-shot references can prove a selling point. The agent proposes, tests the reasoning in conversation, records the decision, and only then moves forward.

For each selling point:

```text
卖点 {n}: {卖点名}

我理解它要证明的是：{proof meaning}
可选视觉证明方式：
A. {image/action/video option}
B. {image/action/video option}
C. {image/action/video option}

请确认：
1. 用图片、视频，还是图片+视频证明？
2. 希望选哪类实拍素材？
3. 必须出现哪些部件、颜色、状态或内容物？
4. 哪些素材、状态或动作不能用？
5. 如果没有视频，是否允许降级为结果态图片或删除该动作？
```

Run this dialogue test before recording `OK`:

```text
卖点素材引用对话测试
| 卖点 | 候选实拍引用 | 我建议它证明什么 | 可能继承的错误内容 | A/B 或状态判断 | creator/operator 经验判断 | 结论 | 下一步 |
|---|---|---|---|---|---|---|---|
```

Record before moving on:

```text
| 卖点 | 视觉证明 | 素材类型 | 产品状态 | A/B | P0 | P1 | P2 | 禁用素材 | 降级策略 | 状态 |
|---|---|---|---|:---:|---|---|---|---|---|:---:|
```

Rules:

- Current selling point must be `OK` before the next one unless the creator explicitly asks to batch.
- Creator material-selection experience is the source of truth. The agent may propose candidate references, but must not silently approve them.
- `OK` means the proof route, real-shot reference type, product state, A/B decision, required parts, forbidden materials, and downgrade route are all accepted by the creator.
- Do not use attractive off-message material.
- Do not use "looks good" as proof. State what the material proves and what it must not control.
- Mark uncertainty rather than inventing proof.

## Phase 4.5: Script Unit And Audio-Visual Sync Gate

Use `references/audio-visual-sync.md` before prompt writing. This phase binds script copy, selling-point proof, Unit rhythm, A/B classification, materials, and TS risk into one arrangement.

There are two operating modes:

| Mode | Input | Output |
|---|---|---|
| Test stage | Usually one or two concrete test scripts | First SKU Skill draft, small prompt-plan set, visual test result, feedback, and bad-case rule updates |
| Production stage | Batch scripts after the SKU Skill has passed | Batch prompt-plans, batch script-Unit-material arrangements, validation records, and video task input table |

First extract script semantics:

```text
文案语义抽取表
| 文案原句 | 显性词 | 隐性场景/情绪 | 实际物理环境 | 必须出现的具象画面 | 可选素材类型 | 禁用空泛表达 | 备注 |
|---|---|---|---|---|---|---|---|
```

Output before prompts:

```text
脚本-Unit-素材编排表
| Script | Unit | 文案范围 | 显性/隐性关键词 | 实际环境 | 具象画面实体 | 证明目标 | 画面动作/关键帧 | 产品状态 | A/B | 素材组合 | 时长/节奏 | 禁用素材/状态 | TS风险 | 降级方案 | 确认 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Rules:

- Every meaningful copy beat must map to one Unit or an intentional omission/downgrade.
- Every Unit must have one dominant proof target.
- Every visible script keyword must map to a concrete visual entity, environment, prop, role, or approved omission.
- Words such as `夏日`, `喝咖啡`, `办公室`, `车里`, `一路上`, and `送到` require concrete visual handling, not abstract mood words.
- Every key A/B row must be confirmed by the creator or marked `pending creator judgment`.
- Reference materials may be A, B, or A+B mixed, as long as the material roles do not conflict.
- If the script mentions a visible noun, action, scene, or user, the arrangement must say whether it appears visually, appears as result state, moves to VO/caption/post, or is removed.
- Do not request final approved assets until the proof route and material role needed by each Unit are clear.
- Do not write prompts before this gate.
- When writing each Unit prompt, include a concise `【素材说明】` or `Reference Materials` block before the visual instruction. Explain every `@图片` and `@视频` separately: what it is, P0/P1/P2 or B role, what it controls, what it must not control, and which selling point or copy beat it supports.

After prompts, output:

```text
音画同步核对表
| Script | 文案原句 | Unit | 显性/隐性关键词 | 实际环境 | 应出现的画面/动作/实体 | 实际 prompt 是否覆盖 | 使用素材 | A/B | 风险 | 修复 |
|---|---|---|---|---|---|---|---|---|---|---|
```

If the sync audit exposes unsupported claims or fragile actions, return to Phase 4 or this phase instead of patching prompts directly.

For production batches, also output:

```text
批量生产总表
| Script | status | prompt_plan_path | material_arrangement_path | scripts/Units | A/B counts | missing materials | validation | video_task_status |
|---|---|---|---|---|---|---|---|---|
```

## Phase 5: Approved Material Library

Only after proof routes are confirmed, ask for approved real-shot folders or selected files.

Record:

- material version and source folder
- semantic role for every approved file
- P0/P1/P2 assignment
- product state represented by each file
- missing material and downgrade route
- environment/person/ratio/model/brand red lines

Runtime `assets/` remain pending until the creator selects the approved version.

## Phase 6: Standard Skill Package Draft

Draft a standard Codex skill package:

```text
SKILL.md
agents/openai.yaml
references/product-rules.md
references/core-asset-layer.md
references/asset-manifest.md
references/prompt-plan-format.md
references/gotchas.md
references/trigger-tests.md
references/quickstart.md
scripts/validate_*.py
assets/
```

Create:

- lean trigger/workflow `SKILL.md`
- component/state matrix
- core asset inventory and TS-risk rules
- A/B/A-out/A-in rules
- selling-point visual-proof table
- audio-visual sync arrangement and audit rules
- material manifest
- product-specific gotchas
- prompt-plan output contract
- trigger tests
- validator with common and product-specific checks

Before leaving this phase, run a self-contained handoff audit:

```text
自包含交付审计
| Check | Pass | Fix location |
|---|:---:|---|
| Required reading only points to files inside this package | | |
| Applied industry/category/case-family rules are written into this package | | |
| Runtime assets are in assets/ or marked pending in asset-manifest.md | | |
| No required local absolute path remains | | |
| No instruction tells the user to read another package | | |
| Validator can run from this package | | |
```

## Phase 7: Script-Plan Validation

Use the drafted skill to create a representative prompt-plan.

Validate:

- selling-point coverage
- material role correctness
- state consistency
- A/B behavior
- copy-to-visual mapping
- prompt safety
- duration/ratio/model assumptions
- reference/API/material count consistency
- validator output

If validation reveals a proof or material uncertainty, return to Phase 4 instead of patching around it.

## Phase 8: Video Trial And Bad-Case Regression

When generation is possible, run a representative plan through the video workflow. For every bad case:

```text
| 输出问题 | 根因 | 修复位置 | 规则/校验更新 | 是否复测 |
|---|---|---|---|:---:|
```

Routing:

- product structure/state failure -> `references/product-rules.md`
- material choice failure -> `references/asset-manifest.md`
- wording failure -> `references/gotchas.md`
- repeatable detectable failure -> `scripts/validate_*.py`
- trigger/routing failure -> `SKILL.md` and `references/trigger-tests.md`

## Done Criteria

- Source confirmation completed.
- Product understanding accepted.
- Component/state matrix accepted.
- Core asset inventory and TS risk gate completed.
- Every core selling point has confirmed visual proof and material strategy.
- Script-Unit-material arrangement completed for test scripts or every production batch script.
- Production batch table completed when multiple scripts are provided.
- A/B key rows were confirmed by the creator or explicitly marked pending.
- Audio-visual sync audit exists after representative prompt writing.
- Approved assets are selected or explicitly pending.
- Standard Codex skill package exists.
- Representative prompt-plan passes validator or lists known accepted warnings.
- Bad cases have a regression home.
