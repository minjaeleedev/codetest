"""
# Approach: Combinatorics

## Intuition
The main idea of this approach is that we do not need to generate all k−1 happy strings to find the kth smaller one.
To better understand this, let's make the following observations:

- The total number of happy strings of length n is 3⋅2^n−1.
This is because the first character has 3 choices ('a', 'b', or 'c') and each subsequent character has 2 choices, as it must differ from the preceding character.
Therefore, if k exceeds this total, it implies that the k-th happy string does not exist, and we should return an empty string.

- Moving on to the harder case, note that the set of all happy strings can be divided into three equal groups based on their starting character:
    - Strings starting with 'a': positions 1 to 2^n−1.
    - Strings starting with 'b': positions 2^n−1+1 to 2⋅2^n−1.
    - Strings starting with 'c': positions 2⋅2^n−1+1 to 3⋅2^n−1.

    Each group contains 2^n−1 strings, as fixing the first character leaves 2^n−1 ways to choose the remaining characters.
    By comparing k to these ranges, we can determine the first character of the desired string and adjust k to reflect its position within the subgroup by subtracting the group's starting index.

- Similarly, every subsequent character at the ith position divides the strings of its group into two subgroups of size 2^n−i−1:
    - Strings starting with the smallest valid character ('a' -> 'b', 'b' -> 'a' and 'c' -> 'a').
    - Strings starting with the greatest valid character ('a' -> 'c', 'b' -> 'c' and 'c' -> 'b').

    By comparing k with the midpoint at which the groups are split, i.e., 2^n−i−1, we can determine whether the result string belongs to the first or last subgroup and set the character at position i accordingly.

## Algorithm
Calculate the total number of happy strings of length n as total = 3 * pow(2, n - 1).
If k is greater than total, return an empty string.
Initialize the result string.
Initialize two maps, nextSmallest and nextGreatest, that map each of the three characters to the smallest and largest characters respectively that can go after them.
Set the index of the first string that starts with 'a' (startA) to 1 (the lexicographically smallest happy string with 'a').
Calculate the index of the first string that starts with 'b' as startB = startA + pow(2, n - 1).
Calculate the index of the first string that starts with 'c' as startC = startB + pow(2, n - 1).
Determine the first character of the string:
If k is less than startB, set the first character of result to 'a' and subtract startA from k.
Else if k is less than startC, set the first character of result to 'b' and subtract startB from k.
Else, set the first character of result to 'c' and subtract startC from k.
For each subsequent character, at charIndex:
Calculate the midpoint of its group, as midpoint = pow(2, n - charIndex - 1).
If k is less than midpoint, set result[charIndex] = nextSmallest[result[charIndex - 1]] to extend result with the smallest valid character.
Otherwise:
Set result[charIndex] = nextGreatest[result[charIndex - 1]].
Decrement k by midpoint so that it corresponds to the index of the result string within the current group.
Return result.

## Complexity Analysis
Let n be the length of the happy strings.

Time Complexity: O(n).

We construct the result string by iterating over its characters and determining each of them in constant time. Therefore, the time complexity of this algorithm is O(n).

Space Complexity: O(1).

Excluding the output string, the algorithm only requires a fixed number of variables and two maps (nextGreatest and nextSmallest) of fixed size. Thus, the auxiliary space complexity is constant or O(1).
"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Calculate the total number of happy strings of length n
        total = 3 * (1 << (n - 1))

        # If k is greater than the total number of happy strings, return an empty string
        if k > total:
            return ""

        result = ["a"] * n  # Initialize result with 'a' characters

        # Define mappings for the next smallest and greatest valid characters
        next_smallest = {"a": "b", "b": "a", "c": "a"}
        next_greatest = {"a": "c", "b": "c", "c": "b"}

        # Calculate the starting indices for strings beginning with 'a', 'b', and 'c'
        start_a = 1
        start_b = start_a + (1 << (n - 1))
        start_c = start_b + (1 << (n - 1))

        # Determine the first character based on the value of k
        if k < start_b:
            result[0] = "a"
            k -= start_a
        elif k < start_c:
            result[0] = "b"
            k -= start_b
        else:
            result[0] = "c"
            k -= start_c

        # Iterate through the remaining positions in the result string
        for char_index in range(1, n):
            # Calculate the midpoint of the group for the current character position
            midpoint = 1 << (n - char_index - 1)

            # Determine the next character based on the value of k
            if k < midpoint:
                result[char_index] = next_smallest[result[char_index - 1]]
            else:
                result[char_index] = next_greatest[result[char_index - 1]]
                k -= midpoint

        return "".join(result)
