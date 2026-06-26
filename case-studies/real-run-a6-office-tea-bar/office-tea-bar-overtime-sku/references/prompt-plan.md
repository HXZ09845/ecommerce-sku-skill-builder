# Prompt Plan

## Project Capsule

```text
PROJECT ID: office_tea_bar_overtime_case
FORMAT: 9:16 realistic phone-shot ecommerce video
STORY GOAL: A late-night office worker wants water or a hot drink without breaking focus.
FINAL OUTCOME: The worker returns to the desk with a hot drink visible while the appliance stays stable in the background.
STYLE: realistic phone-shot product seeding video, calm office rhythm, no fake text.
```

## Continuity Locks

- Product remains in the same right-side wall position.
- Office desk, chair, monitor, neutral lighting, and work props remain consistent.
- Exact product text, numeric claims, and CTA text are handled by VO, subtitles, or post.

## Unit Schedule

| Unit | Type | Duration | Proof target | One visible beat | Stop when |
|---|---:|---:|---|---|---|
| U1 | A | 10s | Office overtime thirst problem | Worker looks at empty cup and notices appliance | Worker reaches product side; no water action yet |
| U2 | B | 5s | Auto-fill and water-full stop | Action video shows fill process | Water level stabilizes and fill stops |
| U3 | A | 10s | Remote operation | Worker presses remote from desk | Remote lowers and product is stable in distance |
| U-bridge | A | 5s | Lifestyle warmth | Kettle prepared, result state shows tea | Cup is about 80% full and steam is stable |
| U4 | A | 10s | Clean water and material trust | Whole product to clean water/material detail | Product identity remains stable after detail insert |
| U5 | A | 10s | Hot drink ready and work resumes | Worker returns to desk with hot drink | Hot drink visible and worker resumes work |

## Reference Materials

| Ref | Priority | Role | Controls | Does not control |
|---|---:|---|---|---|
| `@Image1` | P0 | environment_anchor | office layout, wall position, lighting, product placement | product text, action timeline, person identity |
| `@Image2` | P0 | product_identity | whole appliance silhouette, cabinet volume, platform, proportions | office layout, generated text |
| `@Image3` | P1 | detail_material | water clarity, vessel material, metal texture | whole-product identity |
| `@Image4` | P2 | person_reference | protagonist look and general outfit | product structure |
| `@Video1` | P1 | action_video | fill action, water-level timing, stop moment | target office background or new people |

## U1 Prompt Contract

```text
【素材说明】
@Image1：P0，controls office layout, right-side wall product position, lighting, and rough scale; does not control person identity, product text, or actions.
@Image2：P0，controls whole-product silhouette and cabinet structure; does not control environment or screen state.
@Image4：P2，controls general protagonist appearance only; does not control product structure.

【画面要求】
Realistic vertical phone-shot feel. This clip only establishes late-night office thirst and guides attention to the appliance. Keep the product fixed at the right-side wall position from @Image1. The worker looks at an empty cup, the camera lightly turns toward the appliance, and the worker walks beside it but does not start filling water. Stop when the product is stable in the wall position and the worker has arrived beside it. Do not show auto-fill, remote control, fast heating, brand text, or new subtitles.
```

## U2 Prompt Contract

```text
【素材说明】
@Image1：P2，only provides bright office wall-side tone and bokeh background; does not control product identity, motion, composition, or screen text.
@Video1：B-class action source, strictly controls fill motion, water-level change, stop timing, product action framing, and viewpoint; does not control target background, people, or new text.

【画面要求】
This is a B-class action background replacement task. Strictly replicate the action, framing, angle, fill rhythm, and water-full stop from @Video1. The background only borrows bright office wall-side color from @Image1 and becomes f/1.4 bokeh. This clip only proves auto-fill until water-full stop. Stop when the water level is stable and the fill action stops. Do not add people, hands, buttons, stickers, or extra objects.
```

## U5 Prompt Contract

```text
【画面要求】
Realistic vertical phone-shot feel. This clip only shows the result: a hot drink is ready and the worker returns to work. Exact wattage claims are handled by VO or subtitles, not generated in the image. Start beside the appliance with a finished hot drink and stable steam; the worker brings it back to the desk. Stop when the worker has returned to work, the hot drink is visible on the desk, and the appliance remains fixed in the background. Do not generate brand text, numeric wattage, link text, or CTA stickers.
```

## Take Review

| Unit | Accept criteria | Common failure | First repair variable |
|---|---|---|---|
| U1 | Office pain clear; product position stable; no later selling point leaks | worker starts water action too early | narrow to empty cup -> turn to product -> arrive beside product |
| U2 | source action timing preserved; background only bokeh tone | environment overwrites video composition | weaken environment role and strengthen strict action replication |
| U3 | remote intent clear; product stable in distance | tries to show entire boil process | remove boil process, keep remote intent plus machine response |
| U-bridge | lifestyle beat warm; result state clear | long pour distorts hand or liquid | use intent cue plus result state |
| U4 | clean water/material trust; whole product identity stable | detail reference replaces whole product | detail refs become texture-only |
| U5 | worker resumes work; hot drink visible; product fixed in background | fake numbers, link text, or brand text | route exact text to VO/subtitle/post |
