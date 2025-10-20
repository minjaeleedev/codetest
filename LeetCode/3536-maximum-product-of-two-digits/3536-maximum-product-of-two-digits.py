class Solution:
    def maxProduct(self, n: int) -> int:
       s = [int(d) for d in str(n)]
       s.sort()
       return s[-1]*s[-2]
       
