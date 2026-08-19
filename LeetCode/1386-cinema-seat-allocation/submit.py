from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        none_row = n
        seat = defaultdict(list)
        for r, c in reservedSeats:
            if r not in seat:
                none_row -= 1
            seat[r].append(c)

        res = 0
        s1 = set([2, 3, 4, 5])
        s2 = set([4, 5, 6, 7])
        s3 = set([6, 7, 8, 9])

        def assign(arr):
            rs = set(arr)
            c1 = s1 & rs
            c2 = s2 & rs
            c3 = s3 & rs
            if len(c1) == 0:
                return 2 if len(c3) == 0 else 1

            if len(c2) == 0 or len(c3) == 0:
                return 1

            return 0

        for k, v in seat.items():
            res += assign(v)

        return none_row * 2 + res
