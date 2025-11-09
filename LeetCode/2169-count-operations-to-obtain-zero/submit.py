class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        def helper(n1, n2, res):
            if n1 == 0 or n2 == 0:
                return res

            if n1 <= n2:
                return helper(n1, n2 % n1, res + n2 // n1)
            return helper(n1 % n2, n2, res + n1 // n2)

        return helper(num1, num2, 0)
