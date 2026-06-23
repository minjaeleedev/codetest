---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3699"
title: "Number of ZigZag Arrays I"
url: "https://leetcode.com/problems/number-of-zigzag-arrays-i"
difficulty: Hard   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Dynamic Programming
  - Prefix Sum

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted:
date-solved:
attempts:

# Personal Notes
rating:   # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3699. Number of ZigZag Arrays I](https://leetcode.com/problems/number-of-zigzag-arrays-i)

Hard

You are given three integers n, l, and r.

A ZigZag array of length n is defined as follows:

Each element lies in the range [l, r].
No two adjacent elements are equal.
No three consecutive elements form a strictly increasing or strictly decreasing sequence.
Return the total number of valid ZigZag arrays.

Since the answer may be large, return it modulo 109 + 7.

A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).

 
#### Example 1:
> 
> Input: n = 3, l = 4, r = 5
> 
> Output: 2
> 
> Explanation:
> 
> There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:
> 
> [4, 5, 4]
> [5, 4, 5]​​​​​​​

#### Example 2:

> Input: n = 3, l = 1, r = 3
> 
> Output: 10
> 
> Explanation:
> 
> There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:
> 
> [1, 2, 1], [1, 3, 1], [1, 3, 2]
> [2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
> [3, 1, 2], [3, 1, 3], [3, 2, 3]
> All arrays meet the ZigZag conditions.

 
#### Constraints:

- 3 <= n <= 2000
- 1 <= l < r <= 2000