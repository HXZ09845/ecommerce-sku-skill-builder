# Gotchas - Industry General SKU Skill Creator V2

Keep real failures here. When a new SKU produces a repeatable bad case, route it to the relevant product skill and consider whether the pattern belongs in this industry-level file.

## Creator Workflow Failures

| Failure | Symptom | Prevention |
|---|---|---|
| Starting from prompt writing | The skill lacks product structure, material logic, and reusable rules | Start with product understanding and component/state matrix |
| Skipping production archetype routing | Prompt style, A/B split, and bad-case prevention come from the wrong case family | Choose large fixed A+B, small movable A+B, or pure A non-deforming/wearable before core asset inventory |
| Skipping golden case abstractions | Hallucination points and A/B rules are invented from general intuition instead of applying the built-in tea-bar, cup/container, shoes/apparel, or wearable abstractions | Apply `golden-case-abstractions.md`, record the case family used, and route each learned failure to rules, manifest, gotchas, validator, or prompt-plan checks |
| Skipping the core asset layer | Logo, environment, rhythm, prompt form, and submission rules stay implicit | Create the core asset inventory before selling-point mapping |
| Skipping audio-visual sync arrangement | Script, proof route, materials, Unit duration, and prompt wording are each reasonable but do not work together | Fill the script-Unit-material arrangement before prompt writing |
| Misreading script stage | Test-stage 1-2 scripts are treated as production batch, or production batch is treated as one-off testing | Record stage first: test creates initial SKU Skill and visual feedback; production batch generates plans/material arrangements/video task inputs after the Skill passes |
| Asking for all assets first | Creator has to over-prepare before proof strategy is known | First round is product understanding only |
| Batch-approving selling-point materials | Several selling points appear mapped, but the chosen real-shot references have not passed creator/operator material-selection judgment | Run one selling point at a time: propose candidate references, dialogue-test the proof route, record rejected materials, and only move on after status is `OK` |
| Treating weak category meta as blocker | New products stall when the category meta is incomplete | Use industry rules plus nearest golden SKU cases as fallback |
| Copying old SKU rules directly | Old colors, file names, failed methods, or selling-point order leak into new SKU | Use `可继承 / 需改写 / 禁止继承` before applying old cases |
| Producing old package shape as primary output | Coworkers cannot load it as a Codex skill cleanly | Generate standard Codex package shape |
| Generated SKU is not self-contained | A coworker cannot use the package without the creator, another package, local paths, or hidden source folders | Inline all runtime rules into the target package and run the self-contained handoff audit |

## Product And State Failures

| Failure | Symptom | Prevention |
|---|---|---|
| Missing component/state matrix | Open, closed, filled, empty, worn, folded, or color states conflict | Confirm component/state matrix before rules |
| A-out/A-in mixing | Internal parts appear in closed-product scenes, or closed shell appears in internal scenes | Separate A-out and A-in units and references |
| B-class still-image conflict | Product transition follows still image state instead of action video | Do not add conflicting stills to B state-change units |
| Fixed product spatial drift | Large product jumps between rooms/walls/surfaces | Use fixed product-containing anchor and restate position |
| Wearable product detached from body | Clothing/shoes/bags look like flat product ads when worn-state proof is needed | Treat person-product relationship as a state requirement |

## Material Failures

| Failure | Symptom | Prevention |
|---|---|---|
| Assets chosen by prettiness | Video looks good but does not prove the copy | Map copy -> selling point -> visual proof -> asset |
| Reference roles missing | Model uses detail image as full product, or scene as product | Declare what every @ reference controls and does not control |
| Reference explanation missing in prompt | The material table is correct, but the video model still treats every reference as a full-scene instruction | Put a concise `【素材说明】` block inside each Unit prompt, explaining every `@图片` and `@视频` separately |
| Too many references | Visual averaging, text distortion, state pollution | Use P0/P1/P2 roles and remove nonessential references |
| High-text closeup overloaded | Screen, label, logo, or print becomes gibberish | Use fewer materials, minimal motion, and universal clips |
| Unapproved runtime assets | Wrong material version enters final package | Keep assets pending until creator approves source version |

## Prompt And Video Failures

| Failure | Symptom | Prevention |
|---|---|---|
| B prompt describes action timeline | Reference video and prompt fight each other | B prompt assigns roles and background only |
| A prompt uses segmented second-by-second timeline | Prompt bloat dilutes model attention; timing rarely improves control vs. a clear end condition | Use unit goal + one action-flow paragraph + end condition (U32) |
| A prompt lacks unit goal or end condition | Model drifts across multiple proof targets in one clip | Declare `本段只做一件事` and `结束条件` in every standard A-class prompt |
| B background copies main scene blindly | Copy says school/office/road but background stays kitchen/home | Use narrative environment from copy mapping |
| Copy nouns disappear | Voiceover mentions bag, coffee, parents, office, or food but video lacks it | Fill copy-keyword to visual-element table before prompts |
| Scene/time/drink words stay abstract | Copy says "summer" or "coffee" but prompt only says "summer vibe" or "coffee bokeh" | Convert script keywords into concrete visual entities such as daylight, ice/cold drink cue, coffee cup/liquid, cafe table, laptop desk |
| B background uses the wrong physical place | B action video background is replaced with the main scene while the copy beat happens elsewhere | Determine actual physical environment from the copy timeline; B background target follows that environment |
| A+B material roles conflict | A reference supplies one state/environment while B video controls another, producing product or background drift | Declare which asset controls identity, environment, props, person, and B action; split Unit if roles cannot coexist |
| Script and prompt drift apart | The prompt follows pretty materials while the voiceover is proving another selling point | Bind every copy beat to selling point proof, Unit, material role, and prompt action before writing prompts |
| Unit proves too many things | One Unit tries to cover multiple claims, causing weak proof or product drift | Split by proof target, product state, A/B type, scene change, or TS risk |
| A/B row not creator-confirmed | The agent's default classifier conflicts with creator/operator's production judgment | Mark key rows for creator confirmation and follow the creator's decision |
| Audio-visual sync overfit | Prompt forces every copy detail into one fragile Unit, causing identity drift or action failure | Split Units, reduce references, use result-state proof, or request creator-approved downgrade |
| Test script lessons not folded back | Test-stage outputs improve once but the SKU Skill does not become more stable | Route repeated issues to product rules, manifest, gotchas, validator, or prompt-plan format |
| TS swap-back risk ignored | Product state, background, logo, or material identity changes mid-plan or between Units | Add a TS risk line per Unit and route prevention to rules, manifest, gotchas, or validator |
| Complex physical action over-described | Hands, lids, liquid, body parts, or mechanisms hallucinate | Use video or implied-action montage; direct only simple verified actions |
| Exact text requested in prompt | Screen/logo/label/print mutates into unreadable text | Use reference as visual texture; exact claims go to VO/post |
| Placeholders remain | `{待提供}` or placeholder text causes missing anchors | Grep placeholders before generation handoff |

## Validation Failures

| Failure | Symptom | Prevention |
|---|---|---|
| Validator only checks generic syntax | It passes while product-specific failures remain | Derive validator checks from product hard rules and bad cases |
| No representative prompt-plan | Skill looks complete but cannot drive a real script | Generate and validate at least one prompt-plan |
| No audio-visual sync audit | Validator can pass while copy, prompt, and materials are misaligned | Require the post-prompt sync audit table before handoff |
| Bad cases not routed | Same error repeats across scripts | Record failure and update product rules, manifest, gotchas, or validator |
| Version changes do not refresh downstream plans | Existing prompt-plans mix old and new rules | Version history must include impact and refresh status |
