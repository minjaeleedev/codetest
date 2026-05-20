---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2657"
title: "Find the Prefix Common Array of Two Arrays"
url: "https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - Bit Manipulation

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-05-20
date-solved: 2026-05-20
attempts: 1

# Personal Notes
rating: 3  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
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

## [2657. Find the Prefix Common Array of Two Arrays](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays)

Medium

You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

#### Example 1:

> Input: A = [1,3,2,4], B = [3,1,2,4]
> Output: [0,2,3,4]
> Explanation: At i = 0: no number is common, so C[0] = 0.
> At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
> At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
> At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

#### Example 2:

> Input: A = [2,3,1], B = [3,1,2]
> Output: [0,1,3]
> Explanation: At i = 0: no number is common, so C[0] = 0.
> At i = 1: only 3 is common in A and B, so C[1] = 1.
> At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
 
#### Constraints:

- 1 <= A.length == B.length == n <= 50
- 1 <= A[i], B[i] <= n
- It is guaranteed that A and B are both a permutation of n integers.