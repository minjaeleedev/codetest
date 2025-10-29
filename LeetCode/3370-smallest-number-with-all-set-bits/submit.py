class Solution:
    def smallestNumber(self, n: int) -> int:
        res = 0
        exp = 1
        while res < n:
            res = 2**exp - 1
            exp += 1

        return res
