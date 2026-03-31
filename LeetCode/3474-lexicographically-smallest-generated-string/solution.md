# Approach: Greedy

## Intuition
We first process the 'T' constraints, followed by the 'F' constraints.

We traverse all 'T' positions in str1 and fill str2 into the target string word. 
If a conflict occurs during this process, meaning a different character has already been assigned to the same position, then no valid solution exists, and we return an empty string. 
We also maintain a fixed array to record which positions are fixed by 'T' constraints.

Next, for all positions that are not fixed, we assign the character 'a' by default to ensure the lexicographically smallest result.

We then process the 'F' constraints. For each position i where str1[i]= ′F′, we check whether the substring word[i…i+m−1] is exactly equal to str2. 
If it is not equal, no action is needed. 
However, if it is equal, we must modify at least one non-fixed character within this window to break the match.

To maintain the smallest lexicographical order, we choose to modify the rightmost non-fixed character in the window, changing it to 'b'.

A natural concern is whether modifying the rightmost non-fixed character could invalidate a previously satisfied 'F' constraint. 
We now show that this cannot happen.

Suppose str1 contains two 'F' positions at indices i_1 and i_2. 

When processing i_2, we modify a character in its window, which could potentially make the substring at i_1 equal to str_2, violating the 'F' constraint.

Consider str_2=A+′a′+B+′b′+C.
At index i_1, the substring is A+′a′+B+′a′+C, and at index i_2, it is A+′a′+B+′b′+C. 

We modify the 'a' in the i_2 window to 'b', which may affect the substring at i_1.

From this structure, we can derive the following:

[3474](3474.png)

As shown in the figure, we can obtain the following information:

1. Since the rightmost non-fixed character in the i_2 window is the first 'a', there are no non-fixed characters to its right within the window. 
2. Also, the prefix B+′b′+C must match a prefix of str_2 due to 'T' constraints.
The string A must be a suffix of A+′a′+B.

We now consider three cases based on the relative lengths of A and B:

1. Length of A equals length of B

    Since B+′b′+C is a prefix of str_2=A+′a′+B+′b′+C, this implies 'b' = 'a', which is impossible.

2. Length of A is greater than length of B

    Since both A and B+′b′+C are prefixes of str_2, let A=B+′b′+D.
    Because A is also a suffix of A+′a′+B, we obtain:
    $B+′b′+D=D+′a′+B$
    Removing common parts leads to 'b' = 'a', which is impossible.

3. Length of A is less than length of B

    Since A is a suffix of A+′a′+B, let B=D+A.
    Since B+′b′+C is a prefix of str_2, we obtain:
    (D+A)+′b′=A+′a′+D
    Again, this leads to 'b' = 'a', which is impossible.

In all cases, we reach a contradiction. 
Therefore, modifying the rightmost non-fixed character will never violate any previously satisfied 'F' constraint, while also minimizing the lexicographical impact.

## Complexity Analysis
Let n be the length of str_1, and m be the length of str_2.

- Time complexity: O(nm).
 
- Space complexity: O(n+m).