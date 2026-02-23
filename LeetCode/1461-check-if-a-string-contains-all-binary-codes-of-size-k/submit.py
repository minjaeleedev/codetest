class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if 2**k > len(s):
            return False

        mask = 2**k - 1
        bins = set()
        cur = 0
        for i in range(k):
            cur = cur << 1
            cur = cur | 1 if s[i] == "1" else cur

        bins.add(cur)

        for i in range(k, len(s)):
            cur = cur << 1
            cur &= mask
            cur |= 1 if s[i] == "1" else cur
            bins.add(cur)

        return len(bins) == 2**k
