from typing import List

"""
# Approach: Sorting

## Intuition
We enumerate every consecutive k×k submatrix in the matrix grid. 
For each submatrix, we collect all its elements into an array kgrid and sort it in ascending order.

After sorting, we traverse kgrid to compute the minimum absolute difference between all adjacent distinct elements. 
This value represents the minimum absolute difference within the submatrix.

## Complexity Analysis
Let m be the number of rows in grid, n be the number of columns, and k be the given integer.

- Time complexity: O((m−k)×(n−k)×k^2×logk)

    We enumerate O((m−k)(n−k)) submatrices. Each submatrix contains k^2 elements, 
    and sorting them takes O(k^2logk) time.

- Space complexity: O(k^2).
    The temporary array kgrid stores up to k^2 elements. 
    The output array is not included in the space complexity.
"""


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                kgrid = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        kgrid.append(grid[x][y])
                kmin = float("inf")
                kgrid.sort()
                for t in range(1, len(kgrid)):
                    if kgrid[t] == kgrid[t - 1]:
                        continue
                    kmin = min(kmin, kgrid[t] - kgrid[t - 1])
                if kmin != float("inf"):
                    res[i][j] = kmin
        return res
