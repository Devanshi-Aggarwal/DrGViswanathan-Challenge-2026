# Best Time to Buy and Sell Stock II

## Problem Statement

You are given an array `prices` where `prices[i]` represents the stock price on the `i-th` day.

You may complete as many buy and sell transactions as you like, but:

- You can hold **at most one share** at any time.
- You may buy and sell on the same day.

Return the maximum profit that can be achieved.

---

## Approach

This solution uses **Dynamic Programming with State Optimization**.

Instead of tracking every transaction, we maintain two states:

- **hold** → Maximum profit after buying (or holding) a stock.
- **sell** → Maximum profit after selling (or not holding) a stock.

For every day's price, we decide whether keeping the previous state or performing a transaction gives a better profit.

---

## Algorithm

1. Initialize:
   - `sell = 0`
   - `hold = -∞`
2. Traverse each stock price.
3. Update:
   - `sell = max(sell, hold + price)`
   - `hold = max(hold, sell - price)`
4. Return `sell` as the final answer.

---

## Example

Input

```text
prices = [7,1,5,3,6,4]
```

Possible transactions:

```text
Buy at 1 → Sell at 5 = 4

Buy at 3 → Sell at 6 = 3

Total Profit = 7
```

Output

```text
7
```

---

## Complexity Analysis

### Time Complexity

**O(n)**

Each price is processed exactly once.

### Space Complexity

**O(1)**

Only two variables are maintained throughout the traversal.

---

## Key Learnings

- Dynamic Programming
- State Optimization
- Greedy Decision Making
- Stock Trading Problems
- Linear Traversal
- Constant Space Optimization
