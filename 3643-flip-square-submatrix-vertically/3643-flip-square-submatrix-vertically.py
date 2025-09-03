class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        s = x
        e = x + k - 1
        while s < e:
            for c in range(y, y+k):
                grid[s][c], grid[e][c] = grid[e][c], grid[s][c]
            
            s += 1
            e -= 1
        
        return grid