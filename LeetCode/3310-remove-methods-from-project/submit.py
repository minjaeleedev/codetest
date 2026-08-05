from collections import defaultdict, deque
from typing import List


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        graph = defaultdict(list)
        rev = defaultdict(set)
        for a, b in invocations:
            graph[a].append(b)
            rev[b].add(a)

        s = set(range(n))
        cur = k
        q = deque([cur])
        group = set([cur])
        while q:
            c = q.popleft()

            for nxt in graph[c]:
                if nxt not in group:
                    q.append(nxt)
                    group.add(nxt)

        removed = True
        for node in group:
            diff = rev[node] - group
            if diff:
                removed = False
                break

        if removed:
            s -= group

        return list(s)
