from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [[0] * (n + 1) for _ in range(m + 1)]
        cols = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                rows[i][j] = rows[i][j - 1] + grid[i - 1][j - 1]

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                cols[i][j] = cols[i - 1][j] + grid[i - 1][j - 1]

        def is_magic(r, c, length):
            s = rows[r + 1][c + length] - rows[r + 1][c]
            diag = [0, 0]
            for i in range(length):
                r_sum = rows[r + i + 1][c + length] - rows[r + i + 1][c]
                if r_sum != s:
                    return False

                c_sum = cols[r + length][c + i + 1] - cols[r][c + i + 1]
                if c_sum != s:
                    return False

                diag[0] += grid[r + i][c + i]
                diag[1] += grid[r + i][c + length - i - 1]

            return diag[0] == s and diag[1] == s

        res = 1
        for i in range(m):
            for j in range(n):
                # skip length smaller than current result.
                length = res
                while i + length - 1 < m and j + length - 1 < n:
                    if is_magic(i, j, length):
                        res = max(res, length)

                    length += 1

        return res
