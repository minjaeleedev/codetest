class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        one = sum([abs(num - nums[n // 2]) for num in nums])
        two = sum([abs(num - nums[n // 2 - 1]) for num in nums])
        return min(one, two)
