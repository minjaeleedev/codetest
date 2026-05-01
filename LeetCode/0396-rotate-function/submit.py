from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # F(k+1) = F(k) + S - n*last.
        n = len(nums)
        s = sum(nums)
        prev = sum([i * n for i, n in enumerate(nums)])
        res = prev
        last = nums[-1]
        for i in range(1, n):
            cur = prev + s - n * last
            res = max(res, cur)
            prev = cur
            last = nums[-1 - i]

        return res
