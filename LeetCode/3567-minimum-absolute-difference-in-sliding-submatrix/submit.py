from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0 for _ in range(n - k + 1)] for _ in range(m - k + 1)]
        if k == 1:
            return res

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                s = set()
                for x in range(k):
                    for y in range(k):
                        s.add(grid[i + x][j + y])

                if len(s) == 1:
                    res[i][j] = 0
                    continue

                mn = 10**9
                srt = sorted(s)
                for idx in range(len(srt) - 1):
                    mn = min(mn, abs(srt[idx + 1] - srt[idx]))

                res[i][j] = mn

        return res
