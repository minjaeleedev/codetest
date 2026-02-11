---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3721"
title: ""
url: ""
difficulty:   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - Divide and Conquer
  - Segment Tree
  - Prefix Sum

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-02-11
date-solved:
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "optimization in brute force"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-03-11  # Auto-managed by review script
review-count: 0
last-reviewed: null
---
## [3721. Longest Balanced Subarray II](https://leetcode.com/problems/longest-balanced-subarray-ii)

Hard

You are given an integer array nums.

A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.

#### Example 1:

> Input: nums = [2,5,4,3]
> 
> Output: 4
> 
> Explanation:
> 
> The longest balanced subarray is [2, 5, 4, 3].
> It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.

#### Example 2:

> Input: nums = [3,2,2,5,4]
> 
> Output: 5
> 
> Explanation:
> 
> The longest balanced subarray is [3, 2, 2, 5, 4].
> It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.

#### Example 3:

> Input: nums = [1,2,3,2]
> 
> Output: 3
> 
> Explanation:
> 
> The longest balanced subarray is [2, 3, 2].
> It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.
 

#### Constraints:

- 1 <= nums.length <= 10<sup>5</sup>
- 1 <= nums[i] <= 10<sup>5</sup>