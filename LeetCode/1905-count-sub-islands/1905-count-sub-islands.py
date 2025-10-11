class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        visit = [[0]*m for _ in range(n)]
        d = [(0,-1), (0,1), (1,0), (-1,0)]
        for i in range(m):
            for j in range(n):
                if not visit[i][j] and grid1[i][j] == 1:
                    q = deque([(i,j)])
                    visit[i][j] += 1
                    while q:
                        cr, cc = q.popleft()
                        for dr, dc in d:
                            nr, nc = cr+dr, cc+dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if visit[nr][nc] == 0 and grid1[nr][nc] == 1:
                                    visit[nr][nc] += 1
                                    q.append((nr, nc))
        
        result = 0
        for i in range(m):
            for j in range(n):
                if visit[i][j] == 1 and grid2[i][j] == 1:
                    q = deque([(i,j)])
                    visit[i][j] += 1
                    is_sub = True
                    while q:
                        cr, cc = q.popleft()
                        for dr, dc in d:
                            nr, nc = cr+dr, cc+dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if not visit[nr][nc] and grid2[nr][nc] == 1:
                                    is_sub = False
                                    break

                                if visit[nr][nc] == 1 and grid2[nr][nc] == 1:
                                    visit[nr][nc] += 1
                                    q.append((nr, nc))
                    
                    if is_sub:
                        result += 1
        return result