---
# Problem Identification
platform: LeetCode
platform-problem-id: "2062"
title: "Count Vowel Substrings of a String"
url: "https://leetcode.com/problems/count-vowel-substrings-of-a-string/"
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

## 2062. Count Vowel Substrings of a String
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

### Example 1:

> Input: word = "aeiouu"<br/>
> Output: 2<br/>
> Explanation: The vowel substrings of word are as follows (underlined):<br/>
> - "aeiouu"
> - "aeiouu"

### Example 2:

> Input: word = "unicornarihan"<br/>
> Output: 0<br/>
> Explanation: Not all 5 vowels are present, so there are no vowel substrings.

### Example 3:

> Input: word = "cuaieuouac"<br/>
> Output: 7<br/>
> Explanation: The vowel substrings of word are as follows (underlined):<br/>
> - "cuaieuouac"
> - "cuaieuouac"
> - "cuaieuouac"
> - "cuaieuouac"
> - "cuaieuouac"
> - "cuaieuouac"
> - "cuaieuouac"
 

### Constraints:

- 1 <= word.length <= 100
- word consists of lowercase English letters only.

### Topics

- Hash Table
- String