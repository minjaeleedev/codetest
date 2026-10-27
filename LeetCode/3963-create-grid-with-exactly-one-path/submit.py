class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = []
        for i in range(m - 1):
            res.append("." + "#" * (n - 1))

        res.append("." * n)
        return res
