from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        long, short = (a, b) if len(a) > len(b) else (b, a)
        res = deque([])
        carry = 0
        i, j = len(long) - 1, len(short) - 1
        while j >= 0:
            cl, cs = int(long[i]), int(short[j])
            if cl == 0 and cs == 0:
                res.appendleft(str(carry))
                carry = 0
            elif cl == 0 or cs == 0:
                temp = 1 if not carry else 0
                res.appendleft(str(temp))
                carry = 1 if temp == 0 else 0
            else:
                temp = 0 if not carry else 1
                res.appendleft(str(temp))
                carry = 1
            i -= 1
            j -= 1

        while i >= 0:
            cur = int(long[i])
            if cur:
                if carry:
                    temp = "0"
                    carry = 1
                else:
                    temp = "1"
                    carry = 0
            else:
                if carry:
                    temp = "1"
                    carry = 0
                else:
                    temp = "0"
                    carry = 0

            res.appendleft(temp)
            i -= 1

        if carry:
            res.appendleft("1")

        return "".join(res)
