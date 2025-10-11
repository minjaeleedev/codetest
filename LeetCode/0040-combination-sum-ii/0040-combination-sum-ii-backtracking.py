class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(start, cur, s):
            if s > target:
                return
            if s == target:
                result.append(cur[:])
                return
            
            for i in range(start, len(candidates)):
                if start < i and candidates[i-1] == candidates[i]:
                    continue
                
                if candidates[i] > target:
                    break
                
                cur.append(candidates[i])
                backtrack(i+1, cur, s+candidates[i])
                cur.pop()
        
        backtrack(0,[],0)
        return result