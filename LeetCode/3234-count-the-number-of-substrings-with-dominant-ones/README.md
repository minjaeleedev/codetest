---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3234"
title: "Count the Number of Substrings With Dominant Ones"
url: "https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - String
  - Sliding Window
  - Enumeration

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-15
date-solved: 2025-11-15
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "O(n sqrt n)"
similar-problems:
  - platform: LeetCode
    id: "696"

# Review Schedule (for spaced repetition)
next-review: 2025-12-16  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [3234. Count the Number of Substrings With Dominant Ones](https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones)

Medium

You are given a binary string s.

Return the number of substrings with dominant ones.

A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

 
#### Example 1:

> Input: s = "00011"
> 
> Output: 5
> 
> Explanation:
> 
> The substrings with dominant ones are shown in the table below.
> 
> | i	| j	  | s[i..j]	| Number of Zeros |	Number of Ones |
> | --- | --- | ------- | --------------- | -------------- |
> | 3	| 3	  | 1	    | 0	              | 1              | 
> | 4	| 4	  | 1	    | 0	              | 1              | 
> | 2	| 3	  | 01	    | 1	              | 1              | 
> | 3	| 4	  | 11	    | 0	              | 2              |
> | 2	| 4	  | 011	    | 1	              | 2              | 

#### Example 2

> Input: s = "101101"
> 
> Output: 16
> 
> Explanation:
> 
> The substrings with non-dominant ones are shown in the table below.
> 
> Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.
> 
> | i	| j	  | s[i..j]	| Number of Zeros | Number of Ones |
> | --- | --- | ------- | --------------- | -------------- |
> | 1	| 1	  | 0	    | 1	              | 0              |
> | 4	| 4	  | 0	    | 1	              | 0              |
> | 1	| 4	  | 0110	| 2	              | 2              |
> | 0	| 4	  | 10110	| 2	              | 3              | 
> | 1	| 5	  | 01101	| 2	              | 3              |
 

#### Constraints

- `1 <= s.length <= 4 * 10^4`
- `s` consists only of characters '0' and '1'.