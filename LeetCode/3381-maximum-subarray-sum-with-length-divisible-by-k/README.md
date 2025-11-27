---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3381"
title: "Maximum Subarray Sum With Length Divisible by K"
url: "https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k"
difficulty:   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - Prefix Sum

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-27
date-solved: 2025-11-27
attempts: 1

# Personal Notes
rating: 5   # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3381. Maximum Subarray Sum With Length Divisible by K](https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k)

Medium

You are given an array of integers nums and an integer k.

Return the maximum sum of a subarray of nums, such that the size of the subarray is divisible by k.

 
#### Example 1:

> Input: nums = [1,2], k = 1
> 
> Output: 3
> 
> Explanation:
> 
> The subarray [1, 2] with sum 3 has length equal to 2 which is divisible by 1.

#### Example 2:

> Input: nums = [-1,-2,-3,-4,-5], k = 4
> 
> Output: -10
> 
> Explanation:
> 
> The maximum sum subarray is [-1, -2, -3, -4] which has length equal to 4 which is divisible by 4.

#### Example 3:

> Input: nums = [-5,1,2,-3,4], k = 2
> 
> Output: 4
> 
> Explanation:
> 
> The maximum sum subarray is [1, 2, -3, 4] which has length equal to 4 which is divisible by 2.


#### Constraints:

- 1 <= k <= nums.length <= 2 * 10<sup>5</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>