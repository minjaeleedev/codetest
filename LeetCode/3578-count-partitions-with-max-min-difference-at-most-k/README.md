---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3578"
title: "Count Partitions With Max-Min Difference at Most K"
url: "https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Dynamic Programming (DP)
  - Queue
  - Sliding Window
  - Prefix Sum
  - Monotonic Queue

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-12-06
date-solved: 2025-12-06
attempts: 1

# Personal Notes
rating: 7  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "what is monotonic queue?"
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2026-01-06  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3578. Count Partitions With Max-Min Difference at Most K](https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k)

Medium

You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 10<sup>9</sup> + 7.

#### Example 1:

> Input: nums = [9,4,1,3,7], k = 4
> 
> Output: 6
> 
> Explanation:
> 
> There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:
> 
> - [[9], [4], [1], [3], [7]]
> - [[9], [4], [1], [3, 7]]
> - [[9], [4], [1, 3], [7]]
> - [[9], [4, 1], [3], [7]]
> - [[9], [4, 1], [3, 7]]
> - [[9], [4, 1, 3], [7]]

#### Example 2:

> Input: nums = [3,3,4], k = 0
> 
> Output: 2
> 
> Explanation:
> 
> There are 2 valid partitions that satisfy the given conditions:
> 
> - [[3], [3], [4]]
> - [[3, 3], [4]]
 

#### Constraints:

- 2 <= nums.length <= 5 * 10<sup>4</sup>
- 1 <= nums[i] <= 10<sup>9</sup>
- 0 <= k <= 10<sup>9</sup>