from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        hBars.sort()
        vBars.sort()

        def longest_conti(arr):
            res = 0
            cur_len = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    cur_len += 1
                else:
                    res = max(res, cur_len)
                    cur_len = 1

            res = max(res, cur_len)
            return res

        h = longest_conti(hBars)
        v = longest_conti(vBars)
        return (min(h, v) + 1) ** 2
