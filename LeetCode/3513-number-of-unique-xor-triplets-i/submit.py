from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return len(nums)

        res = 0
        n = len(nums)
        while n:
            n //= 2
            res += 1

        return 2**res
