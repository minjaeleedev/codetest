class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r, c = 0, 0
        dr, dc = 0, 1
        result = [[0]*n for _ in range(n)]
        for num in range(1,n**2+1):
            result[r][c] = num
            if not 0 <= r + dr < n or not 0 <= c + dc < n or result[r+dr][c+dc] != 0:
                dr, dc = dc, -dr
            
            r, c = r + dr, c + dc
    
        return result
                
            
            
            
            