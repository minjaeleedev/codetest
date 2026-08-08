---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3302"
title: "Find the Lexicographically Smallest Valid Sequence"
url: "https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Two Pointers
  - String
  - Dynamic Programming
  - Greedy

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted:
date-solved:
attempts:

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

## [3302. Find the Lexicographically Smallest Valid Sequence](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence)

Medium

You are given two strings word1 and word2.

A string x is called almost equal to y if you can change at most one character in x to make it identical to y.

A sequence of indices seq is called valid if:

The indices are sorted in ascending order.
Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.
Return an array of size word2.length representing the lexicographically smallest valid sequence of indices. If no such sequence of indices exists, return an empty array.

Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.

 

Example 1:

Input: word1 = "vbcca", word2 = "abc"

Output: [0,1,2]

Explanation:

The lexicographically smallest valid sequence of indices is [0, 1, 2]:

Change word1[0] to 'a'.
word1[1] is already 'b'.
word1[2] is already 'c'.
Example 2:

Input: word1 = "bacdc", word2 = "abc"

Output: [1,2,4]

Explanation:

The lexicographically smallest valid sequence of indices is [1, 2, 4]:

word1[1] is already 'a'.
Change word1[2] to 'b'.
word1[4] is already 'c'.
Example 3:

Input: word1 = "aaaaaa", word2 = "aaabc"

Output: []

Explanation:

There is no valid sequence of indices.

Example 4:

Input: word1 = "abc", word2 = "ab"

Output: [0,1]

 

#### Constraints:

- 1 <= word2.length < word1.length <= 3 * 10<sup>5</sup>
- word1 and word2 consist only of lowercase English letters.