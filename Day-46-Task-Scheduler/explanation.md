# Task Scheduler

## Problem Statement

You are given an array `tasks`, where each task is represented by a capital letter, and an integer `n` representing the cooldown period.

The same task must be separated by at least `n` intervals.

Return the **minimum number of CPU intervals** required to complete all tasks.

---

## Approach

This solution uses a **Greedy + Frequency Counting** approach.

The most frequent task determines the minimum possible schedule length because identical tasks must be separated by cooldown intervals.

### Key Idea

1. Count the frequency of every task.
2. Find the highest frequency (`maxFreq`).
3. Arrange the most frequent task first.
4. Fill the remaining idle slots with other tasks.
5. If there are multiple tasks having the same highest frequency, place them at the end of the schedule.

The final answer is the maximum of:

- The calculated schedule length using the formula.
- The total number of tasks (when idle slots are unnecessary).

---

## Algorithm

1. Count the frequency of every task.
2. Find the maximum frequency.
3. Compute:

   ```text
   (maxFreq - 1) × (n + 1)
   ```

4. Count how many tasks have this maximum frequency.
5. Add these tasks to the last block.
6. Return:

   ```text
   max(calculated_length, total_tasks)
   ```

---

## Example

Input

```text
tasks = ["A","A","A","B","B","B"]
n = 2
```

Possible Schedule

```text
A → B → idle → A → B → idle → A → B
```

Intervals Required

```text
8
```

Output

```text
8
```

---

## Complexity Analysis

### Time Complexity

**O(n)**

Each task is counted once.

### Space Complexity

**O(1)**

At most 26 uppercase letters are stored.

---

## Key Learnings

- Greedy Algorithm
- Frequency Counting
- Hash Map (Counter)
- Scheduling Problems
- Mathematical Observation
- Constant Space Optimization
