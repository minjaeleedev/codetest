from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        if totalSum % 2 == 0:
            # S is even
            # (left even, right even) or (left odd, right odd)
            # therefore left-right is always even.
            return len(nums) - 1

        # S is odd
        # (left odd, right even) or (left even, right odd)
        # therefore left-right is always odd.
        return 0
