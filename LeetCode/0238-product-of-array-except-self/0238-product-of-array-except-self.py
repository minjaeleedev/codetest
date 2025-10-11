class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]*nums[i])
        
        acc = 1
        for i in range(len(nums)-1, -1, -1):
            if i != 0:
                prefix[i] = acc*prefix[i-1]
            else:
                prefix[i] = acc
            
            acc *= nums[i]

        return prefix