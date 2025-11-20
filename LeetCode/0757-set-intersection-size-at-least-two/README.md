---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "757"
title: "Set Inter"
url: "https://leetcode.com/problems/set-intersection-size-at-least-two"
difficulty: Hard   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Greedy
  - Sorting

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-20
date-solved: 2025-11-20
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "greedy, sort"
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2025-12-15  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [757. Set Intersection Size At Least Two](https://leetcode.com/problems/set-intersection-size-at-least-two)

Hard

You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.

Return the minimum possible size of a containing set.

#### Example 1

> Input: intervals = [[1,3],[3,7],[8,9]]
> 
> Output: 5
> 
> Explanation: let nums = [2, 3, 4, 8, 9].
>
> It can be shown that there cannot be any containing array of size 4.

#### Example 2:

> Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
> 
> Output: 3
> 
> Explanation: let nums = [2, 3, 4].
> 
> It can be shown that there cannot be any containing array of size 2.

#### Example 3:

> Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
> 
> Output: 5
> 
> Explanation: let nums = [1, 2, 3, 4, 5].
> 
> It can be shown that there cannot be any containing array of size 4.
 

#### Constraints:

- `1 <= intervals.length <= 3000`
- `intervals[i].length == 2`
- 0 <= start<sub>i</sub> < end<sub>i</sub> <= 10<sup>8</sup>