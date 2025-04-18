class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            low = 0 if i-k < 0 else nums[i-k]
            high = 0 if i+k >=len(nums) else nums[i+k]

            if low < nums[i] and high < nums[i]:
                result += nums[i]
        
        return result