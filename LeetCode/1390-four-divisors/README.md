---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1390"
title: "Four Divisors"
url: "https://leetcode.com/problems/four-divisors"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Math

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-01-04
date-solved: 2026-01-04
attempts: 1

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "optimization with sieve"
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2026-02-04  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1390. Four Divisors](https://leetcode.com/problems/four-divisors)

Medium

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. 
If there is no such integer in the array, return 0.


#### Example 1:

> Input: nums = [21,4,7]
> Output: 32
> Explanation: 
> 21 has 4 divisors: 1, 3, 7, 21
> 4 has 3 divisors: 1, 2, 4
> 7 has 2 divisors: 1, 7
> The answer is the sum of divisors of 21 only.

#### Example 2:

> Input: nums = [21,21]
> Output: 64

#### Example 3:

> Input: nums = [1,2,3,4,5]
> Output: 0
 
#### Constraints:

- 1 <= nums.length <= 10<sup>4</sup>
- 1 <= nums[i] <= 10<sup>5</sup>