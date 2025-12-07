class Solution:
    def countOdds(self, low: int, high: int) -> int:
        s = low if low % 2 else low + 1
        e = high if high % 2 else high - 1

        return (e - s) // 2 + 1
