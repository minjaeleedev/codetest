class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        d = [(0,1), (1,0), (0,-1), (-1,0)]
        visit = [[False]*n for _ in board]
        def dfs(board, r, c, cur):
            print(r,c,cur)
            if len(cur) == len(word):
                return cur == word

            for dr, dc in d:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n:
                    if not visit[nr][nc] and word[len(cur)] == board[nr][nc]:
                        visit[nr][nc] = True
                        nxt = cur + board[nr][nc]
                        result = dfs(board, nr, nc, nxt)
                        visit[nr][nc] = False
                        if result:
                            return result
            
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visit[i][j] = True
                    result = dfs(board, i, j, board[i][j])
                    if result:
                        return True
                    visit[i][j] = False
        
        return False
        

                