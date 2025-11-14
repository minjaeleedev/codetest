---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2536"
title: "Increment Submatrices by One"
url: "https://leetcode.com/problems/increment-submatrices-by-one"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Matrix
  - Prefix Sum

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-14
date-solved: null
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems:
  - platform: LeetCode
    id: "2528"

# Review Schedule (for spaced repetition)
next-review: 2025-12-11  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [2536. Increment Submatrices by One](https://leetcode.com/problems/increment-submatrices-by-one)

Medium

You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

- Add 1 to **every element** in the submatrix with the top left corner `(row1_i, col1)_i)` and the bottom right corner `(row2_i, col2_i)`. That is, add 1 to `mat[x][y]` for all `row1_i <= x <= row2_i` and `col1_i <= y <= col2_i`.

Return the matrix mat after performing every query.

 
#### Example 1

> ![image1](./example1.png)
> 
> Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
> 
> Output: [[1,1,0],[1,2,1],[0,1,1]]
> 
> Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
> 
> - In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
> - In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).

#### Example 2

> ![image2](./example2.png)
> 
> Input: n = 2, queries = [[0,0,1,1]]
> 
> Output: [[1,1],[1,1]]
> 
> Explanation: The diagram above shows the initial matrix and the matrix after the first query.
> - In the first query we add 1 to every element in the matrix.
 

#### Constraints

- 1 <= n <= 500
- `1 <= queries.length <= 10^4`
- 0 <= row1i <= row2i < n
- 0 <= col1i <= col2i < n