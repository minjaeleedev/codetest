from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        w, h = m, n
        for layer in range(min(m, n) // 2):
            # layer positions for each side except last element
            # left
            pos = [(r, layer) for r in range(layer, m - layer - 1)]
            # lower
            pos += [(m - 1 - layer, c) for c in range(layer, n - layer - 1)]
            # right
            pos += [(r, n - 1 - layer) for r in range(m - layer - 1, layer, -1)]
            # upper
            pos += [(layer, c) for c in range(n - layer - 1, layer, -1)]
            val = [grid[r][c] for r, c in pos]

            # shift values
            w, h = n - 2 * layer, m - 2 * layer
            div = 2 * (w + h) - 4
            rot = k % div
            val = val[-rot:] + val[:-rot]

            # input to result
            for i, position in enumerate(pos):
                r, c = position
                res[r][c] = val[i]

        return res
