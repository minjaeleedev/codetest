---
# Problem Identification
platform: LeetCode
platform-problem-id: "1935"
title: "Maximum Number of Words You Can Type"
url: "https://leetcode.com/problems/maximum-number-of-words-you-can-type/"
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

## 1935. Maximum Number of Words You Can Type

There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

### Example 1:

> Input: text = "hello world", brokenLetters = "ad"<br/>
> Output: 1<br/>
> Explanation: We cannot type "world" because the 'd' key is broken.

### Example 2:

> Input: text = "leet code", brokenLetters = "lt"<br/>
> Output: 1<br/>
> Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.

### Example 3:

> Input: text = "leet code", brokenLetters = "e"<br/>
> Output: 0<br/>
> Explanation: We cannot type either word because the 'e' key is broken.
 
### Constraints:

- 1 <= text.length <= 104
- 0 <= brokenLetters.length <= 26
- text consists of words separated by a single space without any leading or trailing spaces.
- Each word only consists of lowercase English letters.
- brokenLetters consists of distinct lowercase English letters.