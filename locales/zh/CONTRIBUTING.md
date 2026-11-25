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

## 多语言文件

- `data/projects.json` 是中文规范审核数据：事实只在这里改一次。
- 其它语言的文案来自 `locales/<lang>/entries.json`（`description`、`boundary`、`license_label`、`license_note`）与 `locales/<lang>/ui.json`；`zh` 直接回落 `data/projects.json`，因此没有 `locales/zh/entries.json`。
- 新增项目或改写定位、边界、许可结论时，同一个 PR 内补齐 en/es/hi/fr 四个 locale，否则 `python scripts/build.py --check` 与 `python -m unittest discover -s tests -v` 会失败。
- 静态文档：英文在根目录 `docs/` 与 `CONTRIBUTING.md`，其它语言在 `locales/<lang>/` 下同名相对路径。镜像里的相对链接按该文件所在目录解析，从 `locales/<lang>/docs/` 指向仓库根的 `data/`、`scripts/`、`research/`、`LICENSE`、`record/` 需要写 `../../../`，从 `locales/<lang>/CONTRIBUTING.md` 需要写 `../../`；`docs/readme-intro.md` 例外，它会被嵌入 README，按语言根目录解析。
- `record/` 与 `research/` 保持撰写时的原文，作为审计痕迹，不做机器翻译。
- 生成物（`README.md`、`docs/projects.md`、`docs/rankings.md`、`data/rankings.csv`、各语言镜像的同名文件）不要手改，由 `python scripts/build.py` 产出。
