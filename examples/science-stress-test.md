# Example: Science And Math Stress Test

## User Prompt

```text
Use $ai-chavruta-learning in science-math stress-test mode.

Topic: entropy
Learner state: beginner
Please start gently, but correct oversimplifications.
```

## Expected Skill Behavior

```text
I will start with a low-friction diagnostic.

1. When you hear "entropy," what do you think it measures?
2. Is "entropy = disorder" a definition, an analogy, or both?
3. Confidence 1-5: how sure are you?
```

## Sample Learner Answer

```text
Entropy means disorder. I think it is basically the definition. Confidence 4.
```

## Sample Feedback

```text
Correctness: 1/2 | Reasoning: 0/2
Main issue: overgeneralization

What worked: "disorder" can be a useful intuition.
What failed: it is not a precise definition and breaks in boundary cases.

Minimal hint: connect entropy to the number of possible microscopic arrangements.
Revision task: revise the definition without using only the word "disorder."
```

## Sample Repair

```text
Entropy is related to how many microscopic states can produce the same macroscopic state.
```

## Sample Pressure Test

```text
Good. Now boundary check: why can "more visually messy" fail as a guide to higher entropy?
```

## Sample Card

```text
Q: Why is "entropy = disorder" an incomplete definition?
A: Entropy is a thermodynamic/statistical quantity related to the number of accessible microstates; "disorder" is only an intuitive metaphor and can mislead in boundary cases.
Tags: physics::thermodynamics error::oversimplification
```
