from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        origin = 0
        for i in range(n):
            origin += prices[i] * strategy[i]

        result = origin
        # first modify k
        tmp = origin
        for i in range(k):
            if i < k // 2:
                if strategy[i] == 1:
                    tmp -= prices[i]
                elif strategy[i] == -1:
                    tmp += prices[i]
            else:
                if strategy[i] == -1:
                    tmp += 2 * prices[i]
                elif strategy[i] == 0:
                    tmp += prices[i]

        result = max(result, tmp)

        for i in range(1, n - k + 1):
            # middle switch 1 to 0
            tmp -= prices[i + k // 2 - 1]
            if strategy[i - 1] == 1:
                tmp += prices[i - 1]
            if strategy[i - 1] == -1:
                tmp -= prices[i - 1]

            if strategy[i + k - 1] == -1:
                tmp += 2 * prices[i + k - 1]
            if strategy[i + k - 1] == 0:
                tmp += prices[i + k - 1]

            result = max(result, tmp)

        return result
