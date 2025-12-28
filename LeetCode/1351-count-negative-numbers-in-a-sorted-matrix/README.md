---
# Problem Identification
platform: LeetCode
platform-problem-id: "1351"
title: "Count Negative Numbers in a Sorted Matrix"
url: "https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix"
difficulty: Easy
topics:
  - Array
  - Binary Search
  - Matrix

# Solution Tracking
status: Solved
date-attempted: 2025-12-28
date-solved: 2025-12-28
attempts: 1

# Personal Notes
rating: 3
needs-review: false
tags: []
notes: "binary search, or exploit non-increasing property"
similar-problems: []

# Review Schedule (for spaced repetition)
next-review: null
review-count: 0
last-reviewed: null
---

## [1351. Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix)

Easy

<p>Given a <code>m x n</code> matrix <code>grid</code> which is sorted in non-increasing order both row-wise and column-wise, return <em>the number of <strong>negative</strong> numbers in</em> <code>grid</code>.
</p>

#### Example 1

<pre><strong>Input:</strong> grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> There are 8 negatives number in the matrix.
</pre>

#### Example 2

<pre><strong>Input:</strong> grid = [[3,2],[1,0]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-100 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>

#### Follow up 
Could you find an `O(n + m)` solution?