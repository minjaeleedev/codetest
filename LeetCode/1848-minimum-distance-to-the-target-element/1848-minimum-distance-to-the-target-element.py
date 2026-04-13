class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        result = None
        for i, num in enumerate(nums):
            if num == target:
                dist = abs(i - start)
                if result is None:
                    result = dist
                else:
                    result = min(dist, result)

        if result is None:
            return -1

        return result
