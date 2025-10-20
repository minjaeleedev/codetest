class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = Counter(str(n))
        m = 999
        res = 9
        for k, v in freq.items():
            if v < m:
                m = v
                res = int(k)
            elif v == m:
                res = min(res, int(k))
        
        return res
