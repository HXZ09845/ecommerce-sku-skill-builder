# Prompt Before / After: Anonymized Real Run

This file shows representative prompt changes from the real office overtime tea-bar machine run. The examples are shortened and anonymized for public release.

## U1: Opening Pain And Product Introduction

| Before | After | Why it improved |
|---|---|---|
| Timeline includes sitting at desk, empty cup, turning to product, walking to product, picking up a glass, and waiting for water | Clip only establishes late-night office thirst and moves attention to the appliance; the user stops beside the product without starting the water action | Removes premature auto-fill behavior and avoids complex hand/cup action in the opening |
| Environment and product are described globally | Environment anchor controls office layout and product position; product images control appliance identity; person reference controls appearance only | Reduces reference contamination |
| Ending is a natural transition to the next Unit | `Stop when` the appliance is stable in the wall position and the user has arrived beside it | Makes the generated clip easier to evaluate and continue |

Representative after prompt:

```text
【素材说明】
@Image1：P0，office environment anchor with product, controls office space, right-side wall position, scale, and lighting; does not control person identity, product text, or actions.
@Image2：P0，front product image, controls overall product proportion and cabinet structure; does not control environment or screen state.
@Image3：P0，side-angle product image, controls cabinet depth; does not control motion or background.
@Image4：P2，person reference, controls general protagonist appearance only.

【画面要求】
Realistic vertical phone-shot feel. This clip only establishes the late-night office thirst problem and guides attention to the appliance. Keep the product fixed at the right-side wall position from @Image1. The user looks at an empty cup, the camera lightly turns toward the appliance, and the user walks beside it but does not start filling water. Stop when the product is stable in the wall position and the user has arrived beside it. Do not show auto-fill, remote control, fast heating, brand text, or new subtitles.
```

## U2: Auto-Fill And Water-Full Stop

| Before | After | Why it improved |
|---|---|---|
| Describes a background replacement task and says the action video should be replicated | Separates source roles: action video controls motion/timeline; environment image only gives bokeh tone | Prevents environment image from overwriting video composition |
| Background is described as bokeh | Background is explicitly forbidden from becoming pure white/gray or recognizable furniture | Keeps office feeling without adding distracting objects |
| No explicit endpoint | `Stop when` water level is stable and fill action stops | Turns action completion into a checkable condition |

Representative after prompt:

```text
【素材说明】
@Image1：P2，office environment anchor, only provides bright wall-side office tone and bokeh background; does not control product identity, motion, composition, or screen text.
@Video1：B-class action source, strictly controls fill motion, water-level change, stop timing, product action framing, and viewpoint; does not control target background, people, or new text.

【画面要求】
This is a B-class action background replacement task. Strictly replicate the action, framing, angle, fill rhythm, and water-full stop from @Video1. The background only borrows bright office wall-side color from @Image1 and becomes f/1.4 bokeh. This clip only proves auto-fill until water-full stop. Stop when the water level is stable and the fill action stops. Do not add people, hands, buttons, stickers, or extra objects.
```

## U-Bridge: Lifestyle Tea Pour

| Before | After | Why it improved |
|---|---|---|
| Requires continuous tea pouring, rising liquid surface, steam, and placing kettle back | Uses intent cue plus result state: hand prepares to pour, then cup already has tea and steam | Avoids long continuous liquid and hand deformation risk |
| Bridge is warm and cinematic | Bridge explicitly does not carry a selling point | Prevents accidental product-function confusion |
| Many physical details compete | Endpoint locks cup level, stable steam, and unchanged kettle shape | Makes failure diagnosis simpler |

Representative after prompt:

```text
【素材说明】
@Image1：P0，kettle still image, controls glass body, filter, black lid, and handle; does not control pour action or background.
@Image2：P1，hand-held kettle pose, controls one-hand grip and natural tilt; does not control final kettle shape.
@Image3：P2，office environment anchor, only provides far-background appliance placement and warm office tone.

【画面要求】
Realistic vertical phone-shot feel in an office break area, not on the product countertop. This clip only works as a lifestyle bridge and carries no selling point. Use intent cue plus result state: first show the kettle on the small table, one hand holds and slightly tilts it, then cut to the result state where the glass cup already contains tea and stable steam. Stop when the cup is about 80% full, steam is stable, and the kettle shape still matches @Image1. Do not show a second hand, subtitles, watermarks, scale marks, or stickers.
```

## U5: Fast Hot Drink Result And CTA Close

| Before | After | Why it improved |
|---|---|---|
| Fast heating, coffee/tea, CTA, and office closing atmosphere are all inside the image prompt | The clip only shows hot drink ready and user returning to work; exact wattage and CTA move to VO/subtitles/post | Prevents fake numeric text or fake link labels |
| Ends with broad atmosphere | Ends with the user back at work, hot drink visible, product stable in background | Provides a clear final outcome |

Representative after prompt:

```text
【画面要求】
Realistic vertical phone-shot feel. This clip only shows the result: a hot drink is ready and the user returns to work. Exact wattage claims are handled by VO or subtitles, not generated in the image. Start beside the appliance with a finished hot drink and stable steam; the user brings it back to the desk. Stop when the user has returned to work, the hot drink is visible on the desk, and the appliance remains fixed in the background. Do not generate brand text, numeric wattage, link text, or CTA stickers.
```

## Net Improvement

| Dimension | Before | After |
|---|---|---|
| Prompt shape | Long timeline with many simultaneous actions | One clip goal, one visible beat, one endpoint |
| Reference handling | Useful but partially implicit | Explicit control and non-transfer contracts |
| Multi-clip continuity | Mostly held by human memory | Project-state capsule and reserved beats |
| Failure repair | Manual prompt edits | Take-review table and first repair variable |
| Platform safety | Precise text sometimes implied in image | Numeric/text claims routed to VO/subtitle/post |
