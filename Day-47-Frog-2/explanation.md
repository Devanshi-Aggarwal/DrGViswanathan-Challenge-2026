# Frog 2

## Problem Statement

There are `N` stones, each having a height.

A frog starts at the first stone and wants to reach the last stone.

From any stone, it can jump forward by at most `K` stones.

The cost of a jump is the absolute difference between the heights of the two stones.

Return the minimum total cost required to reach the last stone.

---

## Approach

This problem is solved using **Dynamic Programming (DP)**.

Let:

- `dp[i]` = Minimum cost required to reach the `i-th` stone.

For every stone, we consider all possible previous stones from which the frog can jump (up to `K` positions behind).

The transition is:

```text
dp[i] = min(dp[j] + |height[i] - height[j]|)
```

where

```text
i-K ≤ j < i
```

The minimum among all valid jumps becomes the answer for the current stone.

---

## Algorithm

1. Initialize a DP array with infinity.
2. Set `dp[0] = 0`.
3. Traverse every stone from left to right.
4. For each stone:
   - Check the previous `K` stones.
   - Compute the jump cost.
   - Update the minimum cost.
5. Return `dp[N-1]`.

---

## Example

Input

```text
N = 5
K = 3

Heights = [10,30,40,50,20]
```

Possible optimal path

```text
10 → 30 → 20
```

Cost

```text
20 + 10 = 30
```

Output

```text
30
```

---

## Complexity Analysis

### Time Complexity

**O(N × K)**

For every stone, we examine at most `K` previous stones.

### Space Complexity

**O(N)**

A DP array of size `N` is maintained.

---

## Key Learnings

- Dynamic Programming
- State Transition
- Optimal Substructure
- Tabulation
- Range-Based DP
- Minimum Cost Path
