# AI Chavruta Learning Skill

[English](README.md) | 简体中文

一个基于开放 [Agent Skills 规范](https://agentskills.io/specification)的通用自适应学习 Skill。它不绑定单一模型或客户端，可以把兼容的 AI Agent 从“替你总结答案的助手”变成苏格拉底式学习伙伴：先提问诊断，再根据回答调整难度，通过追问、最小提示、纠错和迁移练习帮助学习者真正掌握知识。

## 它能做什么

- 先回忆、后讲解，减少“看懂了但不会用”的错觉。
- 根据学习者的基础、信心和状态动态调整问题难度。
- 同时评价答案正确性与推理质量，而不只判断对错。
- 在连续答错或认知过载时，自动缩小问题、增加脚手架或提供示范。
- 支持论文阅读、理科压力测试、人文辩论、语言学习和考试训练。
- 只从真实错误和薄弱点中提取原子化复习卡片，可用于 Anki 或 RemNote。
- 对长文档进行分段学习，并在各段之间建立概念联系。
- 按需导出 Anki 可导入的 TSV，以及 JSON/JSONL 学习记录。
- 在客户端具备本地访问能力时，可选通过 AnkiConnect 导入已确认的卡片。

## 安装

`ai-chavruta-learning/` 是通用 Skill 包。跨客户端推荐放到项目级或用户级 Agent Skills 目录：

```text
<项目目录>/.agents/skills/ai-chavruta-learning
~/.agents/skills/ai-chavruta-learning
```

目前 [Codex](https://learn.chatgpt.com/docs/build-skills)、[GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) 和 [Gemini CLI](https://codelabs.developers.google.com/gemini-cli/how-to-create-agent-skills-for-gemini-cli) 的相关工作流支持 `.agents/skills`。[Claude 系列产品](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)也能使用同一个 Skill 包，但需要通过 Claude Code、claude.ai 设置或 API 的自定义 Skill 流程安装。各产品也可能支持自己的专用目录。

不同客户端的显式调用语法不同。在 Codex 中可以输入：

```text
使用 $ai-chavruta-learning 帮我学习[主题或材料]。
```

如果客户端没有 `$skill-name` 语法，直接自然语言说明：

```text
使用 AI Chavruta Learning Skill 帮我学习[主题或材料]。
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
    references/
      exports-and-integrations.md
    scripts/
      anki_connect.py
  examples/
  README.md
  README.zh-CN.md
  PROJECT-MAP.zh-CN.md
  USAGE.md
  LICENSE
```

`SKILL.md` 是与厂商无关的学习协议；`agents/openai.yaml` 只是可选的 OpenAI 界面适配，其他客户端可以忽略。仓库根目录中的文档和案例用于发布与学习参考。

## 使用指南与实战案例

- 查看 [项目复盘信息图](PROJECT-MAP.zh-CN.md)，快速理解项目演进、学习闭环、自适应机制和文件结构。
- 阅读 [实战用户指南](USAGE.md)，了解完整流程、提示词模板、常见问题和一周训练方案。
- 查看 [AnkiConnect 导入示例](examples/anki-import-payload.json)，了解可选的本地直连数据格式。
- 查看 [学习 Session JSON 示例](examples/learning-session.json)，了解可移植的学习数据结构。
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
