---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "474"
title: "Ones and Zeroes"
url: "https://leetcode.com/problems/ones-and-zeroes"
difficulty: Medium  # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - String
  - Dynamic Programming (DP)

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-11
date-solved: 2025-11-11
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "0-1 knapsack"
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2025-12-02  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes)

Medium

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

#### Example 1

> Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
> 
> Output: 4
> 
> Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
> 
> Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
> 
> {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

#### Example 2

> Input: strs = ["10","0","1"], m = 1, n = 1
> 
> Output: 2
> 
> Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

#### Constraints

- 1 <= strs.length <= 600
- 1 <= strs[i].length <= 100
- strs[i] consists only of digits '0' and '1'.
- 1 <= m, n <= 100