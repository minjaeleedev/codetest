class Solution:
    def maxDepth(self, s: str) -> int:
        cur = 0
        res = 0
        for c in s:
            if c == "(":
                cur += 1
            elif c == ")":
                res = max(res, cur)
                cur -= 1

        return res
