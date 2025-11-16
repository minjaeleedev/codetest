class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        conti = 0
        res = 0
        for c in s:
            if c == "1":
                conti += 1
            else:
                res += conti * (conti + 1) // 2 % mod
                conti = 0

        if conti > 0:
            res += conti * (conti + 1) // 2 % mod

        return res
