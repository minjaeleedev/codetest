class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # row flip - if only leading bit is zero
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        
        # col flip - if total zero greater than one
        for j in range(n):
            zero, one = 0, 0
            for i in range(m):
                if grid[i][j] == 0:
                    zero += 1
                else:
                    one += 1
            
            if zero > one:
                for i in range(m):
                    grid[i][j] ^= 1
        
        # sum
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 ** (n-j-1) if grid[i][j] else 0
        
        return sum([sum(row) for row in grid])

            
            