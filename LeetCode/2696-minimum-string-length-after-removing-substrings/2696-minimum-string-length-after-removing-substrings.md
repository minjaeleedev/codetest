---
# Problem Identification
platform: LeetCode
platform-problem-id: "2696"
title: "Minimum String Length After Removing Substrings"
url: "https://leetcode.com/problems/minimum-string-length-after-removing-substrings/"
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

## 2696. Minimum String Length After Removing Substrings

You are given a string s consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

### Example 1:

> Input: s = "ABFCACDB"</br>
> Output: 2</br>
> Explanation: We can do the following operations:
>
> - Remove the substring "ABFCACDB", so s = "FCACDB".
> - Remove the substring "FCACDB", so s = "FCAB".
> - Remove the substring "FCAB", so s = "FC".</br>
>   So the resulting length of the string is 2.
>   It can be shown that it is the minimum length that we can obtain.

### Example 2:

> Input: s = "ACBBD"</br>
> Output: 5</br>
> Explanation: We cannot do any operations on the string so the length remains the same.

### Constraints:

- 1 <= s.length <= 100
- consists only of uppercase English letters.
