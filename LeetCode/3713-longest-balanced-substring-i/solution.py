from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            counter = defaultdict(int)
            for j in range(i, len(s)):
                counter[s[j]] += 1
                freqs = set(counter.values())
                if len(freqs) == 1:
                    res = max(res, j - i + 1)

        return res
