class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s = set()

        def helper(s1: str, cur: list, pos: int):
            if pos == 2:
                s.add("".join(cur))
                return

            cur[pos], cur[pos + 2] = cur[pos + 2], cur[pos]
            helper(s1, cur, pos + 1)
            cur[pos], cur[pos + 2] = cur[pos + 2], cur[pos]
            helper(s1, cur, pos + 1)

        helper(s1, list(s1), 0)
        return s2 in s
