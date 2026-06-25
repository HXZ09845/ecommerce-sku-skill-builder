# New SKU Skill Creator Questionnaire V2

Use this staged questionnaire when creating a new SKU skill. Ask only what is needed for the current phase.

## Beginner-Safe First Response

Before asking for materials, load `references/creator-onboarding.md` and use its copy-paste startup prompt. The first response must be guided enough for a novice creator to answer.

Rules:

- Ask for named first-round input slots, not "whatever you have."
- Explain that approved runtime assets come later, after product understanding, A/B judgment, selling-point proof, and script sync.
- Let missing fields be marked `pending`, but keep the slot visible.
- After the first-round inputs, output `读取确认卡`, `产品理解卡`, `组件/状态矩阵草稿`, and `A/B 初判`; do not draft the final SKU Skill yet.

## 0. Source Confirmation

Ask for current sources only if they were not already provided.

```text
如果本轮有外部来源，请提供最新版路径或文件；没有也可以写「暂无」，我会先用当前行业通用母 Skill 继续：
1. 行业通用 Meta Skill
2. 品类 Meta Skill（如果有）
3. 同类旧 SKU Skill 或黄金案例
4. 产品 brief / 文本卖点 / 案例视频 / 其他生产要求
```

Output:

```text
读取确认卡
| 来源 | 路径/文件 | 已读范围 | 优先级 | 本轮用途 |
|---|---|---|---:|---|
```

If category meta is missing or weak, write `品类 Meta: fallback` and proceed.

## 1. First Input Round: Product Understanding

Ask for the first-round essentials. Do not move to product understanding if these are missing, except to mark a clearly temporary gap.

```text
我会先帮你做产品理解和素材需求拆解，不会直接写最终 Skill。

请先提供首轮必备四件套。如果某一项暂时没有，可以写 pending：
1. 产品 Brief：产品名、品类必填；型号/版本/颜色/容量可选，除非会影响素材或规则
2. 文本卖点：卖点列表、优先级、必讲/可选/不能夸大的内容
3. 案例视频 / 实拍视频：用于理解结构、动作、场景、节奏；请说明是否可作为生成参考
4. 其他要求：目标平台、视频比例、时长、生成模型、风格方向、品牌/合规红线；如已有脚本，请说明是测试阶段脚本还是生产阶段脚本

我会先从 Brief、脚本、案例视频和素材里提取目标人群与核心使用场景；提取不到时再单独问。
收到后我会输出读取确认卡、产品理解卡、组件/状态矩阵草稿、A/B 初判和需要你确认的问题。
```

Output:

```text
产品理解卡
| 项目 | 当前理解 | 不确定点 |
|---|---|---|
| 产品定位 | | |
| 目标用户/场景 | | |
| 核心卖点初判 | | |
| 组件结构初判 | | |
| 活动件/高危件 | | |
| 案例视频意图 | | |
| 最近似黄金案例 | | |
```

Confirm:

```text
我对产品结构、卖点优先级、使用场景有没有理解错？
哪些卖点是必须讲的？哪些只是辅助？
```

Do not generate final `assets/`, manifest, or product rules in this phase.

## 2. Component And State Matrix

Agent drafts first; creator corrects.

```text
组件/状态草稿
| 组件 | 默认状态 | 结果状态 | 过程动作 | 是否高危 | A/B倾向 | 备注 |
|---|---|---|---|:---:|---|---|
```

Confirm:

- Which components are real?
- Which parts move or change?
- Which states are mandatory?
- Which states cannot mix in one unit?
- Which areas carry text/logo/UI risk?
- Which actions need video?
- Which A/B judgment rows should follow the creator's own standard instead of the default heuristic?

## 3. Core Asset And TS Risk

Before selling-point confirmation, choose the production archetype:

```text
生产原型判断
| Product signal | Production archetype | A/B shape | Prompt learning focus | Hallucination guard | Bad-case prevention |
|---|---|---|---|---|---|
| | Large fixed A+B / Small movable A+B / Pure A non-deforming/wearable | | | | |
```

Confirm:

- Is the product a tea-bar-machine-style large/fixed-space product with both A and B needs?
- Is it a small movable object like cups/containers/tabletop goods with A scenes plus possible B actions?
- Is it a pure A product like shoes/clothes/bags where no state-changing B action is required?
- Which case family should prompt writing learn from first?
- Which hallucination risks are archetype-level risks, not only this one SKU's risks?
- Which built-in abstraction family should be applied first: tea-bar appliance, cup/container, shoes/apparel/T-shirt, bag-like wearable, or nearest method family?
- Which parts of the abstraction need creator confirmation because the current product is not fully covered?
- Which A/B rows are already decided by the creator, and which rows are only agent suggestions?

Before the asset table, output:

```text
黄金案例抽象应用表
| Case family | Archetype fit | Abstracted rule | Applies to this SKU? | Keep / rewrite / reject | Destination |
|---|---|---|:---:|---|---|

幻觉点与 A/B 方案抽象
| Product part / action | Likely hallucination | Abstracted evidence family | A/B decision | Material strategy | Prompt safeguard | Validator / gotchas hook |
|---|---|---|---|---|---|---|
```

Then create this table:

```text
核心资产盘点
| Asset layer | What to extract | Source | Controls | Must not control | TS risk | Rule destination |
|---|---|---|---|---|---|---|
| identity/logo/text | | | | | | |
| structure/state | | | | | | |
| environment | | | | | | |
| rhythm | | | | | | |
| action | | | | | | |
| copy/audio | | | | | | |
| prompt form | | | | | | |
| submission/API | | | | | | |
| bad cases | | | | | | |
```

Confirm:

- Which logo/text/screen/label regions must be visually protected?
- Which environment references control product position, and which only control mood?
- What rhythm does the case video imply: small-object dense cuts, large-appliance slow stability, wearable complete-unit rhythm, or B-video duration?
- Which points are likely TS risks: identity drift, state swap, text hallucination, hand/action failure, material/API mismatch?
- Where should each risk be written: product rules, manifest, gotchas, or validator?

## 4. Old Case Inheritance

When old cases are provided:

```text
| 来源案例 | 可继承 | 需改写 | 禁止继承 | 原因 |
|---|:---:|:---:|:---:|---|
```

Use this before copying any old wording.

## 5. Selling-Point Visual Proof

This phase must be run one selling point at a time. The agent proposes reference choices, but the creator's historical experience decides whether the real-shot material can actually prove the selling point.

For each selling point:

```text
卖点 {n}: {卖点名}

我理解它需要证明的是：{证明目标}
可选视觉证明方式：
A. {动作/画面 1}
B. {动作/画面 2}
C. {动作/画面 3}

请确认：
1. 用图片、视频，还是图片+视频证明？
2. 希望选哪类实拍素材？
3. 必须出现哪些部件、颜色、状态或内容物？
4. 哪些素材、状态或动作不能用？
5. 如果没有视频，是否允许降级为结果态图片或删除该动作？
```

Before marking the row as `OK`, run this test:

```text
卖点素材引用对话测试
| 卖点 | 候选实拍引用 | 证明目标 | 素材会控制什么 | 素材不能控制什么 | A/B/状态判断 | 你的经验判断 | 结论 |
|---|---|---|---|---|---|---|---|
```

Record:

```text
| 卖点 | 用户确认的视觉证明 | 素材类型 | 产品状态 | A/B | P0 | P1 | P2 | 禁用素材 | 降级策略 | 状态 |
|---|---|---|---|:---:|---|---|---|---|---|:---:|
```

Rules:

- Do not batch-confirm unless creator asks.
- Do not replace proof with pretty materials.
- Do not move on while status is not `OK`.
- `OK` requires creator confirmation of proof route, real-shot reference type, A/B or A-out/A-in/B judgment, product state, forbidden materials, and downgrade route.
- If the creator rejects a material based on historical production experience, record the reason and use it as a future gotcha or validator hint.

## 5.5 Script Unit And Audio-Visual Sync

Ask for or confirm script mode:

```text
现在进入脚本-Unit-素材编排。

请确认这次脚本属于哪种：
1. 测试阶段：通常 1-2 条脚本，用来生成初版 SKU Skill、验证画面效果、收集反馈并回填规则
2. 生产阶段：Skill 已走通后批量给脚本，批量生成 prompt-plan、素材编排、校验记录和视频任务输入

我会按脚本文案逐段拆 Unit，并把每段绑定到显性/隐性关键词、实际物理环境、具象画面实体、卖点证明、A/B 判断、素材角色、画面动作、时长节奏和 TS 风险。
```

First output:

```text
文案语义抽取表
| 文案原句 | 显性词 | 隐性场景/情绪 | 实际物理环境 | 必须出现的具象画面 | 可选素材类型 | 禁用空泛表达 | 备注 |
|---|---|---|---|---|---|---|---|
```

Before prompts, output:

```text
脚本-Unit-素材编排表
| Script | Unit | 文案范围 | 显性/隐性关键词 | 实际环境 | 具象画面实体 | 证明目标 | 画面动作/关键帧 | 产品状态 | A/B | 素材组合 | 时长/节奏 | 禁用素材/状态 | TS风险 | 降级方案 | 确认 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Confirm:

- Which A/B rows must follow the creator's judgment?
- Which copy lines require visible proof and which can remain VO/caption?
- Which words like `夏日`, `喝咖啡`, `办公室`, `车里`, or `送到` need matching visual entities?
- Which visual proof方案 is accepted for each selling point?
- Which Units use A material, B material, or A+B mixed material?
- Which Units need B video, and which should downgrade to A-in/A-out result state?
- Which sync points are too risky and should be simplified before prompt writing?
- Does every Unit prompt include a short `【素材说明】` block that explains each `@图片` / `@视频` separately?

After prompts, output:

```text
音画同步核对表
| Script | 文案原句 | Unit | 显性/隐性关键词 | 实际环境 | 应出现的画面/动作/实体 | 实际 prompt 是否覆盖 | 使用素材 | A/B | 风险 | 修复 |
|---|---|---|---|---|---|---|---|---|---|---|
```

For production batches, output:

```text
批量生产总表
| Script | status | prompt_plan_path | material_arrangement_path | scripts/Units | A/B counts | missing materials | validation | video_task_status |
|---|---|---|---|---|---|---|---|---|
```

## 6. Approved Materials

After proof routes are confirmed:

```text
现在请提供或确认：
1. 批准使用的实拍素材文件夹/文件
2. 每个卖点对应的候选图/视频
3. 需要补拍或缺失的素材
4. 品牌红线
5. 场景环境偏好
6. 人物/人脸资产策略
7. Golden Case 脚本文案
```

Record:

```text
| 卖点 | 已批准素材 | 语义角色 | 产品状态 | 缺失素材 | 降级方案 |
|---|---|---|---|---|---|
```

## 7. A/B Confirmation

Output a compact table:

```text
| 动作/画面 | 对应卖点 | 对应组件 | 素材 | A/B/A-out/A-in | 理由 | 缺素材降级 |
|---|---|---|---|---|---|---|
```

Acceptance:

- State-change classifier applied.
- State conflicts are marked.
- Category meta supplements are applied when reliable.
- Creator confirms key rows.

## 8. Package Readiness

Before drafting final package:

```text
| 信息 | 状态 |
|---|:---:|
| 产品理解卡已确认 | |
| 组件/状态矩阵已确认 | |
| 核心资产/TS 风险表已确认 | |
| 旧案例继承判断已完成 | |
| 所有核心卖点映射已确认 | |
| A/B 表已确认 | |
| 文案语义抽取已完成 | |
| 脚本-Unit-素材编排已确认 | |
| 音画同步核对表已完成 | |
| 生产批量表已完成（如为批量脚本） | |
| 素材版本明确或 pending | |
| 品牌红线明确 | |
| Golden Case 有/无 | |
```

Then create the standard Codex package.
