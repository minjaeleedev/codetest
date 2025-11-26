---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2435"
title: ""
url: ""
difficulty:   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Dynamic Programming
  - Matrix

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-26
date-solved: 2025-11-26
attempts: 1

# Personal Notes
rating: 6 # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [2435. Paths in Matrix Whose Sum Is Divisible by K]()

Hard

You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.

Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.

#### Example 1:

> Input: grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
> 
> Output: 2
> 
> Explanation: There are two paths where the sum of the elements on the path is divisible by k.
> 
> The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
> 
> The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.

#### Example 2:

> Input: grid = [[0,0]], k = 5
> 
> Output: 1
> 
> Explanation: The path highlighted in red has a sum of 0 + 0 = 0 which is divisible by 5.

#### Example 3:

> Input: grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
> 
> Output: 10
> 
> Explanation: Every integer is divisible by 1 so the sum of the elements on every possible path is divisible by k.
 
#### Constraints:

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 5 * 104
- 1 <= m * n <= 5 * 104
- 0 <= grid[i][j] <= 100
- 1 <= k <= 50