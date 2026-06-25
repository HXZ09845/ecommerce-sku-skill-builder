# Asset Manifest Contract V2

Use this contract when creating `references/asset-manifest.md` for a target SKU skill. The creator must not copy unapproved raw assets into runtime `assets/`.

## Required Table

```markdown
| runtime_path | original_path | type | required | semantic_role | product_state | status | notes |
|---|---|---|:---:|---|---|---|---|
| `assets/product/front-main.jpg` | `raw/...` | image | yes | product_full / P0 | closed/front | approved | Locks full identity and proportions |
```

## Field Rules

| Field | Meaning |
|---|---|
| `runtime_path` | Path inside the final skill package; use `pending` when not generated yet |
| `original_path` | Human-readable source path or original filename; avoid local-only absolute paths in final handoff unless needed for source review |
| `type` | `image`, `video`, `asset_uri`, `audio`, or `other` |
| `required` | `yes`, `no`, or `conditional` |
| `semantic_role` | Role such as `env_anchor`, `env_anchor_product`, `product_full`, `product_angle`, `detail_anchor`, `logo_text_anchor`, `rhythm_reference`, `reference_video`, `person_asset`, `lifestyle_prop`, `universal_clip`, `submission_asset` |
| `product_state` | closed, open, worn, folded, filled, empty, color/version, screen state, action state, or `n/a` |
| `status` | `approved`, `pending`, `deprecated`, `backup`, or `source-only` |
| `notes` | What the asset controls, what it must not control, and which copy/proof beat it supports when relevant |

## Semantic Role Guidelines

- P0 assets prevent identity, scale, color/version, or space drift.
- P1 assets prove a selling point.
- P2 assets support narrative, lifestyle, person, or scene.
- Logo/text anchors protect risky readable regions as visual texture; they do not license exact text generation unless separately verified.
- Rhythm references describe pacing, shot density, or action timing; they must not silently control product identity.
- Submission assets are normalized files used in API calls; their count must match prompt references and API parameter tables.
- Product-containing environment anchors must say whether they control product position, background mood, or both.
- Pure environment images do not control product position.
- Detail images do not replace whole-product identity anchors.
- Reference videos control action, rhythm, viewpoint, and product state change unless a product rule narrows their role.
- When an asset supports a specific script beat or selling-point proof, record that link in `notes` so it can be checked against the audio-visual sync table.

## Approval Rules

- If multiple material versions exist, keep all runtime assets pending until the creator selects one.
- Mark deprecated assets instead of silently deleting their lesson when they represent a known failed path.
- Do not include large raw videos or camera originals in the runtime package unless they are normalized and intentionally used.
