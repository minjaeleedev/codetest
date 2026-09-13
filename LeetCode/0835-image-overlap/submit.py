from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def translate(mat: List[List[int]], dx: int, dy: int):
            # move x
            res = [[0] * len(mat) for _ in range(len(mat))]
            for r in range(len(mat)):
                if dx > 0:
                    res[r] = [0] * dx + mat[r][:-dx]
                else:
                    res[r] = mat[r][abs(dx) :] + [0] * abs(dx)

            # move y
            for r in range(len(mat)):
                added = [0] * abs(dx)
                if dx > 0:
                    res[r] = added + mat[r][:-dx]
                else:
                    res[r] = mat[r][abs(dx) :] + added

            added = [[0] * len(mat) for _ in range(abs(dy))]
            if dy > 0:
                res = added + res[:-dy]
            else:
                res = res[abs(dy) :] + added

            return res

        def overlap(a: List[List[int]], b: List[List[int]]):
            cnt = 0
            for i in range(len(a)):
                for j in range(len(a)):
                    if a[i][j] != 1:
                        continue
                    if a[i][j] == b[i][j]:
                        cnt += 1

            return cnt

        res = 0
        n = len(img1)
        for dx in range(-n + 1, n):
            for dy in range(-n + 1, n):
                mat = translate(img1, dx, dy)
                res = max(overlap(mat, img2), res)

        return res
