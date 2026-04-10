from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if not (nums[i] == nums[j] == nums[k]):
                        continue

                    dist = abs(i - j) + abs(j - k) + abs(k - i)
                    res = min(res, dist) if res != -1 else dist

        return res
