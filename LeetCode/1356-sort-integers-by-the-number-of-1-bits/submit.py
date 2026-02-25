from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def setbit(x):
            res = 0
            while x:
                res += x & 1
                x = x >> 1
            return res

        return sorted(arr, key=lambda x: (setbit(x), x))
