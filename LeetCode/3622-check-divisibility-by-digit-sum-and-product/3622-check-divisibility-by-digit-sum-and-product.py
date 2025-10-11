class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def digit_sum(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        def digit_product(num):
            res = 1
            while num:
                res *= num % 10
                num //= 10
            
            return res
        s = digit_sum(n)
        p = digit_product(n)
        return n % (s + p) == 0