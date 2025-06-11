class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visit = [[0]*n for _ in range(m)]
        d = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(m):
            for j in range(n):
                if visit[i][j] == 0 and board[i][j] == 'O':
                    visit[i][j]= 1
                    is_surround = True
                    points = [(i, j)]
                    # bfs
                    q = deque([(i, j)])
                    while q:
                        cr, cc = q.popleft()
                        if (cr == 0 or cr == m-1) or (cc == 0 or cc == n-1):
                            is_surround = False
                        
                        for dr, dc in d:
                            nr, nc = cr+dr, cc+dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if visit[nr][nc] == 0 and board[nr][nc] == 'O':
                                    visit[nr][nc] = 1
                                    q.append((nr,nc))
                                    points.append((nr,nc))
                    
                    if is_surround:
                        for r, c in points:
                            board[r][c] = 'X'
                    
        