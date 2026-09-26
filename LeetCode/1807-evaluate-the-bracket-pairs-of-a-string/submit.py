class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        i = 0
        ht = {k: v for k, v in knowledge}
        res = ""
        while i < len(s):
            if s[i] == "(":
                j = i + 1
                key = ""
                while s[j] != ")":
                    key += s[j]
                    j += 1

                if key in ht:
                    res += ht[key]
                else:
                    res += "?"
                i = j + 1
                continue
            elif s[i] != ")":
                res += s[i]

            i += 1

        return res
