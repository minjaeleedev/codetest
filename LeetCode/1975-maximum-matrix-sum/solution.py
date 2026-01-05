from typing import List


class Solution:
    """
    Intuition
    1. There’s an odd number of negative elements
    - it won’t be possible to make everything positive because one negative will always remain.
    - To minimize the impact of this remaining negative(=to maximize sum)
    - we want it to be the smallest number in the matrix.
    2. There’s an even count of negative numbers
    - we can flip them all to positive values. so total is answer.
    """

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_abs = float("inf")
        cnt = 0
        for r in matrix:
            for v in r:
                total += abs(v)
                if v < 0:
                    cnt += 1
                min_abs = min(min_abs, abs(v))

        # negative numbers odd
        if cnt % 2 != 0:
            total -= 2 * min_abs

        return total
