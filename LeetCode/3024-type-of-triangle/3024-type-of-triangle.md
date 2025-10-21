---
# Problem Identification
platform: LeetCode
platform-problem-id: "3024"
title: "Type of Triangle"
url: "https://leetcode.com/problems/type-of-triangle/"
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

## 3024. Type of Triangle
You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.
Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

### Example 1:

> Input: nums = [3,3,3]<br/>
> Output: "equilateral"<br/>
> Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.

### Example 2:

> Input: nums = [3,4,5]<br/>
> Output: "scalene"<br/>
> Explanation: <br/>
> nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.<br/>
> nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.<br/>
> nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. <br/>
> Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.<br/>
> As all the sides are of different lengths, it will form a scalene triangle.

### Constraints:

- nums.length == 3
- 1 <= nums[i] <= 100