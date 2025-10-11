from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        s = sorted(set(nums))
        res = []
        cnt = 0
        while s and cnt < k:
            res.append(s.pop())
            cnt += 1

        return res
