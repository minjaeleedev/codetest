class Solution:
    def rotatedDigits(self, n: int) -> int:
        val = [1, 1, 2, 3, 3, 2, 2, 3, 1, 2]
        dp = [0] * (n + 1)

        for i in range(min(10, n + 1)):
            dp[i] = val[i]

        for i in range(10, n + 1):
            r = i % 10
            prev = dp[i // 10]
            if prev == 1:
                dp[i] = val[r]
            elif prev == 2:
                k = val[r]
                dp[i] = k if k == 2 or k == 3 else 2
            else:
                dp[i] = 3

        return sum([1 for i in dp if dp[i] == 2])
