---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1658"
title: "Minimum Operations to Reduce X to Zero"
url: "https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - Binary Search
  - Sliding Window
  - Prefix Sum

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted:
date-solved:
attempts:

# Personal Notes
rating:   # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "two pointer"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero)

Medium

You are given an integer array nums and an integer x. 
In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. 
Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

#### Example 1:

> Input: nums = [1,1,4,2,3], x = 5
> Output: 2
> Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

#### Example 2:

> Input: nums = [5,6,7,8,9], x = 4
> Output: -1

#### Example 3:

> Input: nums = [3,2,20,1,1,3], x = 10
> Output: 5
> Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

#### Constraints:

- 1 <= nums.length <= 10<sup>5</sup>
- 1 <= nums[i] <= 10<sup>4</sup>
- 1 <= x <= 10<sup>9</sup>