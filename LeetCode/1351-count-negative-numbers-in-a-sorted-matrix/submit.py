from typing import List


# O(m+n) solution
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c = m - 1, 0
        res = 0
        while 0 <= r < m and 0 <= c < n:
            if grid[r][c] < 0:
                res += n - c
                r -= 1
            else:
                c += 1

        return res
