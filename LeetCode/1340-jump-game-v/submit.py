from collections import defaultdict, deque
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        graph = defaultdict(list)
        for i in range(n - 1):
            is_block = False
            mx = arr[i]
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[i] < arr[j] and arr[j] > mx:
                    mx = arr[j]
                    if not is_block:
                        is_block = True
                    graph[j].append(i)
                elif arr[i] > arr[j]:
                    if not is_block:
                        graph[i].append(j)

        res = [0] * n
        steps = [0] * n
        for i in range(n):
            if steps[i]:
                continue

            q = deque([(i, 1)])
            local_mx = 0
            while q:
                ci, cs = q.popleft()
                local_mx = max(local_mx, cs)
                for ni in graph[ci]:
                    if steps[ni] < cs + 1:
                        steps[ni] = cs + 1
                        q.append((ni, cs + 1))

            res[i] = local_mx

        return max(res)
