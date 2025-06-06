class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        n = len(equations)
        for i in range(n):
            a, b = equations[i]
            val = values[i]
            graph[a][b] = val
            graph[b][a] = 1/val
            graph[a][a] = 1
            graph[b][b] = 1
        
        result = []
        for q in queries:
            c, d = q
            visit = {k:-1 for k in graph}
            if c not in visit or d not in visit:
                result.append(-1)
                continue
            
            cur = c
            visit[cur] = 1
            q = deque([(cur, 1)])
            while q:
                x, r = q.popleft()
                for k, v in graph[x].items():
                    if visit[k] == -1:
                        visit[k] = r*v
                        q.append((k, visit[k]))
                
            result.append(visit[d])
        
        return result
            
            
            