---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1254"
title: "Number of Closed Islands"
url: "https://leetcode.com/problems/number-of-closed-islands"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Depth-First Search
  - Breadth-First Search
  - Union-Find
  - Matrix

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted:
date-solved:
attempts:

# Personal Notes
rating:   # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands)

Medium

Given a 2D grid consists of 0s (land) and 1s (water). 
An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

#### Example 1:

> Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
> Output: 2
> Explanation: 
> Islands in gray are closed because they are completely surrounded by water (group of 1s).

#### Example 2:

> Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
> Output: 1

#### Example 3:

> Input: grid = [[1,1,1,1,1,1,1],
>                [1,0,0,0,0,0,1],
>                [1,0,1,1,1,0,1],
>                [1,0,1,0,1,0,1],
>                [1,0,1,1,1,0,1],
>                [1,0,0,0,0,0,1],
>                [1,1,1,1,1,1,1]]
> Output: 2
 
#### Constraints:

- 1 <= grid.length, grid[0].length <= 100
- 0 <= grid[i][j] <=1