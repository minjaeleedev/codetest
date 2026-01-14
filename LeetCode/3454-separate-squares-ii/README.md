---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3454"
title: "Separate Squares II"
url: "https://leetcode.com/problems/separate-squares-ii"
difficulty: Hard   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Binary Search
  - Segment Tree
  - Line Sweep

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-01-14
date-solved: 2026-01-14
attempts: 1

# Personal Notes
rating: 7  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "segment tree?"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-02-14  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3454. Separate Squares II]()

Hard

You are given a 2D integer array squares. 
Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area covered by squares above the line equals the total area covered by squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted only once in this version.

 
#### Example 1:

> Input: squares = [[0,0,1],[2,2,1]]
> 
> Output: 1.00000
> 
> Explanation:
> 
> 
> 
> Any horizontal line between y = 1 and y = 2 results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.
 
#### Example 2:

> Input: squares = [[0,0,2],[1,1,1]]
> 
> Output: 1.00000
> 
> Explanation:
> 
> 
> 
> Since the blue square overlaps with the red square, it will not be counted again. 
> Thus, the line y = 1 splits the squares into two equal parts.

 

#### Constraints:

- 1 <= squares.length <= 5 * 10<sup>4</sup>
- squares[i] = [xi, yi, li]
- squares[i].length == 3
- 0 <= xi, yi <= 10<sup>9</sup>
- 1 <= li <= 10<sup>9</sup>
- The total area of all the squares will not exceed 10<sup>15</sup>.