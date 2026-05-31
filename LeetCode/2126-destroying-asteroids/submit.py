from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        cm = mass
        for a in asteroids:
            if a > cm:
                return False

            cm += a

        return True
