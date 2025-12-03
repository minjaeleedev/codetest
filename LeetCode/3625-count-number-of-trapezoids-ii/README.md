---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3625"
title: "Count Number of Trapezoids II"
url: "https://leetcode.com/problems/count-number-of-trapezoids-ii"
difficulty: Hard  # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - Math
  - Geometry

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-12-03
date-solved: 2025-12-03
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2026-01-03  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3625. Count Number of Trapezoids II](https://leetcode.com/problems/count-number-of-trapezoids-ii)

Hard

You are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.

A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.

 
#### Example 1:

> Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
> 
> Output: 2
> 
> Explanation:
> 
> ![example1-1](./example1-1.png)
> ![example1-2](./example1-2.png)
> 
> There are two distinct ways to pick four points that form a trapezoid:
> 
> The points [-3,2], [2,3], [3,2], [2,-3] form one trapezoid.
> The points [2,3], [3,2], [3,0], [2,-3] form another trapezoid.

#### Example 2:

> Input: points = [[0,0],[1,0],[0,1],[2,1]]
> 
> Output: 1
> 
> Explanation:
> 
> ![example2](./example2.png)
> 
> There is only one trapezoid which can be formed.

 

#### Constraints:

- 4 <= points.length <= 500
- –1000 <= xi, yi <= 1000
- All points are pairwise distinct.