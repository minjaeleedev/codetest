class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s: str) -> str:
            return "1" if s == "0" else "0"

        if n == 1 and k == 1:
            return "0"

        if k == 2 ** (n - 1):
            return "1"

        if k < 2 ** (n - 1):
            return self.findKthBit(n - 1, k)

        return invert(self.findKthBit(n - 1, 2**n - k))
