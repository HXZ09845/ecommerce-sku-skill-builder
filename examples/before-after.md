# Before / After

This fictional example shows how the workflow changes a generic prompt into a SKU Skill-ready generation plan.

## Before

```text
Create a premium short video for a foldable desktop humidifier.
Show that it is compact, quiet, and good for office use.
Use the product image and the office video as references.
Make it realistic and high quality.
```

## Problems

| Problem | Risk |
|---|---|
| "premium" and "high quality" are vague | The model may generate generic advertising footage |
| Product state is not defined | Folded/unfolded/active states may mix |
| References are not role-bound | Office video may overwrite product identity |
| Selling points are not mapped to visuals | Compact/quiet/office use may stay decorative |
| No end condition | The clip may drift or over-generate actions |

## After

```text
【素材说明】
@Image1：P0，controls humidifier identity, folded body shape, color, and scale; does not control the office background.
@Image2：P2，controls desk environment, laptop, keyboard, and office lighting; does not control product identity or product state.

【画面要求】
Realistic vertical phone-shot product video. Keep the humidifier shape and folded state from @Image1. Place it on the office desk context from @Image2 beside a laptop and keyboard. This clip only proves compact desk placement. The camera makes one small handheld push-in and stops when the product is stable, large enough to inspect, and clearly not crowding the workspace. Do not generate readable brand text, subtitles, or extra UI labels.
```

## What Changed

| Change | Why it helps |
|---|---|
| Reference roles are explicit | Reduces identity/background contamination |
| One selling point is isolated | Improves visual proof strength |
| Product state is locked | Prevents folded/unfolded drift |
| End condition is explicit | Makes the clip easier to evaluate |
| Text generation is prohibited | Avoids unreadable labels or fake UI |

