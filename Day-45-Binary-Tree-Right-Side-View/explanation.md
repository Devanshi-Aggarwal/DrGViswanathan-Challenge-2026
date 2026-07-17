# Binary Tree Right Side View

## Problem Statement

Given the `root` of a binary tree, imagine yourself standing on the **right side** of the tree.

Return the values of the nodes that are visible from top to bottom.

---

## Approach

This solution uses **Breadth-First Search (BFS)** with a queue.

The key observation is:

- Traverse each level from **right to left**.
- The **first node** encountered at every level is the one visible from the right side.
- Store this node before processing the remaining nodes of the level.

To ensure right-side nodes are visited first, enqueue the **right child before the left child**.

---

## Algorithm

1. If the tree is empty, return an empty list.
2. Initialize a queue with the root node.
3. While the queue is not empty:
   - Store the value of the first node in the queue.
   - Process all nodes at the current level.
   - Push the right child first.
   - Push the left child next.
4. Return the collected right-side view.

---

## Example

Input

```text
root = [1,2,3,null,5,null,4]
```

Traversal by levels

```text
Level 0 → 1

Level 1 → 3, 2

Level 2 → 4, 5
```

Visible nodes

```text
[1,3,4]
```

Output

```text
[1,3,4]
```

---

## Complexity Analysis

### Time Complexity

**O(n)**

Every node is visited exactly once.

### Space Complexity

**O(n)**

The queue may contain an entire level of the tree.

---

## Key Learnings

- Breadth-First Search (BFS)
- Level Order Traversal
- Queue
- Binary Trees
- Right-to-Left Traversal
- Tree Level Processing
