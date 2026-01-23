---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3510"
title: "Minimum Pair Removal to Sort Array II"
url: "https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii"
difficulty: Hard   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - Linked List
  - Heap (Priority Queue)
  - Simulation
  - Doubly-Linked List
  - Ordered Set

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-01-23
date-solved: 2026-01-23
attempts:

# Personal Notes
rating: 7  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "data structure - doubly linked list with additional values"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-02-23  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3510. Minimum Pair Removal to Sort Array II](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii)

Hard

Given an array nums, you can perform the following operation any number of times:

- Select the **adjacent** pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
- Replace the pair with their sum.

Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 
#### Example 1:

> Input: nums = [5,2,3,1]
> 
> Output: 2
> 
> Explanation:
> 
> - The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
> - The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
> The array nums became non-decreasing in two operations.

#### Example 2:

> Input: nums = [1,2,2]
> 
> Output: 0
> 
> Explanation:
> 
> The array nums is already sorted.

 
#### Constraints:

- 1 <= nums.length <= 10<sup>5</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>