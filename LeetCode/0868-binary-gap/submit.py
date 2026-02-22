class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        left = n & ~(n - 1)  # rightmost set bit. equals to n & -n
        dist = 0
        while left <= n:
            if n & left:
                res = max(res, dist)
                dist = 1
            else:
                dist += 1

            left = left << 1

        return res
