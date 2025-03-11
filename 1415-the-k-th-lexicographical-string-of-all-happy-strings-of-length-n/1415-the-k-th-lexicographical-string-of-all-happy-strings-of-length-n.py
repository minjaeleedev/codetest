class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        def dfs(cur):
            if len(cur) == n:
                result.append("".join(cur))
                return 
            
            for c in 'abc':
                if not cur or cur[-1] != c:
                    cur.append(c)
                    dfs(cur)
                    cur.pop()
        
        dfs([])
        return result[k-1] if len(result) >= k else ""
            