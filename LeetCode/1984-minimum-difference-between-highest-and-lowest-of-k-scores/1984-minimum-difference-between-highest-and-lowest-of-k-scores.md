---
# Problem Identification
platform: LeetCode
platform-problem-id: "1984"
title: "Minimum Difference Between Highest and Lowest of K Scores"
url: "https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/"
difficulty: None
topics:
  - Array
  - Sliding Window
  - Sorting

# Solution Tracking
status: Solved
date-attempted: 2026-01-25
date-solved: 2026-01-25
attempts: 1

# Personal Notes
rating: 2
needs-review: false
tags: []
notes: ""
similar-problems: []

# Review Schedule (for spaced repetition)
next-review: null
review-count: 0
last-reviewed: null
---

## 1984. Minimum Difference Between Highest and Lowest of K Scores
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.

### Example 1:

> Input: nums = [90], k = 1<br/>
> Output: 0<br/>
> Explanation: There is one way to pick score(s) of one student:<br/>
> - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
> The minimum possible difference is 0.

### Example 2:

> Input: nums = [9,4,1,7], k = 2<br/>
> Output: 2<br/>
> Explanation: There are six ways to pick score(s) of two students:<br/>
> - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
> - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
> - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
> - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
> - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
> - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
> The minimum possible difference is 2.
 

### Constraints:

- 1 <= k <= nums.length <= 1000
- 0 <= nums[i] <= 105