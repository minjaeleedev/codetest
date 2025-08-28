class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0]*numCourses
        graph = defaultdict(set)
        for u, v in prerequisites:
            in_degree[u] += 1
            graph[v].add(u)
        
        result = []
        q = deque([])
        # initiate queue with nodes that in_degree is zero.
        for i, n in enumerate(in_degree):
            if n == 0:
                result.append(i)
                q.append(i)
            
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    result.append(nxt)
                    q.append(nxt)

        if any(degree != 0 for degree in in_degree):
            return []

        return result
            
        