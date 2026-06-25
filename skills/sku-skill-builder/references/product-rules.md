# Product Rules - Industry General SKU Skill Creator V2

This file defines the non-negotiable rules for creating concrete product/SKU skills for ecommerce AIGC short-video workflows. Category meta skills may add domain knowledge, but they must not weaken these rules.

Current-stage focus is concrete product SKU Skill building. Future abstract category skills may also be generated with this workflow after enough qualified concrete SKU Skills exist, but those category skills are support layers for building future concrete SKU Skills, not a replacement for this industry-general creator.

## 1. Creator Mission

The creator's job is to turn a new product into a reusable, publishable Codex SKU skill. The work is not complete when a prompt is written. It is complete when a coworker can use the skill package to produce prompt-plans, validate them, and fold future bad cases back into the package.

Do not over-abstract early. Build the concrete SKU skill first, preserve reusable methods, and only promote a rule upward when repeated cases prove that it belongs above the current SKU.

Required output shape:

```text
sku-skill/
  SKILL.md
  agents/openai.yaml
  references/product-rules.md
  references/core-asset-layer.md
  references/audio-visual-sync.md
  references/asset-manifest.md
  references/prompt-plan-format.md
  references/gotchas.md
  references/trigger-tests.md
  references/quickstart.md
  scripts/validate_*.py
  assets/
```

Legacy packages with a core markdown file, quickstart, and validator can be used as source material, but the new primary deliverable is the standard Codex package.

## 1.5 Self-Contained Handoff Contract

Every generated product/SKU Skill must work as an independent package when sent to another person. Creation sources can inform the package, but runtime instructions must not depend on those sources.

The target SKU package must:

- include every runtime rule in its own `SKILL.md`, `references/`, `scripts/`, or `assets/`
- use only relative paths inside the package for required reading, validators, assets, and examples
- inline or adapt all applied industry, category, and golden-case abstraction rules into product-specific files
- keep approved runtime assets inside `assets/` or mark them as `pending` in `asset-manifest.md`
- include a validator script that runs from the target package without reading this creator package

Forbidden in the target SKU package:

- `use/read/load sku-skill-builder`
- `use/read/load the category meta Skill`
- `see tea-bar/fanhua/shoes/apparel Skill for details`
- local absolute paths as required runtime inputs
- rules that only say "refer to the parent/original/golden Skill"
- hidden material dependencies outside the package

If a current-run source or old case teaches a useful rule, rewrite the rule into the target SKU's own `product-rules.md`, `gotchas.md`, `asset-manifest.md`, or `validate_*.py`. Do not leave it as a cross-package dependency.

## 2. Source Priority

Use the most current source, not memory or assumptions.

1. Files, folders, screenshots, scripts, or notes provided in the current thread.
2. Adjacent references inside the provided package, especially `references/product-rules.md`, `asset-manifest.md`, `gotchas.md`, examples, and validators.
3. Current industry-general package files.
4. Built-in golden case abstractions in `references/golden-case-abstractions.md`.
5. Registered category meta skills.
6. Old SKU cases and memory as non-authoritative background.

Always output a source confirmation card before asking for product inputs.

## 3. Product Understanding Before Materials

Do not begin by asking for the full material library. First collect the required first-round inputs: product brief, text selling points, real-shot/case video, and other production requirements. Model/version is optional unless it changes color, capacity, material, bundle, or SKU-specific rules.

Target user and core scene should be extracted from the brief, script, case video, or material first. Ask follow-up questions only when they cannot be inferred.

Required card:

```text
产品理解卡
- 一句话定位
- 目标用户 / 场景
- 核心卖点初判
- 组件结构初判
- 活动件 / 高危件初判
- 案例视频意图
- 最接近的黄金案例
- 不确定问题
```

Then produce a component/state matrix:

```text
| 组件 | 默认状态 | 结果状态 | 过程动作 | 高危原因 | A/B 倾向 |
|---|---|---|---|---|---|
```

The creator must confirm the product structure before the SKU rules become final.

When scripts are provided, record the script mode:

| Mode | Meaning | Rule |
|---|---|---|
| Test stage | Usually one or two scripts are used to create the first SKU Skill draft and verify visual effect | Generate a small number of prompt-plans, run visual tests, collect feedback, and fold bad cases into rules |
| Production stage | Batch scripts are provided after the SKU Skill has passed | Batch-generate prompt-plans, material arrangements, validation records, and video task inputs |

## 4. Golden Case Abstractions

Use built-in golden case abstractions as rule sources, not as copy-paste templates. The creator must apply `references/golden-case-abstractions.md`; do not depend on loading other Skills.

| Case | Abstractable rule |
|---|---|
| Angel tea bar machine | Fixed-space anchoring, product-containing G0 environment anchors, B-class dual-role background replacement, universal clips for text-risk closeups, direct-vs-implied action exceptions, **U32 unit goal + end condition instead of segmented second-by-second A-class prompt prose** |
| Fanhua ice cup / Supor Jingci Fanhua cup | Component/state matrix, A-out/A-in split, mutually exclusive mechanisms, state consistency, color/version control, cup/straw/lid hallucination suppression, copy-to-visual proof mapping, SKU-specific validator |
| Supor insulated food carrier | A-out/A-in separation, product angle completion, state-conflict handling, internal component display rules |
| Shoes / Crewneck T-shirt / apparel competition | Pure A or wear-state priority, person-product inseparability, limb/body hallucination guards, same-color detail filtering, logo/print guards, safe action library |

For any old case, classify extracted rules:

```text
| 来源规则 | 可继承 | 需改写 | 禁止继承 | 原因 |
|---|:---:|:---:|:---:|---|
```

Do not inherit deprecated failure paths. Example: a pure environment image for tea-bar B-class background is forbidden when the current verified rule requires a product-containing G0 anchor.

Required golden-case abstraction output:

```text
黄金案例抽象应用表
| Case family | Archetype fit | Abstracted rule | Applies to this SKU? | Keep / rewrite / reject | Destination |
|---|---|---|:---:|---|---|
```

Required abstraction output:

```text
幻觉点与 A/B 方案抽象
| Product part / action | Likely hallucination | Abstracted evidence family | A/B decision | Material strategy | Prompt safeguard | Validator / gotchas hook |
|---|---|---|---|---|---|---|
```

For bags or other categories without a strong concrete abstraction, use the wearable/apparel abstraction only as method-level evidence. Mark product-specific bag rules as `needs creator confirmation` before turning them into hard category rules.

## 4.5 Core Asset And TS Risk Layer

Before selling-point mapping or prompt writing, read `references/core-asset-layer.md`, classify the production archetype, and create the core asset inventory. The current industry-level router has three archetypes:

- Large fixed A+B: tea-bar-machine-style large appliances with fixed-space logic plus A and B units.
- Small movable A+B: cups, containers, handheld/tabletop objects with A scenes plus possible B actions.
- Pure A non-deforming/wearable: shoes, clothing, bags, and similar products with no required state-changing B action.

Required archetype table:

```text
生产原型判断
| Product signal | Production archetype | A/B shape | Prompt learning focus | Hallucination guard | Bad-case prevention |
|---|---|---|---|---|---|
```

If a product appears to fit multiple archetypes, choose the safest current-production route and record the reason. Do not invent a fourth archetype unless the creator explicitly approves adding one.

Required table:

```text
| Asset layer | What to extract | Source | Controls | Must not control | TS risk | Rule destination |
|---|---|---|---|---|---|---|
```

Minimum asset layers:

- identity/logo/text/UI: product identity, logo, screen, labels, print, color/version, readable-risk zones
- structure/state: components, default/result states, moving parts, internal/external states
- environment: product location, fixed/movable logic, product-containing anchors, scene micro-words
- rhythm: case-video tempo, Unit duration, shot density, slow/fast logic
- action: direct-safe actions, B-only state changes, implied-action candidates
- copy/audio: voiceover nouns, verbs, timing pressure, proof targets
- prompt form: A/B prompt skeleton, material purpose block, clean-video line
- submission: references per Unit, duration, ratio, API counts, compression/upload chain
- bad cases: likely drift, swap-back, text hallucination, state conflict, hand/action failure

This layer is the bridge between high-quality cases and new SKU rules. Promote only reusable methods upward; keep exact product names, file names, colors, rooms, and validated exceptions inside the target SKU or category rule.

## 5. Selling Point To Visual Proof

Every selling point must become visual proof. Do not write "展示卖点" as a final rule.

For each selling point record:

```text
| 卖点 | 证明目标 | 视觉证明动作/画面 | 素材类型 | 产品状态 | A/B | 必选素材 | 禁用素材 | 降级策略 |
|---|---|---|---|---|:---:|---|---|---|
```

Rules:

- Functional selling points require evidence action or evidence state.
- Static beauty shots can support a selling point, but cannot be the only proof for a functional claim unless the creator approves a downgrade.
- Attractive but off-message material must not replace the copy's proof target.
- If a selling point has multiple required proof rows, enumerate every row. Do not select only the first line.

## 6. A/B/A-Out/A-In Classification

Use product state behavior as the core classifier, but treat the creator's explicit standard and current-run judgment as the final authority. A/B is the most important decision point in this workflow.

| Type | Definition | Prompt control | Material rule |
|---|---|---|---|
| A | Image-driven; product state does not change during the shot | Prompt controls scene, rhythm, and action | Reference images anchor product, scene, person, and details |
| A-out | A unit where product stays in closed/external/default state | Lifestyle and external appearance | Do not mix internal/open-state images |
| A-in | A unit where product is already open, unfolded, disassembled, or showing a stable internal result state | Result-state display | Use only references matching the internal/result state |
| B | Video-driven; product state changes during the shot | Reference video controls action, composition, viewpoint, timing | One B unit uses exactly one action video unless a verified product rule says otherwise |

Key distinctions:

- "Already open" is A-in.
- "Opening" is B.
- B prompt does not describe the action process; it describes role assignment, environment/background, safety constraints, and content required by the copy.
- If B action state conflicts with a still product image, do not add that still image.
- If the agent and creator disagree, record the agent's reason, the creator's decision, and the downstream material/prompt impact. Follow the creator's decision.

## 7. Material Roles

Treat assets as semantic roles, not filenames.

| Role | Meaning | Examples |
|---|---|---|
| P0 | Identity or space anchor; missing it causes drift | whole product, worn-body anchor, fixed environment, primary color/version |
| P1 | Selling-point proof material | detail image, component reference, action video, internal structure |
| P2 | Narrative support | person asset, hand, cup, food, sofa, desk, bag, lifestyle prop |

Every reference must state:

- what it is
- what it controls
- what it must not control
- which product state it represents

If the model would be allowed to copy every visual element in a reference and the result would be unacceptable, do not use that reference or explicitly downgrade its role.

## 8. State Consistency

State consistency is non-negotiable.

- One unit must not mix closed, open, disassembled, folded, unfolded, filled, empty, or different color/version states unless the reference video is explicitly controlling the transition.
- A-out units cannot include internal/open-state proof images.
- A-in units cannot include closed exterior anchors unless the rule explains why they do not control state.
- Product color/version must be consistent within a unit.
- Multiple screen states, label states, liquid states, or accessory states need explicit role assignment.

Before writing prompts, add a state consistency line to the material table:

```text
状态一致性：本 Unit 所有参考素材均为 {state}; 冲突素材：无/已排除 {reason}
```

## 9. Text And Logo Risk

High-risk readable regions include logo, screen text, labels, degree numbers, measurement marks, remote buttons, clothing prints, packaging claims, QR codes, warning labels, and product UI.

Rules:

- Do not ask the model to generate exact readable text unless the generation model and case have been verified for that exact text.
- Treat source-material text as visual texture and layout anchor.
- Put exact claims in voiceover, captions, or post-production graphics.
- For high-text-risk closeups, prefer fewer materials, minimal movement, short duration, and reusable universal clips.
- Product logo may remain as part of product appearance, but prompt prose should avoid recopying brand text when it causes hallucination.

## 10. Physical Action Difficulty

Classify actions before writing prompts.

| Action class | Default strategy |
|---|---|
| Complex continuous physical action | Use implied-action montage: intent -> cut -> result state |
| Simple verified hand action | May describe directly if stable in old cases or confirmed by creator |
| Product-state transition with video | Use B-class reference video |
| Missing action video | Downgrade to A-in/A-out result state only if creator approves |

Known direct-action exceptions from golden cases:

- Remote control: hand holds remote, looks, presses once.
- Cabinet opening: human hand must pull the door; do not show a cabinet magically open.

Do not generalize these exceptions to complex actions such as pouring, twisting, assembling, or multi-step manipulation without evidence.

## 11. Space And Environment Anchoring

Every script needs a physical-space model.

Use the four questions:

```text
1. 主人公在哪？
2. 产品在哪？
3. 摄像机在哪？
4. 参考图角度是否等于目标角度？
```

Rules:

- A units must restate the environment in each unit.
- B units replace or adapt background to the copy's actual narrative environment, not blindly to the script's main scene.
- Large/fixed products need a stable position anchor across units.
- Product-containing environment anchors may control product position and background mood; if so, state those roles explicitly.
- Pure environment images do not anchor product position.
- Do not move a fixed product between rooms or surfaces unless the product can physically move and the script says so.

## 11.5 Scene-Adaptive Narrative Engine

Every script runs in a physical scene. When the script scene is the product's default/primary scene (e.g., home living room for a tea bar machine, office desk for a desk lamp), the skill's built-in templates usually provide adequate narrative depth. When the script scene is NOT the default scene (e.g., office for a tea bar machine, car for a food container, bedroom for a cup), the executor must complete a four-step scene derivation BEFORE writing any A-class prompt.

### Step 1: Scene Micro-Action Derivation

List 8-10 micro-actions unique to this scene. Every action must be scene-specific; generic actions that could happen anywhere (e.g., "rubs temples", "picks up phone", "yawns") are forbidden. Good examples for an office scene: "slides keyboard tray back to reach for the teacup", "tilts laptop screen down before standing up", "pulls sticky note from monitor edge."

### Step 2: Scene-Specific Prop List

List 5-8 small props that are unique to this scene and have visible identity. Props must not be generic household items; they must carry visual markers of the specific scene. Good examples for an office: "monitor with a post-it forest", "cable management tray", "branded lanyard badge"; bad: "cup", "book", "plant."

### Step 3: Emotional Arc Design

For each A-class Unit, define a clear emotional transition: "from X emotion → to Y emotion." The product must serve as the pivot of the emotional change, not merely exist in the frame.

### Step 4: Narrative Quality Self-Check (R-NQ)

Every A-class Unit prompt must pass six quality checks before submission:

| Check | Requirement |
|---|---|
| Q1 | Contains ≥2 scene-specific micro-actions (no generic actions) |
| Q2 | Contains ≥3 scene-specific props with visual identity |
| Q3 | Has a clear emotional arc (from X → to Y) |
| Q4 | Person is the protagonist; product serves the story, not the other way around |
| Q5 | No ≥4-second pure-product segment (except universal/closeup clips) |
| Q6 | Closing has a "enjoying the result" moment where the person interacts with the product's output |

When the script scene is NOT the product's default scene, the executor must complete Steps 1-4 and output a **Scene Narrative Adaptation Table** at the top of the prompt plan before writing any A-class prompt. Default-scene scripts may skip Steps 1-3 but must still pass Q1-Q6.

## 12. Prompt Writing Rules

Use prompt prose to direct visible evidence, not to explain features.

Do:

- write concrete verbs and sensory actions
- keep the product or product-use context visible in the opening beat
- alternate distance, viewpoint, and human/product focus
- include scene micro-environment words in every shot
- keep middle units from doing final closing scenes
- make the final unit human/lifestyle-led when the script needs emotional closure

Avoid:

- "展示", "呈现", "突出" as the main visual action
- consecutive pure product shots without lifestyle or proof action
- references with unclear roles
- overlong negative constraints
- prompt wording that conflicts with reference images or videos

## 13. Audio-Visual Sync

Script copy, prompt wording, and actual materials must be arranged together before prompt writing. Use `references/audio-visual-sync.md` for the full gate. Audio-visual sync is keyword/entity level: words such as `夏日`, `喝咖啡`, `办公室`, `车里`, or `送到` must become concrete visible objects, environments, people, and actions.

Priority:

```text
creator A/B judgment > voiceover/copy > concrete visual entity > selling-point proof target > approved material reality > prompt wording
```

Before Unit arrangement, extract script keywords:

```text
文案语义抽取表
| 文案原句 | 显性词 | 隐性场景/情绪 | 实际物理环境 | 必须出现的具象画面 | 可选素材类型 | 禁用空泛表达 | 备注 |
|---|---|---|---|---|---|---|---|
```

Before prompts, create the script-Unit-material arrangement:

```text
脚本-Unit-素材编排表
| Script | Unit | 文案范围 | 显性/隐性关键词 | 实际环境 | 具象画面实体 | 证明目标 | 画面动作/关键帧 | 产品状态 | A/B | 素材组合 | 时长/节奏 | 禁用素材/状态 | TS风险 | 降级方案 | 确认 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Rules:

- Every meaningful copy beat must map to one Unit, an intentional omission, or an approved downgrade.
- Every visible keyword must map to a concrete visual entity, environment, prop, user role, or approved omission.
- Every Unit must have one dominant proof target.
- A/B key rows need creator confirmation or `pending creator judgment`.
- Reference materials may be A, B, or A+B mixed, but each role must be declared and conflicts must be removed.
- Every required material should be bound by semantic role and product state before prompt writing.
- Do not force exact sync if it creates fragile action, text, state, or swap-back risk. Split the Unit or downgrade with creator approval.
- Test scripts are used to create and validate the first SKU Skill draft; production scripts are batch-processed only after the skill has passed or the creator approves.

The lightweight keyword view can still be used:

```text
| 文案关键词/短句 | 环境 | 必须出现的画面内容 | 对应卖点 | Unit |
|---|---|---|---|---|
```

Concrete visual examples:

| Copy signal | Required visual handling |
|---|---|
| 夏日 / 夏天 | Use visible summer cues such as bright daylight, cold drink, outdoor shade, light clothing, fan/ice/sunlight when relevant |
| 喝咖啡 / 冰美式 / 拿铁 | Show coffee cup or coffee liquid, cafe/desk context, and the matching drink action or product relation |
| 办公室 / 工位 | Use desk, laptop, documents, office chair, daylight window, or other office entities |
| 车里 / 车座 / 一路上 | Use car interior, seat, bag, road/travel cue; do not leave the scene in kitchen/home |
| 到了 / 送到 / 递过去 | Switch to destination environment and receiving action |

After prompts, create the sync audit:

```text
音画同步核对表
| Script | 文案原句 | Unit | 显性/隐性关键词 | 实际环境 | 应出现的画面/动作/实体 | 实际 prompt 是否覆盖 | 使用素材 | A/B | 风险 | 修复 |
|---|---|---|---|---|---|---|---|---|---|---|
```

After the whole plan is written, do a second-pass copy audit:

- For every verb, ask where the action physically happens.
- For every noun, ask whether it is visible and in what state.
- For every scene/time/drink/food/lifestyle word, ask which concrete visual entity proves it.
- For every B background, check whether it was copied from the previous unit by habit.
- For every A+B mixed Unit, check whether A materials and B video roles are compatible.
- For every fragile sync point, ask whether the safer path is a B video, A-in/A-out result-state proof, shorter Unit, fewer references, or script/caption rewrite.

## 14. Prompt-Plan Output Contract

Representative prompt-plans must include:

- production archetype decision and reason
- golden case abstraction and hallucination/A-B abstraction tables
- self-contained handoff check
- source/material thumbnails or local paths for every @ reference
- core asset inventory and TS risk table
- A/B/A-out/A-in classification table
- selling-point material lookup list
- script-Unit-material arrangement and audio-visual sync audit
- batch production table when multiple production scripts are provided
- unit prompts
- material role and state consistency table per unit
- API parameter quick table with counts matching references
- image/video preprocessing checklist
- validation log
- second-pass copy audit

Counts must match across material table, prompt @ references, API parameter table, and preprocessing list.

## 15. Validation And Bad-Case Regression

Every mature SKU skill needs a validator.

The validator should start with common checks:

- missing core asset inventory or TS risk lines
- @图片/@视频 numbering continuity
- no unresolved placeholders
- no external Skill dependency wording
- no local absolute paths used as required runtime references
- A/B misuse hints
- B-class action over-description
- missing in-prompt material-purpose blocks for referenced Units
- clean-video declaration when relevant
- high-risk text words
- state consistency placeholders for product-specific rules

Then add product-specific checks derived from actual failure risks. Validator success is not proof of video quality, but validator absence is a maturity risk.

Bad cases must be assigned:

| Failure type | Update location |
|---|---|
| Product structure or state failure | `references/product-rules.md` |
| Material selection failure | `references/asset-manifest.md` |
| Prompt wording failure | `references/gotchas.md` |
| Repeatable detectable failure | `scripts/validate_*.py` |
| Trigger or routing failure | `references/trigger-tests.md` and `SKILL.md` description |

## 16. Industry Hard Rules U1-U32

The following rules are the industry baseline. A SKU or category skill may tighten them, but must not silently weaken them.

| ID | Rule |
|---|---|
| U1 | Use realistic ecommerce seed-video aesthetics unless the user explicitly requests TVC/grid. |
| U2 | Keep generated video clean: no AI-added subtitles, stickers, watermarks, or decorative text overlays. |
| U3 | Product or product-use context appears in the opening beat of the opening unit. |
| U4 | Every shot serves a selling point, narrative beat, or proof need. |
| U5 | Functional selling points require visual proof action or proof state. |
| U6 | Use concrete verbs and sensory details; avoid manual-like "show/display" phrasing. |
| U7 | Reference roles must be declared for every @ image/video in both the material table and the Unit prompt's `【素材说明】` / `Reference Materials` block. |
| U8 | Reference order must match @ numbering and API/material counts. |
| U9 | Choose references by semantic role and product state, not by filename attractiveness. |
| U10 | Minimize references that can conflict; more images can create more visual interference. |
| U11 | A/B classification starts from product state change, but creator-confirmed standards and current-run judgment are final. |
| U12 | One B unit uses one action video by default. |
| U13 | B prompt does not describe the reference video's action timeline. |
| U14 | B background/environment follows narrative physical space, not blindly the main scene. |
| U15 | A-out and A-in states must not conflict in one unit. |
| U16 | Script keyword/entity extraction and script-Unit-material audio-visual arrangement are required before prompt writing. |
| U17 | Second-pass audio-visual sync audit is required after prompt writing, including concrete visual coverage for scene/time/drink/food/lifestyle words. |
| U18 | High-risk text/logo/UI regions are anchored visually, not rewritten as exact prompt text. |
| U19 | Product physical logic must be true: water direction, opening direction, wearable state, scale, and contact points. |
| U20 | Complex actions need video or implied-action montage; do not over-describe fragile motion. |
| U21 | Character/person assets must match the actor doing the action. |
| U22 | Fixed or large products need stable space anchoring across units. |
| U23 | Every visible component needs a matching reference or a clear downgrade route. |
| U24 | Approved material version must be explicit; runtime assets stay pending until approved. |
| U25 | Prompt-plan placeholders must be zero before generation handoff. |
| U26 | Image/video preprocessing and upload chain must be explicit when generation is part of the workflow. |
| U27 | Skill version changes must note downstream prompt-plans affected. |
| U28 | Generation task health should be monitored; stuck jobs need cancel/retry policy when tools exist. |
| U29 | Bad cases must be folded back into rules, manifests, gotchas, or validators. |
| U30 | Production stage is batch mode after the SKU Skill passes: batch scripts require batch prompt-plans, material arrangements, validation records, and video task inputs. |
| U31 | **Scene-adaptive narrative quality gate (§11.5).** Every A-class Unit must pass six quality checks: Q1 ≥2 scene-specific micro-actions (no generic); Q2 ≥3 scene-specific props with visual identity; Q3 clear emotional arc (from→to); Q4 person is protagonist, product serves the story; Q5 no long continuous pure-product segment that breaks lifestyle rhythm (except universal clips); Q6 closing has "enjoying the result" moment. For non-default-scene scripts, the executor must complete the four-step scene derivation (§11.5 Steps 1-4) and output a Scene Narrative Adaptation Table before writing any A-class prompt. |
| U32 | **Unit Scope Contract (A-class submit prompts).** Every standard A-class Unit must declare: (1) **unit goal** — `本段只做一件事` / one-sentence proof target; (2) **action flow** — one paragraph of motion/camera/emotion, not a segmented second-by-second timeline; (3) **end condition** — `结束条件` / which frame the clip stops on. Do **not** write second-marked timeline segments for standard A units. If the SKU documents an explicit bridge-beat or universal-clip exception, keep the prompt prose compact and do not expose concrete second marks. B-class still follows U13: no action timeline in prompt. |

## 17. Method Rule

There are only two top-level production methods:

- Direct-generation flow: default. Script -> unit split -> A/B classification -> prompt-plan -> video.
- Grid/TVC flow: only when the user explicitly asks for TVC, advertising, grid/storyboard, or a similar commercial workflow.

Older labels such as real-shot background replacement, reference-video method, and oral-direct method are material situations inside direct-generation flow, not separate creator methods.
