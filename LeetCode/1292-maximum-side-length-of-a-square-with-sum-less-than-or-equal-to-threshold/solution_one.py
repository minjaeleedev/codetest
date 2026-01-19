from typing import List

# Approach 1: Binary Search


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (
                    P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]
                )

        def getRect(x1, y1, x2, y2):
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            find = any(
                getRect(i, j, i + mid - 1, j + mid - 1) <= threshold
                for i in range(1, m - mid + 2)
                for j in range(1, n - mid + 2)
            )
            if find:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
