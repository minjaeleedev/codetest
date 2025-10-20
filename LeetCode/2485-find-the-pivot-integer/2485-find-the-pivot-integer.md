---
# Problem Identification
platform: LeetCode
platform-problem-id: "2485"
title: "Find the Pivot Integer"
url: "https://leetcode.com/problems/find-the-pivot-integer/"
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

## 2485. Find the Pivot Integer
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.


### Example 1:

> Input: n = 8<br/>
> Output: 6<br/>
> Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

### Example 2:

> Input: n = 1<br/>
> Output: 1<br/>
> Explanation: 1 is the pivot integer since: 1 = 1.

### Example 3:

> Input: n = 4<br/>
> Output: -1<br/>
> Explanation: It can be proved that no such integer exist.
 
### Constraints:

- 1 <= n <= 1000