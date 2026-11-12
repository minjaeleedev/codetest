from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dp_inc = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp_inc[i] = dp_inc[i - 1] + 1

        res = max(dp_inc)
        dp_dec = [1] * n
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                dp_dec[i] = dp_dec[i - 1] + 1
        res = max(max(dp_dec), res)
        return res
