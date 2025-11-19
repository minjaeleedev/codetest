from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)
        res = original
        while res in s:
            res *= 2

        return res
