# Product Rules

## Product Identity

- Treat the product as a freestanding hot-water / tea-bar appliance.
- Keep the appliance on the same side of the office wall across Units.
- Do not let the product become a kettle, humidifier, coffee machine, water dispenser, speaker, cabinet, or lamp.
- Whole-product identity references control silhouette, height, cabinet volume, platform, and visible dual-vessel relationship.
- Detail references control only the named detail; they must not replace whole-product identity.

## Reference Roles

| Role | Controls | Must not control |
|---|---|---|
| `product_identity` | category, silhouette, scale, cabinet structure | office layout, person appearance, action timeline |
| `environment_anchor` | office layout, wall position, lighting, rough scale | product text, action timing, person identity |
| `detail_material` | water clarity, metal texture, vessel detail | whole-product shape, background, generated text |
| `action_video` | motion, timing, product action viewpoint | target background, new people, new UI/text |
| `person_reference` | general age, outfit, posture direction | product shape, device behavior |

## Unit Scope

- One Unit should prove one claim or one bridge role.
- Every prompt must include a clear `This clip only` boundary.
- Every prompt must include a `Stop when` endpoint.
- Do not leak later selling points into earlier Units.

## Text And Claim Handling

Do not ask the video model to generate exact:

- brand names;
- wattage numbers;
- link or CTA text;
- screen labels;
- certification marks;
- price or promotion text.

Route exact text to VO, subtitles, overlays, or post-production.
