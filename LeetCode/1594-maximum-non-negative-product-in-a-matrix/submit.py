from typing import List


# try to use dp[i][j][2] ..
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[1, -1] for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
                mn_up, mn_left = dp[i - 1][j][0], dp[i][j - 1][0]
                mx_up, mx_left = dp[i - 1][j][1], dp[i][j - 1][1]
                if cur >= 0:
                    dp[i][j][0] = min(
                        mn_up * cur % MOD if mn_up < 0 else 1,
                        mn_left * cur % MOD if mn_left < 0 else 1,
                    )
                    dp[i][j][1] = max(
                        mx_up * cur % MOD if mx_up >= 0 else -1,
                        mx_left * cur % MOD if mx_left >= 0 else -1,
                    )
                else:
                    dp[i][j][0] = min(
                        mx_up * cur % MOD if mx_up >= 0 else -1,
                        mx_left * cur % MOD if mx_left >= 0 else -1,
                    )
                    dp[i][j][1] = max(
                        mn_up * cur % MOD if mn_up < 0 else -1,
                        mn_left * cur % MOD if mn_left < 0 else -1,
                    )

        return dp[i][j][1]
