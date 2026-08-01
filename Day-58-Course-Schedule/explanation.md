# 207. Course Schedule

## Difficulty

Medium

---

## Topics

- Graph
- Topological Sort
- Breadth-First Search (BFS)
- Queue
- Indegree
- Kahn's Algorithm

---

## Problem

There are `numCourses` courses labeled from `0` to `numCourses - 1`.

Each prerequisite pair `[a, b]` means:

- You must complete course **b** before taking course **a**.

Return:

- `True` if all courses can be completed.
- `False` otherwise.

---

# Approach

This problem can be modeled as a **Directed Graph**.

- Every course is a node.
- Every prerequisite is a directed edge.

If the graph contains a cycle, it is impossible to finish all courses.

We detect cycles using **Topological Sorting (Kahn's Algorithm)**.

---

# Step 1 — Build the Graph

Create an adjacency list.

```python
graph = [[] for _ in range(numCourses)]
```

For every prerequisite,

```python
graph[prereq].append(course)
```

This means

```
prereq → course
```

---

# Step 2 — Compute Indegree

Each course stores how many prerequisites it still has.

```python
indegree[course] += 1
```

Courses with indegree **0** can be taken immediately.

---

# Step 3 — Initialize Queue

Push every course with indegree 0.

```python
queue = deque()

for i in range(numCourses):
    if indegree[i] == 0:
        queue.append(i)
```

These are the starting nodes.

---

# Step 4 — Process the Queue

Repeatedly remove one course.

```python
node = queue.popleft()
completed += 1
```

This means we have successfully completed this course.

---

# Step 5 — Update Neighbors

Every dependent course loses one prerequisite.

```python
indegree[neighbor] -= 1
```

If a course reaches

```python
indegree == 0
```

it becomes available.

```python
queue.append(neighbor)
```

---

# Step 6 — Check Completion

If every course is processed,

```python
completed == numCourses
```

then

```
No cycle exists.
```

Otherwise,

```
A cycle exists.
```

---

# Example

Input

```
numCourses = 2

[[1,0]]
```

Graph

```
0 → 1
```

Queue

```
0
```

Process

```
Take 0

Take 1
```

Completed

```
2 courses
```

Answer

```
True
```

---

Example

```
0 → 1
↑   ↓
└───┘
```

No node has indegree 0.

Queue remains empty.

Answer

```
False
```

---

# Why Kahn's Algorithm?

Topological sorting only exists for a **Directed Acyclic Graph (DAG)**.

If every node can be removed,

the graph has no cycle.

Otherwise,

some nodes remain stuck inside a cycle.

---

# Complexity Analysis

### Time Complexity

```
O(V + E)
```

where

- V = number of courses
- E = number of prerequisite pairs

---

### Space Complexity

```
O(V + E)
```

For the graph, indegree array, and queue.

---

# Key Takeaways

- Directed Graph
- Topological Sorting
- Kahn's Algorithm
- BFS
- Queue
- Indegree Array
- Cycle Detection

---

# Status

✅ Accepted — 54 / 54 test cases passed
