from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 3 for _ in range(n + 1)]

        for i in range(1, n + 1):
            num = nums[i - 1]
            rem = num % 3
            pd0, pd1, pd2 = dp[i - 1]
            if rem == 0:
                dp[i][0] = pd0 + num
                dp[i][1] = pd1 + num if pd1 != 0 else 0
                dp[i][2] = pd2 + num if pd2 != 0 else 0
            elif rem == 1:
                dp[i][0] = max(pd0, pd2 + num if pd2 != 0 else 0)
                dp[i][1] = max(pd1, pd0 + num if pd0 != 0 else 0) or num
                dp[i][2] = max(pd2, pd1 + num if pd1 != 0 else 0)
            else:
                dp[i][0] = max(pd0, pd1 + num if pd1 != 0 else 0)
                dp[i][1] = max(pd1, pd2 + num if pd2 != 0 else 0)
                dp[i][2] = max(pd2, pd0 + num if pd0 != 0 else 0) or num

        return dp[n][0]
