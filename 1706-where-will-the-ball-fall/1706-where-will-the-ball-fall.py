class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = []
        for j in range(len(grid[0])):
            row = 0
            col = j
            d = 'd'
            while 0 <= row < m and 0 <= col < n:
                if grid[row][col] == -1:
                    if d == 'd':
                        d = 'l'
                    elif d == 'r':
                        d = 'u'
                    elif d == 'l':
                        d = 'd'
                    else:
                        d = 'r'
                else:
                    if d == 'd':
                        d = 'r'
                    elif d == 'r':
                        d = 'd'
                    elif d == 'l':
                        d = 'u'
                    else:
                        d = 'l'

                if d == 'd':
                    row += 1
                elif d == 'r':
                    col += 1
                elif d == 'u':
                    break
                elif d == 'l':
                    col -= 1
                
            result.append(col if row == len(grid) else -1)
        
        return result

            