class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval
        res = []
        for s, e in intervals:
            if e < ns:
                res.append([s,e])
            elif s > ne:
                res.append([ns,ne])
                ns, ne = s, e
            else:
                # merge interval
                ns = min(ns, s)
                ne = max(ne, e)
        
        res.append([ns, ne])
        return res
        