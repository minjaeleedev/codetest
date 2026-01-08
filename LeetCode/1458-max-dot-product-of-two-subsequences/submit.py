from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * n for _ in range(m)]
        # init first row
        for i in range(n):
            dp[0][i] = nums1[0] * nums2[i]

        # init first column
        for i in range(m):
            dp[i][0] = nums1[i] * nums2[0]

        for i in range(1, m):
            for j in range(1, n):
                term = nums1[i] * nums2[j]
                first = dp[i - 1][j - 1] + term
                second = dp[i - 1][j] + term - nums1[i - 1] * nums2[j]
                third = dp[i][j - 1] + term - nums1[i] * nums2[j - 1]
                dp[i][j] = max(first, second, third)

        res = float("-inf")
        for row in dp:
            res = max(res, max(row))

        return res
