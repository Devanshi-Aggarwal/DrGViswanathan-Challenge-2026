# LeetCode 121 - Best Time to Buy and Sell Stock

## Problem Statement

Given an array `prices` where `prices[i]` represents the stock price on the ith day, find the maximum profit that can be achieved by buying on one day and selling on a later day.

Return 0 if no profit can be made.

---

## Approach

I used a greedy approach.

While traversing the array, I keep track of the minimum stock price seen so far. For each price, I calculate the profit that would be earned if the stock were sold on that day and update the maximum profit accordingly.

This allows the solution to be computed in a single pass.

---

## Algorithm

1. Initialize `min_price` as infinity.
2. Initialize `max_profit` as 0.
3. Traverse through the prices array.
4. Update the maximum profit using the current price and the minimum price seen so far.
5. Update the minimum price if a smaller price is found.
6. Return the maximum profit.

---

## Complexity Analysis

### Time Complexity

O(n)

The array is traversed exactly once.

### Space Complexity

O(1)

Only a few variables are used.

---

## Key Learning

Many optimization problems can be solved using a greedy approach by maintaining the best value seen so far.

Tracking the minimum stock price while traversing the array allows us to efficiently compute the maximum possible profit.

---

## Concepts Practiced

- Arrays
- Greedy Algorithm
- One Pass Traversal
- Optimization
