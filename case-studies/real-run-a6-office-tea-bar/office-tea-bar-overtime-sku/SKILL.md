---
name: office-tea-bar-overtime-sku
description: Use this anonymized ecommerce SKU Skill when turning an office overtime tea-bar appliance brief, selling points, and reference assets into Seedance-style shot contracts, prompt plans, take reviews, and repair rules.
---

# Office Tea-Bar Overtime SKU Skill

This is an anonymized output sample generated from a real ecommerce video workflow. It is included to show the package shape that `sku-skill-builder` can produce. It does not include raw product media, brand names, local paths, or unpublished generated videos.

## Scope

Use this Skill for a 9:16 office-overtime product video where a freestanding hot-water appliance helps a desk worker avoid leaving the workflow for water or a hot drink.

## Required Reading

Load only what the task needs:

- `references/product-rules.md` for product-state and reference-role rules.
- `references/prompt-plan.md` for Unit schedule and prompt contracts.
- `references/gotchas.md` for known failures and repair levers.
- `references/trigger-tests.md` for behavior expectations.

## Operating Steps

1. Confirm the available source materials and mark missing assets as pending.
2. Keep the product position, category, and major silhouette stable across all Units.
3. For each Unit, identify one selling point or bridge role.
4. Assign each reference asset a role: identity, environment, detail, motion, person, or result-state.
5. Write one visible beat and one `Stop when` endpoint per Unit.
6. Move exact brand text, numeric wattage, link text, screen text, and claims to VO, subtitles, or post-production.
7. After generation, fill a take review before changing prompts.

## Output Contract

Return:

- source confirmation;
- Unit schedule;
- reference role table;
- Seedance-style prompt plan;
- take-review table;
- repair rules;
- validator result from `scripts/validate_case.py` when a prompt-plan file is available.
