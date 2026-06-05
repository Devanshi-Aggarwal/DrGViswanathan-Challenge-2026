# LeetCode 49 - Group Anagrams

## Problem Statement

Given an array of strings, group all strings that are anagrams of each other.

---

## Approach

I used a Hash Map (Dictionary) to group words.

The key idea is that all anagrams produce the same string when their characters are sorted.

---

## Algorithm

1. Create a dictionary.
2. Traverse each string.
3. Sort the string and use it as a key.
4. Append the original string to the corresponding list.
5. Return all grouped lists.

---

## Complexity Analysis

### Time Complexity

O(n × k log k)

### Space Complexity

O(n × k)

---

## Key Learning

A sorted string can act as a unique identifier for grouping anagrams.

---

## Concepts Practiced

- Hash Maps
- String Manipulation
- Sorting
- defaultdict
