class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        cur = sum
        res = []

        for i in range(num):
            if cur >= 9:
                res.append("9")
                cur -= 9
            else:
                res.append(str(cur))
                cur = 0

        if cur > 0:
            return ""

        return "".join(res)
