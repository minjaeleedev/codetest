---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "840"
title: "Magic Squares In Grid"
url: "https://leetcode.com/problems/magic-squares-in-grid"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - Math
  - Matrix

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-12-30
date-solved: 2025-12-30
attempts: 1

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "optimization with property"
similar-problems:
  - platform: LeetCode
    id: "1895"

# Review Schedule (for spaced repetition)
next-review: 2026-01-30  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [840. Magic Squares In Grid](https://leetcode.com/problems/magic-squares-in-grid)

Medium

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 
#### Example 1:


> Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
> Output: 1
> Explanation: 
> The following subgrid is a 3 x 3 magic square:
> 
> while this one is not:
> 
> In total, there is only one magic square inside the given grid.

#### Example 2:

> Input: grid = [[8]]
> Output: 0
 

#### Constraints:

- row == grid.length
- col == grid[i].length
- 1 <= row, col <= 10
- 0 <= grid[i][j] <= 15