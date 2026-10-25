from collections import deque


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False] * n for _ in range(m)]

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(sr, sc):
            is_closed = not (sr == 0 or sr == m - 1 or sc == 0 or sc == n - 1)
            q = deque([(sr, sc)])
            visit[sr][sc] = True
            while q:
                cr, cc = q.popleft()
                for dr, dc in d:
                    nr, nc = cr + dr, cc + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if visit[nr][nc]:
                        continue

                    if grid[nr][nc] == 0:
                        if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                            is_closed = False
                        visit[nr][nc] = True
                        q.append((nr, nc))

            return is_closed

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or visit[i][j]:
                    continue

                is_closed = bfs(i, j)
                if is_closed:
                    res += 1

        return res
