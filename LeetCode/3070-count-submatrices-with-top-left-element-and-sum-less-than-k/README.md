---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3070"
title: "Count Submatrices with Top-Left Element and Sum Less Than k"
url: "https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Matrix
  - Prefix Sum

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-03-18
date-solved: 2026-03-18
attempts: 1

# Personal Notes
rating: 3  # 1-10 difficulty rating (personal)
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

## [3070. Count Submatrices with Top-Left Element and Sum Less Than k](https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k)

Medium

You are given a 0-indexed integer matrix grid and an integer k.

Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.

#### Example 1:

> Input: grid = [[7,6,3],[6,6,1]], k = 18
> Output: 4
> Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.

#### Example 2:

> Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
> Output: 6
> Explanation: There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.

#### Constraints:

- m == grid.length 
- n == grid[i].length
- 1 <= n, m <= 1000 
- 0 <= grid[i][j] <= 1000
- 1 <= k <= 10<sup>9</sup>