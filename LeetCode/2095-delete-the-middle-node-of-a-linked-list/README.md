---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2095"
title: "Delete the Middle Node of a Linked List"
url: "https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Linked List
  - Two Pointers

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-06-15
date-solved: 2026-06-15
attempts: 1

# Personal Notes
rating: 4  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "fast, slow"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [2095. Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list)

Medium

You are given the head of a linked list. 
Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

#### Example 1:


> Input: head = [1,3,4,7,1,2,6]
> Output: [1,3,4,1,2,6]
> Explanation:
> The above figure represents the given linked list. The indices of the nodes are written below.
> Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
> We return the new list after removing this node. 

#### Example 2:

> Input: head = [1,2,3,4]
> Output: [1,2,4]
> Explanation:
> The above figure represents the given linked list.
> For n = 4, node 2 with value 3 is the middle node, which is marked in red.

#### Example 3:


> Input: head = [2,1]
> Output: [2]
> Explanation:
> The above figure represents the given linked list.
> For n = 2, node 1 with value 1 is the middle node, which is marked in red.
> Node 0 with value 2 is the only node remaining after removing node 1.
 

#### Constraints:

- The number of nodes in the list is in the range [1, 10<sup>5</sup>].
- 1 <= Node.val <= 10<sup>5</sup>