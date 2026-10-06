class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal = 0
        res = 0
        for c in s:
            if c == "(":
                if bal < 0:
                    res += abs(bal)
                    bal = 0
                bal += 1
            else:
                bal -= 1

        res += abs(bal)

        return res
