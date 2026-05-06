from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        res = [["."] * m for _ in range(n)]

        for r in range(m):
            arr = boxGrid[r][::-1]
            temp = []
            empty = []
            stone = []
            for e in arr:
                if e == ".":
                    empty.append(e)
                elif e == "#":
                    stone.append(e)
                elif e == "*":
                    while stone:
                        temp.append(stone.pop())
                    while empty:
                        temp.append(empty.pop())
                    temp.append(e)

            while stone:
                temp.append(stone.pop())
            while empty:
                temp.append(empty.pop())

            for c in range(n):
                res[n - 1 - c][m - 1 - r] = temp[c]

        return res
