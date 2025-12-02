---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3623"
title: "Count Number of Trapezoids I"
url: "https://leetcode.com/problems/count-number-of-trapezoids-i"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - Math
  - Geometry

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-12-02
date-solved: 2025-12-02
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "modular pitfall"
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2026-01-02  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3623. Count Number of Trapezoids I]

Medium

You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

Since the answer may be very large, return it modulo 109 + 7.

 

#### Example 1:

> Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
> 
> Output: 3
> 
> Explanation:
> 
> ![example1-1](./example1-1.png)
> ![example1-2](./example1-2.png)
> ![example1-3](./example1-3.png)
> 
> There are three distinct ways to pick four points that form a horizontal trapezoid:
> 
> Using points [1,0], [2,0], [3,2], and [2,2].
> Using points [2,0], [3,0], [3,2], and [2,2].
> Using points [1,0], [3,0], [3,2], and [2,2].

#### Example 2:

> Input: points = [[0,0],[1,0],[0,1],[2,1]]
> 
> Output: 1
> 
> Explanation:
> 
> ![example2](./example2.png)
> 
> There is only one horizontal trapezoid that can be formed.

 

#### Constraints:

- 4 <= points.length <= 10<sup>5</sup>
- –10<sup>8</sup> <= xi, yi <= 10<sup>8</sup>
- All points are pairwise distinct.