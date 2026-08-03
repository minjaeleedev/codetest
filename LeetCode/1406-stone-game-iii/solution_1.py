from typing import List


class Solution:
    """
    Approach 1: Bottom-Up Dynamic Programming

    Complexity Analysis

    - Time complexity: O(n).
    There is a for loop that performs n iterations.
    For each state, we try up to three options: to take 1, 2, or 3 stones,
    so each iteration takes O(1) time.

    - Space complexity: O(n).
    We store the array dp[n + 1] of size O(n).
    """

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = stoneValue[i] - dp[i + 1]
            if i + 2 <= n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] - dp[i + 2])
            if i + 3 <= n:
                dp[i] = max(
                    dp[i],
                    stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3],
                )
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"
