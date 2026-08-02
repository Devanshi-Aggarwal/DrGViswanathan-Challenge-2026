# 146. LRU Cache

## Difficulty

Medium

---

## Topics

- Design
- Hash Map
- Doubly Linked List
- Cache
- Data Structures

---

# Problem

Design an **LRU (Least Recently Used) Cache** supporting:

- `get(key)`
- `put(key, value)`

Both operations must run in

```
O(1)
```

average time.

When the cache exceeds its capacity, remove the **least recently used** item.

---

# Approach

To achieve constant time operations, we combine:

- Hash Map
- Doubly Linked List

The Hash Map provides direct access to nodes.

The Doubly Linked List maintains the order of usage.

---

# Why Two Data Structures?

## Hash Map

Stores

```
key → node
```

This allows

```
get(key)
```

in O(1).

---

## Doubly Linked List

Maintains usage order.

```
Head
↑
Most Recently Used

...

Least Recently Used
↓

Tail
```

Whenever a key is accessed, move it to the front.

When capacity is full, remove the node before the tail.

---

# Dummy Head and Tail

Two dummy nodes simplify insertion and deletion.

```
Head <-> Node <-> Node <-> Tail
```

No special handling is needed for empty or single-node cases.

---

# get()

If the key doesn't exist,

```
return -1
```

Otherwise

- Remove the node.
- Move it to the head.
- Return its value.

---

# put()

### Case 1

Key already exists.

Update its value.

Move it to the front.

---

### Case 2

New key.

If cache is full,

remove

```
tail.prev
```

which is the least recently used node.

Insert the new node at the front.

---

# Helper Functions

## remove()

Disconnects a node from the list.

---

## moveToHead()

Places a node immediately after the head.

---

## join()

Connects two nodes together.

```
left <-> right
```

Used by both insertion and deletion.

---

# Example

Capacity

```
2
```

Operations

```
put(1,1)

put(2,2)

get(1)

put(3,3)
```

Order

```
Head

1

2

Tail
```

After

```
get(1)
```

```
Head

1

2

Tail
```

becomes

```
Head

1

2

Tail
```

where 1 becomes the most recently used.

Now

```
put(3,3)
```

removes

```
2
```

because it is the least recently used.

---

# Why This Works

The Hash Map ensures direct node lookup.

The Doubly Linked List keeps elements ordered by recent usage.

Every insertion, deletion, and movement takes constant time.

---

# Complexity Analysis

### Time Complexity

```
get()  -> O(1)

put()  -> O(1)
```

---

### Space Complexity

```
O(capacity)
```

---

# Key Takeaways

- Hash Map
- Doubly Linked List
- LRU Cache Design
- O(1) Lookup
- O(1) Insertion
- O(1) Deletion
- Cache Eviction Policy
- Design Problems

---

# Status

✅ Accepted — 25 / 25 test cases passed
