---
# Problem Identification
platform: LeetCode
platform-problem-id: "2255"
title: "Count Prefixes of a Given String"
url: "https://leetcode.com/problems/count-prefixes-of-a-given-string/"
difficulty: None
topics:
  -

# Solution Tracking
status: Solved
date-attempted:
date-solved:
attempts:

# Personal Notes
rating:
needs-review: false
tags: []
notes: ""
similar-problems: []

# Review Schedule (for spaced repetition)
next-review: null
review-count: 0
last-reviewed: null
---

## 2255. Count Prefixes of a Given String

You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.

Return the number of strings in words that are a prefix of s.

A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string.

### Example 1:

> Input: words = ["a","b","c","ab","bc","abc"], s = "abc"<br/>
> Output: 3<br/>
> Explanation:<br/>
> The strings in words which are a prefix of s = "abc" are:<br/>
> "a", "ab", and "abc".<br/>
> Thus the number of strings in words which are a prefix of s is 3.

### Example 2:

> Input: words = ["a","a"], s = "aa"<br/>
> Output: 2<br/>
> Explanation:<br/>
> Both of the strings are a prefix of s.<br/>
> Note that the same string can occur multiple times in words, and it should be counted each time.
 
### Constraints:

- 1 <= words.length <= 1000
- 1 <= words[i].length, s.length <= 10
- words[i] and s consist of lowercase English letters only.