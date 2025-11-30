---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1590"
title: "Make Sum Divisible by P"
url: "https://leetcode.com/problems/make-sum-divisible-by-p"
difficulty: Medium  # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - Prefix Sum

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-30
date-solved: 2025-11-30
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: ["modulo"]  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "modulo arithmetic, prefix sum, update hash table over iteration"
similar-problems:
  - platform: "LeetCode"
    id: "974"

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1590. Make Sum Divisible by P](https://leetcode.com/problems/make-sum-divisible-by-p)

Medium

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

#### Example 1

> Input: nums = [3,1,4,2], p = 6
> 
> Output: 1
> 
> Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

#### Example 2:

> Input: nums = [6,3,5,2], p = 9
> 
> Output: 2
> 
> Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

#### Example 3:

> Input: nums = [1,2,3], p = 3
> 
> Output: 0
> 
> Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.

#### Constraints:

- 1 <= nums.length <= 10<sup>5</sup>
- 1 <= nums[i] <= 10<sup>9</sup>
- 1 <= p <= 10<sup>9</sup>