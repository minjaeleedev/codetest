class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = Counter(s)
        valid = set(d for d in cnt if str(cnt[d]) == d)
        
        for d1, d2 in pairwise(s):
            if d1 == d2:
                continue
            
            if d1 in valid and d2 in valid:
                return d1 + d2
        
        return ''