# AI Chavruta Learning Skill

[English](README.md) | [简体中文](README.zh-CN.md)

An adaptive Codex skill that turns the assistant into a Socratic learning partner: it asks calibrated questions, challenges vague answers, gives minimal hints, repairs mistakes, tests transfer, and extracts only mistake-based flashcards.

## What It Does

- Starts with lightweight calibration instead of a passive summary.
- Uses retrieval practice before explanation.
- Adjusts difficulty for beginners, anxious learners, review sessions, and exam prep.
- Scores answers by correctness and reasoning quality.
- Handles overload by stepping down to smaller questions or worked examples.
- Supports humanities debate, science/math stress tests, language learning, exam practice, and card compilation.
- Produces atomic Anki or RemNote-style cards from real weak points.

## Install In Codex

Copy the `ai-chavruta-learning` folder into your Codex skills directory:

```text
~/.codex/skills/ai-chavruta-learning
```

On Windows, that is usually:

```text
%USERPROFILE%\.codex\skills\ai-chavruta-learning
```

Then start a new Codex conversation and invoke it with:

```text
Use $ai-chavruta-learning to help me study [topic/material].
```

## Repository Layout

```text
ai-chavruta-learning-skill/
  ai-chavruta-learning/
    SKILL.md
    agents/
      openai.yaml
  README.md
  README.zh-CN.md
  USAGE.md
  examples/
  LICENSE
  .gitignore
```

The `ai-chavruta-learning/` folder is the installable skill. The files at the repository root are for GitHub publishing.

## Example Prompt

```text
Use $ai-chavruta-learning to help me study this paper. Start by diagnosing my understanding, then challenge my weak points and create flashcards only from mistakes.
```

## Usage Guide And Examples

- See [USAGE.md](USAGE.md) for the practical user guide.
- See [examples/](examples/) for tested scenario walkthroughs:
  - Paper reading
  - Exam stress test
  - Humanities debate
  - Language learning
  - Flashcard compilation

## License

MIT
