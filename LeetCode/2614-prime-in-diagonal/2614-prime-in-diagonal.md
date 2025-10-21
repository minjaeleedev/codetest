---
# Problem Identification
platform: LeetCode
platform-problem-id: "2614"
title: "Prime In Diagonal"
url: "https://leetcode.com/problems/prime-in-diagonal/"
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

## 2614. Prime In Diagonal
You are given a 0-indexed two-dimensional integer array nums.

Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of the diagonals, return 0.

Note that:

- An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
- An integer val is on one of the diagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val.


In the above diagram, one diagonal is [1,5,9] and another diagonal is [3,5,7].

### Example 1:

> Input: nums = [[1,2,3],[5,6,7],[9,10,11]]<br/>
> Output: 11<br/>
> Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11.

### Example 2:

> Input: nums = [[1,2,3],[5,17,7],[9,11,10]]<br/>
> Output: 17<br/>
> Explanation: The numbers 1, 3, 9, 10, and 17 are all present on at least one of the diagonals. 17 is the largest prime, so we return 17.
 
### Constraints:

- 1 <= nums.length <= 300
- nums.length == numsi.length
- 1 <= nums[i][j] <= 4*106