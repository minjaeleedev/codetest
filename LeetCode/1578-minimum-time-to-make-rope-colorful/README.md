---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1578"
title: "Minimum Time to Make Rope Colorful"
url: "https://leetcode.com/problems/minimum-time-to-make-rope-colorful"
difficulty: Medium
topics:
  - Array
  - String
  - Dynamic Programming (DP)
  - Greedy

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-11-03
date-solved: 2025-11-03
attempts: 2

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "dp, greedy, two pointer"
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2025-11-17  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [1578. Minimum Time to Make Rope Colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful)

Medium

Alice has `n` balloons arranged on a rope. 
You are given a 0-indexed string `colors` where colors[i] is the color of the `ith` balloon.

Alice wants the rope to be **colorful**. 
She does not want **two consecutive balloons** to be of the same color, so she asks Bob for help. 
Bob can remove some balloons from the rope to make it **colorful**. 
You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the **minimum time** ***Bob needs to make the rope colorful***.

 

#### Example 1

![image1](./example1.jpg)

> Input: colors = "abaac", neededTime = [1,2,3,4,5]
> 
> Output: 3
> 
> Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
> 
> Bob can remove the blue balloon at index 2. This takes 3 seconds.
> 
> There are no longer two consecutive balloons of the same color. Total time = 3.

#### Example 2

![image2](./example2.jpg)

> Input: colors = "abc", neededTime = [1,2,3]
> 
> Output: 0
> 
> Explanation: The rope is already colorful. 
> Bob does not need to remove any balloons from the rope.

#### Example 3


![image3](./example3.jpg)

> Input: colors = "aabaa", neededTime = [1,2,3,4,1]
> 
> Output: 2
> 
> Explanation: Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
> 
> There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
 
#### Constraints

- `n == colors.length == neededTime.length`
- `1 <= n <= 10^5`
- `1 <= neededTime[i] <= 10^4`
- colors contains only lowercase English letters.