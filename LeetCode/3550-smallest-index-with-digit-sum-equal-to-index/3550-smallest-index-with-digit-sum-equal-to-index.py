class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        result = -1
        for i in range(len(nums)):
            if i == self.digit_sum(nums[i]):
                return i
        
        return result
    
    def digit_sum(self, num:int)->int:
        res = 0
        while num:
            res += num%10
            num //= 10
        return res
            
            