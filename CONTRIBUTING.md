# 贡献指南

欢迎提交设计 Agent、Agent Skills、设计编辑器或研究基准。请提供 canonical GitHub 仓库、主要用途、适用边界、功能及许可证原文链接。仅有托管服务的项目不列入核心；文档、格式与参考索引需明确标注其形态。

编辑 `data/projects.json`，保留 README 或官方文档的固定提交链接；检查 LICENSE、NOTICE 与数据、字体、素材的独立条款。不要直接编辑生成的 README 或榜单。新增项 `baseline` 保持 `false`；首版四个种子保持不变。

本地需要 Python 3.12+ 和已认证的 GitHub CLI（或配置 `GH_TOKEN`）。

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```
