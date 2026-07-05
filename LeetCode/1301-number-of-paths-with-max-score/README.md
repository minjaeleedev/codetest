---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1301"
title: "Number of Paths with Max Score"
url: "https://leetcode.com/problems/number-of-paths-with-max-score"
difficulty: Hard   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Dynamic Programming
  - Matrix

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-07-05
date-solved: 2026-07-05
attempts: 2

# Personal Notes
rating: 6  # 1-10 difficulty rating (personal)
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

## [1301. Number of Paths with Max Score](https://leetcode.com/problems/number-of-paths-with-max-score)

Hard

You are given a square board of characters. 
You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. 
The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. 
In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].

#### Example 1:

> Input: board = ["E23","2X2","12S"]
> Output: [7,1]

#### Example 2:

> Input: board = ["E12","1X1","21S"]
> Output: [4,2]

#### Example 3:

> Input: board = ["E11","XXX","11S"]
> Output: [0,0]
 
#### Constraints:

- 2 <= board.length == board[i].length <= 100