---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2840"
title: "Check if Strings Can be Made Equal With Operations II"
url: "https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Hash Table
  - String
  - Sorting

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-03-30
date-solved: 2026-03-30
attempts: 1

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "solution?"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [2840. Check if Strings Can be Made Equal With Operations II](https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii)

Medium

You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.

Return true if you can make the strings s1 and s2 equal, and false otherwise.

#### Example 1:

> Input: s1 = "abcdba", s2 = "cabdab"
> Output: true
> Explanation: We can apply the following operations on s1:
> - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
> - Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
> - Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.

#### Example 2:

> Input: s1 = "abe", s2 = "bea"
> Output: false
> Explanation: It is not possible to make the two strings equal.
 

#### Constraints:

- n == s1.length == s2.length
- 1 <= n <= 10<sup>5</sup>
- s1 and s2 consist only of lowercase English letters.