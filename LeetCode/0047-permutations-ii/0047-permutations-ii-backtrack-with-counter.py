class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def dfs(arr, counter):
            if len(arr) == n:
                result.append(arr[:])
                return
            
            for num in counter:
                if counter[num] > 0:
                    arr.append(num)
                    counter[num] -= 1
                    dfs(arr, counter)
                    arr.pop()
                    counter[num] += 1
                    
        dfs([], Counter(nums))
        return result
        