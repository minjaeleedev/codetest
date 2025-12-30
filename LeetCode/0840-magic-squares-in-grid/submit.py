from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        nums = set([i for i in range(1, 10)])  # 1-9 set

        def is_magic(square):
            s = set()
            for x in range(3):
                for y in range(3):
                    s.add(square[x][y])

            if s != nums:
                return False

            for x in range(3):
                if sum(square[x]) != 15:
                    return False

            for col in zip(*square):
                if sum(col) != 15:
                    return False

            diag = square[0][0] + square[1][1] + square[2][2]
            down = square[0][2] + square[1][1] + square[2][0]
            if diag != 15 or down != 15:
                return False

            return True

        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if is_magic([r[j : j + 3] for r in grid[i : i + 3]]):
                    res += 1

        return res
