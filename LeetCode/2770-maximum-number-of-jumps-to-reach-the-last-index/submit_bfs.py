from collections import defaultdict, deque
from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # init graph: O(n^2)
        graph = defaultdict(list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if -target <= nums[j] - nums[i] <= target:
                    graph[i].append(j)

        q = deque([(0, 0)])
        visit = [-1] * n
        # bfs
        while q:
            cur_index, cnt = q.popleft()

            for nxt_index in graph[cur_index]:
                nxt = visit[nxt_index]
                if nxt < cnt + 1:
                    visit[nxt_index] = cnt + 1
                    q.append((nxt_index, cnt + 1))

        return visit[n - 1]
