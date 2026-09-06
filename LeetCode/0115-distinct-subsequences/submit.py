class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if s[0] == t[0] else 0
        for i in range(1, m):
            if s[i] == t[0]:
                dp[i][0] = dp[i - 1][0] + 1
            else:
                dp[i][0] = dp[i - 1][0]

        for i in range(m):
            for j in range(1, min(i + 1, n)):
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m - 1][n - 1]
