class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        l, s = max(n, m), min(n, m)
        if l <= k and s <= k:
            return 0
        
        return (l-k)*k