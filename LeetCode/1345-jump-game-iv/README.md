---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1345"
title: "Jump Game IV"
url: "https://leetcode.com/problems/jump-game-iv"
difficulty: Hard   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - BFS

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-05-18
date-solved: 2026-05-18
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "dedup"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1345. Jump Game IV](https://leetcode.com/problems/jump-game-iv)

Hard

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

- i + 1 where: i + 1 < arr.length.
- i - 1 where: i - 1 >= 0.
- j where: arr[i] == arr[j] and i != j.

Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 
#### Example 1:

> Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
> Output: 3
> Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

#### Example 2:

> Input: arr = [7]
> Output: 0
> Explanation: Start index is the last index. You do not need to jump.

#### Example 3:

> Input: arr = [7,6,9,6,9,6,9,7]
> Output: 1
> Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
 

#### Constraints:

- 1 <= arr.length <= 5 * 10<sup>4</sup>
- -10<sup>8</sup> <= arr[i] <= 10<sup>8</sup>