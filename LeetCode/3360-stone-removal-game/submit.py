class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice = False
        for i in range(10, 1, -1):
            if n >= i:
                n -= i
                alice = not alice
            else:
                break

        return alice
