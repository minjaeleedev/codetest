from collections import deque
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        next_cell = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(1, 0), (0, -1)],
            4: [(1, 0), (0, 1)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)],
        }

        def is_connected(a, b, dr, dc):
            if a == 1:
                if b == 1:
                    return True
                if b == 3 or b == 5:
                    return dc == 1
                if b == 4 or b == 6:
                    return dc == -1
            if a == 2:
                if b == 2:
                    return True
                if b == 5 or b == 6:
                    return dr == 1
                if b == 3 or b == 4:
                    return dr == -1
            if a == 3:
                if b == 6:
                    return True
                if b == 1 or b == 4:
                    return dc == -1
                if b == 2 or b == 5:
                    return dr == 1
            if a == 4:
                if b == 5:
                    return True
                if b == 1 or b == 3:
                    return dc == 1
                if b == 2 or b == 6:
                    return dr == 1
            if a == 5:
                if b == 4:
                    return True
                if b == 3 or b == 2:
                    return dr == -1
                if b == 1 or b == 6:
                    return dc == -1
            if a == 6:
                if b == 3:
                    return True
                if b == 2 or b == 4:
                    return dr == -1
                if b == 5 or b == 1:
                    return dc == 1

        m, n = len(grid), len(grid[0])
        visit = [[False for _ in range(n)] for _ in range(m)]
        q = deque([(0, 0)])
        visit[0][0] = True
        while q:
            cr, cc = q.popleft()
            if cr == m - 1 and cc == n - 1:
                return True

            for dr, dc in next_cell[grid[cr][cc]]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if visit[nr][nc]:
                        continue

                    if is_connected(grid[cr][cc], grid[nr][nc], dr, dc):
                        visit[nr][nc] = True
                        q.append((nr, nc))

        return False
