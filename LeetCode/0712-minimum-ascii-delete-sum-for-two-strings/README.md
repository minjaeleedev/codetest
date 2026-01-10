---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "712"
title: "Minimum ASCII Delete Sum for Two Strings"
url: "https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Dynamic Programming (DP)

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-01-10
date-solved: 2026-01-10
attempts: 1

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "longest common subsequence"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-02-10  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings)

Medium

Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

#### Example 1:

> Input: s1 = "sea", s2 = "eat"
> 
> Output: 231
> 
> Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
> 
> Deleting "t" from "eat" adds 116 to the sum.
> 
> At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

####  Example 2:

> Input: s1 = "delete", s2 = "leet"
> 
> Output: 403
> 
> Explanation: Deleting "dee" from "delete" to turn the string into "let",
> 
> adds 100[d] + 101[e] + 101[e] to the sum.
> 
> Deleting "e" from "leet" adds 101[e] to the sum.
> 
> At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
> 
> If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 

#### Constraints:

- 1 <= s1.length, s2.length <= 1000
- s1 and s2 consist of lowercase English letters.