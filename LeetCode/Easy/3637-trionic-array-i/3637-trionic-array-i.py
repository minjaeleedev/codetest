class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        p, i = 0, 1
        while i < n and nums[i] > nums[i-1]:
            p = i
            i += 1
        
        q = n-1
        while i < n and nums[i] < nums[i-1]:
            q = i
            i += 1
        
        while i < n and nums[i] > nums[i-1]:
            i += 1
        
        return 0 < p < q < n - 1 and i == n
            