class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        cur = []
        for s,e in intervals:
            if not cur:
                cur = [s,e]
                continue
            
            if s > cur[1]:
                res.append(cur[:])
                cur = [s, e]
            else:
                if e > cur[1]:
                    cur[1] = e

        if cur:
            res.append(cur[:])
        
        return res