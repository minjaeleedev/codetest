class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        for r in range(x, (2*x+k)//2):
            for c in range(y, y+k):
                grid[r][c], grid[2*x+k-1-r][c] = grid[2*x+k-1-r][c], grid[r][c]
        
        return grid