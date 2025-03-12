class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        result = 0

        row_count = [0] * m
        col_count = [0] * n
        # precompute count of server for each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    # there are more than one server in this row or column.
                    result += 1
        
        return result