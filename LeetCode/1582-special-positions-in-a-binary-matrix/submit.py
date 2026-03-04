from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        counts_row = []
        counts_col = []
        for r in range(m):
            cnt = 0
            for c in range(n):
                if mat[r][c] == 1:
                    cnt += 1

            counts_row.append(cnt)

        for c in range(n):
            cnt = 0
            for r in range(m):
                if mat[r][c] == 1:
                    cnt += 1

            counts_col.append(cnt)

        def is_special(row: int, col: int) -> bool:
            return mat[row][col] == 1 and counts_row[row] == 1 and counts_col[col] == 1

        res = 0
        for r in range(m):
            for c in range(n):
                if is_special(r, c):
                    res += 1

        return res
