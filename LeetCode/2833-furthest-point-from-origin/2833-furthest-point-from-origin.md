---
# Problem Identification
platform: LeetCode
platform-problem-id: "2833"
title: "Furthest Point From Origin"
url: "https://leetcode.com/problems/furthest-point-from-origin/"
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

## 2833. Furthest Point From Origin

You are given a string moves of length n consisting only of characters 'L', 'R', and '\_'. The string represents your movement on a number line starting from the origin 0.

In the ith move, you can choose one of the following directions:

- move to the left if moves[i] = 'L' or moves[i] = '\_'
- move to the right if moves[i] = 'R' or moves[i] = '\_'

Return the distance from the origin of the furthest point you can get to after n moves.

### Example 1:

> Input: moves = "L_RL\_\_R"</br>
> Output: 3</br>
> Explanation: The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves "LLRLLLR".

### Example 2:

> Input: moves = "_R\_\_LL_"</br>
> Output: 5</br>
> Explanation: The furthest point we can reach from the origin 0 is point -5 through the following sequence of moves "LRLLLLL".

### Example 3:

> Input: moves = "**\_\_\_**"
> Output: 7
> Explanation: The furthest point we can reach from the origin 0 is point 7 through the following sequence of moves "RRRRRRR".

### Constraints:

- 1 <= moves.length == n <= 50
- moves consists only of characters 'L', 'R' and '\_'.
