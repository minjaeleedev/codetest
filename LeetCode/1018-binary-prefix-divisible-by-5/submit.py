from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = [False] * len(nums)
        rem = 0
        for i in range(len(nums)):
            rem = rem << 1
            rem = (rem + nums[i]) % 5
            res[i] = rem == 0

        return res
