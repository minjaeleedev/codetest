class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        d = 15
        while d:
            if n - 10**d >= 0:
                res += (n - 10**d + 1) * d // 3
                n = 10**d - 1

            d -= 3

        return res
