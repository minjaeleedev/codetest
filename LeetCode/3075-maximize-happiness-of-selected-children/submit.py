from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(key=lambda x: -x)
        res = 0
        dec = 0
        for i in range(k):
            cur = happiness[i]
            if cur - dec > 0:
                res += cur - dec
            else:
                break
            dec += 1

        return res
