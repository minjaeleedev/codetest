---
# Problem Identification
platform: LeetCode
platform-problem-id: "2535"
title: "Difference Between Element Sum and Digit Sum of an Array"
url: "https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/"
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

## 2535. Difference Between Element Sum and Digit Sum of an Array

You are given a positive integer array nums.

- The element sum is the sum of all the elements in nums.
- The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.

Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.

### Example 1:

> Input: nums = [1,15,6,3]<br/>
> Output: 9<br/>
> Explanation:<br/>
> The element sum of nums is 1 + 15 + 6 + 3 = 25.</br>
> The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.</br>
> The absolute difference between the element sum and digit sum is |25 - 16| = 9.

### Example 2:

> Input: nums = [1,2,3,4]</br>
> Output: 0</br>
> Explanation:</br>
> The element sum of nums is 1 + 2 + 3 + 4 = 10.</br>
> The digit sum of nums is 1 + 2 + 3 + 4 = 10.</br>
> The absolute difference between the element sum and digit sum is |10 - 10| = 0.

### Constraints:

- 1 <= nums.length <= 2000
- 1 <= nums[i] <= 2000
