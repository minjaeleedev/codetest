---
# Problem Identification
platform: LeetCode
platform-problem-id: "3120"
title: "Count the Number of Special Characters I"
url: "https://leetcode.com/problems/count-the-number-of-special-characters-i/"
difficulty: None
topics:
  - Hash Table
  - String

# Solution Tracking
status: Solved
date-attempted: 2026-05-26
date-solved: 2026-05-26
attempts: 1

# Personal Notes
rating: 1
needs-review: false
tags: []
notes: ""
similar-problems: []

# Review Schedule (for spaced repetition)
next-review: null
review-count: 0
last-reviewed: null
---

## [3120. Count the Number of Special Characters I](https://leetcode.com/problems/count-the-number-of-special-characters-i)

You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.

### Example 1:

> Input: word = "aaAbcBC"
> 
> Output: 3
> 
> Explanation:
> 
> The special characters in word are 'a', 'b', and 'c'.

### Example 2:

> Input: word = "abc"
> 
> Output: 0
> 
> Explanation:
> 
> No character in word appears in uppercase.

### Example 3:

> Input: word = "abBCab"
> 
> Output: 1
> 
> Explanation:
> 
> The only special character in word is 'b'.

### Constraints:

- 1 <= word.length <= 50
- word consists of only lowercase and uppercase English letters.