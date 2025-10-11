class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        def backtrack(cur):
            result.append(cur)
            
            if cur * 10 <= n:
                backtrack(cur*10)
            
            if cur + 1 <= n and (cur+1)//10 == cur//10:
                backtrack(cur+1)
        
        backtrack(1)
        return result