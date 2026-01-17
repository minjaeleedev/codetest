from typing import List


class Solution:
    def square_area(self, rec1: List[List[int]], rec2: List[List[int]]):
        bl1, tr1 = rec1
        bl2, tr2 = rec2

        if bl1[0] >= tr2[0] or bl2[0] >= tr1[0]:
            return 0
        if bl1[1] >= tr2[1] or bl2[1] >= tr1[1]:
            return 0

        x = [bl1[0], bl2[0], tr1[0], tr2[0]]
        y = [bl1[1], bl2[1], tr1[1], tr2[1]]
        x.sort()
        y.sort()
        res = min(x[2] - x[1], y[2] - y[1]) ** 2
        return res

    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        n = len(bottomLeft)
        res = 0
        for i in range(n - 1):
            rec1 = (bottomLeft[i], topRight[i])
            for j in range(i + 1, n):
                rec2 = (bottomLeft[j], topRight[j])
                res = max(res, self.square_area(rec1, rec2))

        return res
