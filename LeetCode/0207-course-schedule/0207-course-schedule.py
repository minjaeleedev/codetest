class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # init graph and in-degree array
        graph = {num:set() for num in range(numCourses)}
        in_degree = [0]*numCourses
        for pair in prerequisites:
            u, v = pair
            graph[u].add(v)
            in_degree[v] += 1
        
        print(graph)
        print(in_degree)
        q = deque([i for i, v in enumerate(in_degree) if v == 0])
        cnt = 0
        while q:
            cur = q.popleft()
            cnt += 1
            for nxt in graph[cur]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    q.append(nxt)

        return cnt == numCourses
