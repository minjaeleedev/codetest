---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3542"
title: "Minimum Operations to Convert All Elements to Zero"
url: "https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero"
difficulty: Medium  # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - Stack
  - Greedy
  - Monotonic Stack

# Solution Tracking
status: Attemptd  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-10
date-solved: 2025-11-10
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2025-12-01  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3542. Minimum Operations to Convert All Elements to Zero](https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero)

Medium

You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero) operations on the array so that all elements become 0.

In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences of the minimum non-negative integer in that subarray to 0.

Return the minimum number of operations required to make all elements in the array 0.

#### Example 1:

> Input: nums = [0,2]
> 
> Output: 1
> 
> Explanation:
> 
> Select the subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0].
> Thus, the minimum number of operations required is 1.

#### Example 2:

> Input: nums = [3,1,2,1]
> 
> Output: 3
> 
> Explanation:
> 
> - Select subarray [1,3] (which is [1,2,1]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [3,0,2,0].
> - Select subarray [2,2] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [3,0,0,0].
> - Select subarray [0,0] (which is [3]), where the minimum non-negative integer is 3. Setting all occurrences of 3 to 0 results in [0,0,0,0].
> - Thus, the minimum number of operations required is 3.

#### Example 3:

> Input: nums = [1,2,1,2,1,2]
> 
> Output: 4
> 
> Explanation:
> 
> - Select subarray [0,5] (which is [1,2,1,2,1,2]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [0,2,0,2,0,2].
> - Select subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,2,0,2].
> - Select subarray [3,3] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,2].
> - Select subarray [5,5] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,0].
> - Thus, the minimum number of operations required is 4.
 
#### Constraints:

- `1 <= n == nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`