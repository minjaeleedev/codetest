class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        one = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                if s[i + 1] == "1":
                    res += one
            else:
                one += 1

        if s[-1] == "0":
            res += one

        return res
