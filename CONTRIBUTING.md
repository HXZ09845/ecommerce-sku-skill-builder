# Contributing

Thanks for helping improve Ecommerce SKU Skill Builder.

This project is a workflow Skill for building product-specific ecommerce AI video-generation Skills. The most useful contributions make the workflow more reproducible, easier to validate, or easier to understand from real examples.

## Good Contribution Areas

- Fictional demo product briefs, selling-point maps, and prompt plans.
- New validation checks for Skill package quality.
- Better docs for asset role binding, A/B state decisions, and bad-case regression.
- Cleaner examples of product understanding, component/state matrices, and visual proof maps.
- Bug reports with a minimal input, expected behavior, actual behavior, and failed output.

## Please Avoid

- Private product briefs, unreleased assets, customer data, credentials, or paid case materials without permission.
- Model-specific claims that cannot be reproduced.
- Generic prompt templates that skip product understanding, asset roles, or validation.

## Local Checks

Run these before opening a pull request:

```bash
python3 scripts/validate_release.py
python3 -m compileall scripts skills/sku-skill-builder/scripts skills/sku-skill-builder/references
git diff --check
```

If you are changing the packaged Skill itself, also test it in an agent environment by copying `skills/sku-skill-builder/` into your local skill directory and invoking `$sku-skill-builder`.

## Pull Request Checklist

- The change is scoped to docs, examples, validators, references, or the Skill package.
- Public examples are fictional or explicitly approved for release.
- No local machine paths, private credentials, or internal customer data are included.
- Release validation passes.
- The README or docs are updated when behavior changes.
