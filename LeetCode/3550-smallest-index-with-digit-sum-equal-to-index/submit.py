from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            t = n
            ds = 0
            while t:
                ds += t % 10
                t //= 10
            if i == ds:
                return i

        return -1
