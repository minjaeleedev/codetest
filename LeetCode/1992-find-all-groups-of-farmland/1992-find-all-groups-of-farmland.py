class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        visit = [[0]*len(row) for row in land]
        result = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1 and visit[i][j] == 0:
                    result.append(self.bfs(land, visit, i, j))
    
        return result
    
    def bfs(self, land, visit, sr, sc):
        d = [(0,1), (1,0)]
        q = deque([(sr, sc)])
        visit[sr][sc] = 1
        last = None
        while q:
            last = q.popleft()
            for dr, dc in d:
                nr, nc = last[0] + dr, last[1] + dc
                if 0 <= nr < len(land) and 0 <= nc < len(land[0]):
                    if not visit[nr][nc] and land[nr][nc] == 1:
                        q.append((nr, nc))
                        visit[nr][nc] = 1
        
        return [sr, sc, last[0], last[1]]

    
