from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        hs = [0 for _ in range(m)]
        vs = [0 for _ in range(n)]
        for i in range(m):
            hs[i] = sum(grid[i])

        for i in range(1, m):
            hs[i] += hs[i - 1]

        for i in range(n):
            vs[i] = sum([grid[j][i] for j in range(m)])

        for i in range(1, n):
            vs[i] += vs[i - 1]

        for i in range(1, m):
            if hs[i - 1] == hs[m - 1] - hs[i - 1]:
                return True

        for i in range(1, n):
            if vs[i - 1] == vs[n - 1] - vs[i - 1]:
                return True

        return False
