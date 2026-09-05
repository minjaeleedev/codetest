class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mx = [nums[0]]
        for i in range(1, n):
            mx.append(max(nums[i], mx[-1]))

        mn = [nums[-1]]
        for i in range(n - 2, -1, -1):
            mn.append(min(nums[i], mn[-1]))

        for i in range(n):
            if mx[i] - mn[n - 1 - i] <= k:
                return i

        return -1
