from collections import deque
from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def bfs(day):
            grid = [[0] * col for _ in range(row)]
            q = deque()

            for r, c in cells[:day]:
                grid[r - 1][c - 1] = 1

            for i in range(col):
                # starting points
                if not grid[0][i]:
                    q.append((0, i))
                    # mark visit
                    grid[0][i] = -1

            while q:
                r, c = q.popleft()
                if r == row - 1:
                    # land last row
                    return True

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = -1
                        q.append((nr, nc))

            return False

        l, r = 1, row * col
        while l < r:
            mid = r - (r - l) // 2
            if bfs(mid):
                l = mid
            else:
                r = mid - 1

        return l
