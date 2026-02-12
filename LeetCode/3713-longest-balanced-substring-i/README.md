---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3713"
title: "Longest Balanced Substring I"
url: "https://leetcode.com/problems/longest-balanced-substring-i"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Hash Table
  - String
  - Counting
  - Enumeration

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-02-12
date-solved:
attempts:

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "use index simply."
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3713. Longest Balanced Substring I](https://leetcode.com/problems/longest-balanced-substring-i)

Medium

You are given a string s consisting of lowercase English letters.

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

> Input: s = "zzabccy"
> 
> Output: 4
> 
> Explanation:
> 
> The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​

#### Example 3:

> Input: s = "aba"
> 
> Output: 2
> 
> Explanation:
> 
> One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".


#### Constraints:

- 1 <= s.length <= 1000
- s consists of lowercase English letters.