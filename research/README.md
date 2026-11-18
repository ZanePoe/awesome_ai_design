# 检索与收录

首版基于 [四个种子](baseline.md)，通过 GitHub、公开网页与内容工厂做候选发现。功能、许可和 canonical 仓库只以官方材料复核；收录决定和固定证据保存在 [projects.json](../data/projects.json)。

- 第一轮：设计 Agent、可编辑画布、设计到代码、前端设计 Skills、公开索引、基准、访问限制和近期项目；交叉查阅 [Awesome AI Design](https://github.com/jangtrinh/awesome-ai-design) 发现漏项。
- 第二轮：基于 SVG、Agent 宿主、UI UX Pro Max 等线索补搜动效、可访问性、设计 MCP 与前端评测。
- 第三轮：交叉核验同名 OpenPencil、Onlook 与 Velloo；通过固定提交的 README、LICENSE 与适用的 NOTICE 核实功能与授权边界。三轮预算结束，不声称穷尽。
- 内容工厂：2026-08-18 至 2026-11-18，查询 `OpenDesign OR OpenPencil OR diagram-design` 和 `AI design OR DESIGN.md OR UI UX Pro Max`。每组首样本 8 条，未提取到可直接核验的 GitHub 地址。公开目录不复制内部正文或接口数据。

## 代表性收录决定

- 两个 OpenPencil 分别收录，按 owner/repo 去重，不合计维护指标。
- Talk to Figma 使用重定向后的 canonical 仓库；官方 Figma MCP 指南作为相邻参考，不能当可部署源码。
- SuperDesign IDE 扩展与 Penpot 独立 MCP 保留为历史；后者的活跃实现见 Penpot 主仓。
- 许可证未确认的 DesignBench 仅列为学术参考；论文、代码、数据和模型权重的许可证不能互相替代。
- 首版未安装或运行上游项目。对视觉质量、跨工具文件保真或用户体验没有统一实测，不作排名。
