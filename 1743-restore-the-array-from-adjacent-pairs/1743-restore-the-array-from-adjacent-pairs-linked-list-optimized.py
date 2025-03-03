class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)

        root = None
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break
        
        # linked-list logic.
        cur = root
        prev = None
        ans = [root]
        while len(ans) < len(graph):
            # iterate over each node in order.
            for nxt in graph[cur]:
                if nxt != prev:
                    ans.append(nxt)
                    prev = cur
                    cur = nxt
                    break
        
        return ans
            