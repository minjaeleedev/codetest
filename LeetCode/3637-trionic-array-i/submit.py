from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p = -1
        q = -1
        for i in range(1, len(nums)):
            if p == -1:
                if nums[i - 1] < nums[i]:
                    continue
                elif nums[i - 1] == nums[i]:
                    return False
                else:
                    p = i - 1
            elif q == -1:
                if nums[i - 1] > nums[i]:
                    continue
                elif nums[i - 1] == nums[i]:
                    return False
                else:
                    q = i - 1
            else:
                if nums[i - 1] < nums[i]:
                    continue
                else:
                    return False

        return 0 < p < q < len(nums) - 1
