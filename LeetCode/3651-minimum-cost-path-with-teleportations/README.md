---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3651"
title: "Minimum Cost Path with Teleportations"
url: "https://leetcode.com/problems/minimum-cost-path-with-teleportations"
difficulty: Hard  # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Dynamic Programming (DP)
  - Matrix

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-01-28
date-solved: 2026-01-28
attempts: 1

# Personal Notes
rating: 7  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-02-28  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3651. Minimum Cost Path with Teleportations](https://leetcode.com/problems/minimum-cost-path-with-teleportations)

Hard

You are given a m x n 2D integer array grid and an integer `k`. 
You start at the top-left cell (0, 0) and your goal is to reach the bottom‐right cell (m - 1, n - 1).

There are two types of moves available:

- **Normal move**: You can move right or down from your current cell (i, j), i.e. you can move to (i, j + 1) (right) or (i + 1, j) (down). The cost is the value of the destination cell.

- **Teleportation**: You can teleport from any cell (i, j), to any cell (x, y) such that grid[x][y] <= grid[i][j]; the cost of this move is 0. You may teleport at most k times.

Return the **minimum** total cost to reach cell (m - 1, n - 1) from (0, 0).

 

#### Example 1:

> Input: grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2
> 
> Output: 7
> 
> Explanation:
> 
> Initially we are at (0, 0) and cost is 0.
> 
> | Current Position  |	Move        | New Position | Total Cost |
> | ----------------- | ----------- | ------------ | ------- |
> | (0, 0)	          | Move Down	| (1, 0)	   | 0 + 2 = 2
> | (1, 0)	          | Move Right	| (1, 1)	   | 2 + 5 = 7
> | (1, 1)	          | Teleport to | (2, 2)	   | 7 + 0 = 7
> 
> The minimum cost to reach bottom-right cell is 7.

#### Example 2:

> Input: grid = [[1,2],[2,3],[3,4]], k = 1
> 
> Output: 9
> 
> Explanation:
> 
> Initially we are at (0, 0) and cost is 0.
> 
> | Current Position |	Move |	New Position |	Total Cost
> | ----------------- | ----------- | ------------ | ------- |
> | (0, 0)	| Move Down	| (1, 0)	| 0 + 2 = 2
> | (1, 0)	| Move Right| 	(1, 1)	| 2 + 3 = 5
> | (1, 1)	| Move Down	| (2, 1)	| 5 + 4 = 9
>
> The minimum cost to reach bottom-right cell is 9.

#### Constraints:

- 2 <= m, n <= 80
- m == grid.length
- n == grid[i].length
- 0 <= grid[i][j] <= 10<sup>4</sup>
- 0 <= k <= 10