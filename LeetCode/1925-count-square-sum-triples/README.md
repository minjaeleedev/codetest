---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1925"
title: "Count Square Sum Triples"
url: "https://leetcode.com/problems/count-square-sum-triples"
difficulty: Easy   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Math
  - Enumeration

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-12-08
date-solved: 2025-12-08
attempts: 1

# Personal Notes
rating: 2  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1925. Count Square Sum Triples](https://leetcode.com/problems/count-square-sum-triples)

Easy

A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

 
#### Example 1:

> Input: n = 5
> 
> Output: 2
> 
> Explanation: The square triples are (3,4,5) and (4,3,5).

#### Example 2:

> Input: n = 10
> 
> Output: 4
> 
> Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
 

#### Constraints:

1 <= n <= 250