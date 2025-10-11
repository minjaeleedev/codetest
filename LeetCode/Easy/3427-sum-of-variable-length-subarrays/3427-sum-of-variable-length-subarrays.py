from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        result = [0] * n
        for i in range(n):
            start = max(0, i - nums[i])
            s = prefix[i + 1] - prefix[start]
            result[i] = s

        return sum(result)
