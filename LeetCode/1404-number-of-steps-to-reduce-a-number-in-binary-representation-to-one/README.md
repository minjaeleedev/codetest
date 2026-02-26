---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1404"
title: "Number of Steps to Reduce a Number in Binary Representation to One"
url: "https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - String
  - Bit Manipulation
  - Simulation

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-02-26
date-solved: 2026-02-26
attempts: 1

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
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

## [1404. Number of Steps to Reduce a Number in Binary Representation to One](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one)

Medium

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

 

#### Example 1:

> Input: s = "1101"
> Output: 6
> Explanation: "1101" corressponds to number 13 in their decimal representation.
> Step 1) 13 is odd, add 1 and obtain 14. 
> Step 2) 14 is even, divide by 2 and obtain 7.
> Step 3) 7 is odd, add 1 and obtain 8.
> Step 4) 8 is even, divide by 2 and obtain 4.  
> Step 5) 4 is even, divide by 2 and obtain 2. 
> Step 6) 2 is even, divide by 2 and obtain 1.  

#### Example 2:

> Input: s = "10"
> Output: 1
> Explanation: "10" corresponds to number 2 in their decimal representation.
> Step 1) 2 is even, divide by 2 and obtain 1.  

#### Example 3:

> Input: s = "1"
> Output: 0
 

#### Constraints:

- 1 <= s.length <= 500
- s consists of characters '0' or '1'
- s[0] == '1'