---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3727"
title: "Maximum Alternating Sum of Squares"
url: "https://leetcode.com/problems/maximum-alternating-sum-of-squares"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Greedy
  - Sorting

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
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

## [3727. Maximum Alternating Sum of Squares](https://leetcode.com/problems/maximum-alternating-sum-of-squares)

Medium

You are given an integer array nums. You may rearrange the elements in any order.

The alternating score of an array arr is defined as:

score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...
Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.

 
#### Example 1:

> Input: nums = [1,2,3]
> 
> Output: 12
> 
> Explanation:
> 
> A possible rearrangement for nums is [2,1,3], which gives the maximum alternating score among all possible rearrangements.
> 
> The alternating score is calculated as:
> 
> score = 22 - 12 + 32 = 4 - 1 + 9 = 12

#### Example 2:

> Input: nums = [1,-1,2,-2,3,-3]
> 
> Output: 16
> 
> Explanation:
> 
> A possible rearrangement for nums is [-3,-1,-2,1,3,2], which gives the maximum alternating score among all possible rearrangements.
> 
> The alternating score is calculated as:
> 
> score = (-3)2 - (-1)2 + (-2)2 - (1)2 + (3)2 - (2)2 = 9 - 1 + 4 - 1 + 9 - 4 = 16

 
#### Constraints:

- 1 <= nums.length <= 10<sup>5</sup>
- -4 * 104 <= nums[i] <= 4 * 10<sup>4</sup>