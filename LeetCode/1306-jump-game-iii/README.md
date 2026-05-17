---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1306"
title: "Jump Game III"
url: "https://leetcode.com/problems/jump-game-iii"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - BFS
  - DFS

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-05-17
date-solved: 2026-05-17
attempts: 1

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

## [1306. Jump Game III](https://leetcode.com/problems/jump-game-iii)
Medium

Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.

#### Example 1:

> Input: arr = [4,2,3,0,3,1,2], start = 5
> Output: true
> Explanation: 
> All possible ways to reach at index 3 with value 0 are: 
> index 5 -> index 4 -> index 1 -> index 3 
> index 5 -> index 6 -> index 4 -> index 1 -> index 3 

#### Example 2:

> Input: arr = [4,2,3,0,3,1,2], start = 0
> Output: true 
> Explanation: 
> One possible way to reach at index 3 with value 0 is: 
> index 0 -> index 4 -> index 1 -> index 3

#### Example 3:

> Input: arr = [3,0,2,1,2], start = 2
> Output: false
> Explanation: There is no way to reach at index 1 with value 0.
 
#### Constraints:

- 1 <= arr.length <= 5 * 104
- 0 <= arr[i] < arr.length
- 0 <= start < arr.length