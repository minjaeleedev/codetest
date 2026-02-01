from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        res = float("inf")
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                s = nums[:i][0] + nums[i:j][0] + nums[j:][0]
                res = min(res, s)

        return res

    # optimize by exploiting the fact that a cost of the each subarray is the value of first element.
    # nums[0] is always included in the cost.
    # we can choose the other two elements after sort the original array.
    def minimumCostV2(self, nums: List[int]) -> int:
        tmp = sorted(nums[1:])
        return nums[0] + tmp[0] + tmp[1]
