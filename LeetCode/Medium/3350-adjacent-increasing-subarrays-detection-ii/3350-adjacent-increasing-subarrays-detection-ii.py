from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        lengths = []
        i = 0
        while i < len(nums):
            cur_len = 1
            j = i
            while j < len(nums) - 1 and nums[j] < nums[j + 1]:
                cur_len += 1
                j += 1

            lengths.append(cur_len)
            i = j + 1

        res = 0
        for i in range(len(lengths)):
            itself = lengths[i] // 2
            if i == len(lengths) - 1:
                res = max(itself, res)
            else:
                adj = min(lengths[i], lengths[i + 1])
                res = max(itself, adj, res)

        return res
