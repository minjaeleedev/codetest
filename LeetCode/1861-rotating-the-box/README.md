---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1861"
title: "Rotating the Box"
url: "https://leetcode.com/problems/rotating-the-box"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Two Pointers
  - Matrix

# Solution Tracking
status: Not Started  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-05-06
date-solved: 2026-05-06
attempts: 1

# Personal Notes
rating:   # 1-10 difficulty rating (personal)
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

## [1861. Rotating the Box](https://leetcode.com/problems/rotating-the-box)

Medium

You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

- A stone '#'
- A stationary obstacle '*'
- Empty '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. 
Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. 
Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.
 

#### Example 1:


> Input: boxGrid = [["#",".","#"]]
> Output: [["."],
>          ["#"],
>          ["#"]]

#### Example 2:


> Input: boxGrid = [["#",".","*","."],
>               ["#","#","*","."]]
> Output: [["#","."],
>          ["#","#"],
>          ["*","*"],
>          [".","."]]

#### Example 3:


> Input: boxGrid = [["#","#","*",".","*","."],
>               ["#","#","#","*",".","."],
>               ["#","#","#",".","#","."]]
> Output: [[".","#","#"],
>          [".","#","#"],
>          ["#","#","*"],
>          ["#","*","."],
>          ["#",".","*"],
>          ["#",".","."]]
 

#### Constraints:

- m == boxGrid.length
- n == boxGrid[i].length
- 1 <= m, n <= 500
- boxGrid[i][j] is either '#', '*', or '.'.