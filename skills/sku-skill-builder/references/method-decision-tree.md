# Method Decision Tree V2

There are only two top-level production methods. Choose the method before drafting a SKU skill package.

## 1. Direct-Generation Flow

Default for almost every ecommerce product.

Flow:

```text
script/copy -> unit split -> A/B/A-out/A-in classification -> material role mapping -> prompt-plan -> validation -> generation
```

Material situations inside this method:

| Situation | Meaning |
|---|---|
| Product images only | Mostly A/A-out/A-in units |
| Product images + action videos | A/B mixed |
| Reference videos from brand or old case | B units use the reference videos for action/composition |
| Oral/voiceover generation needed | Still direct-generation; set audio behavior in the prompt-plan/API section |
| Background replacement | A B-unit material strategy, not a separate method |

Skill package output is always the standard Codex package shape. Do not switch back to legacy package formats because a project uses reference videos or real-shot background replacement.

## 2. Grid/TVC Flow

Use only when the user explicitly requests TVC, advertising film, grid storyboard, multi-frame key visual generation, or a similar commercial workflow.

Flow:

```text
script -> grid/keyframe planning -> image frames -> video from frames -> edit/composite
```

The agent must not auto-select this method just because the product is premium, stylish, or brand-led.

## Decision Table

| User/project signal | Method |
|---|---|
| "新品 SKU Skill", "种草视频", product brief, selling-point table | Direct-generation |
| Real-shot product material plus action videos | Direct-generation |
| Old SKU with A/B prompt-plan examples | Direct-generation |
| "TVC", "广告片", "宫格", "关键帧", "多宫格" explicitly requested | Grid/TVC |
| User only asks to write a product script, not a skill or prompt-plan | This creator may not be needed |

## Package Consequence

Both methods must still produce or use a standard Codex skill package when the user asks to create a skill. The method changes prompt-plan behavior, not the package architecture.
