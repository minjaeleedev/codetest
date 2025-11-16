---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1513"
title: "Number of Substrings With Only 1s"
url: "https://leetcode.com/problems/number-of-substrings-with-only-1s"
difficulty: Medium  # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Math
  - String

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-16
date-solved: 2025-11-16
attempts: 1

# Personal Notes
rating: 3  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "greedy"
similar-problems:
  - platform: LeetCode
    id: "1759"

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1513. Number of Substrings With Only 1s](https://leetcode.com/problems/number-of-substrings-with-only-1s)

Medium

Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

#### Example 1

> Input: s = "0110111"
> 
> Output: 9
> 
> Explanation: There are 9 substring in total with only 1's characters.
> 
> "1" -> 5 times.
> 
> "11" -> 3 times.
> 
> "111" -> 1 time.

#### Example 2

> Input: s = "101"
> 
> Output: 2
> 
> Explanation: Substring "1" is shown 2 times in s.

#### Example 3

> Input: s = "111111"
> 
> Output: 21
> 
> Explanation: Each substring contains only 1's characters.
 

#### Constraints

- `1 <= s.length <= 10^5`
- s[i] is either '0' or '1'.