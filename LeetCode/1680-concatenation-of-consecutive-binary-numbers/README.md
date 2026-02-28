---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1680"
title: "Concatenation of Consecutive Binary Numbers"
url: "https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Math
  - Bit Manipulation
  - Simulation

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-02-28
date-solved: 2026-02-28
attempts: 1

# Personal Notes
rating: 3  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "optimization by bit trick - is power of 2"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1680. Concatenation of Consecutive Binary Numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers)

Medium

Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

#### Example 1:

> Input: n = 1
> Output: 1
> Explanation: "1" in binary corresponds to the decimal value 1. 

#### Example 2:

> Input: n = 3
> Output: 27
> Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
> After concatenating them, we have "11011", which corresponds to the decimal value 27.

#### Example 3:

> Input: n = 12
> Output: 505379714
> Explanation: The concatenation results in "1101110010111011110001001101010111100".
> The decimal value of that is 118505380540.
> After modulo 109 + 7, the result is 505379714.
 
#### Constraints:

- 1 <= n <= 10<sup>5</sup>