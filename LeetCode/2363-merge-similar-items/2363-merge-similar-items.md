---
# Problem Identification
platform: LeetCode
platform-problem-id: "2363"
title: "Merge Similar Items"
url: "https://leetcode.com/problems/merge-similar-items/"
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

### 2363. Merge Similar Items
You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:

- items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
- The value of each item in items is unique.
 
Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.

Note: ret should be returned in ascending order by value.

### Example 1:

> Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]<br/>
> Output: [[1,6],[3,9],[4,5]]<br/>
> Explanation: <br/>
> The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.<br/>
> The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.<br/>
> The item with value = 4 occurs in items1 with weight = 5, total weight = 5.  <br/>
> Therefore, we return [[1,6],[3,9],[4,5]].

### Example 2:

> Input: items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]<br/>
> Output: [[1,4],[2,4],[3,4]]<br/>
> Explanation: <br/>
> The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 3, total weight = 1 + 3 = 4.<br/>
> The item with value = 2 occurs in items1 with weight = 3 and in items2 with weight = 1, total weight = 3 + 1 = 4.<br/>
> The item with value = 3 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4.<br/>
> Therefore, we return [[1,4],[2,4],[3,4]].

### Example 3:

> Input: items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]<br/>
> Output: [[1,7],[2,4],[7,1]]<br/>
> Explanation:<br/>
> The item with value = 1 occurs in items1 with weight = 3 and in items2 with weight = 4, total weight = 3 + 4 = 7. <br/>
> The item with value = 2 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4. <br/>
> The item with value = 7 occurs in items2 with weight = 1, total weight = 1.<br/>
> Therefore, we return [[1,7],[2,4],[7,1]].

### Constraints:

- 1 <= items1.length, items2.length <= 1000
- items1[i].length == items2[i].length == 2
- 1 <= valuei, weighti <= 1000
- Each valuei in items1 is unique.
- Each valuei in items2 is unique.