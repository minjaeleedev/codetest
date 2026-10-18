---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "1569"
title: "Number of Ways to Reorder Array to Get Same BST"
url: "https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst"
difficulty: Hard   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Math
  - Divide and Conquer
  - Dynamic Programming
  - Tree
  - Union-Find
  - Binary Search Tree
  - Memoization
  - Combinatorics
  - Binary Tree
  - Fermat's Little Theorem

# Solution Tracking
status: Not Started  # Not Started | Attempted | Solved | Reviewed
date-attempted:
date-solved:
attempts:

# Personal Notes
rating:   # 1-10 difficulty rating (personal)
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

## [1569. Number of Ways to Reorder Array to Get Same BST](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst)

Hard

Given an array nums that represents a permutation of integers from 1 to n. 
We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. 
Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. 
The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 109 + 7.


#### Example 1:

> Input: nums = [2,1,3]
> Output: 1
> Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.

#### Example 2:

> Input: nums = [3,4,5,1,2]
> Output: 5
> Explanation: The following 5 arrays will yield the same BST: 
> [3,1,2,4,5]
> [3,1,4,2,5]
> [3,1,4,5,2]
> [3,4,1,2,5]
> [3,4,1,5,2]

#### Example 3:

> Input: nums = [1,2,3]
> Output: 0
> Explanation: There are no other orderings of nums that will yield the same BST.
 
#### Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
All integers in nums are distinct.