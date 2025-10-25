class Solution:
    def totalMoney(self, n: int) -> int:
        div, mod = n // 7, n % 7
        entire = div * (56 + (div - 1) * 7) // 2
        last = mod * (2 * div + mod + 1) // 2
        return entire + last
