---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1081"
title: "Smallest Subsequence of Distinct Characters"
url: "https://leetcode.com/problems/smallest-subsequence-of-distinct-characters"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Stack
  - Greedy
  - Monotonic Stack

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-07-19
date-solved: 2026-07-19
attempts: 2

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "stack"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1081. Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters)

Medium

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

#### Example 1:

> Input: s = "bcabc"
> Output: "abc"

#### Example 2:

> Input: s = "cbacdcbc"
> Output: "acdb"

#### Constraints:

- 1 <= s.length <= 1000
- s consists of lowercase English letters.
 

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/