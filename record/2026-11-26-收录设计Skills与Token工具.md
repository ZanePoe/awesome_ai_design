# 2026-11-26 收录七个设计 Skills 与 token 工具（帖子分诊）

来源：[用户提供的帖子](https://x.com/RoundtableSpace/status/2125767746881486920)（2026-11-26，@RoundtableSpace / 0xMarioNawfal），列出 9 个「让 vibe-coding 项目不像 AI 做的」Claude Skill。其中 2 个（Remocn、Awesome Motion Design Agent Skills）属视频链路，已加入 `awesome_ai_video_creation`；本仓库收 7 个条目，合集从 29 → 36 个项目，其中 1 个需要新增分类（见下）。

## 新增条目与分类

| 仓库 | 分类 | Stars | 90 天提交 | 默认分支最后提交 | 许可 | 证据提交 |
| --- | --- | --- | --- | --- | --- | --- |
| `samber/cc-skills` | skills | 283 | 16 | 2026-11-01 | MIT | `50a33836b20f690c668af557bd9ef9d07a8c7ef2` |
| `Devesh-Shirsath/spotkit` | diagrams | 130 | 33 | 2026-10-08 | MIT | `f9b6a611e14c68a88fae44b4c67777a25b9c1d2c` |
| `Moddingflow/better-design` | skills | 79 | 9 | 2026-10-27 | MIT | `c373ad7fa122b8c0d63b1be756443cc93a56e71d` |
| `arvindrk/extract-design-system` | design_systems | 316 | 0 | 2026-06-19 | MIT | `1873741ba8dea755e35e6e15134f7918cd58e036` |
| `kaankiziltug/logo-design-skill` | skills | 7,782 | 32 | 2026-11-13 | MIT + 商标库除外 | `e9eaddc07895575253d6663320354a708f53e955` |
| `jakubkrehel/make-interfaces-feel-better` | skills | 4,294 | 3 | 2026-11-18 | MIT | `6d9f2f1df10e8ce2ae1708598a73b0506fb98794` |
| `Akxan/ppt-agent-skill` | presentations | 209 | 11 | 2026-11-18 | MIT（上游署名另计） | `e2f97f46a2f92633d3f9b95a1a61b0a668c704b3` |

维护层由脚本按默认分支提交时间分层：`extract-design-system` 落在「91–365 天未提交」层，`make-interfaces-feel-better` 虽 90 天仅 3 次提交但仍在活跃层；star 与提交量不代表设计质量。

分类理由：`spotkit` 产出的是成套 SVG 视觉表达而非前端细节，归入「图解与视觉表达」（与 `cathrynlavery/diagram-design` 同类）；`extract-design-system` 的产物是 tokens（W3C 兼容 `tokens.json` + `tokens.css`），归入「设计系统与 DESIGN.md」；`ppt-agent-skill` 产出演示文稿，归入本次新增的「演示与文档设计」；其余四项都是可直接安装的 Agent Skills，归入「前端设计、动效与审查 Skills」。

## 许可与边界要点

- `logo-design-skill`：`license_review.status = custom`。`TRADEMARKS.md` 明确 `assets/library/svg` 的 1,432 个 logo 均为各自权利人商标，**MIT 不覆盖、不授权**，只作品构研究，权利人可要求下架；README 亦写明「never to copy」。边界另记：示例品牌为虚构，商标检索需使用者自行完成，16 px/单色/反白/镜像/竞品货架等测试来自自带脚本，未做统一效果评测。
- `better-design`：README 自述结果依赖模型、简报、项目、参考与运行时工具，技能只提供流程/配方/评审清单；demo 的盲评是作者实验；references 记录 Impeccable（Apache-2.0）等第三方来源，各自授权。
- `cc-skills`：跨领域技能合集（文案、Git、调研、安全扫描等），设计只是其中一条线；README 表格里的 -28% 等数字为作者自建评测；Go 技能在另一仓库 `cc-skills-golang`。
- `extract-design-system`：抽取公开站点的配色/字体/图形不产生任何授权，产出需按站点条款、字体许可与商标法核对。
- `spotkit`：单色抽象插图，不处理照片与复杂插画；一套规则十二个版式，明暗双主题共用十二个 CSS 变量；示例取自作者自有功能集。
- `make-interfaces-feel-better`：只给细节规则与清单，不替代布局与信息架构决策；需在真实浏览器、键盘与辅助技术下验证；作者未发布 benchmark 数字。

全部条目 `baseline: false`（本仓库基线集合仍为 4 个种子项目，`validate()` 断言不变），`reviewed_at = 2026-11-26`，证据 URL 由 `evidence_commit` + `path` + `line` 逐字重建（本仓库 `validate()` 强制）。四语 `locales/{en,es,hi,fr}/entries.json` 同步补齐 `name`/`description`/`boundary`/`license_label`/`license_note`，`zh` 回落 `data/projects.json`。

## 分类扩展：演示与文档设计

`Akxan/ppt-agent-skill`（209 Stars、MIT、最后提交 2026-11-18；一句话 → 六步流程 → HTML 设计稿 + 可编辑 PPTX，26 风格、18 图表，自称与 Linear/Anthropic/Stripe/Apple/NYT 排版做法对照）产出的既不是界面、原型、矢量图、图解也不是设计系统，原有八个分类都不贴合。经用户确认，新增分类 `presentations`（zh「演示与文档设计」/ en "Presentations and document design" / es "Presentaciones y diseño de documentos" / hi "प्रस्तुति और दस्तावेज़ डिज़ाइन" / fr "Présentations et conception de documents"），位置排在 `diagrams` 之后、`research` 之前，五语 `ui.json` 同步。

随之变更的范围口径：

- `docs/readme-intro.md` 与四语副本的定义句把「演示稿/presentaciones/प्रस्तुतियाँ/présentations」并入 AI 设计对象列表（界面、原型、矢量图、图解、演示稿或设计系统）。
- `docs/selection.md` 与四语副本新增一条选型指引：只有一句话、要可继续编辑的 PPTX 时看该条目，并提醒先核对导出依赖与上游署名。
- 该合集仍不覆盖视频链路（归 `awesome_ai_video_creation`）；「演示与文档设计」目前只有 1 个条目，后续同类（deck 生成、文档排版、PDF/幻灯导出）直接进这一类，不再临时塞进 `skills` 或 `diagrams`。

条目要点（已写进 boundary/license note）：26 风格、18 图表与「对标世界级品牌」是作者自述、无统一评测；导出 SVG/PPTX 需 Python≥3.9、Node≥18 等依赖，缺依赖时只交付 HTML 预览；`LICENSE` 的版权行署的是上游作者 sunbigfly（2025），`ATTRIBUTIONS.md` 列出 `references/principles`、`design-runtime`、`blocks`、`page-templates`、`layouts` 等目录来自 `sunbigfly/ppt-agent-skills` 的修改版，再分发需同时保留 MIT 声明与署名；风格参考真实品牌排版不产生任何商标授权。

## 校验

`python scripts/refresh_metrics.py` → 36/36；`python scripts/build.py` → 16 个生成文件；`python -m unittest discover -s tests` → 22 项通过；`python scripts/build.py --check` 幂等。
