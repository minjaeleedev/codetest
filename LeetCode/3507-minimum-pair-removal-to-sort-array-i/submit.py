from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr):
            if not arr:
                return True

            p = arr[0]
            for c in arr[1:]:
                if p > c:
                    return False
                p = c

            return True

        cnt = 0
        while not is_non_decreasing(nums):
            s = float("inf")
            idx = 0
            for i in range(len(nums) - 1):
                adj = nums[i] + nums[i + 1]
                if adj < s:
                    s = adj
                    idx = i

            nums = nums[:idx] + [s] + nums[idx + 2 :]
            cnt += 1

        return cnt
