class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        result = 0
        cnt = defaultdict(list)
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                product = nums[i]*nums[j]
                cnt[product].append((nums[i], nums[j]))
        
        for k, v in cnt.items():
            result += 8 * len(v) *(len(v)-1) // 2
        
        return result

        