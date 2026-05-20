from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s = set()
        n = len(A)
        res = [0] * n
        for i in range(n):
            a, b = A[i], B[i]
            res[i] = res[i - 1] if i > 0 else 0
            if a == b:
                res[i] += 1
                continue

            if a in s:
                res[i] += 1
                s.remove(a)
            else:
                s.add(a)
            if b in s:
                res[i] += 1
                s.remove(b)
            else:
                s.add(b)

        return res
