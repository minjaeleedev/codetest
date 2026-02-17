from collections import defaultdict
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def setbit(n):
            s = 0
            while n:
                if n & 1:
                    s += 1
                n = n >> 1
            return s

        sbit = defaultdict(list)
        for i in range(60):
            sbit[setbit(i)].append(i)

        res = []
        for t in range(turnedOn + 1):
            hs = [h for h in sbit[t] if h < 12]
            ms = sbit[turnedOn - t]
            for h in hs:
                for m in ms:
                    mst = str(m) if m >= 10 else "0" + str(m)
                    res.append(str(h) + ":" + mst)

        return res
