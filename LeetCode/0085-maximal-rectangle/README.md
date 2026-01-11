---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "85"
title: "Maximal Rectangle"
url: "https://leetcode.com/problems/maximal-rectangle"
difficulty: Hard   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Dynamic Programming (DP)
  - Stack
  - Matrix
  - Monotonic Stack

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-01-11
date-solved: 2026-01-11
attempts: 1

# Personal Notes
rating: 6  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-02-11  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle)

Hard

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

#### Example 1:

![image1](./image1.jpg)

> Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
> 
> Output: 6
> 
> Explanation: The maximal rectangle is shown in the above picture.

#### Example 2:

> Input: matrix = [["0"]]
> 
> Output: 0

#### Example 3:

> Input: matrix = [["1"]]
> 
> Output: 1

#### Constraints:

- rows == matrix.length
- cols == matrix[i].length
- 1 <= rows, cols <= 200
- matrix[i][j] is '0' or '1'.