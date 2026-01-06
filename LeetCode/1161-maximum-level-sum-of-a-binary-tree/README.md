---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1161"
title: "Maximum Level Sum of a Binary Tree"
url: "https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Tree
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
  - Binary Tree

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-01-06
date-solved: 2026-01-06
attempts: 1

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1161. Maximum Level Sum of a Binary Tree]()

Medium

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

#### Example 1:


> Input: root = [1,7,0,7,-8,null,null]
> Output: 2
> Explanation: 
> - Level 1 sum = 1.
> - Level 2 sum = 7 + 0 = 7.
> - Level 3 sum = 7 + -8 = -1.
> So we return the level with the maximum sum which is level 2.

#### Example 2:

> Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
> Output: 2
 

#### Constraints:

- The number of nodes in the tree is in the range [1, 10<sup>4</sup>].
- -10<sup>5</sup> <= Node.val <= 10<sup>5</sup>