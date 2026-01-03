---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1411"
title: "Number of Ways to Paint N × 3 Grid"
url: "https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid"
difficulty: Hard   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Dynamic Programming (DP)

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-01-03
date-solved: 2026-01-03
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "optimize space"
similar-problems:
  - platform: LeetCode
    id: "1931"

# Review Schedule (for spaced repetition)
next-review: 2026-02-03  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1411. Number of Ways to Paint N × 3 Grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid)

Hard

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

#### Example 1:

![image1](./example1.png)

> Input: n = 1
> 
> Output: 12
> 
> Explanation: There are 12 possible way to paint the grid as shown.

#### Example 2:

> Input: n = 5000
> 
> Output: 30228214
 

#### Constraints:

- n == grid.length
- 1 <= n <= 5000