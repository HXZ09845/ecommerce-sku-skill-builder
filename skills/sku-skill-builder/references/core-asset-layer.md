# Core Asset And TS Risk Layer

Use this layer after product understanding and component/state analysis, before selling-point material mapping and prompt writing. Its job is to preserve the real reusable assets from high-quality cases: product identity, logo/text handling, environment anchoring, rhythm, unit splitting, prompt form, submission contract, and bad-case prevention.

This file is a method layer, not a fixed case library. Concrete cases are sources for abstraction only.

## 1. Production Archetype Router

Choose exactly one production archetype before core asset inventory, selling-point mapping, or prompt writing. The archetype is the first abstraction layer; it decides which prompt form, hallucination controls, material rules, and bad-case prevention to load.

After choosing the archetype, apply the matching golden case abstraction family that was already written into this SKU package during creation. In a generated product SKU Skill, do not instruct the user to read the parent creator or any external Skill. Core assets and TS risks should cite the abstraction family, not an external file dependency.

```text
生产原型判断
| Product signal | Production archetype | A/B shape | Prompt learning focus | Hallucination guard | Bad-case prevention |
|---|---|---|---|---|---|
```

### Archetype 1: Large Fixed A+B

Use for tea-bar-machine-style large appliances and other products that live in a fixed space but still need both A-class lifestyle shots and B-class state/action/reference-video shots.

- Product signals: large appliance, fixed location, wall/cabinet/floor/counter relationship, screen/panel/logo risk, user interaction around the product, real-shot case video shows space and placement.
- Prompt learning focus: slower stable rhythm, fewer scenes, product-containing environment anchor, repeated product position line, **A-class unit goal + action flow + end condition (U32, no segmented second-by-second prompt prose)**, B prompt assigns role/background instead of rewriting action timeline.
- Hallucination guard: do not let pure environment images control product placement; protect screens, labels, logos, and buttons as visual texture unless exact text is verified; do not move the product between rooms or surfaces inside one Unit.
- Bad-case prevention: fixed-space drift, background replacement that forgets the product, exact-text hallucination, over-fast cuts, B still-image conflict, environment copied from reference when the copy asks for another scene.

### Archetype 2: Small Movable A+B

Use for cups, bottles, thermos products, food containers, small table objects, handheld products, and nested/assembled objects that have static A scenes plus possible B-class actions.

- Product signals: handheld or tabletop product, components/lids/inner state, filled/empty/open/closed states, pouring/opening/closing/assembling/placing actions, scene can move across desk, kitchen, office, school, bag, or outdoor micro-environments.
- Prompt learning focus: component/state matrix, A-out/A-in separation, copy-to-visual proof mapping, scene signal words, material purpose declaration, one B video for one state-changing action, duration following the reference video.
- Hallucination guard: do not mix internal and external states; do not attach closed-state stills to state-changing B actions; keep color/version consistent; declare what each reference controls and does not control.
- Bad-case prevention: state conflict, component invention, handle/straw/lid/liquid hallucination, over-dense reference sets, unsupported selling-point proof, B action fighting the prompt.

### Archetype 3: Pure A Non-Deforming / Wearable

Use for shoes, clothing, bags, accessories, and other products where the expected video can be solved with A-class static/result states because the product does not need a state-changing B action.

- Product signals: no required product deformation or mechanism transition, product identity is a worn/used result state, model/person/body relation is part of the product state, claims are proven by styling, movement, fit, texture, or scenario.
- Prompt learning focus: worn/used state as identity anchor, product and body inseparability, model-worn or in-use P0 asset, complete production Units when suitable, action library that proves claims without changing product structure.
- Hallucination guard: do not build the video from flat lays only when worn proof is needed; protect logo/print/pattern/pocket/sole/shape details; do not let environment references override product-body relation.
- Bad-case prevention: fake pattern/logo, product detached from body, wrong fit/silhouette, invented components, pure static product ad when the claim needs movement, unnecessary B-class action.

## 2. Built-In Abstraction Families

Use these abstraction families as internal methods, not as external references.

| Abstraction family | Archetype | Reusable method | Do not over-copy |
|---|---|---|---|
| Fixed-space appliance | Large fixed A+B | Product-containing environment anchors; slower stable rhythm; B-class background replacement must still preserve product position; high-text closeups become universal clips or short low-motion shots | Do not copy rooms, models, exact B assets, or case-specific exceptions to unrelated products |
| Drinkware and small table objects | Small movable A+B | Component/state matrix first; A-out/A-in split; scene micro-environment words; copy-to-visual mapping; B class uses one action video for one state-changing action | Do not treat every cup-like product as the same structure; multi-drink, straw, lid, handle, rope, and inner state must be re-derived |
| Nested or internal/external containers | Small movable A+B | Internal/external state separation; sequence order matters; do not attach closed-state stills to state-changing B units; same-color material matching reduces drift | Do not use internal-component images in external lifestyle units |
| Wearable and body-linked goods | Pure A non-deforming/wearable | Product and body are one state; worn/in-use image is the identity anchor; logo/print needs repeated guarded anchoring; pure environment references may over-constrain and are optional when text can describe the scene | Do not build a wearable video from flat lays alone when worn/in-use proof is required |
| Cross-family production hygiene | All archetypes | Unit density, A/B prompt forms, scene signal words, material purpose declaration, preprocessing checks, and pre/post copy-to-visual validation are reusable operating rules | Do not carry legacy package shapes or exact historical case surfaces forward as runtime dependencies |

## 3. Core Asset Inventory

Before writing SKU rules, create this inventory:

```text
| Asset layer | What to extract | Source | Controls | Must not control | TS risk | Rule destination |
|---|---|---|---|---|---|---|
| Identity/logo | product silhouette, color, logo, label, screen, print, proportions | brief / product images / video | identity, version, readable-risk zones | exact generated text unless verified | logo drift, text hallucination | product-rules / manifest / validator |
| Structure/state | components, default/result states, moving parts, internal/external states | brief / video / current-run source notes | state consistency, A/B split | impossible mixed states | state swap, wrong component | product-rules / validator |
| Environment | where the product lives, whether product position is fixed, scene micro-words | video / brief / script / material | space, mood, product position when product-containing | product identity unless declared | background drift, product relocation | product-rules / manifest |
| Rhythm | case-video pacing, Unit duration, scene density, slow/fast logic | case video / script | cut density and shot length | product state | over-fast cuts, weak proof | prompt-plan-format |
| Action | simple direct actions, B-only state changes, implied-action candidates | case video / component matrix | action feasibility | text claims not visible | hand/action hallucination | product-rules / gotchas |
| Copy/audio | VO lines, flower words, required nouns/verbs, timing pressure | script / selling points | proof target and audio-visual sync | material choice by prettiness | audio-visual mismatch | prompt-plan-format |
| Prompt form | A template, B template, material purpose block, clean-video line | high-quality cases | instruction priority | action timeline in B units | prompt fights reference | gotchas / validator |
| Submission | per-Unit references, API counts, duration, ratio, compression/upload chain | model requirement / prompt-plan | reproducibility | hidden local-only assets | missing refs, API mismatch | prompt-plan-format |
| Bad cases | known drift, swap-back, text, state, hand, material failures | trial output / old cases | prevention rules | unverified one-off conclusions | repeated failure | gotchas / validator |
```

Also create an abstraction-to-core-asset bridge:

```text
黄金案例抽象到核心资产
| Case family | Reused abstract method | Current SKU adaptation | Hallucination point covered | A/B impact | Destination |
|---|---|---|---|---|---|
```

## 4. Unit Split And Rhythm Rules

Split Units from copy, proof need, product state, and TS risk, not from arbitrary equal time.

| Production archetype | Default Unit rhythm |
|---|---|
| Large fixed A+B | Slower rhythm; fewer shots; preserve fixed product position; use lifestyle return structure |
| Small movable A+B | Higher density; each Unit should contain several concrete scene beats and micro-environment anchors |
| Pure A non-deforming/wearable | Complete production units work well when suitable; product must appear worn/used early; movement and styling prove claims |
| B-class state-changing action | Duration follows the reference video, usually rounded up; one B Unit should use one action video by default |

Every Unit must record:

```text
| Unit | copy range | proof target | state | A/B | duration | rhythm reason | TS risk | downgrade |
|---|---|---|---|---|---:|---|---|---|
```

## 5. Audio-Visual Sync Versus TS Risk

Read `references/audio-visual-sync.md` before prompt writing. Do not blindly maximize audio-visual sync if doing so creates fragile generation points. Balance the two:

| Situation | Preferred move |
|---|---|
| Copy contains a visible noun | Make the noun visible in the mapped Unit, or ask to rewrite/cut the claim |
| Copy contains a complex action without video | Use implied-action montage or result-state proof; ask creator before downgrading |
| Copy asks for exact readable text | Put exact claim in VO/caption/post; treat source text as visual texture |
| Copy demands a state change | Use B video if available; otherwise downgrade to A-in/A-out result state |
| Sync would require too many references | Choose the minimum proof references and record what is intentionally not controlled |
| A unit becomes a swap-back risk | Shorten the beat, reduce references, simplify movement, or split into safer Units |

TS risk means any point likely to cause product identity drift, environment swap, state conflict, logo/text hallucination, hand/action failure, or reference/API mismatch during test submission. Add a TS risk line before prompt handoff.

```text
TS 风险：{risk}; 规避：{prompt/material/unit choice}; 仍需复测：yes/no
```

Before prompts, always create:

```text
文案语义抽取表
| 文案原句 | 显性词 | 隐性场景/情绪 | 实际物理环境 | 必须出现的具象画面 | 可选素材类型 | 禁用空泛表达 | 备注 |
|---|---|---|---|---|---|---|---|

脚本-Unit-素材编排表
| Script | Unit | 文案范围 | 显性/隐性关键词 | 实际环境 | 具象画面实体 | 证明目标 | 画面动作/关键帧 | 产品状态 | A/B | 素材组合 | 时长/节奏 | 禁用素材/状态 | TS风险 | 降级方案 | 确认 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Use scripts differently by stage:

- Test stage: use the usual one or two provided scripts to create the first SKU Skill draft, test visual output, collect feedback, and fold bad cases back into rules.
- Production stage: batch scripts are provided after the skill has passed; batch-generate prompt-plans, material arrangements, validation records, and video task inputs.

The creator has final judgment on key A/B rows. If the agent's state-based suggestion differs from the creator's standard, record both and follow the creator's decision.

Script words like `夏日`, `喝咖啡`, `办公室`, `车里`, or `送到` are core sync assets. Convert them into concrete visible entities and actual physical environments before selecting A, B, or A+B mixed materials.

## 6. Prompt And Material Submission Contract

Before generation handoff, each Unit must have:

- production archetype and why this Unit follows or deviates from it
- copy range and proof target
- declared A/B/A-out/A-in type
- duration and reason
- reference materials with roles, states, controls, and does-not-control notes
- material purpose block copied into the prompt
- state consistency line
- TS risk and downgrade line
- API count table matching the prompt references
- preprocessing/upload status for every referenced file

B-class Units additionally require:

- exactly one action video by default
- duration based on the source video, rounded up when needed
- prompt states that the video controls action, rhythm, viewpoint, and product state change
- prompt does not describe the action timeline
- conflicting still images removed unless product rules explicitly narrow their role

## 7. Promotion Rule

Promote only the method, not the case-specific surface.

| Promote to industry meta | Keep inside target SKU/category |
|---|---|
| three-archetype router, inventory tables, state consistency gate, Unit risk gate, material purpose declaration, copy-to-visual pre/post checks, B-class one-video default, API count matching | exact product names, model IDs, file names, case-specific rooms, colors, validated exceptions, brand-only rules |
