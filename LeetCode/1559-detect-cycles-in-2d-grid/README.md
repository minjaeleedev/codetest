---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1559"
title: "Detect Cycles in 2D Grid"
url: "https://leetcode.com/problems/detect-cycles-in-2d-grid"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Depth-First Search
  - Breadth-First Search
  - Union-Find
  - Matrix

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-04-26
date-solved: 2026-04-26
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "union find?"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-05-26  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1559. Detect Cycles in 2D Grid](https://leetcode.com/problems/detect-cycles-in-2d-grid)

Medium

Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. 
From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. 
For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.

#### Example 1:

![fig1](./example1.png)

> Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
>
> Output: true
>
> Explanation: There are two valid cycles shown in different colors in the image below:
>
> ![fig1-1](./example1-1.png)

#### Example 2:

![fig2](./example2.png)

> Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
>
> Output: true
>
> Explanation: There is only one valid cycle highlighted in the image below:
> 
> ![fig2-2](./example2-2.png)

#### Example 3:

![fig3](./example3.png)

> Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
>
> Output: false
 

#### Constraints:

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 500
- grid consists only of lowercase English letters.