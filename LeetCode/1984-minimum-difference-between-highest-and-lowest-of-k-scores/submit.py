from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        nums.sort()
        res = float("inf")
        for i in range(len(nums) - k + 1):
            low, high = nums[i], nums[i + k - 1]
            res = min(high - low, res)

        return res
