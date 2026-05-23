from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        dec = False
        for i in range(n):
            if not dec:
                if i == n - 1:
                    return nums[i] >= nums[(i + 1) % n]
                if nums[i] > nums[i + 1]:
                    dec = True
            else:
                if i == n - 1:
                    return nums[i] <= nums[(i + 1) % n]
                if nums[i] > nums[i + 1]:
                    return False

        return True
