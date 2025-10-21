---
# Problem Identification
platform: LeetCode
platform-problem-id: "2540"
title: "Minimum Common Value"
url: "https://leetcode.com/problems/minimum-common-value/"
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

## 2540. Minimum Common Value
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

### Example 1:

> Input: nums1 = [1,2,3], nums2 = [2,4]<br/>
> Output: 2<br/>
> Explanation: The smallest element common to both arrays is 2, so we return 2.

### Example 2:

> Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]<br/>
> Output: 2<br/>
> Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

### Constraints:

- 1 <= nums1.length, nums2.length <= 105
- 1 <= nums1[i], nums2[j] <= 109
- Both nums1 and nums2 are sorted in non-decreasing order.

### Topics

- Array
- Hash Table
- Two Pointers
- Binary Search