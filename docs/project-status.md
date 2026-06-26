# Project Status

Current release level: **project-ready**.

This repository is ready for developers and AI-video workflow builders to inspect, install locally, run validation checks, study examples, and adapt the `sku-skill-builder` Agent Skill. It is not an end-user video application and does not call any video-generation model directly.

## Trust Matrix

| Area | Current state | Evidence | How to verify |
|---|---|---|---|
| Agent Skill package | Included and self-contained | `skills/sku-skill-builder/` | `python3 scripts/validate_release.py` |
| Local install path | Supported by install helper | `scripts/install_codex_skill.py` | `python3 scripts/install_codex_skill.py --dry-run` |
| Public examples | Fictional walkthrough plus JSON examples | `examples/` | Read `examples/complete-chinese-case.md` and run structured checks |
| Real-run evidence | One anonymized production case | `case-studies/real-run-a6-office-tea-bar/` | `python3 case-studies/real-run-a6-office-tea-bar/office-tea-bar-overtime-sku/scripts/validate_case.py` |
| Prompt-plan validation | Markdown prompt-plan checker and evals | `scripts/prompt_plan_check.py`, `evals/` | `python3 scripts/prompt_plan_check.py --evals evals/prompt-plan-evals.json` |
| Structured data validation | Asset-manifest and take-review JSON checker | `scripts/structured_data_check.py` | `python3 scripts/structured_data_check.py --asset-manifest examples/demo-asset-manifest.json --take-review examples/demo-take-review.json` |
| Source and privacy boundary | Machine-readable source registry | `data/source-registry.json` | `python3 scripts/source_registry_check.py` |
| CI | GitHub Actions validation workflow | `.github/workflows/validate.yml` | Check the `Validate` badge in the README |

## What It Does Not Do

- It does not generate final videos by itself.
- It does not wrap Seedance, Veo, Kling, Runway, or any other model API.
- It does not include private product footage, unpublished generated clips, or raw client materials.
- It does not guarantee model output quality without human review and platform-specific testing.
- It does not replace product judgment, selling-point selection, or material approval.

## Reproducible Health Check

Run these from the repository root:

```bash
python3 scripts/validate_release.py
python3 scripts/install_codex_skill.py --dry-run
python3 scripts/prompt_plan_check.py --evals evals/prompt-plan-evals.json
python3 scripts/prompt_plan_check.py templates/prompt-plan-template.md
python3 scripts/selling_point_check.py templates/prompt-plan-template.md --require-map --min-proof-units 2
python3 scripts/unit_contract_check.py templates/prompt-plan-template.md
python3 scripts/source_registry_check.py
python3 scripts/structured_data_check.py --asset-manifest examples/demo-asset-manifest.json --asset-manifest templates/asset-manifest-template.json --take-review examples/demo-take-review.json --take-review templates/take-review-template.json
python3 case-studies/real-run-a6-office-tea-bar/office-tea-bar-overtime-sku/scripts/validate_case.py
python3 -m unittest discover -s tests -v
```

## Recommended First Evaluation

1. Read the quick positioning in `README.md` or `README.zh.md`.
2. Read `examples/complete-chinese-case.md` to understand the before/after workflow.
3. Inspect the anonymized real-run case under `case-studies/`.
4. Run the health check commands above.
5. Install the Skill locally with `scripts/install_codex_skill.py`, then ask Codex to start with source confirmation instead of final prompt writing.
