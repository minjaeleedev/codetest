---
platform: LeetCode  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "2054"
title: "Two Best Non-Overlapping Events"
url: "https://leetcode.com/problems/two-best-non-overlapping-events"
difficulty: Medium   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Array
  - Binary Search
  - Dynamic Programming (DP)
  - Sorting
  - Heap (Priority Queue)

# Solution Tracking
status: Attempted  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2025-12-23
date-solved: 2025-12-23
attempts: 1

# Personal Notes
rating: 6  # 1-10 difficulty rating (personal)
needs-review: true  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: "line sweeping problems"
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## [2054. Two Best Non-Overlapping Events](https://leetcode.com/problems/two-best-non-overlapping-events)

Medium

You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

 

#### Example 1:

Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.

#### Example 2:

Example 1 Diagram
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.

#### Example 3:

Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
 
#### Constraints:

- 2 <= events.length <= 10<sup>5</sup>
- events[i].length == 3
- 1 <= startTimei <= endTimei <= 10<sup>9</sup>
- 1 <= valuei <= 10<sup>6</sup>