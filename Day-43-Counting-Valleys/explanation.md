# Counting Valleys

## Problem Statement

An avid hiker records every step taken during a hike.

- `U` represents an uphill step.
- `D` represents a downhill step.

A valley is a sequence of steps below sea level that starts with a downhill step from sea level and ends with an uphill step back to sea level.

Given the hike path, determine the total number of valleys traversed.

---

## Approach

The solution keeps track of the hiker's current altitude throughout the hike.

### Key Observations

- Start at sea level (`altitude = 0`).
- Every `U` increases altitude by 1.
- Every `D` decreases altitude by 1.
- A valley is completed when an uphill step brings the altitude back to sea level.

---

## Algorithm

1. Initialize:
   - `altitude = 0`
   - `valleys = 0`
2. Traverse every step in the path.
3. If the step is `U`:
   - Increase altitude.
   - If altitude becomes `0`, increment the valley count.
4. Otherwise (`D`):
   - Decrease altitude.
5. Return the number of valleys.

---

## Example

Input

```text
steps = 8
path = "DDUUUUDD"
```

Altitude changes:

```text
0
↓
-1
↓
-2
↑
-1
↑
0  ← Valley completed
↑
1
↑
2
↓
1
↓
0
```

Output

```text
1
```

---

## Complexity Analysis

### Time Complexity

**O(n)**

Each step is processed exactly once.

### Space Complexity

**O(1)**

Only two integer variables are maintained.

---

## Key Learnings

- Simulation
- Altitude Tracking
- State-Based Counting
- Conditional Logic
- Linear Traversal
- Constant Space Optimization
