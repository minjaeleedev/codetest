from collections import deque
from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False] * n for _ in range(m)]
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        for i in range(m):
            for j in range(n):
                if not visit[i][j] and grid[i][j] > 0:
                    val = self.bfs(i, j, m, n, visit, grid, d)
                    if val % k == 0:
                        res += 1
        return res

    def bfs(self, sr, sc, m, n, visit, grid, d) -> int:
        visit[sr][sc] = True
        q = deque([(sr, sc)])
        res = 0
        while q:
            cr, cc = q.popleft()
            res += grid[cr][cc]
            for dr, dc in d:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if not visit[nr][nc] and grid[nr][nc] > 0:
                        visit[nr][nc] = True
                        q.append((nr, nc))

        return res
