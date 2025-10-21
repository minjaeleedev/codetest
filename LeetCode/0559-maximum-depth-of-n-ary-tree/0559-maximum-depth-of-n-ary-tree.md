---
# Problem Identification
platform: LeetCode
platform-problem-id: "559"
title: "Maximum Depth of N-ary Tree"
url: "https://leetcode.com/problems/maximum-depth-of-n-ary-tree/"
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

## 559. Maximum Depth of N-ary Tree
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

### Example 1:

![](./image1.png)

> Input: root = [1,null,3,2,4,null,5,6]<br/>
> Output: 3

### Example 2:

![](./image2.png)

> Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]<br/>
> Output: 5
 

### Constraints:

- The total number of nodes is in the range [0, 104].
- The depth of the n-ary tree is less than or equal to 1000.

### Topics

- Tree
- Depth-First Search
- Breadth-First Search