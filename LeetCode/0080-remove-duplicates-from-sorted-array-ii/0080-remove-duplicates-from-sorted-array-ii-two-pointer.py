class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 1
        filled = 0 # filled first elem
        cnt = 1
        for i in range(1, len(nums)):
            cur = nums[i]
            if cnt == 2 and cur == nums[filled]:
                continue
            if cur != nums[filled]:
                cnt = 1
            else:
                cnt += 1
            
            filled += 1
            nums[filled] = cur
            res += 1
        
        return res
            