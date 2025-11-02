---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2257"
title: "Count Unguarded Cells in the Grid"
url: "https://leetcode.com/problems/count-unguarded-cells-in-the-grid"
difficulty: Medium
topics:
  - Array
  - Matrix
  - Simulation

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-02
date-solved: 2025-11-02
attempts: 2

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "time complexity. mark the guard and the wall before the simuation"
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2025-11-11  # Auto-managed by review script
review-count: 0
last-reviewed: 2025-11-02
---

## [2257. Count Unguarded Cells in the Grid](https://leetcode.com/problems/count-unguarded-cells-in-the-grid)

Medium

You are given two integers `m` and `n` representing a **0-indexed** `m x n` grid. 
You are also given two 2D integer arrays `guards` and `walls` where `guards[i] = [row_i, col_i]` and `walls[j] = [row_j, col_j]` represent the positions of the ith guard and jth wall respectively.

A guard can see **every** cell in the four cardinal directions (north, east, south, or west) starting from their position unless **obstructed** by a wall or another guard. 
A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.
 

#### Example 1

![image1](./example1.png)
> **Input**: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
> 
> **Output**: 7
> 
> **Explanation**: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
> 
> There are a total of 7 unguarded cells, so we return 7.

#### Example 2

![image2](./example2.png)
> **Input**: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
> 
> **Output**: 4
> 
> **Explanation**: The unguarded cells are shown in green in the above diagram.
> 
> There are a total of 4 unguarded cells, so we return 4.
 

#### Constraints

- `1 <= m, n <= 10^5`
- `2 <= m * n <= 10^5`
- `1 <= guards.length, walls.length <= 5 * 10^4`
- `2 <= guards.length + walls.length <= m * n`
- `guards[i].length == walls[j].length == 2`
- `0 <= rowi, rowj < m`
- `0 <= coli, colj < n`
- All the positions in `guards` and `walls` are **unique**.