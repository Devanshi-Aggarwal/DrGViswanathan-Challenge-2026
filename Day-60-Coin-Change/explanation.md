# 322. Coin Change

## Difficulty

Medium

---

## Topics

- Dynamic Programming
- Array
- Bottom-Up DP
- Unbounded Knapsack

---

# Problem

You are given an array of coin denominations and a target amount.

Return the **minimum number of coins** needed to make the given amount.

If it is impossible, return **-1**.

Each coin can be used an unlimited number of times.

---

# Approach

This problem is a classic **Dynamic Programming** problem.

We build a DP array where:

```
dp[i]
```

represents the minimum number of coins required to make amount `i`.

Initially,

```
dp[0] = 0
```

because zero coins are needed to make amount 0.

All other values are initialized with

```
amount + 1
```

which acts as infinity.

---

# DP Transition

For every coin,

we try updating every reachable amount.

```
dp[i] = min(dp[i], dp[i - coin] + 1)
```

Meaning:

- Don't use this coin
- Use this coin once and add it to the best solution for the remaining amount

Choose the minimum.

---

# Example

Coins

```
[1,2,5]
```

Amount

```
11
```

Initially

```
dp

[0,∞,∞,∞,∞,∞,∞,∞,∞,∞,∞,∞]
```

After processing coin 1

```
[0,1,2,3,4,5,6,7,8,9,10,11]
```

After coin 2

```
[0,1,1,2,2,3,3,4,4,5,5,6]
```

After coin 5

```
[0,1,1,2,2,1,2,2,3,3,2,3]
```

Answer

```
3
```

because

```
11 = 5 + 5 + 1
```

---

# Why This Works

The DP array always stores the minimum coins required for every smaller amount.

When calculating a larger amount,

all smaller optimal answers are already known.

This guarantees an optimal solution.

---

# Complexity Analysis

### Time Complexity

```
O(number_of_coins × amount)
```

---

### Space Complexity

```
O(amount)
```

---

# Key Takeaways

- Dynamic Programming
- Bottom-Up DP
- Unbounded Knapsack
- State Transition
- Optimization Problems
- Minimum Coin Count

---

# Status

✅ Accepted — 189 / 189 test cases passed
