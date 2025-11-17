---
platform: LeetCode
platform-problem-id: "1437"
title: "Check If All 1's Are at Least Length K Places Away"
url: "https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/"
difficulty: Easy
topics:
  - Array

# Solution Tracking
status: Solved
date-attempted: 2025-11-17
date-solved: 2025-11-17
attempts: 1

# Personal Notes
rating: 2
needs-review: false
tags: []
notes: "array"
similar-problems: []

# Review Schedule (for spaced repetition)
next-review: null
review-count: 0
last-reviewed: null
---

## [1437. Check If All 1's Are at Least Length K Places Away](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away)

Easy
Given an binary array `nums` and an integer `k`, return `true` if all `1`'s are at least `k` places away from each other, otherwise return `false`.

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png" style="width: 428px; height: 181px;">
<pre><strong>Input:</strong> nums = [1,0,0,0,1,0,0,1], k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> Each of the 1s are at least 2 places away from each other.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png" style="width: 320px; height: 173px;">
<pre><strong>Input:</strong> nums = [1,0,0,1,0,1], k = 2
<strong>Output:</strong> false
<strong>Explanation:</strong> The second 1 and third 1 are only one apart from each other.
</pre>


#### Constraints

- 1 <= nums.length <= 10<sup>5</sup>
- `0 <= k <= nums.length`
- `nums[i]` is `0` or `1`