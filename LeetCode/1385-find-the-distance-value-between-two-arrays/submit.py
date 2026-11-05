class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res = 0
        for i in arr1:
            is_dist = True
            for j in arr2:
                if abs(i - j) <= d:
                    is_dist = False
                    break

            if is_dist:
                res += 1

        return res
