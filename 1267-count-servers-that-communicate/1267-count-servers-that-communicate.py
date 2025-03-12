class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[0]*n for r in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                if not visit[i][j] and grid[i][j] == 1:
                    # bfs
                    graph = defaultdict(list)
                    q = deque([(i,j)])
                    while q:
                        cr, cc = q.popleft()
                        for col in range(n):
                            if not visit[cr][col] and grid[cr][col]:
                                visit[cr][col] = True
                                q.append((cr, col))
                                graph[str(cr)+'-'+str(cc)].append((cr, col))
                                graph[str(cr)+'-'+str(col)].append((cr, cc))
                                break
                        
                        for row in range(m):
                            if not visit[row][cc] and grid[row][cc]:
                                visit[row][cc] = True
                                q.append((row, cc))
                                graph[str(cr)+'-'+str(cc)].append((row, cc))
                                graph[str(row)+'-'+str(cc)].append((cr, cc))
                                break
                    
                    nodes = len(graph.keys())
                    if nodes >= 2:
                        result += nodes
            
        return result