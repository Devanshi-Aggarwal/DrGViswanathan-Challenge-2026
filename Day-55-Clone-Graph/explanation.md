# 133. Clone Graph

## Difficulty

Medium

---

## Topics

- Graph
- Breadth First Search (BFS)
- Queue
- Hash Map
- Graph Traversal

---

## Problem

Given a reference to a node in a connected undirected graph, create and return a deep copy (clone) of the graph.

Each cloned node should have:

- the same value
- cloned neighbors
- no reference to the original graph

---

# Approach

This solution uses **Breadth First Search (BFS)**.

The main challenge is ensuring that:

- every node is cloned exactly once
- graph cycles do not cause infinite traversal

To accomplish this, we maintain a dictionary that maps every original node to its cloned node.

```python
mp = {node: Node(node.val)}
```

The graph is explored level by level using a queue.

---

# Step 1 — Handle Empty Graph

If the graph is empty,

```python
if not node:
    return None
```

there is nothing to clone.

---

# Step 2 — Initialize BFS

We begin traversal from the given node.

```python
q = collections.deque([node])
```

The first cloned node is created immediately.

```python
mp = {node: Node(node.val)}
```

---

# Step 3 — Traverse the Graph

While nodes remain inside the queue,

```python
while q:
```

remove the current node.

```python
u = q.popleft()
```

---

# Step 4 — Visit Every Neighbor

For every neighboring node,

```python
for v in u.neighbors:
```

check whether it has already been cloned.

If not,

```python
if v not in mp:
```

create its clone,

```python
mp[v] = Node(v.val)
```

and push it into the queue.

```python
q.append(v)
```

---

# Step 5 — Connect the Cloned Nodes

Regardless of whether the neighbor was newly discovered or previously visited,

connect the cloned nodes.

```python
mp[u].neighbors.append(mp[v])
```

This builds the adjacency list of the cloned graph.

---

# Step 6 — Return the Cloned Graph

After BFS finishes,

```python
return mp[node]
```

returns the cloned starting node.

Since every cloned node is reachable from this node, the entire graph has been copied.

---

# Example

Original Graph

```
1 ---- 2
|      |
|      |
4 ---- 3
```

BFS Order

```
1
↓

2,4
↓

3
```

Each original node gets exactly one cloned node.

Finally, cloned neighbors are connected in the same way as the original graph.

---

# Why Hash Map?

Without storing cloned nodes,

the same node could be cloned multiple times.

The dictionary guarantees

- one clone per original node
- efficient O(1) lookup
- proper handling of cycles

---

# Complexity Analysis

### Time Complexity

O(V + E)

where

- V = number of vertices
- E = number of edges

Every node and edge is processed once.

---

### Space Complexity

O(V)

Extra space is used for

- queue
- cloned node map

---

# Key Takeaways

- Breadth First Search
- Graph Traversal
- Queue
- Hash Map
- Deep Copy
- Graph Cloning
- Handling Cycles
- Adjacency List

---

# Status

✅ Accepted — 22 / 22 test cases passed
