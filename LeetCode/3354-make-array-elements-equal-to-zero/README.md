---
# Problem Identification
platform: LeetCode
platform-problem-id: "3354"
title: "Make Array Elements Equal to Zero"
url: "https://leetcode.com/problems/make-array-elements-equal-to-zero"
difficulty: Easy
topics:
  - Array
  - Simulation
  - Prefix Sum

# Solution Tracking
status: Solved
date-attempted: 2024-11-17
date-solved: 2024-11-17
attempts: 2

# Personal Notes
rating: 3
needs-review: true
tags: []
notes: "two prefix sum"
similar-problems: []

# Review Schedule (for spaced repetition)
next-review: 2025-11-11
review-count: 1
last-reviewed: 2025-10-28
---

## [3354. Make Array Elements Equal to Zero](https://leetcode.com/problems/make-array-elements-equal-to-zero)
Easy
You are given an integer array <code>nums</code>.

<p>Start by selecting a starting position <code>curr</code> such that <code>nums[curr] == 0</code>, and choose a movement <strong>direction</strong> of&nbsp;either left or right.</p>

<p>After that, you repeat the following process:</p>

<ul>
	<li>If <code>curr</code> is out of the range <code>[0, n - 1]</code>, this process ends.</li>
	<li>If <code>nums[curr] == 0</code>, move in the current direction by <strong>incrementing</strong> <code>curr</code> if you are moving right, or <strong>decrementing</strong> <code>curr</code> if you are moving left.</li>
	<li>Else if <code>nums[curr] &gt; 0</code>:
	<ul>
		<li>Decrement <code>nums[curr]</code> by 1.</li>
		<li><strong>Reverse</strong>&nbsp;your movement direction (left becomes right and vice versa).</li>
		<li>Take a step in your new direction.</li>
	</ul>
	</li>
</ul>

<p>A selection of the initial position <code>curr</code> and movement direction is considered <strong>valid</strong> if every element in <code>nums</code> becomes 0 by the end of the process.</p>

<p>Return the number of possible <strong>valid</strong> selections.</p>

#### Example 1

> **Input**: `nums = [1,0,2,0,3]`
> 
> **Output**: 2
> 
> **Explanation**:
> 
> The only possible valid selections are the following:
> - Choose `curr = 3`, and a movement direction to the left.
> 	- `[1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,3] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,0,0,2] -> [1,0,0,0,2] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,0]`.
> - Choose `curr = 3`, and a movement direction to the right.
> 	- `[1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,1,0,1] -> [1,0,1,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0]`.

#### Example 2

> **Input**: nums = [2,3,4,0,4,1,0]
> 
> **Output**: 0
> 
> **Explanation**:
> 
> There are no possible valid selections.

#### Constraints

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
	<li>There is at least one element <code>i</code> where <code>nums[i] == 0</code>.</li>
</ul>
