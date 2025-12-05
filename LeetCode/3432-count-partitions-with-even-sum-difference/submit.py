from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res = 0
        r = sum(nums)
        l = 0
        for i in range(len(nums) - 1):
            n = nums[i]
            r -= n
            l += n
            if abs(r - l) % 2 == 0:
                res += 1

        return res
