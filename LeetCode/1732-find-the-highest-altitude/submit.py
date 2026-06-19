from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for g in gain:
            res.append(g + res[-1])

        return max(res)
