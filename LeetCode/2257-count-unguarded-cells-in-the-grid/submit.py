from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        mat = [["E"] * n for _ in range(m)]
        # check guards and walls before simulation
        for wr, wc in walls:
            mat[wr][wc] = "W"

        for gr, gc in guards:
            mat[gr][gc] = "G"

        # simulation guard
        for gr, gc in guards:
            for x in range(gr + 1, m):
                if mat[x][gc] == "W" or mat[x][gc] == "G":
                    break

                mat[x][gc] = "O"

            # east
            for x in range(gc + 1, n):
                if mat[gr][x] == "W" or mat[gr][x] == "G":
                    break

                mat[gr][x] = "O"

            # north
            for x in range(gr - 1, -1, -1):
                if mat[x][gc] == "W" or mat[x][gc] == "G":
                    break

                mat[x][gc] = "O"

            # west
            for x in range(gc - 1, -1, -1):
                if mat[gr][x] == "W" or mat[gr][x] == "G":
                    break

                mat[gr][x] = "O"

        result = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == "E":
                    result += 1

        return result
