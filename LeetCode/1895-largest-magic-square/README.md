---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1895"
title: "Largest Magic Square"
url: "https://leetcode.com/problems/largest-magic-square"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Matrix
  - Prefix Sum

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-01-18
date-solved: 2026-01-18
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "prefix sum idea. optimization"
similar-problems:
  - platform: LeetCode
    id: "840"

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1895. Largest Magic Square](https://leetcode.com/problems/largest-magic-square)

Medium

A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. 
The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.


#### Example 1:


> Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
> Output: 3
> Explanation: The largest magic square has a size of 3.
> Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
> - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
> - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
> - Diagonal sums: 5+4+3 = 6+4+2 = 12

#### Example 2:


> Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
> Output: 2
 

#### Constraints:

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- 1 <= grid[i][j] <= 10<sup>6</sup>