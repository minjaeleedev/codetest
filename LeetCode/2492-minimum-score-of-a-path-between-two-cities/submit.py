import heapq
import math
from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, d in roads:
            graph[u][v] = d
            graph[v][u] = d

        score = [math.inf] * (n + 1)  # score[i] = min score 1 and i
        pq = [(math.inf, 1)]
        while pq:
            cs, cn = heapq.heappop(pq)
            for nn, nd in graph[cn].items():
                ns = min(cs, nd)
                if score[nn] > ns:
                    score[nn] = ns
                    heapq.heappush(pq, (ns, nn))

        return score[n]
