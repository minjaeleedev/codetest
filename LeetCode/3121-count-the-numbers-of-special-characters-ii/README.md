---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3121"
title: "Count the Number of Special Characters II"
url: "https://leetcode.com/problems/count-the-number-of-special-characters-ii"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Hash Table
  - String

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-05-27
date-solved: 2026-05-27
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

## [3121. Count the Number of Special Characters II](https://leetcode.com/problems/count-the-number-of-special-characters-ii)

Medium

You are given a string word. 
A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

#### Example 1:

> Input: word = "aaAbcBC"
> 
> Output: 3
> 
> Explanation:
> 
> The special characters are 'a', 'b', and 'c'.

#### Example 2:

> Input: word = "abc"
> 
> Output: 0
> 
> Explanation:
> 
> There are no special characters in word.

#### Example 3:

> Input: word = "AbBCab"
> 
> Output: 0
> 
> Explanation:
> 
> There are no special characters in word.

 

#### Constraints:

- 1 <= word.length <= 2 * 10<sup>5</sup>
- word consists of only lowercase and uppercase English letters.