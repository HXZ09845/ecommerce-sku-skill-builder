# Quickstart Template - {产品名}

Use this as `references/quickstart.md` in the generated SKU skill. Keep it operational and short.

## 1. What This Skill Does

This skill creates and validates prompt-plans for {产品名}. It is for {品类名} ecommerce short videos using the confirmed material version in `asset-manifest.md`. It is self-contained: use only files inside this package unless a row is explicitly marked `pending`.

## 2. Start Here

1. Read `SKILL.md`.
2. Read `references/product-rules.md`.
3. Read `references/audio-visual-sync.md`.
4. Read `references/asset-manifest.md`.
5. Confirm the script mode, ratio, platform, and material version.
6. In test stage, use 1-2 scripts to create the first prompt-plans and collect visual feedback.
7. In production stage, batch-create one prompt-plan and one material arrangement per script.
8. Create the script keyword/entity extraction and script-Unit-material arrangement before prompt writing.
9. Create the prompt-plan with `references/prompt-plan-format.md`.
10. Run `scripts/validate_{english_module}.py path/to/prompt-plan.md`.

## 3. Fast Checks

| Check | Pass condition |
|---|---|
| Selling-point coverage | Every core copy line maps to a visual proof |
| Keyword/entity coverage | Words like summer, coffee, office, car, food, user role, and destination have concrete visual entities or approved omissions |
| Audio-visual sync | Script copy, actual environment, Unit, material roles, prompt action, and A/B decision align |
| A/B decision | Key A/B rows are creator-confirmed or marked pending |
| Material roles | Every @ reference says what it controls and does not control |
| State consistency | A-out/A-in/B states do not conflict |
| Text risk | Logo/screen/label/print text is not rewritten as exact prompt text |
| Self-contained handoff | Required files, assets, and validator resolve inside this package or are marked pending |
| Validator | 0 errors before handoff |

## 4. Common First Run

```bash
python3 scripts/validate_{english_module}.py path/to/prompt-plan.md
```

Record warnings and accepted downgrades in the prompt-plan validation section.
