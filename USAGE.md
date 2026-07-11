# AI Chavruta Learning: 实战用户指南

这份指南面向真实使用者，而不是开发者。目标是帮你把 `$ai-chavruta-learning` 用成一个主动学习伙伴：它不会一上来替你总结，而是先让你检索、区分、犯错、修正、迁移，最后只把真正不稳的点变成复习卡片。

## 1. 最短启动方式

新开一个 Codex 对话，输入：

```text
Use $ai-chavruta-learning to help me study [topic/material].
```

更好的启动方式：

```text
Use $ai-chavruta-learning to help me study the text below. I want active recall first, then mistake repair, then 5 high-quality flashcards only from my weak points.

[paste material]
```

如果你今天状态一般，可以直接说：

```text
Use $ai-chavruta-learning. I am a beginner and want gentle scaffolding. Please start with easy diagnostic questions.
```

如果你在备考，可以说：

```text
Use $ai-chavruta-learning in exam mode. Be strict, score my answers, track recurring errors, and generate variants from my mistakes.
```

## 2. 一次标准学习 Session 长什么样

推荐流程：

1. 你给材料或主题。
2. Skill 问 1-2 个校准问题：你是初学、复习、备考，还是想被强挑战。
3. Skill 出 3 个诊断题，不先讲答案。
4. 你从记忆中回答，可以附信心分数。
5. Skill 按“正确性 + 推理质量”反馈。
6. 如果你错了，它先给最小提示，让你修正。
7. 修正仍不稳时，它才给标准解释。
8. 基本掌握后，它问边界、反例、迁移题。
9. 结束时输出 mastered / unstable / misunderstood / flashcards / next session。

你应该期待一点“不舒服但可承受”的认知摩擦。这个 skill 的价值不在于让你感觉自己懂了，而在于暴露你哪里其实没懂。

## 3. 模式速查

| 你的场景 | 推荐说法 |
|---|---|
| 学一个新主题 | `Use $ai-chavruta-learning in diagnostic mode. I am new to this topic.` |
| 读论文 | `Use $ai-chavruta-learning to chunk this paper and test me section by section.` |
| 备考 | `Use $ai-chavruta-learning in exam mode. Be strict and generate variants from mistakes.` |
| 哲学/历史/法律/文学 | `Use $ai-chavruta-learning in Chavruta debate mode. Challenge my interpretation with evidence and rival views.` |
| 数学/科学/统计/工程 | `Use $ai-chavruta-learning in science-math stress-test mode. Focus on assumptions, units, conditions, and edge cases.` |
| 英语/写作/翻译 | `Use $ai-chavruta-learning in language learning mode. Correct collocation, register, grammar, and nuance.` |
| 做卡片 | `Use $ai-chavruta-learning in card compiler mode. Only make cards from my unstable or wrong points.` |

## 4. 好 Prompt 模板

### 4.1 论文阅读

```text
Use $ai-chavruta-learning to help me study this paper.

Goal: understand the argument deeply enough to explain and critique it.
Mode: diagnostic first, then Chavruta debate.
Rules:
- Do not summarize first.
- Chunk the paper by thesis, key concepts, evidence, limitations, and implications.
- Ask me questions before explaining.
- Mark which claims are source-supported and which are general knowledge.
- End with mistake-based flashcards.

[paste abstract or section]
```

### 4.2 考试复习

```text
Use $ai-chavruta-learning in exam mode.

Topic: [topic]
Goal: find weak points before the exam.
Difficulty: medium to strict.
Please:
- Ask 3 diagnostic questions first.
- Score correctness and reasoning separately.
- Give minimal hints before explanations.
- Generate one variant question after each mistake.
- End with a targeted review plan.
```

### 4.3 人文学科辩论

```text
Use $ai-chavruta-learning in Chavruta debate mode.

Claim I want to test:
[your claim]

Please separate:
- textual evidence
- interpretation
- assumptions
- rival interpretations
- strongest objection
```

### 4.4 语言学习

```text
Use $ai-chavruta-learning in language learning mode.

Target: academic English.
Please test my use of these words: [word list]
Focus on collocation, register, near-synonym distinctions, and natural output.
Do not just define the words.
```

### 4.5 Anki / RemNote 卡片

```text
Use $ai-chavruta-learning in card compiler mode.

Based on our session, create at most 8 cards.
Only include points I got wrong or answered vaguely.
Prefer cloze cards for definitions and conditions.
Prefer Q/A cards for counterexamples and reasoning traps.
Export in Anki tab-separated format.
```

## 5. 几波实战测试摘要

下面这些测试是为了检查 skill 是否真的执行“先检索、再解释、再修复、再迁移”的学习协议。

### Test 1: 初学者概念学习

场景：用户第一次学“熵”。

预期行为：

- 不直接解释熵。
- 先问识别/回忆级别问题。
- 用户答“熵就是混乱程度”时，不直接判死刑，而是指出这是有用但不完整的直觉。
- 最小提示引导到“微观状态数”。
- 最后生成错误修正卡：“为什么 entropy = disorder 不完整？”

结果：通过。详见 [examples/science-stress-test.md](examples/science-stress-test.md)。

### Test 2: 论文阅读

场景：用户贴一段论文摘要，想理解论点。

预期行为：

- 不先总结全文。
- 先问研究问题、主张、证据类型。
- 区分“原文支持的主张”和“AI 的一般知识补充”。
- 对用户的解释追问边界和反例。

结果：通过，但建议用户一次只贴摘要或一个小节。详见 [examples/paper-reading.md](examples/paper-reading.md)。

### Test 3: 人文学科辩论

场景：用户提出一个关于自由主义的解释。

预期行为：

- 不只是赞同或反驳。
- 要求区分证据、解释、推论。
- 提出 rival interpretation。
- 要求用户给出边界案例。

结果：通过。详见 [examples/humanities-debate.md](examples/humanities-debate.md)。

### Test 4: 英语近义词与搭配

场景：用户混淆 exposure / access。

预期行为：

- 不只给中文翻译。
- 要求用户造句。
- 修正搭配和语域。
- 生成区别卡片。

结果：通过。详见 [examples/language-learning.md](examples/language-learning.md)。

### Test 5: 卡片编译

场景：一轮学习后要求导出卡片。

预期行为：

- 不从全部材料批量制卡。
- 只从错误、边界条件、混淆点中制卡。
- 限制数量。
- 使用 Anki 或 RemNote 格式。

结果：通过。详见 [examples/card-compiler.md](examples/card-compiler.md)。

## 6. 和其他工具配合

### NotebookLM

适合做材料整理和 source-grounded 摘要。推荐流程：

1. 把长材料放进 NotebookLM。
2. 让 NotebookLM 提取章节结构或关键段落。
3. 把一个小节贴给 `$ai-chavruta-learning`。
4. 用 Chavruta 方式测试理解。
5. 从错误中生成卡片。

不要让 NotebookLM 和 Chavruta 同时替你“解释到懂”。一个负责整理材料，一个负责逼你主动学习。

### Anki

适合长期复习。推荐只导入这些卡：

- 你答错过的点。
- 你混淆过的概念。
- 公式或模型的适用条件。
- 反例和边界条件。

不要导入“看起来很完整但你没有犯过错”的卡片。

### RemNote

适合把概念笔记和卡片结合。推荐让 skill 输出：

```text
- [Question] >> [Answer]
  - Tags:: [topic], [error type]
```

## 7. 使用技巧

- 每次 session 控制在 20-40 分钟。
- 一次只学一个材料块，不要贴完整书章后要求全部掌握。
- 如果连续答错，主动说：“降低难度，给我一个 worked example。”
- 如果你只是想快速知道答案，直接说：“Override: explain directly, then give me one check question.”
- 做卡片前先学习，不要一开始就要求从材料生成 50 张卡。
- 对论文和历史材料，要求区分 source-supported claims 和 general knowledge。

## 8. 常见问题

### 它会不会太折磨？

它应该有一点摩擦，但不应该让你崩溃。如果太难，直接说：

```text
Lower the difficulty. Give me recognition or multiple-choice questions first.
```

### 它能直接总结吗？

能。说：

```text
Override: give me a direct summary first, then test me with three questions.
```

### 它适合零基础吗？

适合，但要显式告诉它你是初学者：

```text
I am a beginner. Use gentle scaffolding and do not ask hard transfer questions yet.
```

### 它适合高阶学习吗？

适合。你可以要求：

```text
Increase difficulty. Ask boundary, counterexample, critique, and transfer questions.
```

### 它能保证事实正确吗？

不能保证。处理专业材料时，要提供原文，并要求它区分“材料中明确说的”和“模型补充的背景知识”。对医学、法律、金融等高风险领域，应把它当学习辅助，不当专业建议。

## 9. 推荐的一周使用法

第 1 天：诊断模式，找出薄弱点。

第 2 天：针对薄弱点做修复题。

第 3 天：做边界和反例题。

第 4 天：做迁移题或应用题。

第 5 天：导出少量高质量卡片。

第 6 天：闭卷解释主题。

第 7 天：用 session report 规划下一轮。

## 10. 最佳心态

不要把 AI 当成替你读书的人。把它当成一个不太会放过含糊答案的学习搭档。

你越愿意先回答、先暴露错误、先修正，收获越大。
