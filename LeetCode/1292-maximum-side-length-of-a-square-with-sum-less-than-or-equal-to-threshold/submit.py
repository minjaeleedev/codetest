from typing import List


# Runtime - 5658ms
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    prefix[i][j - 1]
                    + prefix[i - 1][j]
                    - prefix[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        res = 0
        r = min(m, n)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for c in range(res + 1, r + 1):
                    if i + c - 1 <= m and j + c - 1 <= n:
                        s = prefix[i + c - 1][j + c - 1]
                        s -= prefix[i + c - 1][j - 1]
                        s -= prefix[i - 1][j + c - 1]
                        s += prefix[i - 1][j - 1]
                        if s <= threshold:
                            res += 1
                    else:
                        break

        return res
