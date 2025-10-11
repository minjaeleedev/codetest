class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res = [[0]*n for _ in range(m)]
        res[0][0] = 1
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    res[r][c] = 0
                    continue
                if r > 0:
                    res[r][c] += res[r-1][c]
                if c > 0:
                    res[r][c] += res[r][c-1]

        return res[m-1][n-1]