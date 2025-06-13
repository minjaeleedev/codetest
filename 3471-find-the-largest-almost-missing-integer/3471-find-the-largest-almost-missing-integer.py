class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        for i in range(len(nums)-k+1):
            sub = set(nums[i:i+k])
            for n in sub:
                freq[n] += 1
        
        missing = [k for k, v in freq.items() if v == 1]
        return max(missing) if missing else -1
            