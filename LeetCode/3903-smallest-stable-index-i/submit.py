class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        res = -1
        for i in range(len(nums)):
            mx = max(nums[: i + 1])
            mn = min(nums[i:])
            if (mx - mn) <= k and res == -1:
                res = i
                break

        return res
