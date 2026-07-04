---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2492"
title: "Minimum Score of a Path Between Two Cities"
url: "https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Depth-First Search
  - Breadth-First Search
  - Union-Find
  - Graph Theory

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-07-04
date-solved: 2026-07-04
attempts: 2

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "not dijkstra?"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [2492. Minimum Score of a Path Between Two Cities](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities)

Medium

You are given a positive integer n representing n cities numbered from 1 to n. 
You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a **bidirectional** road between cities ai and bi with a distance equal to distancei. 
The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

#### Note:

- A path is a sequence of roads between two cities.
- It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
- The test cases are generated such that there is at least one path between 1 and n.
 

#### Example 1:


> Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
> Output: 5
> Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
> It can be shown that no other path has less score.

#### Example 2:

> Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
> Output: 2
> Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
 

#### Constraints:

- 2 <= n <= 10<sup>5</sup>
- 1 <= roads.length <= 10<sup>5</sup>
- roads[i].length == 3
- 1 <= ai, bi <= n
- ai != bi
- 1 <= distancei <= 10<sup>4</sup>
- There are no repeated edges.
- There is at least one path between 1 and n.