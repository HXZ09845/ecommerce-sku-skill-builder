# Golden Case Abstractions

Use this self-contained rule bank before writing hallucination rules, A/B rules, or prompt templates for a new SKU Skill. These rules are already abstracted from high-quality prior cases. Do not treat this file as an instruction to load or depend on those prior Skills at runtime.

Core principle:

```text
黄金案例只提供抽象规则，不作为运行时依赖。
母 Skill 内置这些抽象后的结构化规则；生成新品 SKU Skill 时直接使用本文件。
只有当用户在当前对话明确提供新的案例 Skill/文件时，才把它当作本轮输入继续抽象。
```

When creating a target product SKU Skill, copy or rewrite the relevant abstract rules into that target package's own `references/product-rules.md`, `references/gotchas.md`, `references/asset-manifest.md`, or `scripts/validate_*.py`. The generated target package must not require this file at runtime.

## 1. Case Families

| Production archetype | Case family | Use for | Abstracted learning goal |
|---|---|---|---|
| Large fixed A+B | Tea-bar-style large appliance | Floor-standing or countertop appliances with fixed space, screens, panels, cabinets, water/heat/action clips | Fixed-space prompt structure, B-video priority, text/screen hallucination handling, slow lifestyle rhythm |
| Small movable A+B | Fanhua / ice cup / drinkware container | Cups, bottles, thermos products, food containers, handheld/tabletop objects with lids, straws, handles, liquid, internal states | Component/state matrix, A-out/A-in split, mutually exclusive mechanisms, B one-action-video rule, source-background suppression |
| Pure A non-deforming/wearable | Shoes / T-shirt / apparel / bag-like wearables | Shoes, clothing, bags, accessories, products whose proof is worn/used rather than mechanically transformed | Product-body relation, pure A handling, safe motion library, limb/body hallucination guards, same-color detail filtering |

Bag products currently use the wearable/apparel abstraction unless a current-run bag case is provided. Mark bag-specific rules as `needs creator confirmation` when the rule depends on carrying, opening, strap length, or internal storage.

## 2. Required Abstraction Tables

Before drafting new SKU rules, output these tables from the built-in abstractions below.

```text
黄金案例抽象应用表
| Case family | Archetype fit | Abstracted rule | Applies to this SKU? | Keep / rewrite / reject | Destination |
|---|---|---|:---:|---|---|
```

```text
幻觉点与 A/B 方案抽象
| Product part / action | Likely hallucination | Abstracted evidence family | A/B decision | Material strategy | Prompt safeguard | Validator / gotchas hook |
|---|---|---|---|---|---|---|
```

Destination must be one of:

- target `references/product-rules.md`
- target `references/audio-visual-sync.md`
- target `references/asset-manifest.md`
- target `references/gotchas.md`
- target `scripts/validate_*.py`
- target prompt-plan self-check

## 2.5 Audio-Visual Sync Abstractions

Use these abstractions to write the target SKU's own `references/audio-visual-sync.md`. Do not tell the generated SKU to read this file at runtime.

```text
音画同步抽象应用表
| Case family | Sync pattern | Unit split logic | A/B impact | Material rhythm | Bad-case avoided | Destination |
|---|---|---|---|---|---|---|
```

| Case family | Sync pattern | Unit split logic | A/B impact | Material rhythm | Bad-case avoided |
|---|---|---|---|---|---|
| Tea-bar-style large appliance | Voiceover often describes a home need, then the product or B action proves it in a slower stable beat | Split by scene need, fixed product position, and B action reference | B only when real action/state video controls the process; A returns to lifestyle and fixed-space proof | Fewer references, slower cuts, product-containing environment anchor, low-motion text/screen closeups | Fixed-space drift, over-fast cuts, screen/label hallucination, B background losing product |
| Fanhua / drinkware / small containers | Copy nouns and verbs must map tightly to visible parts, states, and hand/tabletop actions | Split by A-out/A-in/B state, component mutex, and proof target | Opening/pouring/switching is B when shown as process; already-open or already-filled is A-in | Higher density, micro-scene words, exact component/state references, one action video per B Unit | Straw/lid/handle/liquid hallucination, state mixing, attractive but off-proof material |
| Internal/external containers | Copy about inner capacity, layering, insulation, or storage must use result-state proof before action claims | Split external lifestyle and internal/result proof into separate Units | Internal display is A-in; transition into internal display is B only with video | Angle completion and state-matched references matter more than scene variety | Closed/open conflict, missing inner component, impossible object placement |
| Shoes/apparel/wearables | Voiceover claims are proven through worn/use-state movement, fit, texture, and styling | Split by user action, body relation, detail proof, and scene rhythm | Body movement stays A; product mechanism changes are avoided or require video | Worn/in-use P0 early, detail inserts only when same-color/same-version | Detached product, fake pattern/logo, limb/body errors, flat-lay-only proof |
| Cross-space script stories | Copy may move across several physical spaces even when the script has one main scene name | Split or tag each copy beat by actual physical environment | A and B both follow the copy beat's actual environment; B background target is not the source-video background or the main scene by habit | Scene references should supply concrete entities; avoid vague "coffee/outdoor/office bokeh" | Audio-visual mismatch where copy says car/office/cafe but video remains kitchen/home |

When a sync requirement conflicts with hallucination prevention, prefer the safer production route and record the downgrade:

- complex action without video -> implied action or result state
- exact readable text -> VO/caption/post, source text as visual texture
- too many proof references -> split Unit or choose one dominant proof
- scene/time/drink/food/lifestyle words -> translate to concrete visual entities before prompt writing
- A+B mixed references -> declare role boundaries and remove state conflicts
- creator disagrees with default A/B -> follow creator judgment and write the impact into the target SKU rules

## 3. Large Fixed A+B Abstractions

### Prompt Structure

Use this structure when the product must stay in a fixed space:

```text
【素材说明】
@环境图 = product-containing space anchor; controls product position, scale, room light, and wall/counter/floor relationship.
@产品图 = product identity and structural proportions only.
@视频 = B action, viewpoint, timing, product state change, and camera rhythm.

【环境锁定】（when a product-containing space anchor exists）
Space layout, furniture, wall relation, product position, and light follow @环境图.
Write concrete spatial coordinates; do not compress this into narrative prose alone.

【A Unit — Unit Scope Contract】
本段只做一件事：[single proof goal for this unit, one sentence].
动作流：[one paragraph describing motion/camera/emotion flow — no segmented second-by-second prompt prose].
结束条件：[stop state — which frame the clip ends on].

Optional: 禁止内容 list for claims/actions that must NOT appear in this unit.

【B Unit】
Reference video controls action/composition/timing/state.
Prompt controls target environment, background treatment, identity safety, and forbidden additions.
Do not describe the action timeline frame by frame.
```

**Timeline policy (verified on large-appliance A/B cases):**
- Standard A-class units: **do not** write segmented second-by-second prompt prose; it dilutes model attention without improving control.
- Use **unit goal + action flow + end condition** instead.
- Exceptions: short special bridge units or universal clips may use a compact beat description, but still avoid concrete second marks in prompt prose.
- B-class: never write action timeline (unchanged — video owns timing).

### A/B Handling

| Situation | A/B decision | Rule |
|---|---|---|
| Product stands in room while people use surrounding objects | A | Product state does not change; anchor space and narrative |
| Screen/detail/material closeup with no state transition | A or universal clip | Keep motion low and references few |
| Water flow, heating, cabinet opening, mechanical operation, button sequence shown by real video | B | One B Unit uses one action video by default |
| Prompt wants complex physical action but no reference video exists | A downgrade or ask creator | Use result-state proof, implied action, or request video |

### Hallucination Controls

| Risk | Treatment |
|---|---|
| Product jumps to another room/corner | Use product-containing environment anchor; repeat fixed-position line |
| Pure environment image loses product placement | Avoid pure environment as the only spatial anchor when product position matters |
| B video fights product stills | Keep B material lean; video controls state/action; no extra product stills unless narrowly scoped |
| Screen/label/remote/button text mutates | Treat text as visual texture; exact numbers/claims go to VO/post |
| Large appliance becomes tabletop object | Include whole-product scale/proportion lock and floor/counter relation |
| Slow rhythm becomes empty | Add lifestyle foreground, one evidence insert, and return to context |

## 4. Small Movable A+B Abstractions

### Prompt Structure

Use this structure for cups, containers, and handheld/tabletop products:

```text
【状态判定】
当前 Unit 产品状态：A-out / A-in / B。
本 Unit 禁止混入的状态：...

【素材说明】
@外观图 = closed/default exterior identity only.
@内部图 = opened/internal/result state only.
@动作视频 = state-changing process only.
@场景/人手图 = mood, hand posture, or context only; does not override product state.

【Prompt】
Scene is newly described by the prompt unless the material is explicitly declared as environment control.
Product state stays consistent through the Unit.
If B: action comes from @视频, prompt only assigns target background and safety constraints.
```

### A/B Handling

| Situation | A/B decision | Rule |
|---|---|---|
| Closed exterior, handholding, tabletop, car cup holder, lineup | A-out | Use default/closed exterior references only |
| Already open, already filled, internal coating visible, straw already up, drink mouth already open | A-in | Use matching result-state references only |
| Opening lid, unscrewing cap, switching mouth, straw popping/removal, pouring with visible state transition | B | One state-changing video per B Unit by default |
| Copy needs a state change but no video exists | Downgrade | Use before/after result states or ask creator for B video |

### Hallucination Controls

| Risk | Treatment |
|---|---|
| A-out/A-in state mixing | Split Units and references by state |
| Mutually exclusive mechanisms appear together | Name the physical mutex: straw vs direct mouth, cap closed vs cap open, filled vs empty |
| Straw/lid/handle/liquid hallucination | Use exact component matrix; avoid unsupported component names |
| Source background pollutes target scene | Declare references control product/hand/state, while prompt controls scene |
| Too many references average product color/state | Use P0/P1/P2 roles and remove nonessential references |
| B action fights prompt | Let video control action; prompt controls role/background only |

## 5. Pure A Non-Deforming / Wearable Abstractions

### Prompt Structure

Use this structure when product proof depends on being worn, carried, or used without mechanical state change:

```text
【素材说明】
@上身/上脚/在用图 = P0 identity anchor; controls product-body relation and overall fit.
@平铺图 = structure, color, logo, pattern, front/back shape only.
@细节图 = same-color detail proof only; does not override full product.

【全局】
Product and body/use-state remain connected.
No B action unless a real product mechanism changes.
Function claims become safe body/use actions, not direct mechanical demonstrations.

【Unit rhythm】
Use a complete production Unit with several distinct scenes when suitable.
Open with the product visible in the opening beat.
Alternate full-body/in-use shots and safe detail push-ins.
```

### A/B Handling

| Situation | A/B decision | Rule |
|---|---|---|
| Walking, turning, sitting, stretching, carrying, wearing, stepping, light running | A | Body moves; product state does not mechanically change |
| Shoe slip-on action | A if simple and stable; B only if a provided video controls the transition | Avoid complex limb posture |
| Zipper, buckle, button, pocket opening, strap adjustment, drawstring tightening | Usually avoid or downgrade | Treat as high-risk detail interaction unless verified video exists |
| Bag opening or placing items inside | A result-state or ask for video | Process action is hand/object high-risk |

### Hallucination Controls

| Risk | Treatment |
|---|---|
| Product detached from body/use state | Use worn/in-use P0 when available; do not rely on flat lay only |
| Wrong color from detail image | Same-color detail references only |
| Logo/pattern/print disappears or mutates | Use visual-shape description plus precise reference role; do not ask for exact generated text |
| Extra pockets, fake patterns, wrong shoe side | Declare no extra pockets/patterns; mark inner/outer side for shoes |
| Limb/body errors | Keep legs/arms natural; avoid crossed legs, large lifted leg, dancing, multi-step finger actions |
| Reference contamination | State that flat lay/background/person clothing in references does not control scene or styling unless explicitly assigned |

## 6. Selling-Point To Safe Visual Proof

Use this table when no stronger product-specific mapping exists.

| Selling point type | Safe proof pattern | Avoid |
|---|---|---|
| Material/texture | Static or slow push-in under side/natural light; reference controls detail | Rubbing, pinching, repeated hand contact |
| Fit/shape | Full-body/in-use movement, sit/stand recovery, front/side/back turn | Static-only proof for functional fit claims |
| Design detail | Push-in to same-color detail; person naturally keeps detail unobstructed | Finger pointing, opening/closing small parts |
| Function | Indirect safe body/environment action: walking, squat/stand, breeze, sunlight, light movement | Sweat, exact liquid behavior, complex stress tests |
| Style | Scene, posture, rhythm, outfit/context harmony | Abstract words like "premium" without visual action |

## 7. Prompt Compression Rules

High-quality cases converge on the same prompt discipline:

- Images say appearance; text says state, role, constraints, and action intent.
- Every reference must state what it controls and what it must not control.
- Do not repeat all visible details from images; repetition dilutes priority.
- **Every A-class submit prompt declares a unit goal and end condition** (`本段只做一件事` + `结束条件`, or equivalent English labels). One action-flow paragraph replaces segmented second-by-second prompt prose for standard units.
- Use positive identity locks first, then short forbidden lines for known failure points.
- For exact text/logo/UI claims, use VO/post unless the model is only preserving a reference texture.

## 8. New Case Promotion

When a current-run SKU produces a repeated new bad case:

1. Record it in the target SKU `gotchas.md`.
2. Add a validator hook if detectable.
3. Promote it into this file only if it is reusable across more than one SKU or one production archetype.
4. Promote the method, not the exact product name, file path, color, room, or script line.
