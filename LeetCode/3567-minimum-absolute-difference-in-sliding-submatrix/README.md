---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3567"
title: "Minimum Absolute Difference in Sliding Submatrix"
url: "https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix"
difficulty: Medium  # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Sorting
  - Matrix

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-03-20
date-solved: 2026-03-20
attempts: 2

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
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

## [3567. Minimum Absolute Difference in Sliding Submatrix](https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix)

Medium

You are given an m x n integer matrix grid and an integer k.

For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.

Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid.

Note: If all elements in the submatrix have the same value, the answer will be 0.

A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.
 

#### Example 1:

> Input: grid = [[1,8],[3,-2]], k = 2
> 
> Output: [[2]]
> 
> Explanation:
> 
> There is only one possible k x k submatrix: [[1, 8], [3, -2]].
> Distinct values in the submatrix are [1, 8, 3, -2].
> The minimum absolute difference in the submatrix is |1 - 3| = 2. Thus, the answer is [[2]].

#### Example 2:

> Input: grid = [[3,-1]], k = 1
> 
> Output: [[0,0]]
> 
> Explanation:
> 
> Both k x k submatrix has only one distinct element.
> Thus, the answer is [[0, 0]].

#### Example 3:

> Input: grid = [[1,-2,3],[2,3,5]], k = 2
> 
> Output: [[1,2]]
> 
> Explanation:
> 
> - There are two possible k × k submatrix:
>   - Starting at (0, 0): [[1, -2], [2, 3]].
>       - Distinct values in the submatrix are [1, -2, 2, 3].
>       - The minimum absolute difference in the submatrix is |1 - 2| = 1.
>   - Starting at (0, 1): [[-2, 3], [3, 5]].
>       - Distinct values in the submatrix are [-2, 3, 5].
>       - The minimum absolute difference in the submatrix is |3 - 5| = 2.
> - Thus, the answer is [[1, 2]].

#### Constraints:

- 1 <= m == grid.length <= 30
- 1 <= n == grid[i].length <= 30
- -10<sup>5 <= grid[i][j] <= 10<sup>5</sup>
- 1 <= k <= min(m, n)