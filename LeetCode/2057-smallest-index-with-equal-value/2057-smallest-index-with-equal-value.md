---
# Problem Identification
platform: LeetCode
platform-problem-id: "2057"
title: "Smallest Index With Equal Value"
url: "https://leetcode.com/problems/smallest-index-with-equal-value/"
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

## 2057. Smallest Index With Equal Value

Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.

x mod y denotes the remainder when x is divided by y.

### Example 1:

> Input: nums = [0,1,2]<br/>
> Output: 0<br/>
> Explanation:<br/>
> i=0: 0 mod 10 = 0 == nums[0].<br/>
> i=1: 1 mod 10 = 1 == nums[1].<br/>
> i=2: 2 mod 10 = 2 == nums[2].<br/>
> All indices have i mod 10 == nums[i], so we return the smallest index 0.

### Example 2:

> Input: nums = [4,3,2,1]<br/>
> Output: 2<br/>
> Explanation:<br/>
> i=0: 0 mod 10 = 0 != nums[0].<br/>
> i=1: 1 mod 10 = 1 != nums[1].<br/>
> i=2: 2 mod 10 = 2 == nums[2].<br/>
> i=3: 3 mod 10 = 3 != nums[3].<br/>
> 2 is the only index which has i mod 10 == nums[i].<br/>

### Example 3:

> Input: nums = [1,2,3,4,5,6,7,8,9,0]<br/>
> Output: -1<br/>
> Explanation: No index satisfies i mod 10 == nums[i].

### Constraints:

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 9
