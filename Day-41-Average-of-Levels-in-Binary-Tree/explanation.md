# 637. Average of Levels in Binary Tree

## Problem Statement

Given the `root` of a binary tree, return the average value of the nodes on each level as an array.

---

## Approach

This solution uses **Breadth-First Search (BFS)** or **Level Order Traversal**.

### Key Observations

- BFS naturally processes nodes level by level.
- For each level:
  - Count the number of nodes.
  - Compute the sum of their values.
  - Calculate the average.
- Add the average to the answer list.
- Continue until all levels are processed.

---

## Algorithm

1. Initialize a queue with the root node.
2. While the queue is not empty:
   - Determine the number of nodes at the current level.
   - Traverse all nodes in that level.
   - Sum their values.
   - Push their children into the queue.
   - Compute `sum / count`.
   - Store the average.
3. Return the list of averages.

---

## Example

Input:

```text
        3
       / \
      9  20
        /  \
       15   7
```

Level 0:

```text
Nodes = [3]

Average = 3
```

Level 1:

```text
Nodes = [9,20]

Average = (9+20)/2 = 14.5
```

Level 2:

```text
Nodes = [15,7]

Average = (15+7)/2 = 11
```

Output:

```text
[3.0,14.5,11.0]
```

---

## Complexity Analysis

### Time Complexity

**O(n)**

Each node is visited exactly once.

### Space Complexity

**O(n)**

The queue may contain an entire level of the tree.

---

## Key Learnings

- Breadth-First Search (BFS)
- Level Order Traversal
- Queue Data Structure
- Tree Level Processing
- Running Sum Calculation
- Average Computation
