# Prompt-Plan Template

## Source Confirmation

| Source | Status | Used for | Not used for |
|---|---|---|---|
| Product brief | pending | Product facts and selling-point priority | Imagined claims |
| Asset manifest | pending | Reference role binding | Raw private file names |

## Product Understanding

- Product:
- Target user:
- Core use scenario:
- Required product state:
- Forbidden product state:

## Asset Manifest

| Asset | controls | does_not_control | status |
|---|---|---|---|
| @Image1 | product shape, color, scale, and component layout | background, motion, generated text | approved |
| @Image2 | scene category and lighting mood | product identity, product state, brand text | pending |
| @Video1 | camera rhythm and hand timing only | product identity, scene layout, new objects | pending |

## Selling-Point Proof Map

| Selling point | Visual proof | Unit | Fallback |
|---|---|---|---|
| SP1 | Show the problem and product solution in the same shot | U1 | Static before/after end state |
| SP2 | Show one visible action tied to the key component | U2 | Reduce motion and lock product state |

## Unit Plan

| Unit | A/B type | Goal | Product state | Reference assets | Stop when |
|---|---|---|---|---|---|
| U1 | A | Establish product identity and first proof | Required state here | @Image1, @Image2 | Stop when the product is stable, centered, and free of readable generated text. |
| U2 | A-in | Continue from U1 and show one action | Same identity, action begins | @Image1, @Video1 | Stop when the action has clearly demonstrated the selling point without changing product identity. |

## Seedance-Style Shot Prompts

### U1

This clip only establishes product identity and first visual proof. Use @Image1 for product identity and @Image2 for scene mood. Keep the product shape, scale, material, and component layout locked. Do not add readable subtitles, UI labels, brand text, extra product parts, or unrelated props.

Stop when the product is stable, centered, and the selling-point proof is visible without text explanation.

### U2

This clip only continues the approved product identity from U1 and adds one visible action. Use @Video1 for camera rhythm and hand timing only. Do not transfer product identity, scene layout, or objects from @Video1.

Stop when the action has clearly demonstrated the selling point and the product remains in the same approved state.

## Take Review

| Unit | Verdict | Observed end state | Root cause | First repair variable |
|---|---|---|---|---|
| U1 | retake | | | |
| U2 | post_fix | | | |
