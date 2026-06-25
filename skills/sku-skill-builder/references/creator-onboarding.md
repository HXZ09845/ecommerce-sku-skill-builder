# Creator Onboarding - Beginner-Safe Intake

Use this file immediately after loading `sku-skill-builder` and before asking the creator for materials. The goal is to make a novice creator know exactly what to provide and what the agent will output next.

## First Response Contract

The first response must do four things:

1. State that the agent will create a concrete SKU Skill through stages, not write the final Skill immediately.
2. Produce or promise a `读取确认卡` for the sources already provided.
3. Ask for the first-round required slots by name.
4. Explain that approved runtime assets are collected later, after product understanding, A/B judgment, and selling-point proof are aligned.

Do not say:

- "随便给一个"
- "任意给一种"
- "你有什么就先给什么"
- "直接把所有素材都发来"

Allowed fallback phrasing:

```text
如果某一项暂时没有，可以先写「暂无」或「pending」，但我会保留这个槽位，后面继续补齐。
```

## Copy-Paste Startup Prompt

Use this when the creator says they want to make a new product Skill:

```text
我会先帮你做产品理解和素材需求拆解，不会直接写最终 Skill。

请先提供首轮必备四件套。如果某项暂时没有，可以写 pending：

1. 产品 Brief
   - 产品名：
   - 品类：
   - 型号/版本/颜色/容量（可选，影响规则时必填）：
   - 目标人群/核心场景（没有也可以先空，我会从素材和脚本里提取）：

2. 文本卖点
   - 必讲卖点：
   - 可选卖点：
   - 不能夸大/不能说的点：

3. 案例视频 / 实拍视频
   - 文件或链接：
   - 用途：理解结构 / 动作参考 / 场景参考 / 节奏参考 / 可作为生成参考

4. 其他生产要求
   - 平台：
   - 比例：
   - 时长：
   - 生成模型：
   - 风格方向：
   - 品牌/合规红线：
   - 如果已有脚本：测试阶段 1-2 条 / 生产阶段批量脚本

收到后我会先输出：
1. 读取确认卡
2. 产品理解卡
3. 组件/状态矩阵草稿
4. A/B 初判和需要你确认的问题
```

## Staged Intake Map

| Stage | Ask from creator | Agent output | Stop condition |
|---|---|---|---|
| 0. Source | Current parent skill path, category meta if any, old cases if explicitly provided | 读取确认卡 | Source priority is clear |
| 1. Product | Brief, selling points, case/real video, production requirements | 产品理解卡 | Creator corrects product/category/scene misunderstandings |
| 2. Structure | Corrections to components, states, moving parts, risky regions | 组件/状态矩阵 | Structure and state conflicts are clear |
| 3. Archetype | Creator judgment on product type and A/B standard | 生产原型判断 + A/B 初判 | Key A/B rows confirmed or marked pending |
| 4. Selling points | One selling point at a time: proof route, required state, forbidden material, downgrade | 卖点 -> 视觉证明表 | Current selling point is `OK` |
| 5. Script sync | Test scripts or production batch scripts | 文案语义抽取表 + 脚本-Unit-素材编排表 | Every copy beat has visual handling |
| 6. Approved assets | Selected files/folders by role after proof route is known | asset manifest / 素材绑定表 | P0/P1/P2 roles and missing assets are known |
| 7. Skill package | Confirmed rules, manifest, gotchas, representative plans | Standard Codex SKU Skill package | Validator and handoff audit pass |

## Guidance Rules For Novice Creators

- Ask one phase at a time. Do not overwhelm the creator with all later-stage tables in the first response.
- Keep every input tied to a purpose: structure, proof, A/B, audio-visual sync, or validation.
- If the creator only gives video, ask for Brief and text selling points before writing rules.
- If the creator only gives selling points, ask for case/real video before judging structure.
- If the creator gives a full material folder early, do not treat it as approved. First classify what each asset should prove.
- If target user or core scene is missing, first try to infer it from Brief, script, video, and materials; ask only if it cannot be inferred.
- If the creator is unsure, provide 2-3 concrete proof options for one selling point and ask them to choose or correct.
- Keep saying what the next output will be, so the creator understands why they are providing each input.

## First Output Shape

After the creator provides the first-round four slots, output this shape before any final Skill draft:

```text
读取确认卡
| 来源 | 路径/文件 | 已读范围 | 优先级 | 本轮用途 |
|---|---|---|---:|---|

产品理解卡
| 项目 | 当前理解 | 不确定点 |
|---|---|---|
| 产品定位 | | |
| 目标用户/场景 | | |
| 核心卖点初判 | | |
| 组件结构初判 | | |
| 活动件/高危件 | | |
| 案例视频意图 | | |
| 最近似黄金案例抽象 | | |

下一步需要你确认：
1. 我对产品结构有没有理解错？
2. 哪些卖点必须讲，哪些只是辅助？
3. 是否同意进入组件/状态矩阵和 A/B 初判？
```

## Acceptance

The onboarding is successful when a novice creator can answer the first message without knowing the internal workflow, and the agent can proceed to product understanding without guessing missing business-critical inputs.
