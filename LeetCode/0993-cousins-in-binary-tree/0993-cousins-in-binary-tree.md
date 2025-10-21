---
# Problem Identification
platform: LeetCode
platform-problem-id: "993"
title: "Cousins in Binary Tree"
url: "https://leetcode.com/problems/cousins-in-binary-tree/"
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

## 993. Cousins in Binary Tree
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

### Example 1:

![](image1.png)
> Input: root = [1,2,3,4], x = 4, y = 3<br/>
> Output: false

### Example 2:

![](image2.png)
> Input: root = [1,2,3,null,4,null,5], x = 5, y = 4<br/>
> Output: true

### Example 3:

![](image3.png)
> Input: root = [1,2,3,null,4], x = 2, y = 3<br/>
> Output: false

### Constraints:

- The number of nodes in the tree is in the range [2, 100].
- 1 <= Node.val <= 100
- Each node has a unique value.
- x != y
- x and y are exist in the tree.

### Topics

- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree

###

BFS로 풀면 depth 같게 루프 돌 수 있음