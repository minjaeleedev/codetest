---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1536"
title: "Minimum Swaps to Arrange a Binary Grid"
url: "https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Greedy
  - Matrix

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-03-02
date-solved: null
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "take greedy, then operate"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-04-02  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1536. Minimum Swaps to Arrange a Binary Grid](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid)

Medium

Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

#### Example 1:

> Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
> Output: 3

#### Example 2:

> Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
> Output: -1
> Explanation: All rows are similar, swaps have no effect on the grid.

#### Example 3:

> Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
> Output: 0

#### Constraints:

- n == grid.length == grid[i].length
- 1 <= n <= 200
- grid[i][j] is either `0` or `1`