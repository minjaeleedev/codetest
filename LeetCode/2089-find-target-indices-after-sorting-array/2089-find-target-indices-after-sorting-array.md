---
# Problem Identification
platform: LeetCode
platform-problem-id: "2089"
title: "Find Target Indices After Sorting Array"
url: "https://leetcode.com/problems/find-target-indices-after-sorting-array/"
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

## 2089. Find Target Indices After Sorting Array
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

### Example 1:

> Input: nums = [1,2,5,2,3], target = 2<br/>
> Output: [1,2]<br/>
> Explanation: After sorting, nums is [1,2,2,3,5].<br/>
> The indices where nums[i] == 2 are 1 and 2.

### Example 2:

> Input: nums = [1,2,5,2,3], target = 3<br/>
> Output: [3]<br/>
> Explanation: After sorting, nums is [1,2,2,3,5].<br/>
> The index where nums[i] == 3 is 3.

### Example 3:

> Input: nums = [1,2,5,2,3], target = 5<br/>
> Output: [4]<br/>
> Explanation: After sorting, nums is [1,2,2,3,5].<br/>
> The index where nums[i] == 5 is 4.
 

### Constraints:

- 1 <= nums.length <= 100
- 1 <= nums[i], target <= 100