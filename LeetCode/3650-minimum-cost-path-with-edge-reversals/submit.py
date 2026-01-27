import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # init with bidirectional, doubling the cost of the reverse direction edge
        # graph init - O(n)
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))

        # dijkstra - O(mlogm)
        res = -1
        costs = [-1] * n
        costs[0] = 0
        q = []
        heapq.heapify(q)
        heapq.heappush(q, (0, 0))
        while q:
            w, v = heapq.heappop(q)

            for nv, nw in graph[v]:
                if costs[nv] == -1 or costs[nv] > nw + costs[v]:
                    costs[nv] = nw + costs[v]
                    heapq.heappush(q, (nw + costs[v], nv))

        res = costs[n - 1]
        return res
