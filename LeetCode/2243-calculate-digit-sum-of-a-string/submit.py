class Solution:
    def digitSum(self, s: str, k: int) -> str:
        res = [c for c in s]
        while len(res) > k:
            tmp = []
            for i in range(0, len(res), k):
                s = 0
                for j in range(i, i + k):
                    if j >= len(res):
                        break
                    s += int(res[j])

                tmp += list(str(s))

            res = tmp

        return "".join(res)
