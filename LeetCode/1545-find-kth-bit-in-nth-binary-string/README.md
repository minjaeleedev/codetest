---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1545"
title: "Find Kth Bit in Nth Binary String"
url: "https://leetcode.com/problems/find-kth-bit-in-nth-binary-string"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - String
  - Recursion
  - Simulation

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-03-03
date-solved: 2026-03-03
attempts: 1

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "recursion sense"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-04-03  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1545. Find Kth Bit in Nth Binary String](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string)

Medium

Given two positive integers n and k, the binary string Sn is formed as follows:

- S1 = "0"
- Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1

Where `+` denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

- S1 = "0"
- S2 = "011"
- S3 = "0111001"
- S4 = "011100110110001"

Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

#### Example 1:

> Input: n = 3, k = 1
> Output: "0"
> Explanation: S3 is "0111001".
> The 1st bit is "0".

#### Example 2:

> Input: n = 4, k = 11
> Output: "1"
> Explanation: S4 is "011100110110001".
> The 11th bit is "1".
 

#### Constraints:

- 1 <= n <= 20
- 1 <= k <= 2n - 1