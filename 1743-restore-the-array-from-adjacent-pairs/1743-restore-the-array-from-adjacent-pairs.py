class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = {}
        for u, v in adjacentPairs:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            
            graph[u].append(v)
            graph[v].append(u)
        
        first = None
        for i in graph.keys():
            if len(graph[i]) == 1:
                first = i
                break
        
        visit = {i: False for i in graph}
        result = [first]
        visit[first] = True
        def dfs(cur_node):
            for nxt in graph[cur_node]:
                if not visit[nxt]:
                    result.append(nxt)
                    visit[nxt] = True
                    dfs(nxt)
        
        dfs(first)
        return result
            