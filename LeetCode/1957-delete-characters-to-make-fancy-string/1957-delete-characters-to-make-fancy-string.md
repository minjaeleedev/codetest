---
# Problem Identification
platform: LeetCode
platform-problem-id: "1957"
title: "Delete Characters to Make Fancy String"
url: "https://leetcode.com/problems/delete-characters-to-make-fancy-string/"
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

## 1957. Delete Characters to Make Fancy String

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

### Example 1:

> Input: s = "leeetcode"<br/>
> Output: "leetcode"<br/>
> Explanation:<br/>
> Remove an 'e' from the first group of 'e's to create "leetcode".<br/>
> No three consecutive characters are equal, so return "leetcode".<br/>

### Example 2:

> Input: s = "aaabaaaa"<br/>
> Output: "aabaa"<br/>
> Explanation:<br/>
> Remove an 'a' from the first group of 'a's to create "aabaaaa".<br/>
> Remove two 'a's from the second group of 'a's to create "aabaa".<br/>
> No three consecutive characters are equal, so return "aabaa".<br/>

### Example 3:

> Input: s = "aab"<br/>
> Output: "aab"<br/>
> Explanation: No three consecutive characters are equal, so return "aab".
 
### Constraints:

- 1 <= s.length <= 105
- s consists only of lowercase English letters.