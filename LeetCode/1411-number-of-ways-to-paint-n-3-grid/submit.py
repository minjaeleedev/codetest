class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[0, 0] for _ in range(n + 1)]
        dp[1][0] = 6
        dp[1][1] = 6
        for i in range(2, n + 1):
            dp[i][0] = (dp[i - 1][0] * 2 + dp[i - 1][1] * 2) % mod
            dp[i][1] = (dp[i - 1][0] * 2 + dp[i - 1][1] * 3) % mod

        return sum(dp[n]) % mod
