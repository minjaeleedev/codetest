class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        result = [[0]*n for _ in range(m)]
        prefix = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prefix[i][j] = mat[0][0]
                elif i == 0:
                    prefix[i][j] = prefix[i][j-1] + mat[0][j]
                elif j == 0:
                    prefix[i][j] = prefix[i-1][j] + mat[i][0]
                else:
                    prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + mat[i][j]
                
        
        for i in range(m):
            for j in range(n):
                tr = i-k-1 if i-k-1 >= 0 else -1 # top row
                br = i+k if i+k < m else m-1 # bottom row
                rc = j+k if j+k < n else n-1 # right col
                lc = j-k-1 if j-k-1 >= 0 else -1 # left col
                top_left = prefix[tr][lc] if tr >= 0 and lc >= 0 else 0
                top_right = prefix[tr][rc] if tr >= 0 else 0
                bottom_right = prefix[br][rc]
                bottom_left = prefix[br][lc] if lc >= 0 else 0
                result[i][j] = bottom_right + top_left - top_right - bottom_left
        
        return result