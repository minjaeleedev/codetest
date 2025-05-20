class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visit = [[0]*n for row in grid]
        q = deque([(0,0,grid[0][0])])
        visit[0][0] = grid[0][0]

        while q:
            cr, cc, cur_sum = q.popleft()
            if 0 <= cr + 1 < m:
                nxt = grid[cr+1][cc]
                if not visit[cr+1][cc] or visit[cr+1][cc] > cur_sum+nxt:
                    visit[cr+1][cc] = cur_sum+nxt
                    q.append((cr+1, cc, cur_sum+nxt))
            if 0 <= cc + 1 < n:
                nxt = grid[cr][cc+1]
                if not visit[cr][cc+1] or visit[cr][cc+1] > cur_sum+nxt:
                    visit[cr][cc+1] = cur_sum+nxt
                    q.append((cr, cc+1, cur_sum+nxt))
        
        return visit[m-1][n-1]
                
            