class Solution:
    def bulbSwitch(self, n: int) -> int:
        # nth bulb is toggled as much its divisor
        # ex. 3 has divisor 1, 3 -> toggle 2
        # ex. 4 has divisor 1, 2, 4 -> toggle 3
        # ex. 6 has divisor 1, 2, 3, 6 -> toggle 4
        # therefore, numbers that have odd number of divisors are toggle on.
        # -> how many perfect squares in n.
        return int(n ** 0.5)