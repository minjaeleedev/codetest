class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(n, k, idx, cur):
            if len(cur) == k:
                result.append(cur[:])
            
            for i in range(idx+1, n+1):
                cur.append(i)
                dfs(n, k, i, cur)
                cur.pop()
        
        dfs(n, k, 0, [])
        return result