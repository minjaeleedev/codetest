---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id:
title: ""
url: ""
difficulty:   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Math
  - Sliding Window
  - Enumerator
  - Number Theory

# Solution Tracking
status: Not Started  # Not Started | Attempted | Solved | Reviewed
date-attempted:
date-solved:
attempts:

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

## [3411. Maximum Subarray With Equal Products](https://leetcode.com/problems/maximum-subarray-with-equal-products)

Easy

You are given an array of positive integers nums.

An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

- prod(arr) is the product of all elements of arr.
- gcd(arr) is the GCD of all elements of arr.
- lcm(arr) is the LCM of all elements of arr.

Return the length of the longest product equivalent subarray of nums.

#### Example 1:

> Input: nums = [1,2,1,2,1,1,1]
> 
> Output: 5
> 
> Explanation: 
> 
> The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

#### Example 2:

> Input: nums = [2,3,4,5,6]
> 
> Output: 3
> 
> Explanation: 
> 
> The longest product equivalent subarray is [3, 4, 5].

#### Example 3:

> Input: nums = [1,2,3,1,4,5,1]
> 
> Output: 5

#### Constraints:

- 2 <= nums.length <= 100
- 1 <= nums[i] <= 10