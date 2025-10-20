---
# Problem Identification
platform: LeetCode
platform-problem-id: "2544"
title: "Alternating Digit Sum"
url: "https://leetcode.com/problems/alternating-digit-sum/"
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

## 2544. Alternating Digit Sum

You are given a positive integer n. Each digit of n has a sign according to the following rules:

- The most significant digit is assigned a positive sign.
- Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign.

### Example 1:

> Input: n = 521<br/>
> Output: 4<br/>
> Explanation: (+5) + (-2) + (+1) = 4.

### Example 2:

> Input: n = 111<br/>
> Output: 1<br/>
> Explanation: (+1) + (-1) + (+1) = 1.

### Example 3:

> Input: n = 886996<br/>
> Output: 0<br/>
> Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.
 
### Constraints:

- 1 <= n <= 109