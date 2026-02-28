class Solution:
    def concatenatedBinary(self, n: int) -> int:
        def digit(num: int) -> int:
            d = 0
            while num:
                d += 1
                num = num >> 1

            return d

        MOD = 10**9 + 7
        res = 0
        dp = 0
        # O (N)
        for i in range(1, n + 1):
            # O(log N)
            shift = dp * (2 ** digit(i)) % MOD
            res = (shift + i) % MOD
            dp = res

        return res
