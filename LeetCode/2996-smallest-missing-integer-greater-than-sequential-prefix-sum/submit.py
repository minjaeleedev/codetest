from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        pref = nums[0]
        i = 0
        while i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
            pref += nums[i + 1]
            i += 1

        s = set(nums)
        while True:
            if pref not in s:
                return pref
            pref += 1

        return 0
