---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3531"
title: "Count Covered Buildings"
url: "https://leetcode.com/problems/count-covered-buildings"
difficulty:   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Hash Table
  - Sorting

# Solution Tracking
status: Not Started  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-12-11
date-solved: 2025-12-11
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

## [3531. Count Covered Buildings](https://leetcode.com/problems/count-covered-buildings)

Medium

You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

A building is covered if there is at least one building in all four directions: left, right, above, and below.

Return the number of covered buildings.

 
#### Example 1:


![example1](./example1.jpg)

> Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
> 
> Output: 1
> 
> Explanation:
> 
> - Only building [2,2] is covered as it has at least one building:
>   - above ([1,2])
>   - below ([3,2])
>   - left ([2,1])
>   - right ([2,3])
> - Thus, the count of covered buildings is 1.

#### Example 2:


![example2](./example2.jpg)

> Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]
> 
> Output: 0
> 
> Explanation:
> 
> No building has at least one building in all four directions.

#### Example 3:

![example3](./example3.jpg)

> Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]
> 
> Output: 1
> 
> Explanation:
> 
> - Only building [3,3] is covered as it has at least one building:
>   - above ([1,3])
>   - below ([5,3])
>   - left ([3,2])
>   - right ([3,5])
> - Thus, the count of covered buildings is 1.
 

#### Constraints:

- 2 <= n <= 10<sup>5</sup>
- 1 <= buildings.length <= 10<sup>5</sup>
- buildings[i] = [x, y]
- 1 <= x, y <= n
- All coordinates of buildings are unique.