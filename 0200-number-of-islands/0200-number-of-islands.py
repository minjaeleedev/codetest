class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False]*n for _ in range(m)]
        res = 0
        d = [(-1, 0), (0,-1),(1,0),(0,1)]
        for r in range(m):
            for c in range(n):
                if not visit[r][c] and grid[r][c] == '1':
                    # bfs
                    res += 1
                    q = deque([(r, c)])
                    while q:
                        cr, cc = q.popleft()
                        for dr, dc in d:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if not visit[nr][nc] and grid[nr][nc] == '1':
                                    visit[nr][nc] = True
                                    q.append((nr, nc))
        
        return res