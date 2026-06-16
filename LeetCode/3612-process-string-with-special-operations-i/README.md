---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3612"
title: "Process String with Special Operations I"
url: "https://leetcode.com/problems/process-string-with-special-operations-i"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - String
  - Simulation

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-06-16
date-solved: 2026-06-16
attempts: 1

# Personal Notes
rating: 2  # 1-10 difficulty rating (personal)
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

## [3612. Process String with Special Operations I](https://leetcode.com/problems/process-string-with-special-operations-i)

Medium

You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.

Build a new string result by processing s according to the following rules from left to right:

- If the letter is a lowercase English letter append it to result.
- A '*' removes the last character from result, if it exists.
- A '#' duplicates the current result and appends it to itself.
- A '%' reverses the current result.
Return the final string result after processing all characters in s.


#### Example 1:

> Input: s = "a#b%*"
> 
> Output: "ba"
> 
> Explanation:
> 
> i	s[i]	Operation	Current result
> 0	'a'	Append 'a'	"a"
> 1	'#'	Duplicate result	"aa"
> 2	'b'	Append 'b'	"aab"
> 3	'%'	Reverse result	"baa"
> 4	'*'	Remove the last character	"ba"
> Thus, the final result is "ba".

#### Example 2:

> Input: s = "z*#"
> 
> Output: ""
> 
> Explanation:
> 
> i	s[i]	Operation	Current result
> 0	'z'	Append 'z'	"z"
> 1	'*'	Remove the last character	""
> 2	'#'	Duplicate the string	""
> Thus, the final result is "".

#### Constraints:

- 1 <= s.length <= 20
- s consists of only lowercase English letters and special characters *, #, and %.