from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        eff = k % (m * n)
        res = [[0] * n for _ in range(m)]
        r, c = divmod(eff, n)
        idx = r * n + c
        while idx < m * n:
            res[idx // n][idx % n] = grid[(idx - (r * n + c)) // n][
                (idx - (r * n + c)) % n
            ]
            idx += 1

        i = 0
        d = m * n - (r * n + c)
        while i < r * n + c:
            res[i // n][i % n] = grid[d // n][d % n]
            i += 1
            d += 1

        return res
