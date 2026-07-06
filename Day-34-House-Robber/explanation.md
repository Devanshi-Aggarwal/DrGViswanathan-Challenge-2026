# LeetCode 198. House Robber - Explanation

## Problem Statement

You are given an array where each element represents the amount of money in a house.

The constraint is:

- You **cannot rob two adjacent houses**.

Return the maximum amount of money that can be robbed.

---

## Intuition

At every house, there are only two choices:

1. Skip the current house.
2. Rob the current house.

If we rob the current house, we cannot rob the previous one.

So,

```
Current Profit =
Money in Current House
+
Maximum Profit till Two Houses Before
```

Otherwise,

```
Current Profit =
Maximum Profit till Previous House
```

Take whichever is larger.

---

## DP State

```
dp[i]

= Maximum money that can be robbed
from houses 0 to i.
```

Transition:

```
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

---

## Dry Run

### Input

```
nums = [1,2,3,1]
```

---

### Initialization

```
dp[0] = 1

dp[1] = max(1,2)

      = 2
```

Current DP

```
[1,2,0,0]
```

---

### House 2

Current value

```
3
```

Options

```
Skip

= dp[1]

= 2
```

```
Rob

= dp[0] + 3

= 1 + 3

= 4
```

Take maximum

```
dp[2] = 4
```

Current DP

```
[1,2,4,0]
```

---

### House 3

Current value

```
1
```

Options

```
Skip

= dp[2]

= 4
```

```
Rob

= dp[1] + 1

= 2 + 1

= 3
```

Take maximum

```
dp[3] = 4
```

Final DP

```
[1,2,4,4]
```

---

## Output

```
4
```

The robber chooses:

```
House 1

+

House 3

1 + 3 = 4
```

---

## Why Dynamic Programming?

The best answer for each house depends on answers already computed for previous houses.

Instead of solving the same subproblems repeatedly, we store them in the DP array.

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

Each house is processed once.

---

### Space Complexity

```
O(n)
```

The DP array stores one value per house.

---

## Key Concepts Learned

- Dynamic Programming
- State Definition
- State Transition
- Decision Making
- Optimal Substructure
- 1D DP
