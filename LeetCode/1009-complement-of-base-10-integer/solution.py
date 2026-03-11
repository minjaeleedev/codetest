# highestOneBit OpenJDK algorithm from Hacker's Delight
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        # bitmask has the same length as N and contains only ones 1...1
        # ex) N is 1000001
        bitmask = N  # bitmask = 1000001
        bitmask |= bitmask >> 1  # 1000001 | 0100000 = 1100001
        bitmask |= bitmask >> 2  # 1100001 | 0011000 = 1111001
        bitmask |= bitmask >> 4  # 1111001 | 0000111 = 1111111
        bitmask |= bitmask >> 8
        bitmask |= bitmask >> 16  # we can cover all 32 bits integers.

        # flip all bits
        return bitmask ^ N
