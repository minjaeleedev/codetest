from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(n):
            res = 0
            while n:
                res += n % 10
                n //= 10

            return res

        return min([digit_sum(n) for n in nums])
