from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        start = 0
        while start < n and nums[start] == 0:
            start += 1

        dist = 0
        for i in range(start + 1, n):
            if nums[i] == 1:
                if dist < k:
                    return False
                dist = 0
            else:
                dist += 1

        return True
