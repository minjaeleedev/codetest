from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = -1
        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] += pref[i - 1] + nums[i - 1]

        for i in range(n):
            for j in range(l, r + 1):
                ri = i + j
                if ri > n:
                    break
                s = pref[ri] - pref[i]
                if s > 0:
                    res = min(res, s) if res > 0 else s

        return res
