---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1611"
title: "Minimum One Bit Operations to Make Integers Zero"
url: "https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Dynamic Programming
  - Bit Manipulation
  - Memoization

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-08
date-solved: 2025-11-08
attempts: 1

# Personal Notes
rating: 8  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2025-12-01  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1611. Minimum One Bit Operations to Make Integers Zero](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero)

Hard

Given an integer n, you must transform it into 0 using the following operations any number of times:

- Change the rightmost (`0th`) bit in the binary representation of n.
- Change the `ith` bit in the binary representation of `n` if the `(i-1)th` bit is set to `1` and the `(i-2)th` through `0th` bits are set to 0.

Return the minimum number of operations to transform n into 0.

#### Example 1

> Input: n = 3
> 
> Output: 2
> 
> Explanation: The binary representation of 3 is "11".
> 
> "11" -> "01" with the 2nd operation since the 0th bit is 1.
>
> "01" -> "00" with the 1st operation.

#### Example 2

> Input: n = 6
> 
> Output: 4
> 
> Explanation: The binary representation of 6 is "110".
> 
> "110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
> 
> "010" -> "011" with the 1st operation.
> 
> "011" -> "001" with the 2nd operation since the 0th bit is 1.
> 
> "001" -> "000" with the 1st operation.
 
#### Constraints

- `0 <= n <= 10^9`