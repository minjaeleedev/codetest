class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rot = [0]*n
        for i in range(n):
            rot[(i+k)%n] = nums[i]
        
        for i in range(n):
            nums[i] = rot[i]
        