class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        result = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result += 1
                if nums[j] + nums[i] == target:
                    result += 1
        
        return result
