class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r = 0
        c = n-1
        while r < m and c >= 0:
            cur = matrix[r][c]
            if cur == target:
                return True
            elif cur < target:
                r += 1
            else:
                c -= 1

        return False
            