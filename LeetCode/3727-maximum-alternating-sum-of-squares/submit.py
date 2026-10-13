from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: -abs(x))
        res = 0
        for i, n in enumerate(nums):
            res += (n**2) if i < (len(nums) + 1) // 2 else -(n**2)
        return res
