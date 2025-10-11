class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for winner, loser in matches:
            graph[loser].append(winner)
            if winner not in graph:
                graph[winner] = []
        
        result = [[],[]]
        for k, v in graph.items():
            if len(v) == 1:
                result[1].append(k)
            elif len(v) == 0:
                result[0].append(k)
        
        result[0].sort()
        result[1].sort()
        return result
            
        
            
