class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0]*n
        dp[0] = 1
        
        # key: prime, value: [index, next number]
        meta = {p:[0,1*p] for p in [2,3,5]}
        for i in range(1, n):
            nxt = min([num for idx, num in meta.values()])
            dp[i] = nxt

            for prime, v in meta.items():
                if nxt == v[1]:
                    v[0] += 1
                    v[1] = dp[v[0]] * prime

        return dp[n-1]
        
