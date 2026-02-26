from collections import deque


class Solution:
    def numSteps(self, s: str) -> int:
        q = deque(s)
        res = 0
        while len(q) > 1:
            while len(q) >= 1 and q[-1] == "0":
                res += 1
                q.pop()

            if len(q) == 1:
                break

            flag = False
            while len(q) >= 1 and q[-1] == "1":
                flag = True
                res += 1
                q.pop()

            if q:
                if flag and q[-1] == "0":
                    q.pop()
                    q.append("1")
            else:
                if flag:
                    q.append("1")

            res += 1

        return res
