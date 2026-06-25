# Demo Prompt Plan

## Unit U1 - Compact Office Desk Setup

### Unit Info

- type: A-out
- duration: 5s
- selling_point: Compact foldable body
- purpose: Show the product fitting naturally on a desk without crowding the workspace.

### Reference Materials

| ref | priority | role | material | product_state | controls | does_not_control |
|---|---:|---|---|---|---|---|
| @Image1 | P0 | product_identity | product front image | folded | product shape, color, scale | office background |
| @Image2 | P2 | desk_scene | office desk scene | n/a | laptop, keyboard, desk context | product identity |

### Prompt

```text
【素材说明】
@Image1：P0，controls the humidifier identity, folded body shape, color, and scale; does not control the office background.
@Image2：P2，controls the desk environment, laptop, keyboard, and office lighting; does not control product identity or product state.

【画面要求】
Realistic vertical phone-shot product video. Keep the humidifier shape and folded state from @Image1. Place it on the office desk context from @Image2 beside a laptop and keyboard. This clip only proves compact desk placement. The camera makes one small handheld push-in and stops when the product is stable, large enough to inspect, and clearly not crowding the workspace. Do not generate readable brand text, subtitles, or extra UI labels.
```

### Self Check

| check | result |
|---|---|
| one selling point only | pass |
| reference roles declared | pass |
| state consistent | pass |
| text risk controlled | pass |

