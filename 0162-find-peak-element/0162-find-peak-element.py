class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l+h)//2
            nxt = float('-inf') if m == len(nums) - 1 else nums[m+1]
            if nxt > nums[m]:
                l = m + 1
            else:
                h = m
        
        return l