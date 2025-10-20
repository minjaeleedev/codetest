---
# Problem Identification
platform: LeetCode
platform-problem-id: "3083"
title: "Existence of a Substring in a String and Its Reverse"
url: "https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/"
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

## 3083. Existence of a Substring in a String and Its Reverse

Given a string s, find any substring of length 2 which is also present in the reverse of s.

Return true if such a substring exists, and false otherwise.

### Example 1:

> Input: s = "leetcode"<br/>
> Output: true<br/>
> Explanation: Substring "ee" is of length 2 which is also present in reverse(s) == "edocteel".

### Example 2:

> Input: s = "abcba"<br/>
> Output: true<br/>
> Explanation: All of the substrings of length 2 "ab", "bc", "cb", "ba" are also present in reverse(s) == "abcba".

### Example 3:

> Input: s = "abcd"<br/>
> Output: false<br/>
> Explanation: There is no substring of length 2 in s, which is also present in the reverse of s.

### Constraints:

- 1 <= s.length <= 100
- s consists only of lowercase English letters.
