class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = minutes * 360 / 60
        h = hour * 360 / 12
        rem = minutes * 30 / 60
        theta = (h + rem) % 360
        return min(
            abs(m - theta), abs(theta - m), abs(360 - m + theta), abs(360 - theta + m)
        )
