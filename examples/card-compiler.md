# Example: Card Compiler Session

## User Prompt

```text
Use $ai-chavruta-learning in card compiler mode.

Based on this session, create at most 5 Anki cards.
Only use points I got wrong or answered vaguely.
```

## Session Weak Points

```text
- The learner treated retrieval practice as the same thing as rereading.
- The learner defined entropy as "disorder" only.
- The learner confused access with exposure.
- The learner gave a correct answer in a formula problem but used the wrong method.
```

## Expected Skill Behavior

```text
I will not create cards from every topic we touched. I will only use unstable or wrong points.

Front	Back	Tags
What is the key difference between retrieval practice and rereading?	Retrieval practice requires producing an answer from memory before seeing feedback; rereading mainly re-exposes the learner to material.	learning-science retrieval-practice distinction
Why is "entropy = disorder" an incomplete definition?	Entropy is related to the number of accessible microstates; "disorder" is only an intuition and can mislead in boundary cases.	physics thermodynamics error-oversimplification
What is the difference between access to information and exposure to information?	Access means possibility or permission to obtain information; exposure means actually encountering it.	english word-distinction error-concept-confusion
Why should a correct answer reached by the wrong method become a flashcard?	Because it signals unstable reasoning: the result may not transfer to variant problems even if the final answer was right once.	exam-prep reasoning error-correction
```

## Quality Check

This passes if:

- The cards are atomic.
- The cards come from actual weak points.
- The deck is small.
- Each card has a tag.
- No card simply asks for a broad explanation of an entire topic.
