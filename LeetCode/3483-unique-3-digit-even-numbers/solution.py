from typing import List


class Solution:
    """
    Approach: Enumeration

    Intuition
    We can enumerate three distinct indices i, j, and k, and
    use their corresponding digits as the hundreds, tens, and ones digits, respectively.

    A valid three-digit even number must satisfy the following conditions:
    - Its hundreds digit cannot be 0.
    - Its ones digit must be even.
    - Its three digits must come from distinct indices.

    Because the array can contain duplicate digits, different index triples may form the same three-digit number.
    We can use a boolean array vis of length 1000 to record whether each three-digit number has already appeared.
    Whenever a valid, unseen number is formed, we mark it as visited and increment the answer.
    """

    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        vis = [False] * 1000
        ans = 0

        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j or digits[k] % 2 != 0:
                        continue
                    x = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if not vis[x]:
                        vis[x] = True
                        ans += 1

        return ans
