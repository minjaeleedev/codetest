from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        parents = [i for i in range(n)]

        cp = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                parents[i] = cp
            else:
                cp = i

        res = []
        for u, v in queries:
            res.append(parents[u] == parents[v])

        return res
