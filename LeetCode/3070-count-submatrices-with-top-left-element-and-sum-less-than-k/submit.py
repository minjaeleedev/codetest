from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] += grid[i - 1][j] if i > 0 else 0
                grid[i][j] += grid[i][j - 1] if j > 0 else 0
                grid[i][j] -= grid[i - 1][j - 1] if i > 0 and j > 0 else 0
                if grid[i][j] <= k:
                    res += 1

        return res
