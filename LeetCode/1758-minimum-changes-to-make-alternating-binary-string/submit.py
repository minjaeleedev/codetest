class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if s[i] == "0":
                if i % 2 == 0:
                    cnt1 += 1
                else:
                    cnt2 += 1
            else:
                if i % 2 != 0:
                    cnt1 += 1
                else:
                    cnt2 += 1

        return min(cnt1, cnt2)
