from typing import List
import math


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        cnt = 0
        prev = -math.inf

        for num in nums:
            # smallest candidates: nums[i]-k, a_{i-1}+1
            # if a_{i-1}+1 < nums[i]-k, it is invalid.
            # so we take max(nums[i]-k, a_{i-1}+1).
            # and if current candidate greater than nums[i] + k, it is invalid.
            # therefore, a_i = min(max(nums[i]-k, a_{i-1}+1), nums[i]+k)
            curr = min(max(num - k, prev + 1), num + k)
            if curr > prev:
                cnt += 1
                prev = curr

        return cnt
