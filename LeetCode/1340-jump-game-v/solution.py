from typing import List


class Solution:
    """
    Approach: Memoization Search
    dp[i]: the maximum number of indices that can be visited starting from position i.

    Then,  dp[i]=max(dp[j])+1

    where j must satisfy the following three conditions:

    - 0 <= j < arr.length
    - i − d <= j <= i + d
    - Every element between arr[i] and arr[j] must be smaller than arr[i].

    With memoized search, whenever we need dp[j]:
    - if it has already been computed, we directly reuse the stored value;
    - otherwise, we temporarily pause the computation of dp[i], recursively compute dp[j], and then use the result to update dp[i].
    """

    def maxJumps(self, arr: List[int], d: int) -> int:
        seen = dict()

        def dfs(pos):
            if pos in seen:
                return
            seen[pos] = 1

            i = pos - 1
            while i >= 0 and pos - i <= d and arr[pos] > arr[i]:
                dfs(i)
                seen[pos] = max(seen[pos], seen[i] + 1)
                i -= 1
            i = pos + 1
            while i < len(arr) and i - pos <= d and arr[pos] > arr[i]:
                dfs(i)
                seen[pos] = max(seen[pos], seen[i] + 1)
                i += 1

        for i in range(len(arr)):
            dfs(i)

        return max(seen.values())
