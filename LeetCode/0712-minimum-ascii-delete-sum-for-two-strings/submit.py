class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                o1, o2 = ord(s1[i]), ord(s2[j])
                prev_row = dp[i - 1][j] if i >= 1 else 0
                prev_col = dp[i][j - 1] if j >= 1 else 0
                new = dp[i - 1][j - 1] if i >= 1 and j >= 1 else 0
                new += o1 if o1 == o2 else 0
                dp[i][j] = max(prev_row, prev_col, new)

        s1_ord, s2_ord = sum([ord(c) for c in s1]), sum([ord(c) for c in s2])
        return s1_ord + s2_ord - 2 * dp[m - 1][n - 1]
