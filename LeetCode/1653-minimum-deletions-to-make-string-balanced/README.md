---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1653"
title: "Minimum Deletions to Make String Balanced"
url: "https://leetcode.com/problems/minimum-deletions-to-make-string-balanced"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - String
  - Dynamic Programming (DP)
  - Stack

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-02-07
date-solved:
attempts:

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: tru  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-03-07  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1653. Minimum Deletions to Make String Balanced]()

Medium

You are given a string s consisting only of characters 'a' and 'b'.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

#### Example 1:

> Input: s = "aababbab"
> Output: 2
> Explanation: You can either:
> Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
> Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

#### Example 2:

> Input: s = "bbaaaaabb"
> Output: 2
> Explanation: The only solution is to delete the first two characters.

#### Constraints:

- 1 <= s.length <= 105
- s[i] is 'a' or 'b'.