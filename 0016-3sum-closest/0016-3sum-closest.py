class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort - nlogn
        nums.sort()
        # two pointer : i, l, r
        result = float('inf')
        min_diff = float('inf')
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                t_sum = nums[i]+nums[l]+nums[r]
                diff = abs(t_sum - target)
                if diff < min_diff:
                    min_diff = diff
                    result = t_sum
                
                if t_sum > target:
                    r -= 1
                else:
                    l += 1

        return result
            
            
            