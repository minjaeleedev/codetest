from math import inf
from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn_idx, mx_idx = 0, 0
        mn, mx = inf, -inf
        for i in range(len(nums)):
            cur = nums[i]
            if cur > mx:
                mx_idx = i
                mx = cur

            if cur < mn:
                mn_idx = i
                mn = cur

        head, tail = min(mn_idx, mx_idx), max(mn_idx, mx_idx)
        ff = tail + 1
        fb = len(nums) - tail + head + 1
        bb = len(nums) - head

        return min(ff, fb, bb)
