class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        result = 0
        cnt = defaultdict(int)
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                product = nums[i]*nums[j]
                if product in cnt:
                    result += 8 * cnt[product]
                
                cnt[product] += 1
        
        return result

        