from typing import List


# use dp
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        dp = [0] * (n + 1)
        dp[1] = 0
        last = colors[0]
        mx = neededTime[0]
        for i in range(2, n + 1):
            if colors[i - 1] == last:
                dp[i] = dp[i - 1] + min(mx, neededTime[i - 1])
                mx = max(neededTime[i - 1], mx)
            else:
                last = colors[i - 1]
                mx = neededTime[i - 1]
                dp[i] = dp[i - 1]

        return dp[n]
