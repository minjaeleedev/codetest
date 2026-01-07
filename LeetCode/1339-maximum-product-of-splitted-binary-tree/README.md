---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1339"
title: "Maximum Product of Splitted Binary Tree"
url: "https://leetcode.com/problems/maximum-product-of-splitted-binary-tree"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Tree
  - Depth-First Search
  - Binary Tree

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-01-07
date-solved: 2026-01-07
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "one pass dfs"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-02-07  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1339. Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree)

Medium

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. 
Since the answer may be too large, return it modulo 10<sup>9</sup> + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 
#### Example 1:


> Input: root = [1,2,3,4,5,6]
> 
> Output: 110
> 
> Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

#### Example 2:


> Input: root = [1,null,2,3,4,null,null,5,6]
> 
> Output: 90
> 
> Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

#### Constraints:

- The number of nodes in the tree is in the range [2, 5 * 10<sup>4</sup>].
- 1 <= Node.val <= 10<sup>4</sup>