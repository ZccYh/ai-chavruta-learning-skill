# AI Chavruta Learning Skill

[English](README.md) | [简体中文](README.zh-CN.md)

A portable Agent Skill that turns a compatible AI agent into an adaptive Socratic learning partner. It follows the open [Agent Skills specification](https://agentskills.io/specification) and keeps the core workflow independent of any one model vendor or client.

## What It Does

- Starts with lightweight calibration instead of a passive summary.
- Uses retrieval practice before explanation.
- Adjusts difficulty for beginners, anxious learners, review sessions, and exam prep.
- Scores answers by correctness and reasoning quality.
- Handles overload by stepping down to smaller questions or worked examples.
- Supports humanities debate, science/math stress tests, language learning, exam practice, and card compilation.
- Produces atomic Anki or RemNote-style cards from real weak points.
- Exports Anki-ready TSV and structured JSON/JSONL learning records on request.
- Can optionally import approved cards through a local AnkiConnect service.

## Install

The `ai-chavruta-learning/` folder is the portable skill package. For cross-client use, place it in a project or user-level Agent Skills directory:

```text
<project>/.agents/skills/ai-chavruta-learning
~/.agents/skills/ai-chavruta-learning
```

This shared location is supported by current [Codex](https://learn.chatgpt.com/docs/build-skills), [GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), and [Gemini CLI](https://codelabs.developers.google.com/gemini-cli/how-to-create-agent-skills-for-gemini-cli) workflows. [Claude products](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) can use the same skill package through their custom Skill installation or upload flow. Client-specific locations may also work; consult the client documentation.

Invocation syntax varies by client. In Codex:

```text
Use $ai-chavruta-learning to help me study [topic/material].
```

In clients without a skill mention syntax, ask naturally:

```text
Use the AI Chavruta Learning skill to help me study [topic/material].
```

## Repository Layout

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
  README.md
  README.zh-CN.md
  PROJECT-MAP.zh-CN.md
  USAGE.md
  examples/
  LICENSE
  .gitignore
```

`SKILL.md` contains the vendor-neutral learning protocol. `agents/openai.yaml` is an optional OpenAI UI adapter; other clients may ignore it. The files at the repository root are for documentation and publishing.

## Example Prompt

```text
Use $ai-chavruta-learning to help me study this paper. Start by diagnosing my understanding, then challenge my weak points and create flashcards only from mistakes.
```

## Usage Guide And Examples

- See [PROJECT-MAP.zh-CN.md](PROJECT-MAP.zh-CN.md) for Chinese Mermaid diagrams covering the product journey, adaptive learning loop, and repository structure.
- See [USAGE.md](USAGE.md) for the practical user guide.
- See [examples/anki-import-payload.json](examples/anki-import-payload.json) for the optional AnkiConnect payload format.
- See [examples/learning-session.json](examples/learning-session.json) for the portable learning-data schema in use.
- See [examples/](examples/) for tested scenario walkthroughs:
  - Paper reading
  - Exam stress test
  - Humanities debate
  - Language learning
  - Flashcard compilation

## License

MIT
