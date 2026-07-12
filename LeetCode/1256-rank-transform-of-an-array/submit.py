from collections import defaultdict
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        rank = defaultdict(int)
        tmp = sorted(arr)
        r = 1
        prev = tmp[0]
        for n in tmp:
            if n > prev:
                r += 1
                prev = n
            rank[n] = r

        return [rank[n] for n in arr]
