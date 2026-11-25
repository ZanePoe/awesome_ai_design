# 论文与基准

用于复现实验或建立自己的评测。以下论文不参加 GitHub 维护榜；有配套仓库的项目在目录的“论文、基准与数据集”分类中独立列出。

| 研究 | 测什么 | 从哪里开始 |
| --- | --- | --- |
| [Design2Code: How Far Are We From Automating Front-End Engineering?](https://arxiv.org/abs/2403.03163) | 从真实网页截图生成前端代码，关注页面复现 | [作者仓库](https://github.com/NoviScl/Design2Code) · [数据集](https://huggingface.co/datasets/SALT-NLP/Design2Code-hf) |
| [DesignBench: Exploring and Benchmarking MLLMs in Multi-framework Multi-task Front-end Code Generation](https://arxiv.org/abs/2506.06251) | 跨框架评估生成、编辑和修复，不只考截图复刻 | [作者项目页](https://webpai.github.io/DesignBench/) · [代码与数据入口](https://github.com/WebPAI/DesignBench) |

两个基准的任务、样本与评分条件不同，不能互换分数。首版未运行基准，没有报告跨项目质量排名。评测工作台时可额外检查可编辑性、交互状态、响应式布局和无障碍；这些不是 Stars 的替代口径。
