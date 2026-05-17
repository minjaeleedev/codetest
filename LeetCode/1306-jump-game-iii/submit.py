from collections import deque
from typing import List

"""
BFS
"""


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visit = [False] * n
        q = deque([])
        q.append(start)
        visit[start] = True
        while q:
            cur = q.popleft()

            if arr[cur] == 0:
                return True

            head, tail = cur + arr[cur], cur - arr[cur]
            if 0 <= head < n:
                if not visit[head]:
                    visit[head] = True
                    q.append(head)

            if 0 <= tail < n:
                if not visit[tail]:
                    visit[tail] = True
                    q.append(tail)

        return False
