---
# Problem Identification
platform: LeetCode
platform-problem-id: "2553"
title: "Separate The Digits In An Array"
url: "https://leetcode.com/problems/separate-the-digits-in-an-array/"
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

## 2553 separate the digits in an array

Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.

To separate the digits of an integer is to get all the digits it has in the same order.

For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].

### Example 1:

> Input: nums = [13,25,83,77]<br/>
> Output: [1,3,2,5,8,3,7,7]<br/>
> Explanation:<br/>
>
> - The separation of 13 is [1,3].
> - The separation of 25 is [2,5].
> - The separation of 83 is [8,3].
> - The separation of 77 is [7,7].<br/>
>   answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.

### Example 2:

> Input: nums = [7,1,3,9]<br/>
> Output: [7,1,3,9]<br/>
> Explanation: The separation of each integer in nums is itself.<br/>
> answer = [7,1,3,9].

### Constraints:

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 105
