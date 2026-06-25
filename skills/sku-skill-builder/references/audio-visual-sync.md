# Audio-Visual Sync Rules - SKU Skill Creator

Use this file before prompt writing. The goal is to make the script copy, visual proof, prompt, and actual materials work as one arrangement instead of four disconnected layers.

Audio-visual sync is not "match every word literally." It means every important script noun, verb, scene cue, and selling-point claim has a visible proof route, while fragile actions are downgraded before they become hallucination or TS failures.

## 1. Authority Order

Use this priority:

```text
creator A/B judgment > script copy / voiceover > selling-point proof target > approved material reality > prompt wording
```

Rules:

- A/B classification is the primary decision gate. The agent proposes the safest classification, but the creator's current-run standard is the source of truth.
- Prompt wording must serve the script and materials. Do not let an attractive material change what the copy is proving.
- If the script asks for a claim that cannot be visually proven with available materials, ask for a downgrade, rewrite, or deletion.
- If exact sync would cause state conflict, text hallucination, hand/action failure, or product swap-back, choose a safer Unit split and explain the tradeoff.

## 2. Script Modes

The creator may work in two modes.

| Mode | Input pattern | What to do |
|---|---|---|
| Test stage | Usually one or two concrete scripts | Create the first SKU Skill draft, generate a small number of prompt-plans, test visual output, collect feedback, and fold bad cases back into rules |
| Production stage | A batch of scripts after the SKU Skill has already passed | Batch-generate prompt-plans, script-Unit-material arrangements, material packages, validation records, and video task inputs |

Do not require a complete production material library before script arrangement. First establish what each copy beat needs to prove, then confirm whether the approved materials can support it. In production stage, keep each script's prompt-plan independent while reusing the approved product rules and material manifest.

## 3. Script Keyword To Concrete Visuals

Audio-visual sync happens at keyword and entity level. When the copy says `夏日`, `喝咖啡`, `办公室`, `一路上`, or `妈妈给孩子带饭`, the plan must translate those words into concrete visible objects, spaces, people, and actions.

Use this extraction table before Unit prompts:

```text
文案语义抽取表
| 文案原句 | 显性词 | 隐性场景/情绪 | 实际物理环境 | 必须出现的具象画面 | 可选素材类型 | 禁用空泛表达 | 备注 |
|---|---|---|---|---|---|---|---|
```

Examples:

| Copy signal | Concrete visual requirement | Avoid |
|---|---|---|
| 夏日 / 夏天 | bright daylight, light clothing, cold drink cue, outdoor shade, fan/ice/sunlight when relevant | only writing "summer vibe" |
| 喝咖啡 / 冰美式 / 拿铁 | visible coffee cup or coffee liquid, cafe/desk context, matching hand/drink action, product if relevant | vague "coffee bokeh" with no coffee |
| 办公室 / 工位 | desk, laptop, documents, office chair, daylight window or office lighting | generic indoor background |
| 一路上 / 车里 / 车座 | car interior, seat, bag, road/travel cue | kitchen or home table |
| 到了 / 送到 / 递过去 | destination environment and receiving action | departure environment |

Rules:

- A copy word is not covered until its visible entity is covered.
- Environment words must become physical space, not abstract mood.
- Object words must become visible props, content, or product-state proof.
- Role words must decide who appears or whose hands/asset are used.
- If a keyword cannot be safely visualized, record the downgrade or move it to VO/caption/post.
- Do not use vague environment phrases such as `咖啡散景`, `户外散景`, `办公散景`, or `室内散景` as final prompt evidence. Extract concrete entities from the scene reference instead.

## 4. Pre-Prompt Arrangement

Before writing Unit prompts, output this table:

```text
脚本-Unit-素材编排表
| Script | Unit | 文案范围 | 显性/隐性关键词 | 实际环境 | 具象画面实体 | 证明目标 | 画面动作/关键帧 | 产品状态 | A/B | 素材组合 | 时长/节奏 | 禁用素材/状态 | TS风险 | 降级方案 | 确认 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Acceptance:

- Every important script sentence is assigned to a Unit.
- Every Unit has one dominant proof target.
- Every copy keyword that affects visuals has a concrete entity or approved omission.
- Every Unit records the actual physical environment described by the copy, not only the script's main scene name.
- Every Unit declares product state and A/B/A-out/A-in/B type.
- Every required material is described by semantic role, not only filename.
- Materials may be A, B, or A+B mixed. Mixed use is allowed only when roles do not conflict and one B action video still controls the state-changing action.
- Every fragile sync point has a downgrade plan.
- Creator confirmation is recorded for A/B rows and proof rows that affect the final prompt.

## 5. Unit Splitting Rules

Split by proof and risk, not by equal clock slices.

Create a new Unit when:

- the copy changes selling point
- the product state changes
- the scene or user context changes
- the actual physical environment changes, even if the script's main scene name stays the same
- the proof method changes from static result to action/process
- a B-class action video is required
- a text/logo/UI closeup needs lower motion
- too many references would be needed in one Unit

Keep in the same Unit when:

- the copy describes one coherent proof target
- the product state stays consistent
- the same P0 identity anchor and P1 proof material can support the beat
- adding another Unit would weaken rhythm without reducing risk

## 6. A/B And Sync

Use product state behavior first, then creator judgment.

| Type | Sync behavior | Material behavior |
|---|---|---|
| A | Copy is proven through stable image-driven scenes, gesture, styling, environment, or result state | P0 identity anchor plus P1/P2 support; no state-changing reference video |
| A-out | Copy is proven while product remains exterior/default/closed | Do not include open/internal/result-state references |
| A-in | Copy is proven by already-open/internal/result state | Do not include closed-state anchors unless their role is narrowed and approved |
| B | Copy needs a state-changing action or process | One action video controls action/rhythm/viewpoint/state change by default |
| A+B mixed | Copy needs a B action while also needing A-class environment/person/product anchors | Use one B action video plus compatible A references; declare which material controls action, environment, identity, and props |

B prompt rules:

- The reference video controls the action timeline.
- The prompt should assign product role, actual narrative environment, key visible result, and safety constraints.
- Do not rewrite the action step-by-step in prose.
- B background target comes from the copy's actual physical environment, not from the script's main scene name or the original video background.
- If the creator says a row is not B, follow the creator's decision and record the reason.

## 7. Material Binding

For each Unit, bind materials like this:

```text
素材绑定表
| Unit | ref | P级 | semantic_role | product_state | controls | does_not_control | copy/proof link |
|---|---|---:|---|---|---|---|---|
```

Rules:

- P0 locks identity, product version, body relation, or fixed space.
- P1 proves the current selling point.
- P2 supports scene, human action, mood, or props.
- A material cannot control everything. Always state `does_not_control`.
- Scene/environment materials must say which concrete copy words they support.
- If a material's visible state conflicts with the Unit state, remove it or ask the creator to approve a narrowed role.

## 8. Prompt Sync Block

Each Unit prompt that uses `@图片` or `@视频` must include a short material-purpose block before the actual visual instruction. This is the historical stable pattern for preventing the model from treating every reference as a full-scene instruction.

For standard A-class prompts, place the Unit Scope Contract after the material lines: one unit goal, one action-flow paragraph, and one end condition. For B-class prompts, the reference video owns the action timeline; do not rewrite it in prose.

Keep each line short, but explain every reference separately:

- what the reference is
- whether it is P0/P1/P2 or B
- what it controls
- what it must not control
- which selling point or copy beat it supports

```text
【素材说明】
@图片1：P0，控制{产品身份/版本/空间}，不控制{不应继承的内容}
@图片2：P1，证明{卖点/部件/状态}，不控制{不应继承的内容}
@图片3：P2，控制{夏日/咖啡/办公室等文案实体或环境氛围}，不控制{产品状态/动作}
@视频1：B类动作参考，控制{动作/节奏/视角/状态变化}，不控制{背景/人物/其他}

本段只做一件事：[标准 A 类 Unit 的唯一证明目标；B 类可改为参考视频优先说明]
动作流：[标准 A 类用一段动作/运镜/情绪描述，不写具体秒段或逐秒分段；B 类不重写参考视频动作时间线]
结束条件：[标准 A 类 clip 停在哪一帧；B 类按参考视频动作结果结束]

【画面要求】
...
```

The visual instruction must use concrete visible actions and scene words. Avoid using "展示/突出/呈现" as the main proof verb.

If a prompt references materials but lacks this block, treat the prompt-plan as incomplete even when the visual prose looks good.

## 9. Post-Prompt Audit

After writing prompts, output:

```text
音画同步核对表
| Script | 文案原句 | Unit | 显性/隐性关键词 | 实际环境 | 应出现的画面/动作/实体 | 实际 prompt 是否覆盖 | 使用素材 | A/B | 风险 | 修复 |
|---|---|---|---|---|---|---|---|---|---|---|
```

Checklist:

- Each noun in the copy is either visible, intentionally omitted, or moved to voiceover/caption.
- Each verb in the copy has a physical action, result state, or approved downgrade.
- Each scene/time/drink/food/lifestyle word has a concrete visual entity or environment cue.
- Each selling point has visual proof, not just decorative footage.
- A and B materials in the same Unit have non-conflicting roles.
- B background follows the copy's actual environment.
- B Units follow video timing instead of prose timing.
- A Units do not pretend to show unsupported state changes.
- Text/logo claims are handled through VO/caption/post when exact readable text is unsafe.
- Prompt references, material table references, and API counts match.
- Each prompt's `【素材说明】` / `Reference Materials` block explains every referenced image and video separately.

## 10. Batch Production Output

In production stage, output a batch table before submitting video tasks:

```text
批量生产总表
| Script | status | prompt_plan_path | material_arrangement_path | scripts/Units | A/B counts | missing materials | validation | video_task_status |
|---|---|---|---|---|---|---|---|---|
```

Rules:

- Each script gets its own prompt-plan and material arrangement.
- Shared assets can be reused, but each Unit still needs its own material role declaration.
- Batch generation is allowed only after the SKU Skill has passed the test-stage visual feedback loop or the creator explicitly approves skipping that loop.

## 11. Bad Case Routing

If sync fails, route it before retrying:

| Failure | Route |
|---|---|
| Copy claim has no visual proof | selling-point proof table / script rewrite |
| Unit tries to prove too many things | Unit split / prompt-plan-format |
| Copy keyword has no concrete visual entity | audio-visual-sync / asset-manifest / prompt rewrite |
| B background follows the wrong place | audio-visual-sync / product-rules / prompt-plan-format |
| Action cannot be generated reliably | B video requirement / A-in result downgrade / gotchas |
| Reference state conflicts with copy state | asset-manifest / product-rules |
| Logo/text hallucination caused by sync demand | product-rules / gotchas / validator |
| API count or material count mismatch | prompt-plan-format / validator |

## 12. Done Gate

Do not hand off a prompt-plan until:

- A/B key rows have creator confirmation or are marked pending.
- The script keyword extraction table is complete.
- The script-Unit-material arrangement table is complete.
- The post-prompt sync audit is complete.
- In production stage, the batch production table exists when multiple scripts are provided.
- Every accepted downgrade is recorded.
- Every Unit prompt that uses references includes the short material-purpose block.
- Remaining TS risks have a retest note or a rule/validator destination.
