from collections import Counter
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0): 0}

        for s in strs:
            cnt = Counter(s)
            ones, zeroes = cnt["1"], cnt["0"]
            newdp = {}

            for k, v in dp.items():
                prevzeroes, prevones = k
                newzeroes, newones = prevzeroes + zeroes, prevones + ones
                if newzeroes <= m and newones <= n:
                    if (newzeroes, newones) not in dp:
                        newdp[(newzeroes, newones)] = v + 1

                    elif dp[(newzeroes, newones)] < v + 1:
                        newdp[(newzeroes, newones)] = v + 1
            dp.update(newdp)
        return max(dp.values())
