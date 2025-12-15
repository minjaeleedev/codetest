---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2110"
title: "Number of Smooth Descent Periods of a Stock"
url: "https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Math
  - Dynamic Programming (DP)

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-12-15
date-solved: 2025-12-15
attempts: 1

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2026-01-15  # Auto-managed by review script
review-count: 0
last-reviewed: 2026-01-15
---

## [2110. Number of Smooth Descent Periods of a Stock](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock)

Medium

You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

Return the number of smooth descent periods.

 
#### Example 1:

> Input: prices = [3,2,1,4]
> 
> Output: 7
> 
> Explanation: There are 7 smooth descent periods:
> 
> [3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
> 
> Note that a period with one day is a smooth descent period by the definition.

#### Example 2:

> Input: prices = [8,6,7,7]
> 
> Output: 4
> 
> Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]
> 
> Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.

#### Example 3:

> Input: prices = [1]
> 
> Output: 1
> 
> Explanation: There is 1 smooth descent period: [1]
 

#### Constraints:

- 1 <= prices.length <= 10<sup>5</sup>
- 1 <= prices[i] <= 10<sup>5</sup>