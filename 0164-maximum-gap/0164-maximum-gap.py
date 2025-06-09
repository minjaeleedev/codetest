class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        sorted_arr = nums[:]
        radix = [deque([]) for i in range(10)]
        
        digit = 1
        for i in range(10):
            for n in sorted_arr:
                radix[(n//digit)%10].append(n)
            
            j = 0
            for q in radix:
                while q:
                    sorted_arr[j] = q.popleft()
                    j += 1
                    
            digit *= 10

        diff = -1
        for i in range(1, len(sorted_arr)):
            diff = max(diff, sorted_arr[i] - sorted_arr[i-1])

        return diff
            
        
