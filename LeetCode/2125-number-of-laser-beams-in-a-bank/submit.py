from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0
        for s in bank:
            ones = 0
            for c in s:
                if c == "1":
                    ones += 1

            if prev == 0:
                prev = ones
            else:
                res += prev * ones
                if ones != 0:
                    prev = ones

        return res
