---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "3397"
title: "Maximum Number of Distinct Elements After Operations"
url: "https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/description"
difficulty: Medium
topics:
  - Array
  - Greedy
  - Sorting

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-10-18
date-solved: 2025-10-18
attempts: 1

# Personal Notes
rating: 5  # 1-10 difficulty rating (personal)
notes: "Deciding first diff is a little tricky"
similar-problems: null

# Review Schedule (for spaced repetition)
next-review: 2025-10-28
review-count: 0
---

## [3397. Maximum Number of Distinct Elements After Operations](https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/description)

Medium

You are given an integer array `nums` and an integer `k`.

You are allowed to perform the following operation on each element of the array **at most** once:

- Add an integer in the range `[-k, k]` to the element.

Return the **maximum** possible number of **distinct** elements in `nums` after performing the operations.

#### Example 1:

> Input: nums = [1,2,2,3,3,4], k = 2
> 
> Output: 6
> 
> Explanation:
> 
> `nums` changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

#### Example 2:

> Input: nums = [4,4,4,4], k = 1
> 
> Output: 3
> 
> Explanation:
> 
> By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].

#### Constraints:

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= k <= 10^9`