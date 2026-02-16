class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        d = 1
        for i in range(32):
            if i < 16:
                res |= (n & d) << (31 - 2 * i)
            else:
                res |= (n & d) >> (2 * i - 31)

            d = d << 1

        return res
