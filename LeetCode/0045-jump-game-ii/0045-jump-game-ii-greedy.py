class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        result = 0
        end = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                result += 1
                end = farthest

        return result