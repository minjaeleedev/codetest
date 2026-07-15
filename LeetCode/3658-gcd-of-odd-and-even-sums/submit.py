class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a, b):
            if b > a:
                a, b = b, a

            if b == 0:
                return a

            return gcd(b, a % b)

        odd, even = 0, 0
        for i in range(n):
            odd += 2 * i + 1
            even += 2 * i + 2

        return gcd(odd, even)
