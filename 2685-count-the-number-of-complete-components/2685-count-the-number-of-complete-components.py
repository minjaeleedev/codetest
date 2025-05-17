class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = [0]*n
        graph = defaultdict(list)
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
        
        result = 0
        for i in range(n):
            if not visit[i]:
                nodes = [i]
                q = deque([i])
                visit[i] = 1
                while q:
                    cur = q.popleft()
                    for nx in graph[cur]:
                        if not visit[nx]:
                            visit[nx] = 1
                            q.append(nx)
                            nodes.append(nx)
                
                is_complete = True
                for node in nodes:
                    if len(graph[node]) != len(nodes) - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    result += 1
        
        return result