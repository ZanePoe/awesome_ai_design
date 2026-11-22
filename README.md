# Awesome AI Design

面向设计师、产品团队和 coding agent 的中文 AI 设计合集。收录可以复用的设计 Skills，可运行的设计 Agent、编辑器和桥接工具，以及能复核研究结论的论文与基准。

这里的“AI 设计”指 Agent 参与界面、原型、矢量图、图解或设计系统的创建、修改、评审和交接。纯文生图模型、通用 coding agent、无可核验仓库的 SaaS 不作为核心工具收录。官方接入指南和设计系统索引单独标明；已有 [AI 视频合集](https://github.com/ZanePoe/awesome_ai_video_creation) 覆盖视频生成和剪辑。

## 当前收录

**29 个项目，其中 4 个为用户参考项目，25 个为扩展收录。** 功能核验：2026-11-18；指标快照：`2026-11-22T10:16:09+00:00`（UTC）。

每个分类先按维护状态分层，再综合 star（40%）、90 天默认分支提交（35%）和最近提交（25%）排序。维护分不代表设计质量、模型能力、可访问性或生产成熟度。

## 活跃核心项目速览

仅展示核心候选、开放许可证已核验且近 90 天有提交的项目；受限许可、研究基准和相邻工具不进入此表。

| 项目 | 定位 | Stars | 90天提交 | 最近提交 UTC | 维护分 |
| --- | --- | --- | --- | --- | --- |
| [OpenDesign](https://github.com/nexu-io/open-design) | 用本地 coding agent 或 OpenDesign Cloud 生成遵循设计系统的原型，并在团队工作台共享与迭代。 | 108,897 | 488 | 2026-11-21 | 99.5 |
| [Impeccable](https://github.com/pbakaus/impeccable) | 为 coding agent 提供设计词汇、精修、批评与审查命令，用于迭代已有界面。 | 114,719 | 2,170 | 2026-11-18 | 99.0 |
| [Penpot](https://github.com/penpot/penpot) | 可自托管的协作设计平台，提供设计 token、组件和 MCP 接口衔接设计与代码。 | 62,627 | 1,514 | 2026-11-20 | 97.9 |
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) | 将架构、流程、数据等图解输出为带品牌样式的自包含 HTML/SVG。 | 70,008 | 348 | 2026-11-22 | 96.6 |
| [OpenPencil（open-pencil）](https://github.com/open-pencil/open-pencil) | 具备 AI、CLI 与 MCP 的可编程设计编辑器，可打开 .fig 与 .pen 文件。 | 10,008 | 1,551 | 2026-11-22 | 91.9 |
| [OpenPencil（ZSeven-W）](https://github.com/ZSeven-W/openpencil) | 将自然语言转为画布里的可编辑界面，支持多个 Agent 并行设计和 MCP 操作。 | 7,312 | 937 | 2026-11-22 | 90.9 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 为多个前端技术栈提供风格、配色、排版和设计系统建议的 Agent Skill。 | 152,634 | 93 | 2026-11-22 | 90.5 |
| [Open CoDesign](https://github.com/OpenCoworkAI/open-codesign) | 本地桌面设计 Agent，将提示转为可预览的设计产物，允许连接自选模型。 | 8,248 | 141 | 2026-11-21 | 84.0 |
| [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit) | 将 OpenDesign 的设计 Skills、品牌设计系统与示例移植到 coding agent 内使用。 | 1,172 | 414 | 2026-11-22 | 83.5 |
| [Emil Kowalski Skills](https://github.com/emilkowalski/skills) | 为设计师和工程师提供 UI 与动效 Skills，覆盖动效选择、审查和性能改进。 | 58,734 | 19 | 2026-11-15 | 78.2 |
| [Screenshot to Code](https://github.com/abi/screenshot-to-code) | 利用模型将截图、原型、Figma 设计或屏幕录制转为界面代码。 | 81,356 | 6 | 2026-11-15 | 73.4 |
| [fx0](https://github.com/vercel-labs/fx0) | 基于 libfx 的轻量设计 Agent，用自然语言迭代并导出单文件 HTML 页面。 | 442 | 134 | 2026-11-18 | 72.6 |

## 分类目录

`★用户参考` 表示用户直接提供的项目。每个仓库只进入一个主分类；项目详表记录依赖和限制。

| 分类 | 数量 | 维护排序靠前的项目 |
| --- | --- | --- |
| 设计 Agent 与原型工作台 | 5 | OpenDesign、Open CoDesign、fx0 |
| 可编辑画布与矢量设计 | 5 | Penpot、OpenPencil（open-pencil）、OpenPencil（ZSeven-W） |
| 前端设计、动效与审查 Skills | 5 | Impeccable、UI UX Pro Max、Open Design Agent Kit |
| 设计系统与 DESIGN.md | 3 | Google DESIGN.md、Stitch Design Skills、Awesome DESIGN.md |
| 设计转代码与 MCP 桥接 | 4 | Screenshot to Code、Figma MCP 官方指南、Framelink Figma MCP |
| 图解与视觉表达 | 2 | Diagram Design、Excalidraw MCP Server |
| 论文、基准与数据集 | 3 | DesignBench、Design2Code、WebDesignAgent |
| 历史与归档项目 | 2 | SuperDesign IDE 扩展（旧版）、Penpot MCP（旧仓库） |

### 设计 Agent 与原型工作台

| 项目 | 定位 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- |
| [OpenDesign](https://github.com/nexu-io/open-design) · ★用户参考 | 用本地 coding agent 或 OpenDesign Cloud 生成遵循设计系统的原型，并在团队工作台共享与迭代。 | 108,897 | 488 | 2026-11-21 | 99.5 | Apache-2.0 |
| [Open CoDesign](https://github.com/OpenCoworkAI/open-codesign) | 本地桌面设计 Agent，将提示转为可预览的设计产物，允许连接自选模型。 | 8,248 | 141 | 2026-11-21 | 84.0 | MIT |
| [fx0](https://github.com/vercel-labs/fx0) | 基于 libfx 的轻量设计 Agent，用自然语言迭代并导出单文件 HTML 页面。 | 442 | 134 | 2026-11-18 | 72.6 | Apache-2.0 |
| [GitHub Replica](https://github.com/github/replica) · ★用户参考 | 使用团队已有组件、模式和设计指导，通过 GitHub Copilot 生成并迭代交互原型。 | 325 | 117 | 2026-11-20 | 71.5 | MIT |
| [LangChain Content Studio](https://github.com/langchain-ai/design-agent) | 面向团队的品牌设计 Agent，从 Slack 接收素材与需求，交付平面图、演示或动态内容。 | 667 | 65 | 2026-11-18 | 70.1 | Apache-2.0 |

### 可编辑画布与矢量设计

| 项目 | 定位 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- |
| [Penpot](https://github.com/penpot/penpot) | 可自托管的协作设计平台，提供设计 token、组件和 MCP 接口衔接设计与代码。 | 62,627 | 1,514 | 2026-11-20 | 97.9 | MPL-2.0 |
| [OpenPencil（open-pencil）](https://github.com/open-pencil/open-pencil) | 具备 AI、CLI 与 MCP 的可编程设计编辑器，可打开 .fig 与 .pen 文件。 | 10,008 | 1,551 | 2026-11-22 | 91.9 | MIT |
| [OpenPencil（ZSeven-W）](https://github.com/ZSeven-W/openpencil) | 将自然语言转为画布里的可编辑界面，支持多个 Agent 并行设计和 MCP 操作。 | 7,312 | 937 | 2026-11-22 | 90.9 | MIT |
| [Onlook](https://github.com/onlook-dev/onlook) | 本地优先的代码可视化编辑器，由 Claude Code 或 Codex 等现有 Agent 在项目中工作。 | 27,733 | 8 | 2026-11-21 | 72.5 | Apache-2.0 |
| [Velloo](https://github.com/velloo-design/velloo) | 让 coding agent 使用现有应用组件在本地画布探索多个方向，再将选中的设计写回应用。 | 10 | 302 | 2026-11-17 | 64.1 | Apache-2.0 |

### 前端设计、动效与审查 Skills

| 项目 | 定位 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- |
| [Impeccable](https://github.com/pbakaus/impeccable) | 为 coding agent 提供设计词汇、精修、批评与审查命令，用于迭代已有界面。 | 114,719 | 2,170 | 2026-11-18 | 99.0 | Apache-2.0 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 为多个前端技术栈提供风格、配色、排版和设计系统建议的 Agent Skill。 | 152,634 | 93 | 2026-11-22 | 90.5 | MIT |
| [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit) | 将 OpenDesign 的设计 Skills、品牌设计系统与示例移植到 coding agent 内使用。 | 1,172 | 414 | 2026-11-22 | 83.5 | MIT |
| [Emil Kowalski Skills](https://github.com/emilkowalski/skills) · ★用户参考 | 为设计师和工程师提供 UI 与动效 Skills，覆盖动效选择、审查和性能改进。 | 58,734 | 19 | 2026-11-15 | 78.2 | MIT |
| [Frontend AI Skills](https://github.com/JustineBijuPaul/frontend-ai-skills) | 可按需加载的模块化前端 Skills，覆盖动效、交互和可访问性等主题。 | 11 | 86 | 2026-09-04 | 44.2 | MIT |

### 设计系统与 DESIGN.md

| 项目 | 定位 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- |
| [Google DESIGN.md](https://github.com/google-labs-code/design.md) | 视觉身份描述规范，将机器可读的设计 token 和供 Agent 阅读的设计原则放在同一文件。 | 29,025 | 9 | 2026-11-18 | 72.5 | Apache-2.0 |
| [Stitch Design Skills](https://github.com/google-labs-code/stitch-skills) | 面向 Google Stitch 的官方技能和插件集合，连接 Agent 与其设计流程。 | 11,656 | 14 | 2026-11-20 | 72.3 | Apache-2.0 |
| [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md) | 汇集可复用的 DESIGN.md 参考文档，为 Agent 提供品牌风格、排版、色彩和组件约定。 | 128,569 | 8 | 2026-10-28 | 71.4 | MIT |

### 设计转代码与 MCP 桥接

| 项目 | 定位 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- |
| [Screenshot to Code](https://github.com/abi/screenshot-to-code) | 利用模型将截图、原型、Figma 设计或屏幕录制转为界面代码。 | 81,356 | 6 | 2026-11-15 | 73.4 | MIT |
| [Figma MCP 官方指南](https://github.com/figma/mcp-server-guide) · 许可注意 | Figma 官方接入指南，说明 Agent 获取设计上下文及部分远程写入工作流。 | 2,223 | 29 | 2026-11-18 | 69.8 | 未确认 |
| [Framelink Figma MCP](https://github.com/GLips/Figma-Context-MCP) | 向 coding agent 提供 Figma 文件的设计上下文，辅助实现已有界面。 | 16,279 | 0 | 2026-06-24 | 38.4 | MIT |
| [Talk to Figma MCP](https://github.com/grab/cursor-talk-to-figma-mcp) | 通过 MCP 服务、Figma 插件和 WebSocket 桥让 Agent 读取与修改 Figma 设计。 | 7,124 | 0 | 2026-07-26 | 37.5 | MIT |

### 图解与视觉表达

| 项目 | 定位 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- |
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) · ★用户参考 | 将架构、流程、数据等图解输出为带品牌样式的自包含 HTML/SVG。 | 70,008 | 348 | 2026-11-22 | 96.6 | MIT |
| [Excalidraw MCP Server](https://github.com/yctimlin/mcp_excalidraw) | 提供可读写的 Excalidraw 画布，通过 CLI、Skill 或 MCP 修改并保存图解。 | 2,674 | 33 | 2026-11-10 | 69.1 | MIT |

### 论文、基准与数据集

| 项目 | 定位 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- |
| [DesignBench](https://github.com/WebPAI/DesignBench) · 许可注意 | 用于评估多框架前端代码生成、编辑与修复的研究基准。 | 61 | 0 | 2026-07-27 | 21.1 | 未确认 |
| [Design2Code](https://github.com/NoviScl/Design2Code) | 以真实网页的截图到代码为任务，提供数据与自动评估工具。 | 605 | 0 | 2024-11-02 | 22.3 | MIT |
| [WebDesignAgent](https://github.com/DAMO-NLP-SG/WebDesignAgent) | 网站生成研究原型，展示由描述、参考布局、图像和反馈驱动的设计流程。 | 267 | 0 | 2024-09-20 | 19.4 | Apache-2.0 |

### 历史与归档项目

| 项目 | 定位 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- |
| [SuperDesign IDE 扩展（旧版）](https://github.com/superdesigndev/superdesign) · 归档/历史 · 许可注意 | 保留原开放代码的 IDE 界面设计扩展，当前同名产品已改为 Web 应用。 | 7,635 | 0 | 2026-06-29 | 36.0 | AGPL-3.0 + 商业条款 |
| [Penpot MCP（旧仓库）](https://github.com/penpot/penpot-mcp) · 归档/历史 | 历史独立仓库的内容已并入 Penpot 主仓库的 mcp 目录。 | 536 | 0 | 2026-03-19 | 23.4 | MPL-2.0 |

## 怎么选

- 已有组件库，需要让团队生成交互原型：先看 [GitHub Replica](https://github.com/github/replica)；它依赖 GitHub Copilot app。希望自行选择 Agent 或模型时，看 [OpenDesign](https://github.com/nexu-io/open-design)。
- 已有网页或设计文件，需要继续编辑：代码工作区看 [Onlook](https://github.com/onlook-dev/onlook)；需要设计文件读写与脚本控制，看 [open-pencil/open-pencil](https://github.com/open-pencil/open-pencil)。
- 已有页面，只想改善动效或设计质量：动效看 [Emil Kowalski Skills](https://github.com/emilkowalski/skills)，布局和可访问性审查可先试 [Impeccable](https://github.com/pbakaus/impeccable)，再用实际浏览器、键盘和辅助技术验证。
- 需要带品牌样式的架构图，或需要 Agent 在画布上反复编辑：分别看 [Diagram Design](https://github.com/cathrynlavery/diagram-design) 和 [Excalidraw MCP Server](https://github.com/yctimlin/mcp_excalidraw)。
- 想在多个 Agent 中复用同一视觉语言：先用 [DESIGN.md 规范](https://github.com/google-labs-code/design.md) 写出颜色、排版和布局规则；第三方品牌样例只作参考。

首次试用建议选一个可公开的页面或图解，核对交付物能否继续编辑，检查字体和远程模型的数据路径，再用同一输入比较备选项目。

## 数据与维护

- [项目详表与固定版本证据](docs/projects.md)
- [综合、Star、活跃度、最近提交排序](docs/rankings.md)
- [论文与基准](docs/research.md)
- [检索与收录决策](research/README.md)
- [排序方法](docs/methodology.md)
- [贡献指南](CONTRIBUTING.md)

## 许可

本目录原创整理与脚本采用 [MIT](LICENSE)。链接项目、托管服务、数据集、素材和字体遵循各自条款。部分维护脚本沿用 [视频合集](https://github.com/ZanePoe/awesome_ai_video_creation) 的 MIT 实现。
