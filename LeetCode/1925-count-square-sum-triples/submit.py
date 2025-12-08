class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        i = 1
        while i <= n:
            j = 1
            while j <= n:
                k = i**2 + j**2
                rt = k**0.5
                if rt == int(rt) and rt <= n:
                    res += 1

                j += 1
            i += 1

        return res
