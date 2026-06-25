# Trigger Tests - SKU Skill Builder

These tests are for the creator skill itself (`sku-skill-builder`). They are not prompt-plan tests for a target product SKU.

## Should Trigger

- "我拿到一个新品，帮我沉淀成 SKU Skill"
- "基于这些卖点和素材做一个新品类 Skill"
- "这个旧 SKU Skill 能不能迁移成 Codex 标准包"
- "品类 Meta 还不完善，先用行业通用规则帮我做 Skill"
- "把这个产品 Brief / Excel 卖点表 / 案例视频变成可复用 Skill"
- "帮我判断旧案例里哪些规则可继承、哪些要改写"
- "这个新品的 A/B 怎么判断，帮我做成 SKU Skill 规则"
- "根据这条脚本做脚本-Unit-素材编排"
- "帮我把脚本文案、prompt 和素材做到音画同步"
- "脚本里有夏日和喝咖啡，帮我匹配对应画面和素材"
- "这个 Skill 已经走通了，帮我批量生成这些脚本的 plan 和素材编排"
- "套用茶吧机、繁花冰霸杯、鞋服这些黄金案例抽象，整理新品的幻觉点和 A/B 方案"
- "这个新品先按黄金案例抽象判断规则，再生成 SKU Skill"
- "生成标准的 SKILL.md + references + scripts + assets 包"
- "帮我给这个 SKU Skill 做 validator 和 trigger tests"
- "按最高规格创建新品 Skill"
- "更新行业通用 Meta Skill"
- "我第一次用这个母 Skill，带我一步步准备素材并做新品 Skill"
- "让小白也能按这个 Skill 做出一个新品 SKU Skill"

## Should Not Trigger

- "只帮我写一条普通小红书文案"
- "总结这个产品卖点，不做视频生成或 Skill"
- "给我直接生成一条单次 prompt，不需要沉淀成 Skill"
- "发布小红书笔记"
- "编辑已有网页 UI"
- "分析会议纪要"
- "做一个和电商短视频无关的通用 Python 脚本"

## Boundary Cases

| User request | Expected routing |
|---|---|
| "帮我做茶吧机 A3 prompt-plan" | Use the tea-bar SKU skill if available; use this creator only if the user wants to update/create the skill |
| "这个新品没有品类 Meta 怎么办" | Trigger; use industry fallback plus nearest old cases |
| "检查这个 SKU Skill 包能不能给同事用" | Trigger; audit package shape and maturity |
| "给我一个杯子卖点脚本" | Do not trigger unless the user asks to build/update a skill or prompt-plan workflow |
| "我只有一个新品但不知道该给什么素材" | Trigger; use beginner-safe intake and ask for the four first-round slots |
