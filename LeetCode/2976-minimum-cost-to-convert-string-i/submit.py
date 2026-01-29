import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # init graph O(m)
        graph = defaultdict(dict)
        m = len(original)
        for i in range(m):
            origin_v = graph[original[i]]
            c = changed[i]
            if c not in origin_v:
                origin_v[c] = cost[i]
            else:
                origin_v[c] = min(origin_v[c], cost[i])

        # make min cost map by dijkstra O(mlogm)
        min_costs = [[-1] * 26 for _ in range(26)]
        for i in range(26):
            min_costs[i][i] = 0

            q = [(chr(i + ord("a")), 0)]
            heapq.heapify(q)
            while q:
                cur_v, cur_cost = heapq.heappop(q)
                for k, v in graph[cur_v].items():
                    idx = ord(k) - ord("a")
                    if min_costs[i][idx] == -1 or min_costs[i][idx] > cur_cost + v:
                        min_costs[i][idx] = cur_cost + v
                        heapq.heappush(q, (k, cur_cost + v))

        # convert source from cost map
        n = len(source)
        res = 0
        for i in range(n):
            s, t = source[i], target[i]
            idx_s = ord(s) - ord("a")
            idx_t = ord(t) - ord("a")
            if min_costs[idx_s][idx_t] == -1:
                return -1

            res += min_costs[idx_s][idx_t]

        return res
