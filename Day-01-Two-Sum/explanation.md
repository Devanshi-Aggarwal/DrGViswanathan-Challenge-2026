# LeetCode #1 - Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

It is guaranteed that exactly one valid solution exists, and the same element cannot be used twice.

---

## Approach

I used a **Hash Map (Dictionary)** to solve this problem efficiently.

The idea is to store each number along with its index as I traverse the array. For every element, I calculate the complement required to reach the target:

```python
complement = target - num
```

Before storing the current element, I check whether the complement already exists in the dictionary.

* If it exists, I have found the required pair and return their indices.
* Otherwise, I store the current number and its index for future lookups.

This approach allows the problem to be solved in a single pass through the array.

---

## Example

Input:

```python
nums = [2, 7, 11, 15]
target = 9
```

Iteration 1:

* Current number = 2
* Complement = 7
* Dictionary = {2: 0}

Iteration 2:

* Current number = 7
* Complement = 2
* 2 exists in the dictionary

Output:

```python
[0, 1]
```

---

## Complexity Analysis

### Time Complexity

**O(n)**

Each element is visited only once, and dictionary lookups take O(1) on average.

### Space Complexity

**O(n)**

In the worst case, all elements may be stored in the dictionary.

---

## Key Learning

This problem demonstrates how a Hash Map can significantly optimize a solution. Instead of checking every possible pair using nested loops (O(n²)), we can use constant-time lookups to achieve an O(n) solution.

Hashing is one of the most important techniques in Data Structures and Algorithms and is frequently used in coding interviews.

