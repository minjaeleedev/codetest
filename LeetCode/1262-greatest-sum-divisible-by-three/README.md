---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1262"
title: "Greatest Sum Divisible by Three"
url: "https://leetcode.com/problems/greatest-sum-divisible-by-three"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Dynamic Programming (DP)
  - Greedy
  - Sorting

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-23
date-solved: 2025-11-23
attempts: 1

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2025-12-20  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1262. Greatest Sum Divisible by Three]()

Medium

Given an integer array `nums`, return the maximum possible sum of elements of the array such that it is divisible by three.

#### Example 1:

> Input: nums = [3,6,5,1,8]
> 
> Output: 18
> 
> Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

#### Example 2:

> Input: nums = [4]
> 
> Output: 0
> 
> Explanation: Since 4 is not divisible by 3, do not pick any number.

#### Example 3:

> Input: nums = [1,2,3,4,4]
> 
> Output: 12
> 
> Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).

#### Constraints:

- `1 <= nums.length <= 4 * 10^4`
- `1 <= nums[i] <= 10^4`