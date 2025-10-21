---
# Problem Identification
platform: LeetCode
platform-problem-id: "2733"
title: "Neither Minimum nor Maximum"
url: "https://leetcode.com/problems/neither-minimum-nor-maximum/"
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

## 2733. Neither Minimum nor Maximum

Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

Return the selected integer.

### Example 1:

> Input: nums = [3,2,1,4]</br>
> Output: 2</br>
> Explanation: In this example, the minimum value is 1 and the maximum value is 4.</br>
> Therefore, either 2 or 3 can be valid answers.</br>

### Example 2:

> Input: nums = [1,2]
> Output: -1
> Explanation: Since there is no number in nums that is neither the maximum nor the minimum, we cannot select a number that satisfies the given condition.</br>
> Therefore, there is no answer.

### Example 3:

> Input: nums = [2,1,3]
> Output: 2
> Explanation: Since 2 is neither the maximum nor the minimum value in nums, it is the only valid answer.

### Constraints:

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- All values in nums are distinct
