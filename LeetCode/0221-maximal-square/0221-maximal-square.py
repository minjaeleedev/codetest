class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if matrix[r][c] != "1":
                    continue

                prev_diag = dp[r-1][c-1] if r != 0 and c != 0 else 0
                prev_row = dp[r-1][c] if r != 0 else 0
                prev_col = dp[r][c-1] if c != 0 else 0
                if prev_diag != 0 and prev_row != 0 and prev_col != 0:
                    sq = min(prev_diag, prev_row, prev_col)
                    dp[r][c] += sq + int(sq**0.5) * 2 + 1
                else:
                    dp[r][c] = 1
        
        result = 0
        for r in range(m):
            for c in range(n):
                result = max(result, dp[r][c])

        return result