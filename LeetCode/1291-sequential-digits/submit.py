from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        def helper(low, high, cur):
            if cur > high:
                return

            if low <= cur <= high:
                res.append(cur)

            if cur % 10 != 9:
                helper(low, high, cur * 10 + (cur % 10) + 1)

        for i in range(1, 9):
            helper(low, high, i)

        return sorted(res)
