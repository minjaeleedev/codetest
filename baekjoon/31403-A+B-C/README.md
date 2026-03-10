---
platform: Baekjoon  # LeetCode | Baekjoon | Kattis | Codeforces | AtCoder | HackerRank | etc.
platform-problem-id: "30802"
title: "A+B-C"
url: "https://www.acmicpc.net/problem/31403"
difficulty: Bronze   # LeetCode: Easy | Medium | Hard | Baekjoon: Bronze | Silver | Gold | Platinum | Diamond
topics:
  - Math
  - String
  - Operation

# Solution Tracking
status: Solved  # Not Started | Attempted | Solved | Reviewed
date-attempted: 2026-03-11
date-solved: 2026-03-11
attempts: 1

# Personal Notes
rating: 1  # 1-10 difficulty rating (personal)
needs-review: false  # Set to true for problems that need review
tags: []  # Personal tags: interview-prep, tricky, favorite, etc.
notes: ""
similar-problems:
  - platform:
    id:

# Review Schedule (for spaced repetition)
next-review: null  # Auto-managed by review script
review-count: 0
last-reviewed: null
---

## 문제
JavaScript에서  $+, -$은 수에 대해서는 일반적인 의미의 덧셈 뺄셈의 의미를 가지고 있습니다. 하지만 문자열에 대해서 $+$는 두 문자열을 이어붙이라는 의미이고, $-$는 양쪽 문자열을 수로 해석한 이후에 빼라는 의미입니다.
 
$A, B, C$를 각각 수와 문자열로 생각했을 때 
$A+B-C$를 출력하세요.

## 입력
첫 줄에는 정수 
$A$가 주어집니다. 
$(1 \le A \le 1\,000)$ 

둘째 줄에는 정수 
$B$가 주어집니다. 
$(1 \le B \le 1\,000)$ 

셋째 줄에는 정수 
$C$가 주어집니다. 
$(1 \le C \le 1\,000)$ 

주어지는 모든 수는 
$0$으로 시작하지 않는 양의 정수입니다.

## 출력
첫 줄에는 $A, B, C$를 수로 생각했을 때, $A+B-C$를 출력하세요.

둘째 줄에는 
$A, B, C$를 문자열로 생각했을 때, 
$A+B-C$를 출력하세요.

#### 예제 입력 1 
3
4
5

#### 예제 출력 1 
2
29
 
$A, B, C$를 수로 생각했을 때는, 
$3+4-5 = 7 - 5 = 2$입니다.

 
$A, B, C$를 문자열로 생각했을 때는 
$\texttt{`}3\texttt{'}+\texttt{`}4\texttt{'}-\texttt{`}5\texttt{'} = \texttt{`}34\texttt{'} - \texttt{`}5\texttt{'} = 29$입니다.

#### 노트
 
$A+B-C$는 수와 문자열 모두에서 
$+$를 먼저 계산 한 이후 
$-$를 계산합니다.