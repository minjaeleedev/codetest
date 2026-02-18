class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        c = n & 1
        while n:
            n = n >> 1
            if n & 1 == c:
                return False
            c = n & 1

        return True
