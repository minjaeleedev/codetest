---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1288"
title: "Remove Covered Intervals"
url: "https://leetcode.com/problems/remove-covered-intervals"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Sorting
  - Greedy

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-07-06
date-solved: 2026-07-06
attempts: 1

# Personal Notes
rating: 3  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
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

## [1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals)

Medium

Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.


#### Example 1:

> Input: intervals = [[1,4],[3,6],[2,8]]
> Output: 2
> Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

#### Example 2:

> Input: intervals = [[1,4],[2,3]]
> Output: 1
 
#### Constraints:

- 1 <= intervals.length <= 1000
- intervals[i].length == 2
- 0 <= li < ri <= 10<sup>5</sup>
- All the given intervals are unique.