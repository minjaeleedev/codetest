---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1980"
title: "Find Unique Binary String"
url: "https://leetcode.com/problems/find-unique-binary-string"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - String
  - Backtracking

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-03-08
date-solved: 2026-03-08
attempts: 1

# Personal Notes
rating: 3  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "cantor?"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1980. Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string)

Medium

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. 

If there are multiple answers, you may return any of them.

#### Example 1:

> Input: nums = ["01","10"]
> Output: "11"
> Explanation: "11" does not appear in nums. "00" would also be correct.

#### Example 2:

> Input: nums = ["00","01"]
> Output: "11"
> Explanation: "11" does not appear in nums. "10" would also be correct.

#### Example 3:

> Input: nums = ["111","011","001"]
> Output: "101"
> Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

#### Constraints:

- n == nums.length
- 1 <= n <= 16
- nums[i].length == n
- nums[i] is either '0' or '1'.
- All the strings of nums are unique.