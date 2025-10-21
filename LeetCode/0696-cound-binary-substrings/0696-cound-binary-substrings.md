---
# Problem Identification
platform: LeetCode
platform-problem-id: "696"
title: "Count Binary Substrings"
url: "https://leetcode.com/problems/count-binary-substrings/"
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

## 696. Count Binary Substrings
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

### Example 1:

> Input: s = "00110011"<br/>
> Output: 6<br/>
> Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".<br/>
> Notice that some of these substrings repeat and are counted the number of times they occur.<br/>
> Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

### Example 2:

> Input: s = "10101"<br/>
> Output: 4<br/>
> Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 
### Constraints:

- 1 <= s.length <= 105
- s[i] is either '0' or '1'.

### Topics

- Two Pointers
- String