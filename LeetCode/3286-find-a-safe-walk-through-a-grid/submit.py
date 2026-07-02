from collections import deque
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m,n=len(grid), len(grid[0])
        visit = [[-1]*n for _ in range(m)]
        
        q = deque([])
        q.append((0,0))
        visit[0][0] = health - 1 if grid[0][0] == 1 else health
        d = [(0,1), (1,0),(-1,0),(0,-1)]
        while q:
            cr, cc = q.popleft()
            ch = visit[cr][cc]
            if ch == 0:
                continue

            if cr == m-1 and cc == n-1:
                return True

            for dr, dc in d:
                nr, nc = cr+dr, cc+dc
                if 0 <= nr < m and 0 <= nc < n:
                    nx = grid[nr][nc]
                    nh = ch - 1 if nx == 1 else ch
                    if visit[nr][nc] < nh:
                        visit[nr][nc] = nh
                        q.append((nr,nc))

        return False