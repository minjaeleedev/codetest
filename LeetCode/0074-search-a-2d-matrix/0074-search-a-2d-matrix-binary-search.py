class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append(matrix[i][j])

        l, h = 0, len(arr)-1
        while l <= h:
            mid = (l+h)//2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid+1
            else:
                h = mid-1

        return False
