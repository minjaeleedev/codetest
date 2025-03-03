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
        
        cur = None
        for i in graph.keys():
            if len(graph[i]) == 1:
                cur = i
                break
        
        visit = {i: False for i in graph}
        visit[cur] = True
        result = [cur]
        prev = len(result)
        while cur:
            cur = result[-1]
            for nxt in graph[cur]:
                if not visit[nxt]:
                    result.append(nxt)
                    visit[nxt] = True
            
            if prev == len(result):
                break
            
            prev = len(result)

        return result
            