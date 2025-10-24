---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2048"
title: "Next Greater Numerically Balanced Number"
url: "https://leetcode.com/problems/next-greater-numerically-balanced-number"
difficulty: Medium
topics:
  - Hash Table
  - Math
  - Backtracking
  - Counting
  - Enumeration

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-10-24
date-solved: 2025-10-24
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "Solved but slow solution."
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2025-10-25  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [2048. Next Greater Numerically Balanced Number](https://leetcode.com/problems/next-greater-numerically-balanced-number)

Medium

An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

 
#### Example 1:

> Input: n = 1
> 
> Output: 22
> Explanation: 
> 
> 22 is numerically balanced since:
> - The digit 2 occurs 2 times. 
> 
> It is also the smallest numerically balanced number strictly greater than 1.

#### Example 2:

> Input: n = 1000
> 
> Output: 1333
> 
> Explanation: 
> 
> 1333 is numerically balanced since:
> 
> - The digit 1 occurs 1 time.
> - The digit 3 occurs 3 times. 
> 
> It is also the smallest numerically balanced number strictly greater than 1000.
> 
> Note that 1022 cannot be the answer because 0 appeared more than 0 times.

#### Example 3:

> Input: n = 3000
> 
> Output: 3133
> 
> Explanation: 
> 
> 3133 is numerically balanced since:
> - The digit 1 occurs 1 time.
> - The digit 3 occurs 3 times.
> 
> It is also the smallest numerically balanced number strictly greater than 3000.
 

#### Constraints:

- `0 <= n <= 10^6`