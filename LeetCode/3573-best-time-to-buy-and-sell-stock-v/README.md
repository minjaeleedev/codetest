---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3573"
title: "Best Time to Buy and Sell Stock V"
url: "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Dynamic Programming (DP)

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-12-17
date-solved: 2025-12-17
attempts: 1

# Personal Notes
rating: 6  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2026-01-17  # Auto-managed by review script
review-count: 0
last-reviewed: 2026-01-17
---

## [3573. Best Time to Buy and Sell Stock V](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v)

Medium

You are given an integer array prices where prices[i] is the price of a stock in dollars on the ith day, and an integer k.

You are allowed to make at most k transactions, where each transaction can be either of the following:

Normal transaction: Buy on day i, then sell on a later day j where i < j. You profit prices[j] - prices[i].

Short selling transaction: Sell on day i, then buy back on a later day j where i < j. You profit prices[i] - prices[j].

Note that you must complete each transaction before starting another. Additionally, you can't buy or sell on the same day you are selling or buying back as part of a previous transaction.

Return the maximum total profit you can earn by making at most k transactions.

#### Example 1:

> Input: prices = [1,7,9,8,2], k = 2
> 
> Output: 14
> 
> Explanation:
> 
> We can make $14 of profit through 2 transactions:
> - A normal transaction: buy the stock on day 0 for $1 then sell it on day 2 for $9.
> - A short selling transaction: sell the stock on day 3 for $8 then buy back on day 4 for $2.

#### Example 2:

> Input: prices = [12,16,19,19,8,1,19,13,9], k = 3
> 
> Output: 36
> 
> Explanation:
> 
> We can make $36 of profit through 3 transactions:
> - A normal transaction: buy the stock on day 0 for $12 then sell it on day 2 for $19.
> - A short selling transaction: sell the stock on day 3 for $19 then buy back on day 4 for $8.
> - A normal transaction: buy the stock on day 5 for $1 then sell it on day 6 for $19.
 

#### Constraints:

- 2 <= prices.length <= 10<sup>3</sup>
- 1 <= prices[i] <= 10<sup>9</sup>
- 1 <= k <= prices.length / 2