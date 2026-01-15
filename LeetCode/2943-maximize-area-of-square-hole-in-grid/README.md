---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2943"
title: "Maximize Area of Square Hole in Grid"
url: "https://leetcode.com/problems/maximize-area-of-square-hole-in-grid"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Sorting

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-01-15
date-solved: 2026-01-15
attempts: 1

# Personal Notes
rating: 3  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "idea"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [2943. Maximize Area of Square Hole in Grid](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid)

Medium

You are given the two integers, n and m and two integer arrays, hBars and vBars. 
The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. 
The bars are indexed starting from 1.

You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. 
Note that other bars are fixed and cannot be removed.

Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).

 
#### Example 1:

![image1](./example1.png)

> Input: n = 2, m = 1, hBars = [2,3], vBars = [2]
> 
> Output: 4
> 
> Explanation:
> 
> The left image shows the initial grid formed by the bars. The horizontal bars are [1,2,3,4], and the vertical bars are [1,2,3].
> 
> One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.

#### Example 2:


![image2](./example2.png)

> Input: n = 1, m = 1, hBars = [2], vBars = [2]
> 
> Output: 4
> 
> Explanation:
> 
> To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar 2.

#### Example 3:


![image3](./example3.png)

> Input: n = 2, m = 3, hBars = [2,3], vBars = [2,4]
> 
> Output: 4
> 
> Explanation:
> 
> One way to get the maximum square-shaped hole is by removing horizontal bar 3, and vertical bar 4.

 
#### Constraints:

- 1 <= n <= 10<sup>9</sup>
- 1 <= m <= 10<sup>9</sup>
- 1 <= hBars.length <= 100
- 2 <= hBars[i] <= n + 1
- 1 <= vBars.length <= 100
- 2 <= vBars[i] <= m + 1
- All values in hBars are distinct.
- All values in vBars are distinct.
 
