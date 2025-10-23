---
# Problem Identification
platform: LeetCode
platform-problem-id: "3461"
title: "Check If Digits Are Equal in String After Operations I"
url: "https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i"
difficulty: Easy
topics:
  - Math
  - String
  - Simulation
  - Combinatorics

# Solution Tracking
status: Solved
date-attempted: 2025-10-23
date-solved: 2025-10-23
attempts: 1

# Personal Notes
rating: 1
needs-review: false
tags: []
notes: "Easy Problem With O(N^2)"
similar-problems: []

# Review Schedule (for spaced repetition)
next-review: null
review-count: 0
last-reviewed: null
---

## 3461. [3461. Check If Digits Are Equal in String After Operations I](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i)

You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:

- For each pair of consecutive digits in <code>s</code>, starting from the first digit, calculate a new digit as the sum of the two digits <strong>modulo</strong> 10.</li>
- Replace <code>s</code> with the sequence of newly calculated digits, <em>maintaining the order</em> in which they are computed.</li>

Return <code>true</code> if the final two digits in <code>s</code> are the <strong>same</strong>; otherwise, return <code>false</code>.

#### Example 1

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;3902&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Initially, <code>s = &quot;3902&quot;</code></li>
	<li>First operation:
	<ul>
		<li><code>(s[0] + s[1]) % 10 = (3 + 9) % 10 = 2</code></li>
		<li><code>(s[1] + s[2]) % 10 = (9 + 0) % 10 = 9</code></li>
		<li><code>(s[2] + s[3]) % 10 = (0 + 2) % 10 = 2</code></li>
		<li><code>s</code> becomes <code>&quot;292&quot;</code></li>
	</ul>
	</li>
	<li>Second operation:
	<ul>
		<li><code>(s[0] + s[1]) % 10 = (2 + 9) % 10 = 1</code></li>
		<li><code>(s[1] + s[2]) % 10 = (9 + 2) % 10 = 1</code></li>
		<li><code>s</code> becomes <code>&quot;11&quot;</code></li>
	</ul>
	</li>
	<li>Since the digits in <code>&quot;11&quot;</code> are the same, the output is <code>true</code>.</li>
</ul>
</div>

#### Example 2

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;34789&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Initially, <code>s = &quot;34789&quot;</code>.</li>
	<li>After the first operation, <code>s = &quot;7157&quot;</code>.</li>
	<li>After the second operation, <code>s = &quot;862&quot;</code>.</li>
	<li>After the third operation, <code>s = &quot;48&quot;</code>.</li>
	<li>Since <code>&#39;4&#39; != &#39;8&#39;</code>, the output is <code>false</code>.</li>
</ul>
</div>

#### Constraints

- `3 <= s.length <= 100`
- `s` consists of only digits.
