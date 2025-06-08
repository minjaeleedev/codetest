class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = None
        for row in triangle:
            if prev:
                for i in range(len(row)):
                    added = 0
                    if i == 0:
                        added = prev[i]
                    elif i == len(row) - 1:
                        added = prev[i-1]
                    else:
                        added = min(prev[i], prev[i-1])
                    
                    row[i] = added + row[i]
        
            prev = row

        return min(triangle[-1])
        