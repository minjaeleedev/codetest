---
# Problem Identification
platform: LeetCode
platform-problem-id: "1752"
title: "Check if Array Is Sorted and Rotated"
url: "https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/"
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

## 1752. Check if Array Is Sorted and Rotated
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

### Example 1:

> Input: nums = [3,4,5,1,2]<br/>
> Output: true<br/>
> Explanation: [1,2,3,4,5] is the original sorted array.<br/>
> You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

### Example 2:

> Input: nums = [2,1,3,4]<br/>
> Output: false<br/>
> Explanation: There is no sorted array once rotated that can make nums.

### Example 3:

> Input: nums = [1,2,3]<br/>
> Output: true<br/>
> Explanation: [1,2,3] is the original sorted array.<br/>
> You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
 
### Constraints:

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100