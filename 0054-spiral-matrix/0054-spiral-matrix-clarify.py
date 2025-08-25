class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, right, left, bottom = 0, n-1, 0, m-1
        result = []
        while top <= bottom and left <= right:
            # left to right
            for j in range(left, right+1):
                result.append(matrix[top][j])

            top += 1

            # top to bottom
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            
            right -= 1

            # right to left
            if top <= bottom:
                for j in range(right, left-1, -1):
                    result.append(matrix[bottom][j])
            
                bottom -= 1
            
            # bottom to top
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
        
                left += 1
            
        return result