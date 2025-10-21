---
# Problem Identification
platform: LeetCode
platform-problem-id: "2248"
title: "Intersection of Multiple Arrays"
url: "https://leetcode.com/problems/intersection-of-multiple-arrays/"
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

## 2248. Intersection of Multiple Arrays
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, 
return the list of integers that are present in each array of nums sorted in ascending order.

### Example 1:

> Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]<br/>
> Output: [3,4]<br/>
> Explanation: <br/>
> The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].

### Example 2:

> Input: nums = [[1,2,3],[4,5,6]]<br/>
> Output: []<br/>
> Explanation: <br/>
> There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
 
### Constraints:

- 1 <= nums.length <= 1000
- 1 <= sum(nums[i].length) <= 1000
- 1 <= nums[i][j] <= 1000
- All the values of nums[i] are unique.