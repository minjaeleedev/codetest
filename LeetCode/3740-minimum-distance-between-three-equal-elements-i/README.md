---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3740"
title: "Minimum Distance Between Three Equal Elements I"
url: "https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-04-10
date-solved: 2026-04-10
attempts: 1

# Personal Notes
rating: 2  # 1-10 difficulty rating (personal)
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

## [3740. Minimum Distance Between Three Equal Elements I](https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i)

Easy
You are given an integer array nums.

A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

 
#### Example 1:

> Input: nums = [1,2,1,1,3]
> 
> Output: 6
> 
> Explanation:
> 
> The minimum distance is achieved by the good tuple (0, 2, 3).
> 
> (0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

#### Example 2:

> Input: nums = [1,1,2,3,2,1,2]
> 
> Output: 8
> 
> Explanation:
> 
> The minimum distance is achieved by the good tuple (2, 4, 6).
> 
> (2, 4, 6) is a good tuple because nums[2] == nums[4] == nums[6] == 2. Its distance is abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8.

#### Example 3:

> Input: nums = [1]
> 
> Output: -1
> 
> Explanation:
> 
> There are no good tuples. Therefore, the answer is -1.

 

#### Constraints:

1 <= n == nums.length <= 100
1 <= nums[i] <= n