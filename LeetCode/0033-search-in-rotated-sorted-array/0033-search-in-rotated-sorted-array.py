class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        res = -1
        while l <= h:
            m = (l+h)//2
            if nums[m] == target:
                res = m
                break
            
            if nums[l] <= nums[m]: # subarray [l:m] is sorted
                if nums[l] <= target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            else: # subarray [m:h] is sorted
                if nums[m] < target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1

        return res