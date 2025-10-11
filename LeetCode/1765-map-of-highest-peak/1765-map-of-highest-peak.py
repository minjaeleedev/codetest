class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        result = [[-1]*len(row) for row in isWater]
        q = deque([])
        for i in range(len(result)):
            for j in range(len(result[i])):
                if isWater[i][j]:
                    result[i][j] = 0
                    q.append((i,j))
        
        # by the last constraint, it guarantee q exist.
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            cr, cc = q.popleft()
            for dr, dc in d:
                nr, nc = cr+dr, cc+dc
                if 0<=nr<len(result) and 0<=nc < len(result[0]):
                    if result[nr][nc] == -1:
                        result[nr][nc] = result[cr][cc] + 1
                        q.append((nr,nc))
            
        return result
                    
        