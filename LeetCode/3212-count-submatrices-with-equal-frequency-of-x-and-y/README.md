---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3212"
title: "Count Submatrices With Equal Frequency of X and Y"
url: "https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Matrix
  - Prefix Sum

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-03-19
date-solved: 2026-03-19
attempts: 1

# Personal Notes
rating: 3  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "same prefix sum code, different performance."
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3212. Count Submatrices With Equal Frequency of X and Y](https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y)

Medium

Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

- grid[0][0]
- an equal frequency of 'X' and 'Y'.
- at least one 'X'.
 
#### Example 1:

> Input: grid = [["X","Y","."],["Y",".","."]]
> 
> Output: 3
> 
> Explanation:

#### Example 2:

> Input: grid = [["X","X"],["X","Y"]]
> 
> Output: 0
> 
> Explanation:
> 
> No submatrix has an equal frequency of 'X' and 'Y'.

#### Example 3:

> Input: grid = [[".","."],[".","."]]
> 
> Output: 0
> 
> Explanation:
> 
> No submatrix has at least one 'X'.

#### Constraints:

- 1 <= grid.length, grid[i].length <= 1000
- grid[i][j] is either 'X', 'Y', or '.'.