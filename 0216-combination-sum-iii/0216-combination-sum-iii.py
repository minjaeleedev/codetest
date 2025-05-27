class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtrack(arr,s,idx):
            if len(arr) == k:
                if s == n:
                    result.append(arr[:])
                return
            
            for i in range(idx+1, 10):
                arr.append(i)
                backtrack(arr, s+i, i)
                arr.pop()
            
        backtrack([], 0, 0)
        return result