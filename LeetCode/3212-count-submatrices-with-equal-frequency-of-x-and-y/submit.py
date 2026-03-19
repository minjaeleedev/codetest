from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        pref = [[[0, 0] for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                up = pref[i - 1][j] if i > 0 else None
                left = pref[i][j - 1] if j > 0 else None
                diag = pref[i - 1][j - 1] if i > 0 and j > 0 else None
                if grid[i][j] == "X":
                    pref[i][j][0] += 1
                elif grid[i][j] == "Y":
                    pref[i][j][1] += 1
                for k in range(2):
                    pref[i][j][k] += up[k] if up else 0
                    pref[i][j][k] += left[k] if left else 0
                    pref[i][j][k] -= diag[k] if diag else 0

                if pref[i][j][0] == pref[i][j][1] and pref[i][j][0] >= 1:
                    res += 1

        return res
