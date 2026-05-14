from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i < n - 2:
                if nums[i] != i + 1:
                    return False
            else:
                if nums[i] != n - 1:
                    return False

        return True
