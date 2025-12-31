---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1970"
title: "Last Day Where You Can Still Cross"
url: "https://leetcode.com/problems/last-day-where-you-can-still-cross"
difficulty: Hard   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Binary Search
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
  - Union Find
  - Matrix

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-12-31
date-solved: 2025-12-31
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "binary search idea"
similar-problems: 
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: 2026-01-31  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1970. Last Day Where You Can Still Cross](https://leetcode.com/problems/last-day-where-you-can-still-cross)

Hard

There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. 
However, each day a new cell becomes flooded with water. 
You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. 
You can start from any cell in the top row and end at any cell in the bottom row. 
You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

 
#### Example 1:

![image1](./example1.png)

> Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
> Output: 2
> Explanation: The above image depicts how the matrix changes each day starting from day 0.
> The last day where it is possible to cross from top to bottom is on day 2.

#### Example 2:

![image2](./example2.png)

> Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
> Output: 1
> Explanation: The above image depicts how the matrix changes each day starting from day 0.
> The last day where it is possible to cross from top to bottom is on day 1.

#### Example 3:


![image3](./example3.png)

> Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
> Output: 3
> Explanation: The above image depicts how the matrix changes each day starting from day 0.
> The last day where it is possible to cross from top to bottom is on day 3.
 

#### Constraints:

- 2 <= row, col <= 2 * 10<sup>4</sup>
- 4 <= row * col <= 2 * 10<sup>4</sup>
- cells.length == row * col
- 1 <= ri <= row
- 1 <= ci <= col
- All the values of cells are unique.