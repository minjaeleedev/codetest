from math import inf
from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        res = inf
        # land -> water
        tmp = inf
        for i in range(n):
            tmp = min(landStartTime[i] + landDuration[i], tmp)

        end = inf
        for i in range(m):
            if waterStartTime[i] > tmp:
                t = waterStartTime[i] + waterDuration[i]
            else:
                t = tmp + waterDuration[i]

            end = min(end, t)

        res = min(res, end)

        # water -> land
        tmp = inf
        for i in range(m):
            tmp = min(waterStartTime[i] + waterDuration[i], tmp)

        end = inf
        for i in range(n):
            if landStartTime[i] > tmp:
                t = landStartTime[i] + landDuration[i]
            else:
                t = tmp + landDuration[i]

            end = min(end, t)

        res = min(res, end)

        return res
