# Example: Paper Reading Session

## User Prompt

```text
Use $ai-chavruta-learning to help me study this abstract.

Goal: understand the argument deeply enough to critique it.
Do not summarize first. Ask diagnostic questions and distinguish source-supported claims from general background knowledge.

Abstract:
This paper argues that retrieval practice improves long-term retention not merely by strengthening memory traces, but by changing how learners organize and access knowledge. Across two experiments, students who completed short-answer retrieval tasks outperformed students who reread the same material, especially on delayed transfer questions.
```

## Expected Skill Behavior

```text
Before I explain, I will check your current understanding.

1. What is the paper's main claim in one sentence?
2. What comparison group is being used?
3. What would count as evidence that retrieval helps transfer, not just memorization?
```

## Sample Learner Answer

```text
1. Testing helps students remember better.
2. Students who reread.
3. If they remember more facts later.
```

## Sample Feedback

```text
Correctness: 1/2 | Reasoning: 1/2
Main issue: missing condition

What worked: you identified the retrieval vs rereading comparison.
What failed: "remember more facts later" only shows retention, not transfer.

Minimal hint: transfer means using knowledge in a new form or context.
Revision task: rewrite answer 3 in one sentence.
```

## Sample Repair

```text
Evidence for transfer would be students doing better on new questions that require applying the material, not merely recalling the same facts.
```

## Sample Card

```text
Q: In a learning experiment, what evidence shows transfer rather than simple retention?
A: Better performance on new questions or contexts that require applying the learned material, not merely recalling the original facts.
Tags: learning-science::retrieval-practice error::missing-condition
```
