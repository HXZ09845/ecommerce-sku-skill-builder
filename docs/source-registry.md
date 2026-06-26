# Source Registry

This registry records what public evidence is included in the repository and what is intentionally excluded.

The goal is simple: make the project auditable without publishing private product assets.

## Policy

Public repository sources must be one of:

- fictional examples;
- generated public visuals;
- open project files;
- anonymized real-run evidence.

Public repository sources must not include:

- raw private product photos or videos;
- customer or account data;
- local machine paths;
- asset IDs from private tools;
- unpublished generated videos;
- credentials or environment files.

## Registry

The machine-readable registry lives at [`data/source-registry.json`](../data/source-registry.json).

| ID | Type | Privacy | Path | Public value |
|---|---|---|---|---|
| `workflow_hero` | generated asset | public | `assets/workflow-hero.png` | Explains the project flow visually |
| `fictional_humidifier_demo` | fictional demo | public | `examples/complete-chinese-case.md` | Shows the workflow without private materials |
| `real_run_office_tea_bar` | anonymized real run | anonymized | `case-studies/real-run-a6-office-tea-bar/README.md` | Proves the workflow was applied to a real production case |
| `real_run_output_skill_sample` | anonymized output package | anonymized | `case-studies/real-run-a6-office-tea-bar/office-tea-bar-overtime-sku/SKILL.md` | Shows the final SKU Skill package shape |
| `packaged_sku_skill_builder` | skill package | public | `skills/sku-skill-builder/SKILL.md` | The installable Agent Skill |
| `demo_asset_manifest_json` | fictional demo | public | `examples/demo-asset-manifest.json` | Shows structured asset role metadata |
| `demo_take_review_json` | fictional demo | public | `examples/demo-take-review.json` | Shows structured take-review metadata |

## Validation

Run:

```bash
python3 scripts/source_registry_check.py
```

The checker verifies that registry paths exist, required metadata is present, anonymized real-run entries declare exclusions, and registered text files do not contain common private-path or credential-looking patterns.
