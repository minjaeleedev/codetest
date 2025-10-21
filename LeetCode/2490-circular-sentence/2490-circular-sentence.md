---
# Problem Identification
platform: LeetCode
platform-problem-id: "2490"
title: "Circular Sentence"
url: "https://leetcode.com/problems/circular-sentence/"
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

## 2490. Circular Sentence

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

- For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
 
Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

- The last character of a word is equal to the first character of the next word.
- The last character of the last word is equal to the first character of the first word.

For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.

### Example 1:

> Input: sentence = "leetcode exercises sound delightful"<br/>
> Output: true<br/>
> Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].<br/>
> - leetcode's last character is equal to exercises's first character.
> - exercises's last character is equal to sound's first character.
> - sound's last character is equal to delightful's first character.
> - delightful's last character is equal to leetcode's first character.
> 
> The sentence is circular.

### Example 2:

> Input: sentence = "eetcode"<br/>
> Output: true<br/>
> Explanation: The words in sentence are ["eetcode"].<br/>
> - eetcode's last character is equal to eetcode's first character.
> 
> The sentence is circular.

### Example 3:

> Input: sentence = "Leetcode is cool"<br/>
> Output: false<br/>
> Explanation: The words in sentence are ["Leetcode", "is", "cool"].<br/>
> - Leetcode's last character is not equal to is's first character.
> 
> The sentence is not circular.

### Constraints:

- 1 <= sentence.length <= 500
- sentence consist of only lowercase and uppercase English letters and spaces.
- The words in sentence are separated by a single space.
- There are no leading or trailing spaces.
