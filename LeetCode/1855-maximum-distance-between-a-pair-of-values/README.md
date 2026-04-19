---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1855"
title: "Maximum Distance Between a Pair of Values"
url: "https://leetcode.com/problems/maximum-distance-between-a-pair-of-values"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Two Pointers
  - Binary Search

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-04-19
date-solved: 2026-04-19
attempts: 1

# Personal Notes
rating: 3  # 1-10 difficulty rating (personal)
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

## [1855. Maximum Distance Between a Pair of Values](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values)

Medium

You are given two non-increasing 0-indexed integer arrays `nums1` and `nums2`.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. 
The **distance** of the pair is j - i.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.


#### Example 1:

> Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
> Output: 2
> Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
> The maximum distance is 2 with pair (2,4).

#### Example 2:

> Input: nums1 = [2,2,2], nums2 = [10,10,1]
> Output: 1
> Explanation: The valid pairs are (0,0), (0,1), and (1,1).
> The maximum distance is 1 with pair (0,1).

#### Example 3:

> Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
> Output: 2
> Explanation: The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
> The maximum distance is 2 with pair (2,4).

#### Constraints:

- 1 <= nums1.length, nums2.length <= 10<sup>5</sup>
- 1 <= nums1[i], nums2[j] <= 10<sup>5</sup>
- Both nums1 and nums2 are non-increasing.