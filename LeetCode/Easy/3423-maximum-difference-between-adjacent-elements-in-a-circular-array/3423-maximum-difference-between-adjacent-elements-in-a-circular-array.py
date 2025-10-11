from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            result = max(result, abs(nums[i] - nums[i - 1]))

        return result
