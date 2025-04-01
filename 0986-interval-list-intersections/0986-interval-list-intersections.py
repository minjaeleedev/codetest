class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        while i < len(firstList) and j < len(secondList):
            fs, fe = firstList[i]
            ss, se = secondList[j]

            start = max(fs, ss)
            end = min(fe, se)
            if start <= end:
                result.append([start, end])
            if fe > se:
                j += 1
            elif fe < se:
                i += 1
            else:
                i += 1
                j += 1
            
        
        return result