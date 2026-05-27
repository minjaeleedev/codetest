from collections import defaultdict


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ht = defaultdict(int)
        # 1: lower only
        # 2: upper only or upper precede lower.
        # 3: all lower precede upper.
        for c in word:
            if c.lower() == c:
                if not ht[c]:
                    ht[c] = 1
                elif ht[c] == 3:
                    ht[c] = 2
            else:
                key = c.lower()
                if not ht[key]:
                    ht[key] = 2
                elif ht[key] == 1:
                    ht[key] = 3
        return sum([1 for v in ht.values() if v == 3])
