# AI Chavruta Learning Skill

[English](README.md) | 简体中文

一个面向 Codex 的自适应学习 Skill。它把 AI 从“替你总结答案的助手”变成一位苏格拉底式学习伙伴：先提问诊断，再根据你的回答调整难度，通过追问、最小提示、纠错和迁移练习，帮助你真正掌握知识。

## 它能做什么

- 先回忆、后讲解，减少“看懂了但不会用”的错觉。
- 根据学习者的基础、信心和状态动态调整问题难度。
- 同时评价答案正确性与推理质量，而不只判断对错。
- 在连续答错或认知过载时，自动缩小问题、增加脚手架或提供示范。
- 支持论文阅读、理科压力测试、人文辩论、语言学习和考试训练。
- 只从真实错误和薄弱点中提取原子化复习卡片，可用于 Anki 或 RemNote。
- 对长文档进行分段学习，并在各段之间建立概念联系。

## 安装到 Codex

将仓库中的 `ai-chavruta-learning` 文件夹复制到 Codex 的 skills 目录：

```text
~/.codex/skills/ai-chavruta-learning
```

Windows 通常对应：

```text
%USERPROFILE%\.codex\skills\ai-chavruta-learning
```

安装后，新建一个 Codex 对话并输入：

```text
使用 $ai-chavruta-learning 帮我学习[主题或材料]。
```

## 最短使用方式

你只需要提供学习材料或主题，再说明目标。例如：

```text
使用 $ai-chavruta-learning 帮我读这篇论文。先诊断我的理解，再针对薄弱点追问，最后只把我的错误整理成复习卡片。
```

也可以直接指定训练方式：

```text
使用 $ai-chavruta-learning 对我进行高中物理压力测试。每轮只问一个问题，我连续答错时降低难度，但不要立即公布完整答案。
```

```text
使用 $ai-chavruta-learning 和我辩论这个历史观点。重点检查证据、隐含假设和反例。
```

## 学习模式

| 模式 | 适用场景 | 主要方式 |
| --- | --- | --- |
| 诊断模式 | 刚开始学习或不清楚薄弱点 | 用少量问题判断基础与误区 |
| Chavruta 辩论 | 人文、社科、概念辨析 | 追问论据、假设、反例与边界 |
| 理科压力测试 | 数学、物理、科学和编程 | 检查推导、单位、条件与迁移能力 |
| 语言学习 | 词汇、语法、阅读和表达 | 通过回忆、纠错和情境生成训练 |
| 考试模式 | 备考、限时训练和查漏补缺 | 按难度递进并记录稳定性 |
| 卡片编译器 | 阶段复习 | 从真实错误中生成原子化卡片 |

## 仓库结构

```text
ai-chavruta-learning-skill/
  ai-chavruta-learning/
    SKILL.md
    agents/
      openai.yaml
  examples/
  README.md
  README.zh-CN.md
  USAGE.md
  LICENSE
```

`ai-chavruta-learning/` 是可直接安装的 Skill 文件夹；仓库根目录中的文档和案例用于 GitHub 发布与学习参考。

## 使用指南与实战案例

- 阅读 [实战用户指南](USAGE.md)，了解完整流程、提示词模板、常见问题和一周训练方案。
- 查看 [论文阅读案例](examples/paper-reading.md)。
- 查看 [理科压力测试案例](examples/science-stress-test.md)。
- 查看 [人文辩论案例](examples/humanities-debate.md)。
- 查看 [语言学习案例](examples/language-learning.md)。
- 查看 [错题卡片编译案例](examples/card-compiler.md)。

## 使用建议

- 第一次使用时说清楚你的学习目标、当前水平和可用时间。
- 不确定答案时照样作答，并说明置信度；错误本身就是诊断材料。
- 感到吃力时可以要求“一次只问一个问题”或“先给一个最小提示”。
- 想快速查资料时可以直接要求解释，不必强制进入完整训练流程。

## 许可证

本项目采用 [MIT License](LICENSE)。
