---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1292"
title: "Maximum Side Length of a Square with Sum Less than or Equal to Threshold"
url: "https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Binary Search
  - Matrix
  - Prefix Sum

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-01-19
date-solved: 2026-01-19
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "prefix sum for matrix. binary search?"
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold)

Medium

Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.


#### Example 1:


> Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
> Output: 2
> Explanation: The maximum side length of square with sum less than 4 is 2 as shown.

#### Example 2:

> Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
> Output: 0
 

#### Constraints:

- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 300
- 0 <= mat[i][j] <= 10<sup>4</sup>
- 0 <= threshold <= 10<sup>5</sup>