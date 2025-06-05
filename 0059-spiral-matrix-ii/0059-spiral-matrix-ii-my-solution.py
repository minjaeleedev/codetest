class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r, c = 0, 0
        result = [[0]*n for _ in range(n)]
        d = [(0,1), (1,0),(0,-1),(-1,0)]
        idx = 0
        for num in range(1,n**2+1):
            result[r][c] = num
            dr, dc = d[idx][0], d[idx][1]
            if idx == 0:
                if c == n-1 or result[r+dr][c+dc] != 0:
                    idx = (idx+1)%4
            elif idx == 1:
                if r == n-1 or result[r+dr][c+dc] != 0:
                    idx = (idx+1)%4
            elif idx == 2:
                if c == 0 or result[r+dr][c+dc] != 0:
                    idx = (idx+1)%4
            elif idx == 3:
                if r == 0 or result[r+dr][c+dc] != 0:
                    idx = (idx+1)%4
            
            dr, dc = d[idx][0], d[idx][1]
            r, c = r + dr, c + dc
    
        return result