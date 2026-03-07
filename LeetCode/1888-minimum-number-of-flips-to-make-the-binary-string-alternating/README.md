---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1888"
title: "Minimum Number of Flips to Make the Binary String Alternating"
url: "https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - String
  - Dynamic Programming
  - Sliding Window

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-03-07
date-solved: null
attempts: 1

# Personal Notes
rating: 6  # 1-10 difficulty rating (personal)
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

## [1888. Minimum Number of Flips to Make the Binary String Alternating](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating)

Medium

You are given a binary string s. 
You are allowed to perform two types of operations on the string in any sequence:

- Type-1: Remove the character at the start of the string s and append it to the end of the string.
- Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.

Return *the **minimum** number of **type-2** operations you need to perform such that s becomes **alternating**.*

The string is called alternating if no two adjacent characters are equal.

- For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

#### Example 1:

> Input: s = "111000"
> Output: 2
> Explanation: Use the first operation two times to make s = "100011".
> Then, use the second operation on the third and sixth elements to make s = "101010".

#### Example 2:

> Input: s = "010"
> Output: 0
> Explanation: The string is already alternating.

#### Example 3:

> Input: s = "1110"
> Output: 1
> Explanation: Use the second operation on the second element to make s = "1010".
 

#### Constraints:

- 1 <= s.length <= 10<sup>5</sup>
- s[i] is either '0' or '1'.