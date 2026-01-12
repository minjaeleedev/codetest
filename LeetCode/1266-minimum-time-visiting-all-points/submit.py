from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        cur = points[0]
        for i in range(1, len(points)):
            dx, dy = points[i][0] - cur[0], points[i][1] - cur[1]
            # chebyshev distance
            diag = min(abs(dx), abs(dy))
            res += diag
            res += max(abs(dx), abs(dy)) - diag
            cur = points[i]

        return res
