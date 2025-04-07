class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        
        res = len(s)
        for k,v in cnt.items():
            if v >= 3:
                res -= ((v-1)//2)*2 if not v%2 else (v//2)*2
        
        return res