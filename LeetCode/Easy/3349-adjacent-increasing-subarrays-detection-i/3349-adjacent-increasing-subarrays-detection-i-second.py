from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # non optimized
        for i in range(len(nums) - 2 * k + 1):
            is_increasing = True
            for j in range(i, i + k - 1):
                if nums[j] >= nums[j + 1] or nums[j + k] >= nums[j + k + 1]:
                    is_increasing = False
                    break

            if is_increasing:
                return True

        return False
