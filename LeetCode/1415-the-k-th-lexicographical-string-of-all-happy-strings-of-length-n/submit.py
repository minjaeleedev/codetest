from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def helper(n: int, k: int, cur: List[str]):
            if len(res) == k:
                return

            if len(cur) == n:
                res.append("".join(cur))
                return

            for c in "abc":
                if not cur or cur[-1] != c:
                    cur.append(c)
                    helper(n, k, cur)
                    cur.pop()

        helper(n, k, [])

        return res[k - 1] if len(res) == k else ""
