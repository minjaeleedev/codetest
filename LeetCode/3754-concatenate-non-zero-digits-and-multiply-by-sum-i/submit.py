class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        s = 0
        d = 1
        while n:
            if n % 10 != 0:
                x += d * (n % 10)
                d *= 10

            n //= 10

        temp = x
        while temp:
            s += temp % 10
            temp //= 10

        return x * s
