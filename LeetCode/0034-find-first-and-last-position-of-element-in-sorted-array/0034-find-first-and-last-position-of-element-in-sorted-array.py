class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        low, high = 0, len(nums) - 1
        # first : find by decresing high index when mid equals to target
        while low <= high:
            mid = (low+high)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if 0 <= low <= len(nums) -1 and nums[low] == target:
            first = low
        
        last = -1
        low, high = 0, len(nums) - 1
        # last : find by increasing low index when mid equals to target
        while low <= high:
            mid = (low+high)//2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        
        if 0 <= high <= len(nums) -1 and nums[high] == target:
            last = high
        
        return [first, last]