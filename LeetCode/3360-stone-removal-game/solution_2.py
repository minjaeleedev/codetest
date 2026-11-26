from math import sqrt


class Solution:
    def canAliceWin(self, n: int) -> bool:
        k = int((21 - sqrt(441 - 8 * n)) / 2)
        return k % 2 == 1
