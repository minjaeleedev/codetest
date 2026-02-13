---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3714"
title: "Longest Balanced Substring II"
url: "https://leetcode.com/problems/longest-balanced-substring-ii"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Hash Table
  - String
  - Prefix Sum

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-02-13
date-solved:
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "check constraint, and review an idea using diff counts for dict key"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-03-13  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3714. Longest Balanced Substring II](https://leetcode.com/problems/longest-balanced-substring-ii)
You are given a string s consisting only of the characters 'a', 'b', and 'c'.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.

 
#### Example 1:

> Input: s = "abbac"
> 
> Output: 4
> 
> Explanation:
> 
> The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

#### Example 2:

> Input: s = "aabcc"
> 
> Output: 3
> 
> Explanation:
> 
> The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

#### Example 3:

> Input: s = "aba"
> 
> Output: 2
> 
> Explanation:
> 
> One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

 
#### Constraints:

- 1 <= s.length <= 10<sup>5</sup>
- **s contains only the characters 'a', 'b', and 'c'.**