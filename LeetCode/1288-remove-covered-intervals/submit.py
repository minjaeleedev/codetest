from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = len(intervals)
        pl, pr = intervals[0]
        for l, r in intervals[1:]:
            if pl <= l and r <= pr:
                res -= 1
            else:
                pl = l
                pr = r

        return res
