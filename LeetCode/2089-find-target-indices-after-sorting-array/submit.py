class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        idx = 0
        cnt = 0
        for n in nums:
            if target > n:
                idx += 1
            elif target == n:
                cnt += 1

        res = []
        for c in range(cnt):
            res.append(idx)
            idx += 1

        return res
