---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3116"
title: ""
url: ""
difficulty:   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  -

# Solution Tracking
status: Not Started  # Not Started | Attempted | Solved | Reviewed
date-attempted:
date-solved:
attempts:

# Personal Notes
rating:   # 1-10 difficulty rating (personal)
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

## [3116. Kth Smallest Amount With Single Denomination Combination](https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination)

Hard

You are given an integer array coins representing coins of different denominations and an integer k.

You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.

Return the kth smallest amount that can be made using these coins.

 
Example 1:

Input: coins = [3,6,9], k = 3

Output: 9

Explanation: The given coins can make the following amounts:
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
All of the coins combined produce: 3, 6, 9, 12, 15, etc.

Example 2:

Input: coins = [5,2], k = 7

Output: 12

Explanation: The given coins can make the following amounts:
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.

 

Constraints:

1 <= coins.length <= 15
1 <= coins[i] <= 25
1 <= k <= 2 * 109
coins contains pairwise distinct integers.