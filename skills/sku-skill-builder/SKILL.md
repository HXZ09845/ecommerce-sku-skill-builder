---
name: sku-skill-builder
description: "Industry-general SKU Skill Creator V2.3 for ecommerce AIGC short-video workflows. Use when creating, updating, auditing, or migrating concrete product SKU Skills; when the user says 新品Skill, SKU Skill, 品类Skill, 行业通用Meta, sku-skill-builder, Skill Creator, 做新品类Skill, 旧SKU迁移, 按最高规格创建Skill; or when Codex must turn a new product, selling-point table, case video, or old SKU package into a publishable Codex skill package with SKILL.md, references, scripts, assets, and agents/openai.yaml. Current focus is concrete product SKU Skill building; future abstract category skills may be created with this workflow, but only as support layers for building concrete SKU Skills."
---

# SKU Skill Builder

Use this skill as the industry-general creator for new ecommerce product/SKU video-generation skills. It does not merely write prompts. It guides the creator from product understanding to selling-point proof, material mapping, standard package drafting, validation, and bad-case regression.

Current-stage focus: build concrete product SKU Skills well. The same workflow can later generate abstract category skills when enough qualified concrete SKU Skills exist, but those abstract category skills are still meant to help create future concrete product SKU Skills. Do not treat category abstraction as the main task unless the creator explicitly asks for it.

Default output is a publishable Codex skill package:

```text
skill-name/
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
    validate_*.py
  assets/
```

Do not make an old three-file package as the primary deliverable. If converting older Cursor-era materials, preserve them as source inputs and create the standard Codex package as the normalized output.

This creator also has meta-only references such as `references/golden-case-abstractions.md`; use them while building the target SKU skill. They are self-contained abstractions, not dependencies on other Skills.

Generated product SKU Skills must be self-contained handoff packages. The target SKU package must not require this creator, a category meta Skill, a golden case Skill, local source folders, or any external Skill to work. Every rule needed at runtime must be written into the target package's own `SKILL.md`, `references/`, `scripts/`, or `assets/`.

## Operating Contract

1. After loading this skill, guide the creator with a fixed beginner-safe intake. Do not say "provide any one thing" or jump straight to final Skill writing. Use named input slots, explain the next output, and let missing items be marked `pending`.
2. Start with source confirmation. Read the current-thread industry-general meta first, then category meta if available, then old SKU references.
3. If category meta is missing or weak, continue with this industry meta plus nearest verified SKU cases; do not block on absent category meta.
4. First understand the product. Do not ask for the full approved material library or write final rules in the first round unless the creator explicitly provides everything.
5. Confirm product structure and state matrix before detailed rule writing.
6. Classify the product into one production archetype before prompt writing: large fixed A+B, small movable A+B, or pure A non-deforming/wearable.
7. Treat A/B judgment as the most important decision gate. The creator's explicit standard and current-run judgment override default heuristics; when uncertain, present the reasoning and wait for confirmation.
8. Apply the built-in golden case abstractions for the chosen archetype. Extract hallucination points, A/B handling, prompt safeguards, material rules, and validator hooks from those abstractions.
9. Extract the core asset layer from high-quality cases and current inputs: identity/logo, environment, rhythm, action, prompt form, submission contract, and TS risk.
10. Map selling points to visual proof one by one. For each selling point, propose candidate real-shot reference choices and run a dialogue test with the creator's historical material-selection experience before marking it `OK`. Do not move to the next selling point until the current selling point's proof route, reference type, product state, A/B judgment, forbidden materials, and downgrade route are confirmed.
11. Build the audio-visual sync arrangement before prompt writing: script copy -> concrete visual entities -> actual environment -> selling point proof -> Unit -> material roles -> prompt action -> TS risk. Do not write prompts from copy alone or from materials alone.
11.5. **Scene narrative derivation (§11.5 in product-rules.md).** If the script scene is NOT the product's default/primary scene, complete the four-step derivation before writing any A-class prompt: Step 1 scene micro-actions → Step 2 scene-specific props → Step 3 emotional arcs → Step 4 narrative quality self-check (Q1-Q6). Output a "Scene Narrative Adaptation Table" at the top of the prompt plan. Default-scene scripts may skip Steps 1-3 but must still pass Q1-Q6.
12. Every Unit prompt that uses `@图片` or `@视频` must include a concise `【素材说明】` / `Reference Materials` block explaining what each reference is, what it controls, what it must not control, and which selling point or copy beat it supports.
13. Classify each unit as A, A-out, A-in, or B from product state behavior, then confirm key rows with the creator. Do not silently pick "enough" assets.
14. Keep runtime assets pending until the approved material version is selected. In test mode, one or two scripts create the first skill draft and visual-feedback loop; in production mode, batch scripts drive batch prompt-plans, material arrangements, validation, and video task inputs.
15. Generate a standard skill package only after product understanding, production archetype, golden-case abstraction, core asset inventory, selling-point proof, audio-visual sync, and material strategy are aligned.
16. Run a self-contained handoff audit: no external Skill dependency, no local absolute path dependency, no "read the parent/meta/golden Skill" instruction, and all runtime references resolve inside the target package or are explicitly `pending`.
17. Validate with a representative prompt-plan and product validator; feed bad cases back into rules, gotchas, manifest, or validator.

## Required Workflow

1. Read `references/creator-onboarding.md` before the first response to the creator. Use it to ask for named first-round inputs and explain the staged process in beginner-safe language.
2. Read `references/sku-creator-workflow.md`.
3. Read `references/product-rules.md` for industry hard rules, A/B logic, material roles, state consistency, prompt-plan requirements, and case abstraction rules.
4. Read `references/golden-case-abstractions.md` after choosing the production archetype. Use its built-in tea-bar, cup/container, shoes/apparel, and bag-like wearable abstractions for hallucination points and A/B handling. Do not load external Skills unless the creator explicitly provides a current-run source to abstract.
5. Read `references/core-asset-layer.md` before selling-point mapping or prompt writing. Use it first to choose the production archetype, then extract logo/text, environment, rhythm, Unit splitting, prompt form, submission, and TS-risk rules from high-quality cases and current inputs.
6. Read `references/audio-visual-sync.md` before prompt writing. Use it to bind script copy, concrete visual entities, actual environment, selling-point proof, Unit split, A/B or A+B material roles, prompt action, duration, and TS-risk downgrade.
7. Use `references/category-questionnaire.md` for staged creator questions and confirmation cards.
8. Use `references/method-decision-tree.md` to choose generation method. Default to direct-generation; only use grid/TVC flow when the user explicitly requests TVC/advertising.
9. Use `references/skill-template.md` when drafting the target SKU skill package.
10. Use `references/asset-manifest.md` when defining semantic asset roles and approved/pending runtime assets.
11. Use `references/prompt-plan-format.md` when validating the representative script plan.
12. Use `references/gotchas.md` before handoff and when folding in bad cases.
13. Use `references/validate-template.py` and product-specific cases to create `scripts/validate_*.py`.
14. Use `scripts/scaffold_category_skill.py` only as a starting scaffold, then refine with the real product rules.

## Category Meta Fallback

Prefer a mature category meta when it exists, but treat it as an assistant, not a blocker.

| Product signal | Preferred meta | If weak or absent |
|---|---|---|
| Cups, bottles, thermos, drinkware, food containers | cup/category meta | Use drinkware/container golden cases plus industry state matrix and material roles |
| Apparel, shoes, bags, wearable goods | apparel meta | Use wear-state rules: product and body are inseparable unless the script explicitly asks otherwise |
| Appliances, kitchen/cleaning/personal-care devices | appliance meta | Use component/state/action-risk analysis from appliance and tea-bar cases |
| Other ecommerce products | nearest verified SKU cases | Start from industry rules, then build a thin SKU-specific rule system from product structure |

When using old SKU references, output `可继承 / 需改写 / 禁止继承` before applying any rule.

## Quality Gates

- The creator was guided with named first-round input slots, not asked to provide an arbitrary source or material.
- The source confirmation card was produced.
- Product understanding and component/state matrix were confirmed by the creator.
- The product was classified as large fixed A+B, small movable A+B, or pure A non-deforming/wearable, with the reason recorded.
- A/B key rows were confirmed by the creator or explicitly marked pending for creator judgment.
- Golden case abstractions were applied to hallucination points and A/B handling before rules were finalized.
- Core asset inventory and TS risk table were created before prompt writing.
- Every core selling point has a creator-confirmed visual proof route and has passed a one-by-one dialogue test before the next selling point starts.
- The creator's historical material-selection judgment is recorded for accepted real-shot reference choices, rejected attractive-but-off-message materials, A/B decisions, state conflicts, and downgrade routes.
- Every script line or copy beat is mapped to concrete visual entity, actual environment, Unit, proof target, material role, prompt action, duration/rhythm, and TS risk before prompt writing.
- Every Unit prompt with `@图片` or `@视频` includes a concise material-purpose block explaining each reference separately.
- The material map records P0/P1/P2 roles, required state, forbidden state, and downgrade route.
- The SKU skill package is standard Codex shape, not a legacy primary package.
- The generated SKU skill is self-contained and does not depend on this creator, category meta Skills, golden case Skills, or local source paths.
- `SKILL.md` in the generated SKU is lean; detailed rules live in `references/`.
- Runtime assets are approved or explicitly `pending`.
- Trigger tests include should-trigger and should-not-trigger examples.
- **Scene-adaptive narrative quality gate (U31)**: every A-class Unit passes Q1-Q6 checks — Q1: ≥2 scene-specific micro-actions (no generic); Q2: ≥3 scene-specific props; Q3: emotional arc (from→to); Q4: person is protagonist; Q5: no long continuous pure-product segment that breaks lifestyle rhythm; Q6: closing satisfaction moment. Non-default-scene scripts must complete §11.5 four-step derivation first.
- **Unit Scope Contract (U32)**: every standard A-class submit prompt declares unit goal + action flow + end condition; no segmented second-by-second timeline. Exceptions such as bridge beats or universal clips must be documented without writing second-marked prompt prose.
- A representative prompt-plan includes material table, A/B classification, audio-visual sync mapping, API/material counts, and validation record.
- Product-specific validator runs without interface errors.
- Known bad cases are assigned to gotchas, product rules, manifest, or validator checks.
