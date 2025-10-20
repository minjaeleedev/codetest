---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2011"
title: "Final Value of Variable After Performing Operations"
url: "https://leetcode.com/problems/final-value-of-variable-after-performing-operations"
difficulty: Easy
topics:
  - Array
  - String
  - Simulation

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-10-20
date-solved: 2025-10-20
attempts: 1

# Personal Notes
rating: 1  # 1-10 difficulty rating (personal)
notes: null
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: null # null : no need for review
review-count: 0
---

## [2011. Final Value of Variable After Performing Operations](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description)

Easy

There is a programming language with only **four** operations and **one** variable X:

- `++X` and `X++` increments the value of the variable X by 1.
- `--X` and `X--` decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

#### Example 1:

> Input: operations = ["--X","X++","X++"]
> Output: 1
> Explanation: The operations are performed as follows:
> Initially, X = 0.
> --X: X is decremented by 1, X =  0 - 1 = -1.
> X++: X is incremented by 1, X = -1 + 1 =  0.
> X++: X is incremented by 1, X =  0 + 1 =  1.

#### Example 2:

> Input: operations = ["++X","++X","X++"]
> Output: 3
> Explanation: The operations are performed as follows:
> Initially, X = 0.
> ++X: X is incremented by 1, X = 0 + 1 = 1.
> ++X: X is incremented by 1, X = 1 + 1 = 2.
> X++: X is incremented by 1, X = 2 + 1 = 3.

#### Example 3:

> Input: operations = ["X++","++X","--X","X--"]
> Output: 0
> Explanation: The operations are performed as follows:
> Initially, X = 0.
> X++: X is incremented by 1, X = 0 + 1 = 1.
> ++X: X is incremented by 1, X = 1 + 1 = 2.
> --X: X is decremented by 1, X = 2 - 1 = 1.
> X--: X is decremented by 1, X = 1 - 1 = 0.
 
#### Constraints:

- `1 <= operations.length <= 100`
- operations[i] will be either `"++X"`, `"X++"`, `"--X"`, or `"X--"`.