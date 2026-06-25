# Ecommerce SKU Skill Builder

An Agent Skill system for turning ecommerce product briefs, selling points, reference assets, and case videos into validated SKU-specific video-generation skill packages.

电商 AIGC 短视频并不只是写 prompt。一个可复用的 SKU Skill 需要先理解商品结构、卖点证明、实拍素材角色、A/B 状态、脚本-Unit-素材编排、验证规则和 bad-case 回归。This repository packages that production workflow as a Codex-compatible Agent Skill.

## What This Is

This project contains a publishable Agent Skill named `sku-skill-builder`.

It helps an AI coding agent create or update concrete product SKU Skills for ecommerce AIGC short-video workflows. The output target is a self-contained skill package with:

- `SKILL.md`
- `agents/openai.yaml`
- `references/`
- `scripts/`
- optional `assets/`
- representative prompt plans and validation hooks

## What Problem It Solves

Most product-video prompt workflows fail because they jump from copywriting straight to prompt writing.

This skill inserts the missing production gates:

1. Product understanding.
2. Component and state matrix.
3. Production archetype classification.
4. A/B, A-out, A-in, B, and A+B judgment.
5. One-by-one selling-point proof mapping.
6. Reference asset role binding.
7. Script to Unit to material arrangement.
8. Prompt-plan validation.
9. Bad-case regression into rules, gotchas, and validators.

## Repository Layout

```text
ecommerce-sku-skill-builder/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── examples/
│   ├── demo-product-brief.md
│   ├── demo-selling-point-map.md
│   └── demo-prompt-plan.md
├── scripts/
│   └── validate_release.py
└── skills/
    └── sku-skill-builder/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        └── scripts/
```

## Install

Copy the skill folder into a Codex skill location:

```bash
mkdir -p ~/.codex/skills
cp -R skills/sku-skill-builder ~/.codex/skills/sku-skill-builder
```

Restart Codex, then invoke:

```text
$sku-skill-builder
```

## Typical Inputs

- Product brief.
- Selling-point table.
- Case video or real-shot reference material.
- Existing prompt plans or old SKU packages.
- Approved or pending asset manifest.
- Target platform, aspect ratio, model, duration, and compliance constraints.

## Typical Outputs

- Source confirmation card.
- Product understanding card.
- Component/state matrix.
- Selling-point to visual-proof map.
- Script/Unit/material arrangement.
- Standard SKU Skill package draft.
- Representative prompt-plan.
- Product-specific validator.
- Bad-case regression notes.

## Example Workflow

```text
1. Read source materials.
2. Confirm product structure and state matrix.
3. Classify production archetype.
4. Map one selling point to visual proof.
5. Confirm reference assets and A/B judgment.
6. Continue to the next selling point only after OK.
7. Draft prompt-plan and target SKU Skill.
8. Validate and route failures back into rules.
```

See `examples/` for a small fictional product walkthrough.

## Validation

Run the release check:

```bash
python3 scripts/validate_release.py
```

The validator checks the public release shape, skill frontmatter, required references, scripts, examples, and common private-path or token leaks.

## Design Notes

- The root README is for GitHub users.
- The actual Codex skill lives under `skills/sku-skill-builder/`.
- Dense operating rules live in `references/` so `SKILL.md` stays as the routing entrypoint.
- Runtime product assets should stay pending until an operator approves the material version.

## License

MIT

