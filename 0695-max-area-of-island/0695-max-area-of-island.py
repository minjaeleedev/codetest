class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        m, n = len(grid), len(grid[0])
        visit = [[False]*n for _ in range(m)]
        d = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(m):
            for j in range(n):
                if not visit[i][j] and grid[i][j] == 1:
                    q = deque([(i, j)])
                    visit[i][j] = True
                    area = 1
                    while q:
                        cr, cc = q.popleft()
                        for dr,dc in d:
                            nr, nc = cr + dr, cc+dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if not visit[nr][nc] and grid[nr][nc]:
                                    q.append((nr, nc))
                                    visit[nr][nc] = True
                                    area += 1
                    
                    result = max(area, result)
        
        return result
                
                        
                
        