class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def neighbors(i, j):
            res = 0
            for dr, dc in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                if 0 <= i + dr < len(board) and 0 <= j + dc < len(board[0]):
                    if board[i+dr][j+dc] in (1, 9, 10, 11):
                        res += 1
            
            return res
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    if neighbors(i, j) == 3:
                        board[i][j] = 12
                    continue

                if neighbors(i, j) < 2:
                    board[i][j] = 9
                elif neighbors(i, j) > 3:
                    board[i][j] = 11
                else:
                    board[i][j] = 10
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 9 or board[i][j] == 11:
                    board[i][j] = 0
                elif board[i][j] == 10 or board[i][j] == 12:
                    board[i][j] = 1