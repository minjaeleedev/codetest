class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        d = 1
        while d < n:
            d = d << 1

        return ~n & (d - 1)
