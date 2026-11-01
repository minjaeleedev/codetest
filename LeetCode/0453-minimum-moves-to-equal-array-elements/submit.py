class Solution:
    def minMoves(self, nums: list[int]) -> int:
        res = 0
        mn = min(nums)
        for n in nums:
            res += n - mn

        return res
