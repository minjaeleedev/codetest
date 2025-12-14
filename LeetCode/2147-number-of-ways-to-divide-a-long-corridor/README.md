---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2147"
title: "Number of Ways to Divide a Long Corridor"
url: "https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor"
difficulty: Hard   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Math
  - String
  - Dynamic Programming(DP)

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-12-14
date-solved: 2025-12-14
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "combinatoric approach is medium difficulty, dp approach is hard"
similar-problems:
  - platform: LeetCode
    id: "639"

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [2147. Number of Ways to Divide a Long Corridor](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor)

Hard

Hint
Along a long library corridor, there is a line of seats and decorative plants. 
You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has **already** been installed to the left of index 0, and another to the right of index n - 1. 
Additional room dividers can be installed. 
For each position between indices i - 1 and i (`1 <= i <= n - 1`), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has **exactly two seats** with any number of plants. 
There may be multiple ways to perform the division. 
Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo <code>10<sup>9</sup> + 7</code>. If there is no way, return 0.

 

#### Example 1:

![example1](./example1.png)

> Input: corridor = "SSPPSPS"
> 
> Output: 3
> 
> Explanation: There are 3 different ways to divide the corridor.
> 
> The black bars in the above image indicate the two room dividers already installed.
> 
> Note that in each of the ways, each section has exactly two seats.

#### Example 2:

![example2](./example2.png)

> Input: corridor = "PPSPSP"
> 
> Output: 1
> 
> Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers.
> 
> Installing any would create some section that does not have exactly two seats.

#### Example 3:

![example3](./example3.png)

> Input: corridor = "S"
> 
> Output: 0
> 
> Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.
 

#### Constraints:

- n == corridor.length
- 1 <= n <= 10<sup>5</sup>
- corridor[i] is either 'S' or 'P'.