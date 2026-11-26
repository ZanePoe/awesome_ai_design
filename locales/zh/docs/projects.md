# 项目说明与证据

每项定位来自固定提交的官方 README，未安装运行全部项目。指标刷新不会自动重审功能和许可证。


## [OpenDesign](https://github.com/nexu-io/open-design)

用本地 coding agent 或 OpenDesign Cloud 生成遵循设计系统的原型，并在团队工作台共享与迭代。

- 分类：设计 Agent 与原型工作台；核心候选。
- 适用边界：本地工作流、托管 Cloud 和 Go 套餐分开看；模型、模板和品牌素材的条款另计。
- 维护状态：近90天有提交；30 天提交 83 次，90 天提交 410 次。
- 许可：[Apache-2.0](https://github.com/nexu-io/open-design/blob/23812a9d081945704e5e1cdd63b41f653c208d9a/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/nexu-io/open-design/blob/23812a9d081945704e5e1cdd63b41f653c208d9a/README.md#L30) · [来源2](https://github.com/nexu-io/open-design/blob/23812a9d081945704e5e1cdd63b41f653c208d9a/README.md#L105)。

## [Open CoDesign](https://github.com/OpenCoworkAI/open-codesign)

本地桌面设计 Agent，将提示转为可预览的设计产物，允许连接自选模型。

- 分类：设计 Agent 与原型工作台；核心候选。
- 适用边界：本地工作区不代表推理完全离线；具体输出格式和能力随模型与发布版本而异。
- 维护状态：近90天有提交；30 天提交 21 次，90 天提交 145 次。
- 许可：[MIT](https://github.com/OpenCoworkAI/open-codesign/blob/1779bb5b0f15c734ff8ba06e2eb2463b5578e5b6/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/OpenCoworkAI/open-codesign/blob/1779bb5b0f15c734ff8ba06e2eb2463b5578e5b6/README.md#L7)。

## [GitHub Replica](https://github.com/github/replica)

使用团队已有组件、模式和设计指导，通过 GitHub Copilot 生成并迭代交互原型。

- 分类：设计 Agent 与原型工作台；核心候选。
- 适用边界：本地流程依赖 GitHub Copilot app、Git 和 Node.js，官方列出 macOS/Linux；可选的 Replica Hub 由团队托管。
- 维护状态：近90天有提交；30 天提交 78 次，90 天提交 132 次。
- 许可：[MIT](https://github.com/github/replica/blob/f468721924f63d885343acf61076dacb3c3dafc0/LICENSE)；开放许可证已核验。MIT 覆盖自有代码；根目录 NOTICE.md 列出 Mona Sans 等字体的 SIL OFL 1.1 许可。
- 功能核验：2026-11-18；[来源1](https://github.com/github/replica/blob/f468721924f63d885343acf61076dacb3c3dafc0/README.md#L7) · [来源2](https://github.com/github/replica/blob/f468721924f63d885343acf61076dacb3c3dafc0/README.md#L53) · [来源3](https://github.com/github/replica/blob/f468721924f63d885343acf61076dacb3c3dafc0/NOTICE.md#L3)。

## [fx0](https://github.com/vercel-labs/fx0)

基于 libfx 的轻量设计 Agent，用自然语言迭代并导出单文件 HTML 页面。

- 分类：设计 Agent 与原型工作台；核心候选。
- 适用边界：官方部署路线涉及 Vercel 与 AI Gateway；单文件产物不等同于完整产品代码库。
- 维护状态：近90天有提交；30 天提交 53 次，90 天提交 134 次。
- 许可：[Apache-2.0](https://github.com/vercel-labs/fx0/blob/ebc177ea055c863f6da50bfe4241fc8381a6b0c8/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/vercel-labs/fx0/blob/ebc177ea055c863f6da50bfe4241fc8381a6b0c8/README.md#L3)。

## [LangChain Content Studio](https://github.com/langchain-ai/design-agent)

面向团队的品牌设计 Agent，从 Slack 接收素材与需求，交付平面图、演示或动态内容。

- 分类：设计 Agent 与原型工作台；核心候选。
- 适用边界：官方 Slack 部署路线依赖 Managed Deep Agents；开源代码不等于托管免费。
- 维护状态：近90天有提交；30 天提交 29 次，90 天提交 72 次。
- 许可：[Apache-2.0](https://github.com/langchain-ai/design-agent/blob/8134d7ccdc3f91a0192d45499dc368e9f89d7910/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/langchain-ai/design-agent/blob/8134d7ccdc3f91a0192d45499dc368e9f89d7910/README.md#L26)。

## [Penpot](https://github.com/penpot/penpot)

可自托管的协作设计平台，提供设计 token、组件和 MCP 接口衔接设计与代码。

- 分类：可编辑画布与矢量设计；核心候选。
- 适用边界：编辑器可独立使用；MCP 属集成能力，不等同于内置生成模型。
- 维护状态：近90天有提交；30 天提交 670 次，90 天提交 1621 次。
- 许可：[MPL-2.0](https://github.com/penpot/penpot/blob/14abaf93f4ec220970b07e85e915446e7a11150d/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/penpot/penpot/blob/14abaf93f4ec220970b07e85e915446e7a11150d/README.md#L47)。

## [OpenPencil（open-pencil）](https://github.com/open-pencil/open-pencil)

具备 AI、CLI 与 MCP 的可编程设计编辑器，可打开 .fig 与 .pen 文件。

- 分类：可编辑画布与矢量设计；核心候选。
- 适用边界：仍在开发，具体节点、字体和文件往返保真需按真实文件验证；不是 ZSeven-W 的同名仓库。
- 维护状态：近90天有提交；30 天提交 637 次，90 天提交 1585 次。
- 许可：[MIT](https://github.com/open-pencil/open-pencil/blob/82e3d6ad5e94a6017c1b55f4fc61c58803063644/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/open-pencil/open-pencil/blob/82e3d6ad5e94a6017c1b55f4fc61c58803063644/README.md#L9)。

## [OpenPencil（ZSeven-W）](https://github.com/ZSeven-W/openpencil)

将自然语言转为画布里的可编辑界面，支持多个 Agent 并行设计和 MCP 操作。

- 分类：可编辑画布与矢量设计；核心候选。
- 适用边界：模型接入和框架导出需逐项验证；它是独立仓库，不与 open-pencil 合并计算指标。
- 维护状态：近90天有提交；30 天提交 220 次，90 天提交 914 次。
- 许可：[MIT](https://github.com/ZSeven-W/openpencil/blob/2bbc658caba5139cdfeb768b65da7f6f0080a703/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/ZSeven-W/openpencil/blob/2bbc658caba5139cdfeb768b65da7f6f0080a703/README.md#L44)。

## [Onlook](https://github.com/onlook-dev/onlook)

本地优先的代码可视化编辑器，由 Claude Code 或 Codex 等现有 Agent 在项目中工作。

- 分类：可编辑画布与矢量设计；核心候选。
- 适用边界：不自带模型；代码许可不覆盖仓库中部分品牌、字体和第三方资产。
- 维护状态：近90天有提交；30 天提交 40 次，90 天提交 40 次。
- 许可：[Apache-2.0](https://github.com/onlook-dev/onlook/blob/7b17f48c59adb7ac4ec30a6982e4971f22846c2b/LICENSE)；开放许可证已核验。Apache-2.0 覆盖源代码，但 README 及 NOTICE 说明部分字体、标识和图像不在代码授权内。
- 功能核验：2026-11-18；[来源1](https://github.com/onlook-dev/onlook/blob/7b17f48c59adb7ac4ec30a6982e4971f22846c2b/README.md#L45) · [来源2](https://github.com/onlook-dev/onlook/blob/7b17f48c59adb7ac4ec30a6982e4971f22846c2b/README.md#L148)。

## [Velloo](https://github.com/velloo-design/velloo)

让 coding agent 使用现有应用组件在本地画布探索多个方向，再将选中的设计写回应用。

- 分类：可编辑画布与矢量设计；核心候选。
- 适用边界：主要针对已有应用的设计迭代；跨框架支持与实际回写效果未测。
- 维护状态：近90天有提交；30 天提交 39 次，90 天提交 260 次。
- 许可：[Apache-2.0](https://github.com/velloo-design/velloo/blob/8c1f140049bcc1db4e1d6d5c578eddcd2ef74e4a/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/velloo-design/velloo/blob/8c1f140049bcc1db4e1d6d5c578eddcd2ef74e4a/README.md#L12)。

## [Impeccable](https://github.com/pbakaus/impeccable)

为 coding agent 提供设计词汇、精修、批评与审查命令，用于迭代已有界面。

- 分类：前端设计、动效与审查 Skills；核心候选。
- 适用边界：Skill 指导和检查不等于人工设计审查或无障碍认证。
- 维护状态：近90天有提交；30 天提交 1299 次，90 天提交 2250 次。
- 许可：[Apache-2.0](https://github.com/pbakaus/impeccable/blob/d41d9860b0094dcb68030657da63461212835aaa/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/pbakaus/impeccable/blob/d41d9860b0094dcb68030657da63461212835aaa/README.md#L3)。

## [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

为多个前端技术栈提供风格、配色、排版和设计系统建议的 Agent Skill。

- 分类：前端设计、动效与审查 Skills；核心候选。
- 适用边界：规则与生成结果是设计起点；无障碍和最终实现仍需测试。
- 维护状态：近90天有提交；30 天提交 37 次，90 天提交 95 次。
- 许可：[MIT](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7436a6e0b6dc3add7c12d5b6ef1ccd3d410dd7fd/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7436a6e0b6dc3add7c12d5b6ef1ccd3d410dd7fd/README.md#L30)。

## [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit)

将 OpenDesign 的设计 Skills、品牌设计系统与示例移植到 coding agent 内使用。

- 分类：前端设计、动效与审查 Skills；核心候选。
- 适用边界：不是 OpenDesign 桌面应用；示例、品牌资源和生成结果按各自使用条件核验。
- 维护状态：近90天有提交；30 天提交 224 次，90 天提交 435 次。
- 许可：[MIT](https://github.com/feimacode/open-design-agent-kit/blob/1b3832c3452720f028a96b1bdab805ecc1aa3213/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/feimacode/open-design-agent-kit/blob/1b3832c3452720f028a96b1bdab805ecc1aa3213/README.md#L7)。

## [Emil Kowalski Skills](https://github.com/emilkowalski/skills)

为设计师和工程师提供 UI 与动效 Skills，覆盖动效选择、审查和性能改进。

- 分类：前端设计、动效与审查 Skills；核心候选。
- 适用边界：规则源于作者的设计工程实践；建议需结合用户测试、减弱动态效果偏好和真实设备表现。
- 维护状态：近90天有提交；30 天提交 12 次，90 天提交 19 次。
- 许可：[MIT](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/README.md#L11) · [来源2](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/README.md#L45)。

## [Logo Design Skill](https://github.com/kaankiziltug/logo-design-skill)

从 brief 到可交付 SVG 与品牌规范的 logo 设计技能，附 1,400+ 真实 logo 参考库、几何与光学修正规则和无依赖 Python 检查工具。

- 分类：前端设计、动效与审查 Skills；核心候选。
- 适用边界：参考库仅用于研究构造、类型与避免撞型，官方明令不得复制、描摹或模仿；产出需自行做商标检索，README 示例品牌为虚构；16 px、单色、反白、镜像等测试由自带脚本执行，未做统一效果评测。
- 维护状态：近90天有提交；30 天提交 7 次，90 天提交 32 次。
- 许可：[MIT（代码与技能）+ 第三方商标 logo 库除外](https://github.com/kaankiziltug/logo-design-skill/blob/e9eaddc07895575253d6663320354a708f53e955/TRADEMARKS.md)；复合/条件许可。TRADEMARKS.md 声明 assets/library/svg 内 1,432 个 logo 均为各自权利人的商标，MIT 不覆盖也不授权，仅作品构研究参考，权利人可要求下架。
- 功能核验：2026-11-26；[来源1](https://github.com/kaankiziltug/logo-design-skill/blob/e9eaddc07895575253d6663320354a708f53e955/README.md#L7) · [来源2](https://github.com/kaankiziltug/logo-design-skill/blob/e9eaddc07895575253d6663320354a708f53e955/README.md#L16) · [来源3](https://github.com/kaankiziltug/logo-design-skill/blob/e9eaddc07895575253d6663320354a708f53e955/TRADEMARKS.md#L10)。

## [Make Interfaces Feel Better](https://github.com/jakubkrehel/make-interfaces-feel-better)

聚焦界面细节的 agent 技能：动效、字体、图标、hover 状态、光学对齐与同心圆角等，一条 skills CLI 命令安装。

- 分类：前端设计、动效与审查 Skills；核心候选。
- 适用边界：只提供细节规则与清单，不替代布局与信息架构决策；效果需在真实浏览器、键盘与辅助技术下验证，作者未发布统一评测数据。
- 维护状态：近90天有提交；30 天提交 2 次，90 天提交 3 次。
- 许可：[MIT](https://github.com/jakubkrehel/make-interfaces-feel-better/blob/6d9f2f1df10e8ce2ae1708598a73b0506fb98794/LICENSE)；开放许可证已核验。仓库根 LICENSE 为 MIT；SKILL.md 引用的外部资源、字体与示例素材按各自条款核验。
- 功能核验：2026-11-26；[来源1](https://github.com/jakubkrehel/make-interfaces-feel-better/blob/6d9f2f1df10e8ce2ae1708598a73b0506fb98794/README.md#L7) · [来源2](https://github.com/jakubkrehel/make-interfaces-feel-better/blob/6d9f2f1df10e8ce2ae1708598a73b0506fb98794/README.md#L9) · [来源3](https://github.com/jakubkrehel/make-interfaces-feel-better/blob/6d9f2f1df10e8ce2ae1708598a73b0506fb98794/README.md#L14)。

## [cc-skills](https://github.com/samber/cc-skills)

跨领域 Agent Skills 合集，按需加载；设计线里的 frontend-design-deslop 负责去掉前端的“AI 味”。

- 分类：前端设计、动效与审查 Skills；核心候选。
- 适用边界：除界面设计外还含文案、Git、深度调研、安全扫描等技能，设计只是其中一条线；README 的 -28% 等对比数字是作者自建评测，未独立复现；Go 相关技能在另一仓库 cc-skills-golang。
- 维护状态：近90天有提交；30 天提交 2 次，90 天提交 15 次。
- 许可：[MIT](https://github.com/samber/cc-skills/blob/50a33836b20f690c668af557bd9ef9d07a8c7ef2/LICENSE)；开放许可证已核验。仓库根 LICENSE 为 MIT；各技能引用的站点、字体与素材仍按各自条款核验。
- 功能核验：2026-11-26；[来源1](https://github.com/samber/cc-skills/blob/50a33836b20f690c668af557bd9ef9d07a8c7ef2/README.md#L3) · [来源2](https://github.com/samber/cc-skills/blob/50a33836b20f690c668af557bd9ef9d07a8c7ef2/README.md#L20) · [来源3](https://github.com/samber/cc-skills/blob/50a33836b20f690c668af557bd9ef9d07a8c7ef2/README.md#L229)。

## [Better Design](https://github.com/Moddingflow/better-design)

给 coding agent 一套可复用的界面设计流程：产品专属艺术指导、共享 DESIGN.md、量化排版与控件规格，并附校验脚本与可点击演示。

- 分类：前端设计、动效与审查 Skills；核心候选。
- 适用边界：官方说明结果依赖模型、简报、项目、参考与可用运行时工具，技能只提供流程、配方与评审清单；演示中的盲评对比是作者实验，未做统一复现；参考区记录的 Impeccable 等第三方来源保留各自条款。
- 维护状态：近90天有提交；30 天提交 0 次，90 天提交 9 次。
- 许可：[MIT](https://github.com/Moddingflow/better-design/blob/c373ad7fa122b8c0d63b1be756443cc93a56e71d/LICENSE)；开放许可证已核验。仓库根 LICENSE 为 MIT，README 明确可商用但需保留许可声明；references 记录的第三方来源（含 Impeccable，Apache-2.0）各自授权。
- 功能核验：2026-11-26；[来源1](https://github.com/Moddingflow/better-design/blob/c373ad7fa122b8c0d63b1be756443cc93a56e71d/README.md#L5) · [来源2](https://github.com/Moddingflow/better-design/blob/c373ad7fa122b8c0d63b1be756443cc93a56e71d/README.md#L11) · [来源3](https://github.com/Moddingflow/better-design/blob/c373ad7fa122b8c0d63b1be756443cc93a56e71d/README.md#L302)。

## [Frontend AI Skills](https://github.com/JustineBijuPaul/frontend-ai-skills)

可按需加载的模块化前端 Skills，覆盖动效、交互和可访问性等主题。

- 分类：前端设计、动效与审查 Skills；核心候选。
- 适用边界：同时包含通用前端工程知识；重点关注设计与交互相关模块。
- 维护状态：近90天有提交；30 天提交 0 次，90 天提交 86 次。
- 许可：[MIT](https://github.com/JustineBijuPaul/frontend-ai-skills/blob/f52d23c5b8f51caefccb97ea2bc88f6db7bc6120/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/JustineBijuPaul/frontend-ai-skills/blob/f52d23c5b8f51caefccb97ea2bc88f6db7bc6120/README.md#L5)。

## [Stitch Design Skills](https://github.com/google-labs-code/stitch-skills)

面向 Google Stitch 的官方技能和插件集合，连接 Agent 与其设计流程。

- 分类：设计系统与 DESIGN.md；相邻基础设施。
- 适用边界：开源的是技能与插件，Stitch 服务能力、账户和用量按服务条款。
- 维护状态：近90天有提交；30 天提交 22 次，90 天提交 22 次。
- 许可：[Apache-2.0](https://github.com/google-labs-code/stitch-skills/blob/4cf4db8e4143b09e40f9bc887429d81f41ab3947/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/google-labs-code/stitch-skills/blob/4cf4db8e4143b09e40f9bc887429d81f41ab3947/README.md#L3)。

## [StyleSeed](https://github.com/bitjaru/styleseed)

为产品生成起步设计系统（外观、配色、字阶、间距、圆角、动效），把决定锁进 STYLESEED.md 与 CSS token，并让 coding agent 在后续每个页面按 74 条 craft rules 和 0–100 打分闸门守住它。

- 分类：设计系统与 DESIGN.md；核心候选。
- 适用边界：作者的目标是可重复执行专家判断，不宣称当下产出即专家级，分数不替代人工设计验收；README 的 +5.3 分来自 120 个自建渲染单元（Codex 与 Claude Code 分别测评，纯规则不加闸门时结果不稳定），不是第三方基准；安装走 npx skills add 需要 Node.js/npm；核心 skill 声明无运行时依赖，构建与验证所用第三方组件在 THIRD_PARTY.md 逐项列出版本与许可。
- 维护状态：近90天有提交；30 天提交 48 次，90 天提交 96 次。
- 许可：[MIT](https://github.com/bitjaru/styleseed/blob/6963076194fdefd84933d87a1a4d282fdd0a7b0f/LICENSE)；开放许可证已核验。仓库根 LICENSE 为 MIT；THIRD_PARTY.md 逐项列出构建与验证所用组件及版本（Playwright、TypeScript 为 Apache-2.0，lucide-react 为 ISC，其余 MIT），再分发时按各自许可保留声明。
- 功能核验：2026-11-26；[来源1](https://github.com/bitjaru/styleseed/blob/6963076194fdefd84933d87a1a4d282fdd0a7b0f/README.md#L7) · [来源2](https://github.com/bitjaru/styleseed/blob/6963076194fdefd84933d87a1a4d282fdd0a7b0f/README.md#L22) · [来源3](https://github.com/bitjaru/styleseed/blob/6963076194fdefd84933d87a1a4d282fdd0a7b0f/README.md#L88) · [来源4](https://github.com/bitjaru/styleseed/blob/6963076194fdefd84933d87a1a4d282fdd0a7b0f/README.md#L216)。

## [Google DESIGN.md](https://github.com/google-labs-code/design.md)

视觉身份描述规范，将机器可读的设计 token 和供 Agent 阅读的设计原则放在同一文件。

- 分类：设计系统与 DESIGN.md；核心候选。
- 适用边界：它是可移植规范和工具，不是设计 Agent；宿主对规范的支持可能不同。
- 维护状态：近90天有提交；30 天提交 8 次，90 天提交 9 次。
- 许可：[Apache-2.0](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/README.md#L3)。

## [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md)

汇集可复用的 DESIGN.md 参考文档，为 Agent 提供品牌风格、排版、色彩和组件约定。

- 分类：设计系统与 DESIGN.md；相邻基础设施。
- 适用边界：这是参考集合，不是生成器；品牌标识、字体等第三方权利不包含在仓库 MIT 许可内。
- 维护状态：近90天有提交；30 天提交 3 次，90 天提交 8 次。
- 许可：[MIT](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/README.md#L30)。

## [extract-design-system](https://github.com/arvindrk/extract-design-system)

从任意公开网站逆向出颜色、字体、间距、圆角与阴影等 design tokens，输出 W3C 兼容 tokens.json 与 CSS 自定义属性文件。

- 分类：设计系统与 DESIGN.md；核心候选。
- 适用边界：skills-first 仓库，CLI 是技能执行的载体；抽取公开站点得到的品牌配色、字体与图形不等于取得授权，产出需按目标站点条款、字体许可与商标权另行核验。
- 维护状态：91–365天未提交；30 天提交 0 次，90 天提交 0 次。
- 许可：[MIT](https://github.com/arvindrk/extract-design-system/blob/1873741ba8dea755e35e6e15134f7918cd58e036/LICENSE)；开放许可证已核验。仓库根 LICENSE 为 MIT；被抽取站点的商标、字体与素材权利不在该许可范围内。
- 功能核验：2026-11-26；[来源1](https://github.com/arvindrk/extract-design-system/blob/1873741ba8dea755e35e6e15134f7918cd58e036/README.md#L15) · [来源2](https://github.com/arvindrk/extract-design-system/blob/1873741ba8dea755e35e6e15134f7918cd58e036/README.md#L19) · [来源3](https://github.com/arvindrk/extract-design-system/blob/1873741ba8dea755e35e6e15134f7918cd58e036/README.md#L31)。

## [Screenshot to Code](https://github.com/abi/screenshot-to-code)

利用模型将截图、原型、Figma 设计或屏幕录制转为界面代码。

- 分类：设计转代码与 MCP 桥接；核心候选。
- 适用边界：模型费用、数据流向和导出技术栈随配置；视觉近似不等同于可维护或无障碍代码。
- 维护状态：近90天有提交；30 天提交 4 次，90 天提交 6 次。
- 许可：[MIT](https://github.com/abi/screenshot-to-code/blob/f2e5bbdd1dd5d93c259548d9bccf54e2a5f06a30/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/abi/screenshot-to-code/blob/f2e5bbdd1dd5d93c259548d9bccf54e2a5f06a30/README.md#L3)。

## [Figma MCP 官方指南](https://github.com/figma/mcp-server-guide)

Figma 官方接入指南，说明 Agent 获取设计上下文及部分远程写入工作流。

- 分类：设计转代码与 MCP 桥接；相邻基础设施。
- 适用边界：仓库是文档，不是可自托管服务；读取、写入、席位与速率限制不同。
- 维护状态：近90天有提交；30 天提交 9 次，90 天提交 30 次。
- 许可：[未确认](https://github.com/figma/mcp-server-guide/blob/490a73c7537123cb1f0bcaced658585f0ee32fd9/README.md)；许可待核验。未确认仓库根目录许可证；作为公开参考收录，不视为获得重用授权。
- 功能核验：2026-11-18；[来源1](https://github.com/figma/mcp-server-guide/blob/490a73c7537123cb1f0bcaced658585f0ee32fd9/README.md#L3)。

## [Framelink Figma MCP](https://github.com/GLips/Figma-Context-MCP)

向 coding agent 提供 Figma 文件的设计上下文，辅助实现已有界面。

- 分类：设计转代码与 MCP 桥接；核心候选。
- 适用边界：需要有权限的 Figma 访问；这是上下文桥，不是独立画布或官方托管 MCP。
- 维护状态：91–365天未提交；30 天提交 0 次，90 天提交 0 次。
- 许可：[MIT](https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/README.md#L28)。

## [Talk to Figma MCP](https://github.com/grab/cursor-talk-to-figma-mcp)

通过 MCP 服务、Figma 插件和 WebSocket 桥让 Agent 读取与修改 Figma 设计。

- 分类：设计转代码与 MCP 桥接；核心候选。
- 适用边界：核对插件、文件写权限和连接范围；旧地址 sonnylazuardi/cursor-talk-to-figma-mcp 重定向至本仓库。
- 维护状态：91–365天未提交；30 天提交 0 次，90 天提交 0 次。
- 许可：[MIT](https://github.com/grab/cursor-talk-to-figma-mcp/blob/ddd90f3a6d454ea0b2fc29f1b084f50fd062b880/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/grab/cursor-talk-to-figma-mcp/blob/ddd90f3a6d454ea0b2fc29f1b084f50fd062b880/README.md#L3)。

## [Diagram Design](https://github.com/cathrynlavery/diagram-design)

将架构、流程、数据等图解输出为带品牌样式的自包含 HTML/SVG。

- 分类：图解与视觉表达；核心候选。
- 适用边界：它是 Agent Skill；导入文件的版权、第三方依赖和可访问性需要单独核对。
- 维护状态：近90天有提交；30 天提交 96 次，90 天提交 364 次。
- 许可：[MIT](https://github.com/cathrynlavery/diagram-design/blob/f6db0decea96de66b901331a0f79a8d4b147ebae/LICENSE)；开放许可证已核验。自有代码采用 MIT；随附依赖另见 THIRD_PARTY_LICENSES.md。
- 功能核验：2026-11-18；[来源1](https://github.com/cathrynlavery/diagram-design/blob/f6db0decea96de66b901331a0f79a8d4b147ebae/README.md#L10) · [来源2](https://github.com/cathrynlavery/diagram-design/blob/f6db0decea96de66b901331a0f79a8d4b147ebae/README.md#L51)。

## [Excalidraw MCP Server](https://github.com/yctimlin/mcp_excalidraw)

提供可读写的 Excalidraw 画布，通过 CLI、Skill 或 MCP 修改并保存图解。

- 分类：图解与视觉表达；核心候选。
- 适用边界：需要对应画布或服务环境；多人协作与导出保真需按部署测试。
- 维护状态：近90天有提交；30 天提交 7 次，90 天提交 33 次。
- 许可：[MIT](https://github.com/yctimlin/mcp_excalidraw/blob/81720ac819d2325177cd6137c6ad41d52d0f5374/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/yctimlin/mcp_excalidraw/blob/81720ac819d2325177cd6137c6ad41d52d0f5374/README.md#L8)。

## [Spotkit](https://github.com/Devesh-Shirsath/spotkit)

把功能描述转成真正 SVG（不是位图）的抽象产品插图技能：先问功能实际做什么、表达何种关系，再选 2-5 个 UI 原语与版式。

- 分类：图解与视觉表达；核心候选。
- 适用边界：面向单色抽象插图，不处理照片与复杂插画；同一套规则产出十二个版式，明暗双主题共用十二个 CSS 变量；示例取自作者自有功能集，落到自有品牌规范前需验证一致性。
- 维护状态：近90天有提交；30 天提交 0 次，90 天提交 33 次。
- 许可：[MIT](https://github.com/Devesh-Shirsath/spotkit/blob/f9b6a611e14c68a88fae44b4c67777a25b9c1d2c/LICENSE)；开放许可证已核验。仓库根 LICENSE 为 MIT，未见第三方素材例外声明；示例 SVG 与图标脚本产物的再分发需自行核对。
- 功能核验：2026-11-26；[来源1](https://github.com/Devesh-Shirsath/spotkit/blob/f9b6a611e14c68a88fae44b4c67777a25b9c1d2c/README.md#L4) · [来源2](https://github.com/Devesh-Shirsath/spotkit/blob/f9b6a611e14c68a88fae44b4c67777a25b9c1d2c/README.md#L18) · [来源3](https://github.com/Devesh-Shirsath/spotkit/blob/f9b6a611e14c68a88fae44b4c67777a25b9c1d2c/README.md#L117)。

## [Vane GPT Image Skills](https://github.com/VaneAi888/vane-gpt-image-skills)

GPT Image 生图玩法合集，含 36 种版式的电影级海报设计：按影片情绪、故事与素材选构图、设计片名与信息层级，交付方案、可复制提示词或实际图片。

- 分类：平面与图像设计；核心候选。
- 适用边界：产出是位图海报、封面与社交图文，不是界面或矢量稿；实际成图依赖宿主环境可用的图像生成/编辑工具，仓库不自带 API 调用；GIF 动作、图片文字与透明背景效果取决于素材与可用工具；SKILL.md 明写不得编造真实发行信息、获奖桂冠、评分、片方商标或背书；36 版式与中英文预览为作者自测展示，无第三方评测。
- 维护状态：近90天有提交；30 天提交 51 次，90 天提交 51 次。
- 许可：[MIT](https://github.com/VaneAi888/vane-gpt-image-skills/blob/39256f5df550354ab2248bd5ee7a76506dab9c85/LICENSE)；开放许可证已核验。仓库根 LICENSE 为 MIT；海报与预览图是作者生成的示例，复用真实片名、商标或第三方素材仍需另行授权。
- 功能核验：2026-11-26；[来源1](https://github.com/VaneAi888/vane-gpt-image-skills/blob/39256f5df550354ab2248bd5ee7a76506dab9c85/README.md#L3) · [来源2](https://github.com/VaneAi888/vane-gpt-image-skills/blob/39256f5df550354ab2248bd5ee7a76506dab9c85/README.md#L34) · [来源3](https://github.com/VaneAi888/vane-gpt-image-skills/blob/39256f5df550354ab2248bd5ee7a76506dab9c85/docs/vane-cinematic-poster.md#L62) · [来源4](https://github.com/VaneAi888/vane-gpt-image-skills/blob/39256f5df550354ab2248bd5ee7a76506dab9c85/skills/vane-cinematic-poster/SKILL.md#L20)。

## [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill)

模拟高价 PPT 设计公司流程的 Claude Code Skill：需求调研→资料搜集→大纲→策划稿→HTML 设计稿→SVG+PPTX 后处理，把一句话变成可编辑演示稿。

- 分类：演示与文档设计；核心候选。
- 适用边界：26 风格、18 图表与「对标世界级品牌」为作者自述，未做统一评测；导出 SVG/PPTX 需 Python≥3.9 与 Node≥18 等依赖，缺失时只交付 HTML 预览；references 下多个目录来自上游 sunbigfly/ppt-agent-skills 的修改版，再分发需保留 MIT 声明与 ATTRIBUTIONS.md；风格参考真实品牌排版不构成对任何商标的授权。
- 维护状态：近90天有提交；30 天提交 11 次，90 天提交 11 次。
- 许可：[MIT](https://github.com/Akxan/ppt-agent-skill/blob/e2f97f46a2f92633d3f9b95a1a61b0a668c704b3/LICENSE)；开放许可证已核验。仓库根 LICENSE 为 MIT，版权行署上游作者 sunbigfly（2025）；ATTRIBUTIONS.md 说明 references 的 principles/design-runtime/blocks/page-templates/layouts 等目录来自 sunbigfly/ppt-agent-skills 的修改版，再分发需同时保留许可与署名。
- 功能核验：2026-11-26；[来源1](https://github.com/Akxan/ppt-agent-skill/blob/e2f97f46a2f92633d3f9b95a1a61b0a668c704b3/README.md#L59) · [来源2](https://github.com/Akxan/ppt-agent-skill/blob/e2f97f46a2f92633d3f9b95a1a61b0a668c704b3/README.md#L69) · [来源3](https://github.com/Akxan/ppt-agent-skill/blob/e2f97f46a2f92633d3f9b95a1a61b0a668c704b3/README.md#L118) · [来源4](https://github.com/Akxan/ppt-agent-skill/blob/e2f97f46a2f92633d3f9b95a1a61b0a668c704b3/ATTRIBUTIONS.md#L13)。

## [DesignBench](https://github.com/WebPAI/DesignBench)

用于评估多框架前端代码生成、编辑与修复的研究基准。

- 分类：论文、基准与数据集；研究/评测。
- 适用边界：仓库根目录许可证尚未确认；论文、代码和数据的使用条款应分别核对。
- 维护状态：91–365天未提交；30 天提交 0 次，90 天提交 0 次。
- 许可：[未确认](https://github.com/WebPAI/DesignBench/blob/a1e58d66ecbf1f77848bc5529ee7bbbe33bc25ba/README.md)；许可待核验。未确认仓库根目录许可证；作为公开参考收录，不视为获得重用授权。
- 功能核验：2026-11-18；[来源1](https://github.com/WebPAI/DesignBench/blob/a1e58d66ecbf1f77848bc5529ee7bbbe33bc25ba/README.md#L8)。

## [Design2Code](https://github.com/NoviScl/Design2Code)

以真实网页的截图到代码为任务，提供数据与自动评估工具。

- 分类：论文、基准与数据集；研究/评测。
- 适用边界：代码许可不替代数据集和权重条款；其结果不与合集维护分混用。
- 维护状态：超过365天未提交；30 天提交 0 次，90 天提交 0 次。
- 许可：[MIT](https://github.com/NoviScl/Design2Code/blob/7a575e4c33f417c4be5c64072b8f5798de0d0f99/CODE_LICENSE)；开放许可证已核验。MIT 为代码许可；数据集另见仓库 DATA_LICENSE，模型权重需核对发布页。
- 功能核验：2026-11-18；[来源1](https://github.com/NoviScl/Design2Code/blob/7a575e4c33f417c4be5c64072b8f5798de0d0f99/README.md#L13)。

## [WebDesignAgent](https://github.com/DAMO-NLP-SG/WebDesignAgent)

网站生成研究原型，展示由描述、参考布局、图像和反馈驱动的设计流程。

- 分类：论文、基准与数据集；研究/评测。
- 适用边界：学术原型与示例，不假定能直接作为生产设计工作台。
- 维护状态：超过365天未提交；30 天提交 0 次，90 天提交 0 次。
- 许可：[Apache-2.0](https://github.com/DAMO-NLP-SG/WebDesignAgent/blob/03707c4654c1627b4f8ec254147d31495955f44e/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/DAMO-NLP-SG/WebDesignAgent/blob/03707c4654c1627b4f8ec254147d31495955f44e/README.md#L6)。

## [SuperDesign IDE 扩展（旧版）](https://github.com/superdesigndev/superdesign)

保留原开放代码的 IDE 界面设计扩展，当前同名产品已改为 Web 应用。

- 分类：历史与归档项目；历史参考。
- 适用边界：旧扩展不再活跃维护；现行 Web 产品不是这个仓库的自托管版本。
- 维护状态：归档 / 历史；30 天提交 0 次，90 天提交 0 次。
- 许可：[AGPL-3.0 + 商业条款](https://github.com/superdesigndev/superdesign/blob/49e2b9dd9615c6dae936b326b1ddb85d4f1d6f19/LICENSE)；复合/条件许可。大部分文件按 AGPLv3；带 Enterprise 标记的文件适用独立商业许可。
- 功能核验：2026-11-18；[来源1](https://github.com/superdesigndev/superdesign/blob/49e2b9dd9615c6dae936b326b1ddb85d4f1d6f19/README.md#L4)。

## [Penpot MCP（旧仓库）](https://github.com/penpot/penpot-mcp)

历史独立仓库的内容已并入 Penpot 主仓库的 mcp 目录。

- 分类：历史与归档项目；历史参考。
- 适用边界：新用户应从 Penpot 主仓进入；旧仓保留仅供迁移追溯。
- 维护状态：归档 / 历史；30 天提交 0 次，90 天提交 0 次。
- 许可：[MPL-2.0](https://github.com/penpot/penpot-mcp/blob/73e0cd21853dd03103f7ac675042b1277ee0b736/LICENSE)；开放许可证已核验。核验仓库许可文件；第三方素材、字体、数据及托管服务不随代码许可自动授权。
- 功能核验：2026-11-18；[来源1](https://github.com/penpot/penpot-mcp/blob/73e0cd21853dd03103f7ac675042b1277ee0b736/README.md#L2)。
