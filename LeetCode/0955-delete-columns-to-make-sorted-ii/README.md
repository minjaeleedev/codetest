---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "955"
title: "Delete Columns to Make Sorted II"
url: "https://leetcode.com/problems/delete-columns-to-make-sorted-ii"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - String
  - Greedy

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-12-21
date-solved: 2025-12-21
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "greedy, state"
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2026-01-21  # Auto-managed by review script
review-count: 0
last-reviewed: 2026-01-21
---

## [955. Delete Columns to Make Sorted II]()

Medium

You are given an array of n strings strs, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

Suppose we chose a set of deletion indices answer such that after deletions, the final array has its elements in lexicographic order (i.e., strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). Return the minimum possible value of answer.length.

#### Example 1:

> Input: strs = ["ca","bb","ac"]
> 
> Output: 1
> 
> Explanation: 
> 
> After deleting the first column, strs = ["a", "b", "c"].
> 
> Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]).
> 
> We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.

#### Example 2:

> Input: strs = ["xc","yb","za"]
> 
> Output: 0
> 
> Explanation: 
> 
> strs is already in lexicographic order, so we do not need to delete anything.
> 
> Note that the rows of strs are not necessarily in lexicographic order:
> 
> i.e., it is NOT necessarily true that (strs[0][0] <= strs[0][1] <= ...)

#### Example 3:

> Input: strs = ["zyx","wvu","tsr"]
> 
> Output: 3
>
> Explanation: We have to delete every column.
 
#### Constraints:

- `n == strs.length`
- 1 <= n <= 100
- 1 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.