---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1461"
title: "Check If a String Contains All Binary Codes of Size K"
url: "https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Hash Table
  - String
  - Bit Manipulation
  - Rolling Hash
  - Hash Function

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-02-23
date-solved: 2026-02-23
attempts: 2

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-03-23  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1461. Check If a String Contains All Binary Codes of Size K](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k)

Medium

Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

#### Example 1:

> Input: s = "00110110", k = 2
> Output: true
> Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

#### Example 2:

> Input: s = "0110", k = 1
> Output: true
> Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 

#### Example 3:

> Input: s = "0110", k = 2
> Output: false
> Explanation: The binary code "00" is of length 2 and does not exist in the array.
 

#### Constraints:

- 1 <= s.length <= 5 * 10<sup>5</sup>
- s[i] is either '0' or '1'.
- 1 <= k <= 20