from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        one, two = nums[0], None
        for n in nums[1:]:
            if one <= n:
                two = one
                one = n
            else:
                if two is None or two <= n:
                    two = n

        return (one - 1) * (two - 1)
