from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mn = min(complexity[1:])
        root = complexity[0]
        if mn <= root:
            return 0

        n = len(complexity)
        res = 1
        for i in range(2, n):
            res = res * i % (10**9 + 7)

        return res
