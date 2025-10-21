---
# Problem Identification
platform: LeetCode
platform-problem-id: "2582"
title: "Pass the Pillow"
url: "https://leetcode.com/problems/pass-the-pillow/"
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

## 2582. Pass the Pillow
There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

### Example 1:

> Input: n = 4, time = 5<br/>
> Output: 2<br/>
> Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.<br/>
> After five seconds, the 2nd person is holding the pillow.

### Example 2:

> Input: n = 3, time = 2<br/>
> Output: 3<br/>
> Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.<br/>
> After two seconds, the 3rd person is holding the pillow.
 
### Constraints:

- 2 <= n <= 1000
- 1 <= time <= 1000

### Topics

- Math
- Simulation
