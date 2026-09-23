from bisect import bisect_left


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(len(nums)):
            p[i + 1] = p[i] + nums[i]

        if p[-1] < x:
            return -1

        s = [0] * (n + 1)
        for i in range(len(nums) - 1, -1, -1):
            s[i] = s[i + 1] + nums[i]

        if p[1] > x and s[n - 1] > x:
            return -1

        res = -1
        for i, cs in enumerate(p):
            target = x - cs
            if target < 0:
                break
            elif target == 0:
                res = min(res, i) if res != -1 else i
                break

            idx = bisect_left(s, -target, key=lambda x: -x)
            if s[idx] + cs == x:
                res = min(res, i + (n - idx)) if res != -1 else i + (n - idx)

        return res
