from collections import deque
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mat = [[-1] * n for _ in range(n)]

        q = deque([])
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    mat[r][c] = 0
                    q.append((r, c))

        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            cr, cc = q.popleft()
            for dr, dc in d:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if mat[nr][nc] == -1:
                        mat[nr][nc] = mat[cr][cc] + 1
                        q.append((nr, nc))
                    else:
                        mat[nr][nc] = min(mat[nr][nc], mat[cr][cc] + 1)

        for r in range(n):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                prev_row = mat[r - 1][c] if r > 0 else 0
                prev_col = mat[r][c - 1] if c > 0 else 0
                mat[r][c] = min(max(prev_row, prev_col), mat[r][c])

        return mat[n - 1][n - 1]
