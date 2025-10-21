---
# Problem Identification
platform: LeetCode
platform-problem-id: "3264"
title: "Final Array State After K Multiplication Operations I"
url: "https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/"
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

## 3264. Final Array State After K Multiplication Operations I
You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.

### Example 1:

> Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
> 
> Output: [8,4,6,5,6]
> 
> Explanation:
> 
> Operation	Result<br/>
> After operation 1	[2, 2, 3, 5, 6]<br/>
> After operation 2	[4, 2, 3, 5, 6]<br/>
> After operation 3	[4, 4, 3, 5, 6]<br/>
> After operation 4	[4, 4, 6, 5, 6]<br/>
> After operation 5	[8, 4, 6, 5, 6]<br/>

### Example 2:

> Input: nums = [1,2], k = 3, multiplier = 4
> 
> Output: [16,8]
> 
> Explanation:
> 
> Operation	Result<br/>
> After operation 1	[4, 2]<br/>
> After operation 2	[4, 8]<br/>
> After operation 3	[16, 8]<br/>
 

### Constraints:

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= k <= 10
- 1 <= multiplier <= 5

### Topics

- Array
- Math
- Heap (Priority Queue)
- Simulation
