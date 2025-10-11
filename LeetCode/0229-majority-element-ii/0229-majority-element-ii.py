class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []
        for n, f in counter.items():
            if f >= len(nums) // 3 + 1:
                res.append(n)
        
        return res


