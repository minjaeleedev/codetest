from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for query in queries:
            r1, c1, r2, c2 = query
            diff[r1][c1] += 1
            diff[r2 + 1][c1] -= 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        mat = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                x1 = 0 if r == 0 else mat[r - 1][c]
                x2 = 0 if c == 0 else mat[r][c - 1]
                x3 = 0 if r == 0 or c == 0 else mat[r - 1][c - 1]
                mat[r][c] = diff[r][c] + x1 + x2 - x3

        return mat
