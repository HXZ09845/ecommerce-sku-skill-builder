# Migration Map

Source package: previous `meta-行业通用` (legacy display name; same skill as `sku-skill-builder`)
Current package: `sku-skill-builder` V2.3 industry-general SKU Skill Creator

## What Changed

- Primary identity changed from industry rule collection to SKU Skill Creator.
- Primary output changed from legacy core markdown package to standard Codex skill package.
- Old package concepts are retained only as migration/source references.
- Category meta is helpful but no longer a blocker; industry fallback plus golden cases can proceed.
- Case mining now requires `可继承 / 需改写 / 禁止继承`.
- Golden cases currently recognized: tea bar machine, Jingci Fanhua cup, insulated food carrier, crewneck T-shirt.

## Legacy Terms

The old three-file package shape may appear in historical sources. Do not use it as the main output shape for new work.

## Next Review Points

- Add more golden cases as they become stable.
- Forward-test with one new product request and one old SKU migration request.
- Promote repeatable bad cases from product packages back into `gotchas.md` or validator template.
