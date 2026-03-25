---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3546"
title: "Equal Sum Grid Partition I"
url: "https://leetcode.com/problems/equal-sum-grid-partition-i"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Matrix
  - Enumeration
  - Prefix Sum

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-03-25
date-solved: 2026-03-25
attempts: 1

# Personal Notes
rating: 3  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "prefix sum"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3546. Equal Sum Grid Partition I](https://leetcode.com/problems/equal-sum-grid-partition-i)

Medium

You are given an m x n matrix grid of positive integers. 
Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

- Each of the two resulting sections formed by the cut is non-empty.
- The sum of the elements in both sections is equal.

Return true if such a partition exists; otherwise return false.


#### Example 1:

> Input: grid = [[1,4],[2,3]]
> 
> Output: true
> 
> Explanation:
> 
> 
> 
> A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

#### Example 2:

> Input: grid = [[1,3],[2,4]]
> 
> Output: false
> 
> Explanation:
> 
> No horizontal or vertical cut results in two non-empty sections with equal sums. 
> Thus, the answer is false.

#### Constraints:

- 1 <= m == grid.length <= 10<sup>5</sup>
- 1 <= n == grid[i].length <= 10<sup>5</sup>
- 2 <= m * n <= 10<sup>5</sup>
- 1 <= grid[i][j] <= 10<sup>5</sup>