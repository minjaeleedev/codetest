from math import inf
from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn, mx = inf, -inf
        s = set()
        for n in nums:
            if mn > n:
                mn = n

            if mx < n:
                mx = n

            s.add(n)

        return [n for n in range(mn, mx + 1) if n not in s]
