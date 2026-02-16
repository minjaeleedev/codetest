import functools


class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 24
        while n:
            ret += self.reverseByte(n & 0xFF) << power
            n = n >> 8
            power -= 8
        return ret

    # memoization with decorator
    # https://graphics.stanford.edu/~seander/bithacks.html#ReverseByteWith64BitsDiv
    @functools.lru_cache(maxsize=256)
    def reverseByte(self, byte):
        return (byte * 0x0202020202 & 0x010884422010) % 1023
