from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        steps = [-1] * n
        q = deque([(0, 0)])
        steps[0] = 0
        i_dict = defaultdict(list)
        for i, num in enumerate(arr):
            i_dict[num].append(i)

        while q:
            ci, cs = q.popleft()

            if (ci + 1) < n:
                if steps[ci + 1] == -1 or steps[ci + 1] > cs + 1:
                    steps[ci + 1] = cs + 1
                    q.append((ci + 1, cs + 1))
            if ci - 1 >= 0:
                if steps[ci - 1] == -1 or steps[ci - 1] > cs + 1:
                    steps[ci - 1] = cs + 1
                    q.append((ci - 1, cs + 1))

            for i in i_dict[arr[ci]]:
                if i != ci + 1 and i != ci - 1 and i != ci:
                    if steps[i] == -1 or steps[i] > cs + 1:
                        steps[i] = cs + 1
                        q.append((i, cs + 1))

            i_dict[arr[ci]].clear()  # 지워도 안전하다.

        return steps[n - 1]
