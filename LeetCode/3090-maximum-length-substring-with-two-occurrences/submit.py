from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 < res:
                    continue

                cnt = Counter(s[i : j + 1])
                if max(cnt.values()) <= 2:
                    res = max(res, j - i + 1)

        return res
