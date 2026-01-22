from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # [5,2,3,1] - [7,5,4]
        # [5,2,4] - [7,6]
        # [5,6] - [11]
        # [7,1,2,5,1] - [8,3,7,6]
        # [7,3,5,1] - [10,8,6]
        # [7,3,6]
        # [7,9]
        # 2 2 -1 3 -2 2 1 1 1 -1
        # 2 2 -1 3 0 1 1 1 -1
        # 2 2 -1 3 0 1 1 0
        # 2 2 -1 3 1 1 0
        # 2 1 3 1 1 0
        # 2 1 3 1 1
        # 2 1 3 2
        # 3 3 2
        # 3 5
        result = 0

        def is_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False

            return True

        while not is_sorted(nums):
            mn = nums[0] + nums[1] if len(nums) >= 2 else nums[0]
            idx = 0
            for i in range(len(nums) - 1):
                cur, nx = nums[i], nums[i + 1]
                if mn > cur + nx:
                    mn = min(mn, cur + nx)
                    idx = i

            result += 1
            nums = nums[:idx] + [mn] + nums[idx + 2 :]

        return result
