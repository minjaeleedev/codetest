from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def equal(mat1, mat2):
            for i in range(len(mat1)):
                for j in range(len(mat1[0])):
                    if mat1[i][j] != mat2[i][j]:
                        return False

            return True

        def rotate(mat):
            res = []
            for c in range(len(mat[0])):
                res.append([mat[r][c] for r in range(len(mat) - 1, -1, -1)])

            for i in range(len(res)):
                mat[i] = res[i]

        for _ in range(4):
            if equal(mat, target):
                return True

            rotate(mat)

        return False
