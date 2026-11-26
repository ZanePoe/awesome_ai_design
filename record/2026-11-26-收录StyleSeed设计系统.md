# 2026-11-26 收录 StyleSeed 设计系统引擎

来源：[用户提供的帖子](https://x.com/oran_ge/status/2125789243134124334)（2026-11-26，@oran_ge），6 个「AI 味清除 Skill」中的设计侧条目。逐个回到 Cola Skill 目录页的「来源」链接还原真实仓库：本仓库收 2 个（其中 1 个已在同日 `647f163` 收录），1 个新增，2 个待用户定分类。合集 36 → 37 个项目。

## 新增条目

| 仓库 | 分类 | Stars | 90 天提交 | 默认分支最后提交 | 许可 | 证据提交 |
| --- | --- | --- | --- | --- | --- | --- |
| `bitjaru/styleseed` | design_systems | 1,056 | 95 | 2026-11-26 | MIT（构建组件许可另计） | `6963076194fdefd84933d87a1a4d282fdd0a7b0f` |

分类理由：StyleSeed 的主交付物是「产品的设计系统 + 让 coding agent 守住它的规则」——外观、配色、字阶、间距、圆角、动效写进 `STYLESEED.md` 与 CSS token，再由 74 条 craft rules 和 0–100 打分闸门在后续页面上执行。这与 `google-labs-code/design.md`（规范）、`VoltAgent/awesome-design-md`（索引）同属「设计系统与 DESIGN.md」，而不是单页动效或审查类 Skills。

## 功能与边界要点

- 作者自述目标是「可重复地执行专家判断」，并明确不宣称当下产出即专家级；分数不替代人工设计验收（README L26–L28）。
- README 的「120 个渲染基准单元、闸门使 Codex 与 Claude Code 各 +5.3 分」是作者自建测评，且同一段写明「只上原始规则时结果不一致（Codex +1.6、Claude Code −3.7）」；不是第三方基准。
- 安装走 `npx skills add bitjaru/styleseed`，需要 Node.js/npm；只注册一个 `styleseed` 路由，22 个 `ss-*` 工作流打包在内。
- 许可：根 `LICENSE` 为 MIT；`THIRD_PARTY.md` 逐项列出构建与验证所用组件及版本（Playwright、TypeScript 为 Apache-2.0，lucide-react 为 ISC，其余 MIT），核心 skill 声明无运行时依赖；再分发需按各自许可保留声明。

## 同日同帖的其他条目去向

- `kaankiziltug/logo-design-skill`（帖子第 5 项）：已在 `647f163` 收录，`license_review.status = custom`（1,432 个第三方商标 logo 不在 MIT 授权范围）。本次不重复添加。
- `MartinOlivero/saas-builder`（帖子第 3 项 `ui-design` 的真实仓库）：22 个 SaaS 生命周期 skill 的通用产品构建插件，9 Stars、最后提交 2026-10-11；本合集范围句明写「通用 coding agent 不作为核心工具」，是否作为 `adjacent` 收录待用户确认。
- `VaneAi888/vane-gpt-image-skills`（帖子第 6 项 `vane-cinematic-poster` 的真实仓库）：1,536 Stars、MIT、最后提交 2026-11-24，6 个 GPT Image 玩法（电影海报 36 构图、书页电影、微信红包封面、宠物写真、小红书图文、动态表情包）。产出是位图海报/封面，现有 9 个分类（含本日新增的 `presentations`）都不贴合，且范围句把「纯文生图模型」排除在核心工具之外——待用户确认是新增「平面与图像设计」分类、按 `adjacent` 收，还是不收。

## 校验

`python scripts/refresh_metrics.py` → 37/37；`python scripts/build.py` → 16 个生成文件、37 个项目、5 语；`python -m unittest discover -s tests` → Ran 22 tests, OK；`python scripts/build.py --check` 幂等。四语 `locales/{en,es,hi,fr}/entries.json` 同步补齐 `name`/`description`/`boundary`/`license_label`/`license_note`。
