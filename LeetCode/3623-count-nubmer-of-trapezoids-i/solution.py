from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        y_vals = defaultdict(int)
        for x, y in points:
            y_vals[y] += 1

        mod = 10**9 + 7
        s = 0
        ans = 0
        for _, cnt in y_vals.items():
            combi = cnt * (cnt - 1) // 2 % mod
            ans = (ans + combi * s) % mod
            s = (s + combi) % mod

        return ans
