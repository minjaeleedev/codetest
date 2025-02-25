"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(grid, a, b, n, val):
            isLeaf = True
            for i in range(a, a+n):
                if isLeaf:
                    for j in range(b, b+n):
                        if grid[i][j] != val:
                            isLeaf = False
                            break
                else:
                    break
            
            if isLeaf:
                return Node(val, isLeaf, None, None, None, None)
            
            topLeft = helper(grid, a, b, n//2, grid[a][b])
            topRight = helper(grid, a, b+n//2, n//2, grid[a][b+n//2])
            bottomLeft = helper(grid, a+n//2, b, n//2, grid[a+n//2][b])
            bottomRight = helper(grid, a+n//2, b+n//2, n//2, grid[a+n//2][b+n//2])
            return Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
                    
        return helper(grid, 0, 0, len(grid), grid[0][0])
        