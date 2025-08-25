class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        start = 0
        result = []
        while m > 0 and n > 0:
            for j in range(start, start+n):
                result.append(matrix[start][j])

            if m > 1:
                # 행이 2개 이상이면 아래로 이동
                for i in range(start+1, start+m):
                    result.append(matrix[i][start+n-1])

                for j in range(start+n-2, start-1, -1):
                    result.append(matrix[m+start-1][j])

                if n > 1:
                    # 행이 2개 이상, 열이 2개 이상이면 위로 이동
                    for i in range(start+m-2, start, -1):
                        result.append(matrix[i][start])
            
            m -= 2
            n -= 2
            start += 1
        
        return result