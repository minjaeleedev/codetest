class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i < 1:
            nums.reverse()
            return
        
        j = n - 1
        while j > i-1 and nums[j] <= nums[i-1]:
            j -= 1
        
        nums[j], nums[i-1] = nums[i-1], nums[j]
        nums[i:] = nums[len(nums)-1:i-1:-1]
            
        return