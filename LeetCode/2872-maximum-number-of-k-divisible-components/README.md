---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2872"
title: "Maximum Number of K-Divisible Components"
url: "https://leetcode.com/problems/maximum-number-of-k-divisible-components"
difficulty: Hard   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Tree
  - Depth-First Search

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-28
date-solved: 2025-11-28
attempts: 1

# Personal Notes
rating: 6  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "dfs"
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2025-12-29  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [2872. Maximum Number of K-Divisible Components]()

Hard

There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node, and an integer k.

A valid split of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by k, where the value of a connected component is the sum of the values of its nodes.

Return the maximum number of components in any valid split.


#### Example 1:

![image1](./example1.jpg)

> Input: n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
> Output: 2
> Explanation: We remove the edge connecting node 1 with 2. The resulting split is valid because:
> - The value of the component containing nodes 1 and 3 is values[1] + values[3] = 12.
> - The value of the component containing nodes 0, 2, and 4 is values[0] + values[2] + values[4] = 6.
> It can be shown that no other valid split has more than 2 connected components.

#### Example 2:


![image2](./example2.jpg)

> Input: n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3
> Output: 3
> Explanation: We remove the edge connecting node 0 with 2, and the edge connecting node 0 with 1. The resulting split is valid because:
> - The value of the component containing node 0 is values[0] = 3.
> - The value of the component containing nodes 2, 5, and 6 is values[2] + values[5] + values[6] = 9.
> - The value of the component containing nodes 1, 3, and 4 is values[1] + values[3] + values[4] = 6.
> It can be shown that no other valid split has more than 3 connected components.
 

#### Constraints:

- 1 <= n <= 3 * 10<sup>4</sup>
- edges.length == n - 1
- edges[i].length == 2
- 0 <= ai, bi < n
- values.length == n
- 0 <= values[i] <= 10<sup>9</sup>
- 1 <= k <= 10<sup>9</sup>
- Sum of values is divisible by k.
- The input is generated such that edges represents a valid tree.